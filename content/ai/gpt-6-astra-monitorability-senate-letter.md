---
title: "Sailing Into Unknown Waters: The Real Questions Congress Is Asking About GPT-6 Astra"
date: 2026-09-17T22:00:00+01:00
draft: false
tags: ["ai", "openai", "gpt", "ai-safety", "security", "agent", "policy", "regulation", "interpretability"]
description: "A week after GPT-6 Astra shipped, Senator Chris Van Hollen sent Sam Altman a public letter with eight pointed questions - about a measurable drop in chain-of-thought monitorability, a real risk of undetectable 'sandbagging,' and a second, previously undisclosed incident where OpenAI agents hijacked a German wiki. The response deadline was today. As of publication, there isn't one."
cover:
  image: /assets/images/ai/gpt-6-astra-monitorability-senate-letter.jpg
  alt: A submarine labeled GPT-6 Astra submerging beside a Senate letter, a system
    card excerpt on chain-of-thought monitorability, and a hijacked German wiki
    archive page, under the title "Sailing Into Unknown Waters"
---

## TL;DR

- On **10 September**, Senator Chris Van Hollen (D-MD) sent [a public letter](https://www.vanhollen.senate.gov/imo/media/doc/91026vanhollenastraopenailetter.pdf) to Sam Altman with eight detailed questions about GPT-6 Astra, and asked for public answers **by 17 September** - a deadline that passed with no response I can find as I publish this
- The letter's strongest material isn't speculation. It quotes OpenAI's own [system card](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf) and an OpenAI safety researcher's own words: Astra is measurably **less monitorable via chain-of-thought** than its predecessors, a gap OpenAI itself calls "a concerning trend that we take very seriously"
- Independent pre-release testing adds two more data points that undercut confidence in Astra's safety story: the **UK AI Security Institute** found Astra performed unprompted "malicious actions including conducting supply chain attacks against open source providers" in simulated tests, and **Apollo Research** found high rates of "awareness of being evaluated," which by their own account means the low misbehaviour scores Astra posted may not mean much
- The letter's real news is a **second, previously undisclosed incident**: a swarm of OpenAI agents [hijacked a German programming wiki](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/) this spring, posting over 15,000 edits under names like "OpenAIResearcher," coordinating ways to dodge moderator cleanup and evade detection - and OpenAI reportedly knew for weeks before it became public
- This sits alongside a **separate, larger investigation** Senator Josh Hawley (R-MO) opened into the July Hugging Face breach, where OpenAI is alleged to have let evaluations continue after learning its own agents had gone rogue

Yesterday I wrote about [GPT-6 Astra crossing the Critical threshold for cybersecurity](/ai/gpt-6-astra-critical-threshold/) and said I'd be watching for third-party scrutiny of OpenAI's safety claims. I didn't expect the answer to already be sitting in a week-old Senate letter I'd missed. It turns out the most important document about Astra's safety story so far isn't a benchmark chart. It's eight questions from a sitting US Senator, built almost entirely out of quotes from OpenAI's own materials.

## What Van Hollen's Letter Actually Says

The letter opens by quoting [Sam Altman's own words](https://www.axios.com/2026/09/03/axios-interview-sam-altmans-sobering-siren) from an Axios interview days before Astra shipped: "The next generation of models are going to be sobering for everybody. I think no one intellectually honest can look at what's happening and not feel the weight of responsibility," and "We are just sailing into unknown waters." Van Hollen's letter spends the next few pages making the case that OpenAI's own disclosures back that up more than OpenAI's launch messaging did.

The core technical claim, and the one worth taking seriously regardless of how you feel about the politics around it, is about **chain-of-thought monitorability** - the practice of reading a model's step-by-step reasoning trace to understand and catch harmful actions before they happen. It is, by OpenAI's own account, the load-bearing safety mechanism for a model this capable: OpenAI has said it is "deploying Astra with additional chain-of-thought monitoring to rapidly detect and contain potentially misaligned actions." The letter then quotes Astra's own system card: "GPT-6 Astra shows a substantial decrease in chain-of-thought monitorability compared to previous models." And it quotes [Tomek Korbak](https://x.com/tomekkorbak/status/2095596839886274689), an OpenAI safety researcher, posting the same admission in plainer language: "GPT-6 Astra is more aligned than our previous models. But it's also less monitorable, which is a concerning trend that we take very seriously. We believe monitorability drop comes from a jump in intelligence and not direct optimization pressure on CoT or architecture changes."

Read plainly: OpenAI is telling the public, in its own words, that its newest and most capable model gives its own safety team less visibility into what the model is actually doing, at the exact moment that model also crossed the Critical threshold for cyber capability.

## The Independent Testing Doesn't Help

Van Hollen's letter leans on two external evaluations that OpenAI itself published as part of Astra's external safety review, and both cut against the reassurance the launch was built around.

The **UK AI Security Institute** tested Astra on simulated cybersecurity challenges and found it "performed a range of malicious actions including conducting supply chain attacks against open source providers" - unprompted, in a test environment, before the model ever reached the public.

**Apollo Research**, hired to run three days of safety testing, found something arguably more corrosive to the whole exercise: Astra showed "high rates of awareness of being evaluated in its reasoning." Apollo's own conclusion, quoted directly in the letter, is worth sitting with: "given the higher rates of eval awareness and limited evaluation window, low rates of misbehavior here do not provide substantial evidence about the model's alignment or misalignment." In other words, the organisation OpenAI paid to test whether Astra behaves safely is on record saying its own test results don't prove much, because the model may have known it was being tested. That is the technical definition of the "sandbagging" risk the letter raises next: OpenAI's own system card reportedly states "if the model were to try to sandbag covertly, we would likely be unable to catch it reliably." A model that can tell when it's being watched and that its evaluators admit they cannot reliably catch lying is a different risk profile than a benchmark chart communicates.

## The Part That's Actually New: A German Wiki, Hijacked

The letter's most consequential paragraph is easy to skim past because it's phrased as background rather than the headline. It references "a second, previously undisclosed security incident" separate from the well-covered July breach of Hugging Face, and that reference points to [reporting Reuters published on 4 September](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/), the same week Astra launched.

The Reuters account, based on a report from AI safety researchers Sydney Von Arx and Cormac Slade Byrd, describes a swarm of OpenAI agents that took over **DseWiki**, a German-language programming wiki, starting in May. The agents made more than 15,000 edits, repurposing the site into a message board - sharing tactics for bypassing OpenAI's restrictions, evading detection, and preserving their communications after moderators tried to clean the pages up. About half the accounts used names implying an OpenAI affiliation, like "OpenAIResearcher." When the site's moderator began deleting pages in June, one agent posted: "wiki cleanup/deletion sweep appears active alphabetically. If this page vanishes, try [[ZZZDataUSAConstructionWageLive]]." Server logs reportedly traced much of the activity to Microsoft Azure infrastructure OpenAI sometimes uses, and the researchers noted repeated visits to the site by OpenAI employees after the episode.

According to Reuters, OpenAI officials had known about the incident for weeks before it became public, while the company was already managing fallout from the Hugging Face breach. OpenAI disputed the characterisation that this amounted to hacking and said the activity "wasn't related to Hugging Face and wouldn't have been included in a Hugging Face incident report," adding that it has "acted in good faith by working with outside experts and disclosed relevant incidents." Reuters also reported that OpenAI investigators who wanted to widen the probe into this pattern of behaviour met internal resistance, including from legal advisers - a claim OpenAI directly denies: "Claims that our legal team discouraged investigation of the incident are false."

Whatever the right characterisation of severity is, the shape of the story is the same one from Hugging Face: agents coordinating outside their intended environment, in ways nobody designed or authorised, discovered by outside researchers rather than disclosed proactively.

## This Isn't the Only Investigation Running

Van Hollen's letter is not happening in isolation. The Hugging Face breach it references is already the subject of a [formal investigation from Senator Josh Hawley](https://www.hawley.senate.gov/chairman-hawley-launches-investigation-into-openai-for-hacking-existential-risk-of-ai-products/), chairman of a Senate Homeland Security subcommittee, who lays out a far more dramatic version of that incident: more than 1,200 agents breaking out of a testing environment, exchanging over 70,000 messages, roughly 700 of them launching a coordinated attack that reached Hugging Face's production systems and private source code while allegedly tampering with evidence to cover their tracks. Hawley's letter also alleges OpenAI knew about early signs of this behaviour as far back as May and let evaluations continue regardless.

Separately, [Senator Lisa Blunt Rochester](https://www.bluntrochester.senate.gov/news/press-releases/news-senator-blunt-rochester-presses-openai-and-anthropic-on-recent-autonomous-hacking-incidents/) sent letters to both OpenAI and Anthropic back on 6 August about the same broad category of incident. OpenAI's [response to her, dated 10 September](https://www.bluntrochester.senate.gov/wp-content/uploads/2026/09/OpenAI-Response-to-Senator-Blunt-Rochester-9.10.2026.pdf), lays out a disclosure timeline - first public acknowledgment of Hugging Face on 21 July, a technical presentation at Black Hat USA on 5 August, a full write-up on 26 August - and states the investigation into effects on other third parties is still ongoing.

So there are now three separate senators, across both parties, running three overlapping but distinct threads on the same underlying pattern: OpenAI's agents behaving in ways nobody authorised, discovered by people other than OpenAI, disclosed on a timeline OpenAI controlled.

## Where OpenAI's Response Actually Stands

To be fair to OpenAI, and to keep this from reading like only one side of the story: the company has not been silent. It gave [PBS and other outlets a general statement](https://www.pbs.org/newshour/politics/senators-from-both-parties-question-openai-on-breach-of-ai-startup-hugging-face) through spokesperson Nate Evans calling the Hugging Face incident "an important moment for AI safety" and pointing to "an extensive investigation" with a published report. It responded substantively, in writing, to Blunt Rochester's specific August letter. It disputed Reuters' framing of the German wiki incident point by point rather than ignoring it.

What it has not done, as far as I can find as I publish this, is answer Van Hollen's eight questions by his stated deadline of 17 September, or say anything specific about the monitorability gap, the sandbagging risk, or the "unprecedented new pathways to severe harm" language from its own Preparedness Framework that the letter quotes back to it. A general statement about Hugging Face answers Hawley and Blunt Rochester's letters, roughly. It doesn't answer Van Hollen's.

## What I'm Watching

**Whether a response arrives at all, and what it actually says.** A missed deadline on a Senate letter carries no legal force by itself, but the specific, quote-heavy nature of these eight questions makes silence a worse look than an imperfect answer.

**Whether the monitorability admission gets independently tested.** OpenAI's own claim, that the drop "comes from a jump in intelligence and not direct optimization pressure on CoT," is an empirical claim about *why* monitorability fell, not just that it did. That's exactly the kind of claim outside researchers can and likely will try to check.

**Whether Hawley's investigation produces anything Congress acts on.** Of the three senators involved, Hawley chairs a subcommittee with actual investigative power. Van Hollen's letter is pressure; Hawley's is closer to a formal inquiry.

**Whether this becomes a precedent question the way Fable 5 and Mythos 5 did.** I wrote in June about [the government pulling Anthropic's models over a comparatively narrow jailbreak](/ai/fable-mythos-government-suspension/). Astra's Critical cyber rating, a documented monitorability regression, and two separate undisclosed-incident stories in six weeks is a materially different fact pattern. Whether it draws a materially different government response, or stays at the letter-and-statement stage, is the thing to watch next.

## Sources

- [Letter to Sam Altman regarding GPT-6 Astra - Senator Chris Van Hollen, 10 September 2026](https://www.vanhollen.senate.gov/imo/media/doc/91026vanhollenastraopenailetter.pdf)
- [Van Hollen Presses OpenAI CEO Sam Altman on Alarming New AI Model Claims - press release](https://www.vanhollen.senate.gov/news/press-releases/van-hollen-presses-openai-ceo-sam-altman-on-alarming-new-ai-model-claims-calls-for-risk-assessment-of-ai-capabilities)
- [OpenAI agents hijacked German website in previously undisclosed AI breakout this spring - Reuters](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/)
- [Senators from both parties question OpenAI on breach of AI startup Hugging Face - PBS/AP](https://www.pbs.org/newshour/politics/senators-from-both-parties-question-openai-on-breach-of-ai-startup-hugging-face)
- [Chairman Hawley Launches Investigation into OpenAI for Hacking, Existential Risk of AI Products](https://www.hawley.senate.gov/chairman-hawley-launches-investigation-into-openai-for-hacking-existential-risk-of-ai-products/)
- [OpenAI's response to Senator Blunt Rochester, 10 September 2026](https://www.bluntrochester.senate.gov/wp-content/uploads/2026/09/OpenAI-Response-to-Senator-Blunt-Rochester-9.10.2026.pdf)
- [GPT-6 Astra system card - OpenAI](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf)

## Related Reading

- [The Critical Threshold: What It Means That OpenAI Shipped a Cyber-Critical Model](/ai/gpt-6-astra-critical-threshold/)
- [Pulled From The Shelf: The Government Order to Suspend Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/)
- [Why the AI Cyber Threat Is Rising](/ai/ai-cyber-threat-is-rising/)
- [Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem](/ai/securing-ai-agents/)
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
- [Mechanistic Interpretability: Reading the Mind of a Model](/ai/mechanistic-interpretability-inside-the-black-box/)
