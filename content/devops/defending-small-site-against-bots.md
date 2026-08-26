---
title: "You Can't Just 'Block the Bots': Defending a Small Site Against a Month of Bot Attacks"
date: 2026-08-25T22:47:00+01:00
draft: false
tags: ["devops", "security", "cloud", "observability", "incident-response", "2026"]
description: "A month spent defending a one-person, single-VPS community site against fake analytics, a combinatorial crawler, and a WAF rule that blocked a real visitor - and what it taught about layered bot defence."
cover:
  image: /assets/images/devops/platform-engineering-2026.jpg
  alt: Server infrastructure behind a firewall, illustrating layered bot defence
---

## TL;DR

- A small community site running on a single eight-core VPS spent a month fighting bots. The headline lesson: **"just block the bots" is not a plan, it is a wish**.
- Google Analytics reported 263,000 users in 28 days. Real human traffic was under 1,000 sessions - **about 0.3% of the number on the dashboard**. [GA4's anomaly detection](https://support.google.com/analytics/answer/9443595) flagged the spike, but its default bot filtering never caught the bot itself, because it was a real headless browser spoofing a normal Chrome user agent.
- Moving the site behind [Cloudflare's free tier](https://developers.cloudflare.com/bots/get-started/free/) was a multi-day project, not a toggle: it broke SSH, silently proxied DNS records it shouldn't have, and its own Bot Fight Mode quietly downgraded a custom block rule to a challenge that a headless browser sailed straight through.
- A combinatorial crawler minting random filter-URL combinations later pushed server load past 10 on an 8-core box **nine times in one week** - not from any single slow query, but from thousands of individually cheap queries running concurrently.
- Edge rules alone couldn't fix it. The durable fix was an application-level concurrency guard that capped expensive queries at 3 of 10 PHP-FPM workers and degraded gracefully instead of falling over.
- The most humbling incident: an emergency WAF rule built to block the crawler's malformed URLs ended up hard-blocking a real visitor who'd hit an unrelated rendering bug that happened to produce the same URL shape.

Every fix in this post came out of a real month of incidents on a real site: a small, independent community platform built on a PHP CMS with custom directory and listing apps, run by one person, on one VPS, behind a CDN's free tier. Nothing here is theoretical.

## Your Dashboard Is Lying to You

It started with what looked like great news: Google Analytics showing 263,000 active users and 935,000 events in 28 days. Traffic was booming.

It wasn't. When we dug in, roughly 98% of that traffic was bots. Real traffic - organic search, referrals, social, AI-assistant referrals combined - was under 1,000 sessions.

The tells were everywhere once we knew what to look for:

- **98% "direct" traffic.** A real site doesn't get 98% of its visits as direct/no-referrer. Direct is usually the smallest channel for a site without an established app or bookmark habit.
- **An unnaturally uniform device fingerprint.** 262,000 of 263,000 users were Windows / Chrome / desktop. Organic traffic is normally a messy mix of mobile, desktop, Safari, and Android.
- **Geography that reads like a cloud bill.** Singapore, Brazil, Hong Kong, plus Frankfurt and Ashburn, Virginia - two of the largest cloud-hosting regions on Earth, not where this site's real audience lives.
- **A session source of literally `127.0.0.1:8941 / referral`** - localhost, in production analytics.
- **GA4's own anomaly detector flagged it**, with "direct" visits surging from an expected ~1,900 to ~113,000 in a single day.

The uncomfortable part: this wasn't cheap spam sent straight to the [Measurement Protocol](https://support.google.com/analytics/answer/9443595). It was a real headless browser, actually loading pages and firing the GA4 tag, spoofing a normal desktop Chrome user agent. That's why GA4's default bot filtering - which mostly checks user-agent strings against a known-bots list - never caught it. The UA string looked exactly like real Chrome.

The lesson: your dashboard is a liar, and the first thing you have to build is a working definition of "what is a real visitor?" Exclude-lists go stale fast - we built one for Singapore, then Hong Kong, then thirteen more countries, and the bot wave kept spreading faster than we could chase it. A positive filter - traffic from where your real audience actually lives - held up far better than any blocklist.

## Adding a CDN Is a Project, Not a Toggle

The obvious next move was Cloudflare. Moving the zone onto the free plan sounded like a day's work. It was a project, and the cutover alone surfaced lessons that a "just add a CDN" post never mentions:

- **SSH broke the day after cutover.** Cloudflare proxies HTTP/HTTPS only, so the hostname started resolving to an edge IP that doesn't listen on port 22. The fix was SSHing to the origin IP directly via an `~/.ssh/config` alias.
- **DNS auto-import proxied records it shouldn't have.** It quietly put mail-autodiscover, `_dmarc`, and domain-delegation records behind the proxy - which breaks a plain DNS lookup for anything that isn't HTTP, including mail servers checking DMARC.
- **TLS mode matters more than it should.** "Flexible" terminates TLS at the edge and talks plain HTTP to the origin, which causes redirect loops when the origin already forces HTTPS. Full (strict) was the only sane mode - but the auto-scanner defaulted to plain Full, which silently accepts an invalid origin certificate.
- **The free plan's WAF is a fraction of the story.** No configurable managed ruleset, no staging mode, and [no rate limiting on query strings](https://developers.cloudflare.com/waf/rate-limiting-rules/) - free gets Bot Fight Mode and a hardcoded ruleset targeting known exploits.
- **Locking the origin was the single most important fix.** Before this, anyone who knew the origin IP could bypass Cloudflare entirely. Firewalling ports 80/443 to [Cloudflare's published IP ranges](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/) only meant the origin could no longer be reached directly. Everything else is bypassable without this.

The subtlest lesson came from Bot Fight Mode itself. We'd added a custom rule to block a bot swarm from one region - it should have blocked 100% of it, but a constant ~5% trickle kept getting through. The root cause: Bot Fight Mode intercepts traffic in an earlier phase than custom rules and downgrades **Block** to **Managed Challenge**. Since the bot was a real JS-executing headless browser, it solved the challenge and sailed through. Our own security feature was quietly undermining our other security feature. Disabling Bot Fight Mode fixed it - a genuine trade-off: broad bot protection traded for a deterministic block. There's no "just turn everything on."

## The Crawler That Brought a Server to Its Knees

Two weeks after the Cloudflare cutover, the site started falling over - not from the original swarm, but from a combinatorial crawler.

The pattern was unmistakable: not a few hot URLs, but thousands of random multi-filter directory URLs, mixing arbitrary record slugs with random combinations of the site's filter parameters (category, region, type, date range, sort) across every listing app. One incident captured 17,283 requests in 25 minutes, 16,336 of them filtered listing URLs - and almost no single URL repeated more than eight times out of 7,084 requests. It was minting fresh combinations continuously.

The effect was a machine ground down by "cheap" work done at volume:

- **CPU saturation, not memory or disk.** Load average over 10 on an eight-core box, all ten PHP-FPM workers pegged, the database burning 350-470% CPU on short, individually cheap queries.
- **No single slow query.** Each filtered listing page ran 6-11 database round trips with correlated subqueries per active filter - fine once, ruinous thousands of times a second.
- **Throwing workers at it makes it worse.** The site was CPU-bound; more PHP-FPM workers just increased contention.
- **The failure moved up the stack.** One recurrence pushed nginx past its file-descriptor ceiling ([`worker_rlimit_nofile`](https://nginx.org/en/docs/ngx_core_module.html#worker_rlimit_nofile), defaulting to 1024), taking the *whole* site down with 500s - not just the crawled routes.

Over the course of a week the saturation recurred nine times, and each recurrence taught something that generalises well beyond this one incident:

- **Free-plan rate limits can't see query strings.** Matching on `http.request.uri.query` is an Advanced Rate Limiting feature on paid plans - we discovered this mid-incident, when the rule failed to save.
- **Per-IP limits don't help a distributed crawler.** The crawl spread across dozens of unrelated IPv4 and IPv6 addresses; a single-IP limit is a no-op against that.
- **Challenges don't cost the crawler anything.** A Managed Challenge returns a JS redirect the crawler simply doesn't follow - it never spends a cent of CPU. Only a hard block, ideally at the edge before the origin, actually protects you.
- **"Verified bot" is a trust decision you shouldn't make lightly.** The crawler returned under user agents that Cloudflare classifies as verified bots, and our own rules carried a `not cf.client.bot` exemption added so real search engines wouldn't be challenged. The exemption was the hole - the crawler spoofed a verified-bot UA and walked straight through. Any rule that exempts verified bots is only as strong as the classification behind it, and we have direct proof it can be spoofed.
- **Over-tightening a rule is how you lose.** When a separate flood arrived as a bare `Firefox/135.0` UA, we tightened a match from `contains` to `eq` so genuine Firefox users wouldn't be caught. Within minutes the attacker switched to a full, realistic UA string that `eq` no longer matched, and the flood resumed. We reverted to `contains` and settled on a `managed_challenge` rule instead: a real browser passes the JS challenge automatically, a raw GET flood with no JS engine fails.

## Edge Rules Can't Fix an Application Problem

Edge rules stop volume, but there's a class of problem they can't touch: a crawler that mints unlimited fresh URLs from an unlimited pool of IPs. No cache keyed on the filter combination can ever hit, because the crawler can always generate a URL nobody has seen before. So the fix had to move into the application: **capping the concurrency of the expensive queries directly.**

We built a concurrency guard - a set of TTL-leased slots (a cap of 3 out of 10 PHP-FPM workers) that any expensive filtered-listing request has to acquire before running its live queries. Over the cap, the app degrades gracefully, serving cached unfiltered data with a small notice banner, instead of running the expensive path. It fails open in the *safe* direction: a broken guard means "degraded experience," never "unleash the crawler on a database at 400% CPU."

A few design details made it actually hold up:

- **TTL-leased slots, not counters.** A request killed mid-flight self-heals within seconds without depending on a `release()` call ever running. A leaked slot can't wedge the guard shut.
- **Degraded is not the same as broken.** Real visitors who hit the cap still get real content, just without live facet counts. The crawler gets zero database round trips.
- **The guard revealed its own bugs on review.** In one app the lease was released *before* the expensive queries ran, making it an admission probe rather than a real cap. In another, the guard wrapped the cheaper query while the actual cost driver ran unguarded. Auditing "is this app guarded?" misses both; auditing "is this specific query guarded?" catches them.

We also attacked page cost directly - caching unfiltered facet bundles, adding edge caching for anonymous listing HTML with an explicit bypass for logged-in members, and putting a real read index on the roadmap to replace the correlated-subquery filter lookups for good.

## Your Own Defences Will Block Your Own Users

The most humbling incident in the whole month: our own crawler-blocking WAF rule hard-blocked a real visitor.

A user clicked a filter link and got "Sorry, you have been blocked." The link's URL contained a stray `&` right after the `?` - a framework URL builder rendered a leading `&` on every friendly URL it appended a query string to. That exact `?&` shape was what we'd just built an emergency WAF rule to block, because it was the shape the crawler was minting.

A routine rendering bug became a hard, user-facing 403 against a genuine visitor. We fixed the URL builder at the source, added regression and smoke tests so it can't silently reappear, and narrowed the WAF rule to the literal malformed shape instead of "any `&`." The lesson generalises beyond this one bug: when you build a security rule on the *shape* of an attack, you inherit every other bug that happens to produce that same shape.

One more twist worth its own paragraph: a large chunk of the "bot" traffic in the analytics was our own tooling. The single largest source IP in the security analytics - more requests in a day than any other source by a wide margin - resolved to cloud infrastructure registered to an AI company. It was an AI coding assistant fetching and checking the live site while it was being developed. Your own tools will pollute your own dashboards; filter them out before drawing conclusions from the numbers.

## What I'd Tell You Before You Start This Fight

1. **Assume your analytics lie until proven otherwise.** A uniform device fingerprint, cloud-hosting geography, and 98% direct traffic are the fingerprints of bot traffic, and [built-in bot filtering](https://support.google.com/analytics/answer/9443595) will not save you from a headless browser that spoofs a normal UA.
2. **Put a reverse proxy in front, and lock the origin to it.** Nothing else matters if someone can connect to the origin IP and skip all of it.
3. **Layer your defences, and accept every layer has a hole.** Edge rules stop concentrated bursts, rate limits stop single-IP floods, concurrency caps in the application stop combinatorial crawls. The crawler that actually takes a site down is the one that combines the weaknesses.
4. **Trust no classification, not even a "verified bot" flag.** Spoofed UAs are trivial, and exemption rules are exactly how attackers walk through the front door. The wider [OWASP catalogue of automated threats](https://owasp.org/www-project-automated-threats-to-web-applications/) is worth a skim before you assume any single signal is reliable.
5. **Never let a security rule punish legitimate users.** Prefer blocking specific abusive signatures over broad shapes. Challenge when you can, block only when you must, and keep an escape hatch for the genuine visitor.
6. **The durable fix lives in your application, not your WAF.** A rule can stop today's crawler. Only making the expensive pages cheap - and capping concurrency - stops any crawler, forever, regardless of what IPs or URLs it invents next.
7. **Document everything.** Nine recurrences, each with a different root cause, would have been impossible to keep straight without an incident log recording what broke, why, and how it was fixed.

A month later, load averages that used to climb to 10 now sit around 1.4. The crawler that saturated the server nine times gets dropped at the edge within two seconds of a rule going live. Real visitors rarely notice any of it - except, briefly, the one person who clicked a filter link at the wrong moment.

That's the real shape of bot defence on a small site: not one fix, but a process. The bots adapt, your own rules occasionally turn on your users, and your own tools can look like the enemy. The only winning move is making each layer cheaper, tighter, and better documented than the attack that just failed against it.

## Related Reading

- [Understanding Types of Cyber Attacks: A DevOps Guide](/devops/cyber-attack-types/)
- [Monitoring and Observability](/devops/monitoring/)
- [Self-Hosted vs Managed in 2026](/devops/self-hosted-vs-managed-2026/)
- [Kubernetes in 2026 - Is It Still Worth the Complexity Tax?](/devops/kubernetes-2026-complexity-tax/)
- [The eBPF Revolution - What Every Platform Engineer Should Know](/devops/ebpf-revolution/)
