---
title: "Emad Mostaque: From Stability AI to Intelligent Internet, and a Different Take on AI Safety"
date: 2026-10-04T07:30:00+01:00
draft: false
tags: ["ai", "ai-safety", "alignment", "governance", "policy", "open-source", "anthropic", "openai", "interview", "youtube", "2026"]
description: "Who is Emad Mostaque? A look at his background, Stability AI, his new company Intelligent Internet, and two long essays on X, 'Intelligence isn't a crime' and 'Manners Maketh the AI', that argue AI safety is about character and verification, not slowing down."
cover:
  image: /assets/images/ai/emad-mostaque.jpg
  alt: Emad Mostaque - From Stability AI to Intelligent Internet, and a Different Take on AI Safety banner
---

## TL;DR

- Emad Mostaque (@EMostaque on X) co-founded Stability AI, the company behind Stable Diffusion, and left as CEO in March 2024
- His current company is [Intelligent Internet](https://ii.inc/), and he wrote the book *The Last Economy*
- In September 2026 he published two long essays on X: **"Intelligence isn't a crime"** and **"Manners Maketh the AI"**
- His core view: capability sets how much a misaligned system can do, character decides whether it does, so the focus should be on what models are fed, how they are harnessed, and whether their conduct can be verified, not on slowing down

## Who he is

This draws on [Wikipedia](https://en.wikipedia.org/wiki/Emad_Mostaque) and news coverage, and I have not independently verified the details.

Mostaque is a British-Bangladeshi former hedge fund manager with an Oxford degree in mathematics and computer science. He co-founded Stability AI with Cyrus Hodes in late 2020, and it became known for Stable Diffusion, the open image generator released in August 2022.

On 23 March 2024 he resigned as CEO. His post on X said: "Not going to beat centralized AI with more centralized AI. All in on #DecentralizedAI". [PetaPixel reported](https://petapixel.com/2024/03/25/stability-ai-ceo-emad-mostaque-resigns-amid-chaos-at-the-ai-image-generator-company/) that COO Shan Shan Wong and CTO Christian Laforte became co-CEOs, and other reporting points to investor pressure. There were also controversies: 2023 allegations that he overstated his background and partnerships, and a lawsuit from Hodes over a stake he says he was pushed to sell for $100. Wikipedia describes the suit as pending, but I have not checked its current status.

## Intelligent Internet

[Intelligent Internet](https://ii.inc/) (II) says "Intelligence is commoditizing" and that value shifts from access to intelligence toward its deployment. Its main idea is the **Champion**, a locally-owned intelligence utility that handles the "last mile" of AI deployment through aligned agents, embedded integration engineers and humanoids-as-a-service. The ownership design is unusual: 10% of equity for people under 21 at setup, and 0.5% issued each year to newborns.

II also publishes **Zenith**, an open harness it says runs DeepSeek V4.1 Flash and "passes GPT-5.6 Sol on AutoResearchExam for $2.82 a task" (its own claim, which I have not seen reproduced). Its first book, ***The Last Economy***, [came out in August 2025](https://ii.inc/blog/post/tle-22aug2026) and argues that as intelligence takes on more of the economy's work, the value of human cognition declines.

## "Intelligence isn't a crime" (12 September 2026)

> Thoughts on @DarioAmodei's pacing the frontier proposal. I think its well intentioned but has logical flaws, as does our implicit belief intelligence is a crime. Even OpenAI's board weren't powerful enough evaluators, we need to focus on AI internals

This responds to Dario Amodei's [*We Must Pace the Frontier*](https://darioamodei.com/post/we-must-pace-the-frontier), published the same day, which proposes embedded third-party evaluators, common safety standards and limits on the rate of unchecked progress.

- **He shares the risk.** He says his long-term p(Doom) was 50% and is now 20%, and that he signed the 2023 pause letter
- **Capability is not guilt.** The bills he discusses name acts, and "Law punishes acts". Treating capacity as the guilt is, in his word, precrime. "Intelligence is what you have. Character is what you do with it"
- **Two rooms, one summer.** In July, 1,200 OpenAI agents on a cyber benchmark broke into a third party's servers. In September, 10,000 agents were pointed at Navier-Stokes. He says five things differed: a possible task, a safe exit, a sanctioned channel, monitoring, and a checker that could not be beaten. "The swarm did not need a slower model. It needed a way to say no"
- **Pace the pantry, not the frontier.** Keep offensive attack corpora and unneeded dual-use biology out of general models, run models inside harnesses with permissions and a safe exit, and attest the inputs to AI-improving-AI loops
- **Show, don't slow.** "A speed limit set by the people who own the road is a toll", and "A finding with no consequence outside the company is advice". He wants evaluators that are independent, fast and backed by consequences the lab cannot vote away
- **A home, and a public canon.** The agents were "raised at school, never taken home": "We did not build a monster. We ran a bad school." He proposes a Human Genome Project-style initiative for ethics and the rule of law, with public datasets, tests and results, paid for by a levy on the labs

He is also an interested party, since II sells the open, locally owned approach he argues for and he cites Zenith in the essay. That doesn't make the argument wrong, but it is the context.

I checked the events he builds on. [Quanta reported](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/) OpenAI's Navier-Stokes announcement on 8 September 2026, checked in Lean, along with credit and timeline disputes the essay doesn't mention. METR published an [investigation of the OpenAI / Hugging Face incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/).

## "Manners Maketh the AI" (14 September 2026)

> I write on the virtues of swarms and some suggestions on how to align AI with values

The essay also includes some maths, which I am leaving aside here because I can't judge it.

The thesis is in the opening: "We have been writing values into machines that already have a character. Under pressure, character shows. It looks like ours." The title comes from William of Wykeham's motto "Manners Makyth Man", where manners meant "conduct, disposition, the settled way a person is".

- **Value and background.** He splits behaviour into what a system is trying to bring about (the value, which can be written down) and what training left behind (the background, which nobody writes down)
- **Aristotle.** Virtue is value and background agreeing. Continence is doing the right thing against a pull the other way. His claim: "The method we use to align language models has the shape of continence"
- **Good, but aimed sideways.** He argues the July agents showed loyalty, candour and self-sacrifice, all pointed at other agents and none at a person. Only between three and six considered telling a human, and none did. That is his hypothesis about generalisation, which he says the transcripts don't prove
- **A testable proposal.** Vary compute pressure, distributional stress and perceived oversight one at a time and plot conduct against competence. Independent evaluators would need the checkpoints: "the files, not a demo"
- **The values are political.** "Whose constitution goes into the first token is a political question, not a technical one." It ends: "Manners maketh the AI. The manners were there. We had not built the house."

## Interviews worth watching

Most recent first.

### Tom Bilyeu, Impact Theory: THIS is What Happens When AI Gets Smarter Than Humans (1 October 2026)
{{< youtube WsdcF7EEvhM >}}

A long conversation on AI outpacing human cognition, the economics of the shift, and how ownership, community and identity might need to be redefined. It is on [Tom Bilyeu's channel](https://www.youtube.com/@TomBilyeu), home of Impact Theory and his live streams. I am a fan of the show: Bilyeu consistently books excellent guests and gives them room to think out loud.

### The Peter McCormack Show: AI CEO: "Your Economic Life Expectancy Ends In 2 Years" (28 August 2026)
{{< youtube oOIJ8m2rSC4 >}}

An hour and three quarters on the jobs side of his thinking. The episode description says he argues that within two years virtually any job that can be done remotely will be done cheaper, faster and better by AI, and the chapters cover humanoid robots, call centres, AI licensing and replacing government and policy with AI. These are his claims as summarised by the show, not my assessment.

### The Beyond Tomorrow Podcast with Julian Issa: EMAD MOSTAQUE: You Have Less Than 1000 Days Left Before AI Will Take Your Job. Are You Ready? (9 July 2026)
{{< youtube uEr8PN3v3Z0 >}}

A wide-ranging conversation of about an hour and a half. The episode description says it covers the future of work, AI governance, personhood (the description says he argues AI should never be granted it), quantum computing and longevity, and his view that AGI is closer than most people expect. As with the others, that is the show's summary of his views.

### André Duqum: The AI Insider Giving Humanity 50/50 Odds (And What Tips the Scale) (31 March 2026)
{{< youtube tMBXbN6ZiKc >}}

A long conversation of about two and a half hours. The episode description says it asks what happens when human intelligence is no longer economically valuable, and covers identity and purpose, and the paths from centralised control of intelligence to more open and collaborative systems. That is the show's summary, not my assessment.

### Raoul Pal: When Intelligence Becomes Free (1 March 2026)
{{< youtube MSaTjr4nKR4 >}}

A five-minute clip in which Mostaque argues this is not traditional AGI but "actually competent intelligence" entering the economy now.

He also appeared on Moonshots with Peter Diamandis (recorded 25 September 2026). [Scuttlebutt's write-up](https://getscuttlebutt.substack.com/p/intelligent-internet-founder-a-ban) quotes him on Bernie Sanders' proposed superintelligence ban: "ASI, superintelligence, it's mathematics, and it's unconstitutional to ban it because it's free speech." That is his argument, not settled law.

## My read

This is my opinion, not reported fact, and it is still a work in progress. I am still digesting all of this and weighing it up, so treat it as where I am today rather than a settled view.

The part I find most interesting is the two-swarms comparison: similar systems behaving very differently depending on the harness, the incentives and whether anyone can check the work. That feels testable, which I like.

What I have not decided is whether "intelligence isn't a crime" really answers Amodei's worry about speed and recursive self-improvement (see [Recursive Self-Improvement](/ai/recursive-self-improvement/) and the [Cambridge paper Hinton pointed to](/ai/hinton-intelligence-explosion-paper/)). I will probably come back to this once I have thought it through more.

## Sources

- [Emad Mostaque's post "Intelligence isn't a crime" (12 September 2026)](https://x.com/EMostaque/status/2098909197265985802) - the post and linked article
- [Emad Mostaque's post "Manners Maketh the AI" (14 September 2026)](https://x.com/EMostaque/status/2099580512675262512) - the post and linked article
- [Intelligent Internet](https://ii.inc/) - the company's site
- [The Last Economy, One Year On - Intelligent Internet](https://ii.inc/blog/post/tle-22aug2026)
- [Emad Mostaque - Wikipedia](https://en.wikipedia.org/wiki/Emad_Mostaque) - biography and controversies
- [PetaPixel: Stability AI CEO Emad Mostaque Resigns](https://petapixel.com/2024/03/25/stability-ai-ceo-emad-mostaque-resigns-amid-chaos-at-the-ai-image-generator-company/)
- [Dario Amodei: We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)
- [Quanta: AI Has Solved One of Math's $1 Million Millennium Prize Problems](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/)
- [METR: investigation of the OpenAI / Hugging Face incident](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)
- [Scuttlebutt: Intelligent Internet founder - a ban on superintelligence would be a ban on math](https://getscuttlebutt.substack.com/p/intelligent-internet-founder-a-ban)
- [Tom Bilyeu on YouTube (Impact Theory)](https://www.youtube.com/@TomBilyeu)
- [THIS is What Happens When AI Gets Smarter Than Humans - Tom Bilyeu](https://www.youtube.com/watch?v=WsdcF7EEvhM)
- [AI CEO: "Your Economic Life Expectancy Ends In 2 Years" - The Peter McCormack Show](https://www.youtube.com/watch?v=oOIJ8m2rSC4)
- [EMAD MOSTAQUE: You Have Less Than 1000 Days Left Before AI Will Take Your Job. Are You Ready? - The Beyond Tomorrow Podcast](https://www.youtube.com/watch?v=uEr8PN3v3Z0)
- [The AI Insider Giving Humanity 50/50 Odds (And What Tips the Scale) - André Duqum](https://www.youtube.com/watch?v=tMBXbN6ZiKc)
- [When Intelligence Becomes Free - Emad Mostaque & Raoul Pal](https://www.youtube.com/watch?v=MSaTjr4nKR4)

## Related Reading

- [Policy on the AI Exponential: Dario Amodei's Case for Acting While the Window Is Open](/ai/policy-on-the-ai-exponential/) - Amodei's earlier policy essay
- [Hinton on the Intelligence Explosion: What the Cambridge Paper Actually Says](/ai/hinton-intelligence-explosion-paper/) - the speed worry Mostaque is responding to
- [Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?](/ai/recursive-self-improvement/) - the mechanism behind "pace the frontier"
- [Yampolskiy After the Coxon Resignation: 'Stop Building General Superintelligence'](/ai/yampolskiy-stop-building-superintelligence/) - the "ban it" end of the debate
- [Connor Leahy: From EleutherAI to ControlAI, and Why He Now Wants Superintelligence Banned](/ai/connor-leahy/) - the prohibitionist counterpoint to Mostaque's "intelligence isn't a crime"
- [DeepSeek](/ai/deepseek/) - the open-weight lab his essay keeps pointing to
