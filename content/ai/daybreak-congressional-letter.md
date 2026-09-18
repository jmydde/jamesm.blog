---
title: "The Letter Before The Order: Congress Presses OpenAI on Daybreak"
date: 2026-09-17T21:30:00+01:00
draft: false
tags: ["ai", "openai", "anthropic", "gpt", "ai-safety", "security", "policy", "regulation", "governance"]
description: "A day after GPT-6 Astra's Critical cyber classification became public, the Senate Commerce and House Science Committees sent OpenAI a bipartisan letter about Daybreak. No export control directive, no 5:21pm phone call - just questions, on the record, about pre-release access, vetting criteria, and a shared severity framework OpenAI hasn't joined."
cover:
  image: /assets/images/ai/daybreak-congressional-letter.jpg
  alt: A congressional letter next to a gated Daybreak access terminal, contrasted with a redacted export control stamp
---

## TL;DR

- On **17 September**, the Senate Commerce Committee and House Science, Space, and Technology Committee sent a **joint, public letter** to OpenAI about **Daybreak**, the vetted-access program for GPT-6 Astra's Critical-tier cybersecurity capability
- The letter asks four things: whether CAISI and UK AISI got **pre-release access** to Astra under the June 2 Executive Order commitments; when **Daybreak's vetting criteria** will be published; whether OpenAI will **join the jailbreak severity framework** Anthropic, Amazon, Google, and Microsoft have been drafting since July; and for the underlying data behind Astra's **0% scope-violation** alignment claim
- OpenAI's same-day response confirms CAISI and UK AISI **did** get pre-release access - so the "did they skip government review" question has a clean answer, and it's no
- OpenAI commits to publishing Daybreak's vetting criteria "in the coming weeks" but is **conspicuously silent** on the severity framework question - the one part of the letter it didn't answer
- Unlike the [Fable 5 and Mythos 5 suspension](/ai/fable-mythos-government-suspension/) - a verbal directive at 5:21pm ET with no public paper trail - this is playing out entirely in daylight: a public letter, a public response, nothing suspended

Yesterday I wrote about [what I'd be watching](/ai/gpt-6-astra-critical-threshold/) after GPT-6 Astra crossed OpenAI's Critical threshold for cybersecurity: whether Daybreak, the company's answer to a model too cyber-capable to ship unrestricted, would draw the kind of government intervention that pulled Fable 5 and Mythos 5 off the shelf after four days in June. One day later, we have a first data point. It is not a directive. It is a letter.

## What Actually Arrived

The [joint letter](https://www.commerce.senate.gov/2026/9/letter-openai-daybreak-vetting-criteria), sent under the letterhead of both the Senate Commerce Committee and the House Science, Space, and Technology Committee, is notably narrow in what it demands and notably specific in what it asks. Four questions, in order:

1. **Did OpenAI provide pre-release access to Astra** to the Center for AI Standards and Innovation (CAISI) and the UK AI Security Institute, consistent with the pre-release government access commitments made under the 2 June Executive Order - the same commitments [Anthropic and other Glasswing partners agreed to](/ai/redeploying-fable-5/) after the Fable 5 episode?
2. **What are the vetting criteria for Daybreak**, and will they be made public, given the program grants "less restrictive safeguards" for a model that found real zero-days during its own evaluation?
3. **Will OpenAI join the jailbreak and capability severity framework** - the CVSS-style scoring system for capability gain, breadth, weaponisation ease, and discoverability - that Anthropic, Amazon, Google, and Microsoft have been drafting since the Fable 5 redeployment in July?
4. **What is the evaluation methodology** behind Astra's claim of 0% scope violation on the Hugging Face-informed eval, and has any third party reproduced it?

The letter is polite, procedural, and entirely public - posted to the Commerce Committee's site the same day it was sent. That framing matters, and I will come back to it.

## The First Question Has A Clean Answer

OpenAI's response, published a few hours after the letter went public, answers question one directly: yes. CAISI and the UK AI Security Institute both received pre-release access to Astra, ran their own capability evaluations against the Preparedness Framework thresholds, and were briefed on the Critical cybersecurity classification before the 10 September launch. OpenAI's statement frames this as unremarkable - "the process the Executive Order was written to describe" - and points out that the pre-release briefing is precisely why OpenAI knew to gate the model behind Daybreak rather than ship it unrestricted in the first place.

If accurate, this closes off the most dramatic possible reading of the story before it could form: OpenAI did not route around the government-access commitments the industry built in the aftermath of Fable 5 and Mythos 5. That is worth stating plainly, because it would have been easy for this post to be about a lab skipping the process. It is not. It is about what the process didn't cover.

## The Two Questions OpenAI Didn't Fully Answer

Question two gets a partial answer: OpenAI says Daybreak's vetting criteria - who qualifies as a vetted defender, what access tiers exist, what monitoring applies - will be "published in the coming weeks." That is a commitment with a date attached to nothing. I'll be watching for it.

Question three gets no answer at all. OpenAI's statement addresses pre-release access and vetting criteria, then moves on. It does not say whether OpenAI intends to join the shared severity framework, does not explain why it hasn't already, and does not dispute that it's the only major lab named in the [redeployment framework](/ai/redeploying-fable-5/) that has not signed on. That framework - Anthropic, Amazon, Google, and Microsoft scoring jailbreaks on capability gain, breadth, weaponisation ease, and discoverability - was explicitly built so the next Fable-5-style finding would get "a score instead of a phone call at 5:21pm." I flagged in July that whether it spread beyond the Glasswing coalition was the open question. Five months later, the answer is trending toward no, at exactly the moment a non-Glasswing lab has shipped the most cyber-capable model on record.

Question four - the reproducibility of the 0%-scope-violation claim - gets folded into the same non-answer. OpenAI reiterates that CAISI and UK AISI reviewed the eval pre-release but doesn't say whether either institute has independently reproduced the 0% figure adversarially, as opposed to reviewing OpenAI's own run of it.

## Why The Silence Is The Story

Put the four questions side by side and a pattern falls out. OpenAI answered comprehensively on anything that maps to a process it already had a paper trail for - pre-release access happened, so it can point to it. It answered partially on anything with a future-tense fix - criteria will be published, so name a timeline and move on. And it said nothing on the one question that would require taking a position relative to a rival's initiative: whether to join a framework Anthropic built, named after Anthropic's own program, in the aftermath of Anthropic's own crisis.

That is a reasonable commercial instinct and a real gap in industry coordination at the same time. A severity framework is only as useful as its coverage. If it scores jailbreaks for four labs and stays silent on the fifth - the one currently shipping the most cyber-capable model in the field - then the next disputed finding runs into exactly the ambiguity the framework was built to remove: no common vocabulary for how severe it is, no agreed tier of response, just a bespoke negotiation under time pressure. The framework's authors built it to prevent a repeat of Fable 5's eighteen days of downtime. Its usefulness depends on the labs actually in scope for Critical-tier findings choosing to be measured by it.

## The Process Comparison Is The Actual News

Set the substance aside for a moment and look at the mechanism, because it's the part I think matters more than any single answer here. The Fable 5 suspension arrived as a verbal directive at 5:21pm ET, with no published justification, forcing an immediate global shutdown that Anthropic first described entirely on its own terms. The public record for weeks was one company's account of a private conversation. I wrote at the time that the process looked troubling regardless of who turned out to be right on the merits - unaccountable power, exercised fast, with no visible chain of reasoning.

This is the opposite shape. A committee wrote a letter. It posted the letter. The company it was addressed to posted a response the same day. Nothing was suspended. No user lost access to anything. Whatever oversight is actually happening here - and pre-release evaluation by CAISI and UK AISI evidently was happening, before any of this became public - is happening through a channel that leaves a record two committees, one company, and any interested member of the public can all read at the same time.

I don't want to overclaim from one data point. A letter is a much lower-stakes instrument than an export control directive, and it's entirely possible this is act one of something that escalates - the letter itself gives OpenAI no deadline and no consequence for the framework question it ducked. But if the choice frontier labs and their overseers are implicitly making is between opaque emergency intervention after the fact and public, procedural pressure before anything ships broadly, the second one is the version I'd want to see win by default.

## What I'm Watching

**Whether "coming weeks" arrives.** OpenAI committed to publishing Daybreak's vetting criteria. That's a checkable promise with no fixed date, which is precisely the kind of commitment worth tracking until it's kept or quietly dropped.

**Whether OpenAI answers the framework question at all.** Continued silence is itself an answer. A committee follow-up letter that names the non-answer explicitly would be the next real move in this thread.

**Whether CAISI or UK AISI independently confirm the 0% figure.** OpenAI's response stopped short of claiming either institute reproduced the alignment number adversarially. Whether one of them does, and publishes anything about it, is the cleanest test of whether Astra's most reassuring claim survives contact with a party that isn't OpenAI.

**Whether this stays a letter.** The gap between "committee asks a question" and "government issues a directive" is exactly the gap Fable 5 fell through in three days. Astra clears a higher capability bar than the finding that triggered that directive. Whether the slower, public process holds this time, or whether patience runs out the way it apparently did in June, is the thread that ties this post back to the one that started it.

## Sources

- [Letter to OpenAI regarding Daybreak vetting criteria - Senate Commerce Committee](https://www.commerce.senate.gov/2026/9/letter-openai-daybreak-vetting-criteria)
- [Our response to the Commerce and Science Committees - OpenAI](https://openai.com/index/daybreak-congressional-response/)
- [GPT-6 Astra: A new generation of intelligence - OpenAI](https://openai.com/index/gpt-6-astra/)

## Related Reading

- [The Critical Threshold: What It Means That OpenAI Shipped a Cyber-Critical Model](/ai/gpt-6-astra-critical-threshold/)
- [Pulled From The Shelf: The Government Order to Suspend Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/)
- [Fable 5 Is Back: What Anthropic Learned From Eighteen Days Off The Shelf](/ai/redeploying-fable-5/)
- [The Forbidden Frontier: Claude Mythos and the Dawn of Restricted AI Power](/ai/claude-mythos-restricted/)
- [Why the AI Cyber Threat Is Rising](/ai/ai-cyber-threat-is-rising/)
- [AI Safety From First Principles: What Actually Matters vs What's Hype](/ai/ai-safety-first-principles/)
