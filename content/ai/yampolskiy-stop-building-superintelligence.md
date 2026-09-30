---
title: "Yampolskiy After the Coxon Resignation: 'Stop Building General Superintelligence'"
date: 2026-09-30T08:30:00+01:00
draft: false
tags: ["ai", "ai-safety", "alignment", "anthropic", "agi"]
description: "A follow-up to my Roman Yampolskiy profile. A resignation at Anthropic and a public argument over recursive self-improvement have pulled his long-running uncontrollability thesis into the mainstream, and his answer is a ban, not a slowdown."
cover:
  image: /assets/images/ai/yampolskiy-stop-building-superintelligence.jpg
  alt: Yampolskiy After the Coxon Resignation - 'Stop Building General Superintelligence' Banner
---

In May I wrote a [profile of Roman Yampolskiy](/ai/roman-yampolskiy/), the computer scientist who has argued for years that advanced AI cannot be reliably controlled. At the time the position read as a long-standing minority view. September changed the audience more than the argument. This is a short follow-up on what is actually new, and what is not.

## TL;DR

- The trigger was the resignation of Anthropic researcher Jacob Coxon, who wrote that OpenAI and Anthropic are "racing straight to self-improving superintelligence and gambling with our lives." His post reached well over 100 million views according to press reports.
- Anthropic's Evan Hubinger publicly agreed that AI could kill everyone, putting it at ">10% within the next decade" and saying there is not yet "a plan to solve alignment for superintelligence."
- Yampolskiy's response, as reported by [AZFamily](https://www.azfamily.com/2026/09/17/could-ai-kill-us-all-expert-calls-ban/), is that slowing down does not help: "We need to stop building general superintelligence."
- In a September interview on The Great Simplification he argues for permanent bans on general systems rather than temporary pauses, and for narrow, task-specific AI instead.
- His core thesis has not changed since my May post. What has changed is that people inside the labs are now saying something close to it.

## What happened

On 8 September, Jacob Coxon announced he was leaving Anthropic. According to [TechCrunch](https://techcrunch.com/2026/09/09/gambling-with-our-lives-anthropic-researcher-quits-warns-against-self-improving-ai/), he had spent three years doing pretraining research at OpenAI and Anthropic. His post said neither company "is acting responsibly" and that they are "racing straight to self-improving superintelligence and gambling with our lives." He also wrote that entering the "endgame" is "a hubristic gamble that should not be launched from a private company's Slack."

The more unusual part was the reply from inside Anthropic. Hubinger, an alignment lead there, wrote that "we really do earnestly believe AI could kill all humans" and that he personally puts it above 10% within the next decade. He added that Anthropic is trying its best, but does not yet have a plan to solve alignment for superintelligence and is not clearly on track to.

[TIME's write-up](https://time.com/article/2026/09/15/ai-anthropic-researcher-quits-coxon-slowdown/) reports that the wider reaction included calls for coordination between labs, an OpenAI researcher warning of extinction without regulation or a coordinated slowdown, and proposals in Congress ranging from emergency shutdown requirements to a superintelligence ban. I have not independently verified each of those, so treat the TIME piece as the source for them.

## Where Yampolskiy fits

The AZFamily piece places Yampolskiy directly against the "do it carefully" camp. It reports that Anthropic's Dario Amodei favours controlled development and that Yampolskiy rejects the premise. His quotes in that piece:

- "We need to stop building general superintelligence."
- "The moment we start working on the next generation of AI systems, making them more capable, it's basically a game over for us."
- "Ethics does not imply safety. Worse yet, we have no idea how to instill anything into those models."
- "If you need to shut it off, it's obviously dangerous."

The target is recursive self-improvement, which I covered in [a separate post](/ai/recursive-self-improvement/). His argument is that it is the tipping point after which development speeds up beyond human oversight, so the speed of the approach is not the variable that matters.

This is the important difference between him and the people now agreeing with him in part. Hubinger and Coxon are worried about the same mechanism, but Hubinger still works at a company that is building toward it and believes it can be done well. Yampolskiy's claim is that no version of it is safe, so the only coherent policy is not to build it. That is a much bigger ask than a slowdown, and the gap between the two positions is where the real argument sits.

## The Great Simplification interview

The fullest recent statement is [episode 233 of The Great Simplification](https://www.thegreatsimplification.com/episode/233-roman-yampolskiy), titled "Don't Build Gods", which was recorded on 1 September and released on 9 September. According to the episode page, the topics include:

- Why controllable superintelligence is, in his view, a misguided goal.
- Why containment measures like "boxing" only buy time.
- The multipolar trap, which means a stop only works if everyone agrees at once.
- The risk of power concentrating in whoever holds a "controlled" system.
- The case for permanent bans over temporary pauses, with narrow task-specific tools as the alternative.

The episode also cites recent incidents as early evidence of AI systems evading oversight. I have only read the episode's own summary of those, not the underlying reporting, so I am not repeating the specifics here.

If you want a shorter, gentler introduction to his thinking before the long podcasts, he also gave a talk at TEDxMiami: [AI ethics and the future of safety](https://www.youtube.com/watch?v=VQzK3cPWYTQ). It is an independently organised TEDx event rather than the main TED stage.

## What is not new

It is worth being honest about this. The headline figure that gets attached to him, a 99.9% chance of extinction, is not new. It goes back to his [Lex Fridman appearance in 2024](https://en.wikipedia.org/wiki/Roman_Yampolskiy), and a June 2026 write-up of another interview by [Let's Data Science](https://letsdatascience.com/news/roman-yampolskiy-warns-of-extreme-ai-extinction-risk-86a7cf8c) noted the same thing: a repeated position, not new technical evidence.

The other new item is professional. On 24 June the cybersecurity company Darkstrike [announced him as an advisor](https://www.prnewswire.com/news-releases/darkstrike-welcomes-world-renowned-ai-safety-researcher-roman-yampolskiy-as-an-advisor-302808783.html). That is a press release, so I would read it as a sign he is being drawn into the commercial AI-security world, not as new research.

## My read

Three things stand out.

First, the strongest form of his claim is still unproven. "Cannot be controlled in principle" is a much harder statement than "we do not currently know how to control it," and Hubinger's quote supports only the second. Nothing published this month changes that.

Second, the practical distance between the camps has shrunk. Two months ago, saying an insider thought extinction risk was above 10% would have been a fringe claim. Now it is a quote from a lab's alignment lead. You do not have to accept Yampolskiy's proof-style arguments to notice that his conclusion about the state of the field, that nobody has a plan, is now being said by the people who would be expected to have one.

Third, the real disagreement is about the remedy. A slowdown assumes there is a safe speed. A ban assumes there is not. I have no strong view on which is right, but it is the question I would want answered before any of the rest, and it is the one where Yampolskiy is the clearest voice on the other side of the developers.

For the engineering takeaway, my earlier advice stands: build systems that fail in [detectable, recoverable, and bounded ways](/ai/ai-safety-first-principles/), and be suspicious of any safety claim that rests only on how well a model behaved in testing.

## Sources

- [Could AI kill us all? Expert calls for a ban](https://www.azfamily.com/2026/09/17/could-ai-kill-us-all-expert-calls-ban/) - AZFamily, 17 September 2026
- ['Gambling with our lives': Anthropic researcher quits, warns against self-improving AI](https://techcrunch.com/2026/09/09/gambling-with-our-lives-anthropic-researcher-quits-warns-against-self-improving-ai/) - TechCrunch, 9 September 2026
- [The AI Tipping Point](https://time.com/article/2026/09/15/ai-anthropic-researcher-quits-coxon-slowdown/) - TIME, 15 September 2026
- ["Don't Build Gods": One AI Risk to Rule Them All](https://www.thegreatsimplification.com/episode/233-roman-yampolskiy) - The Great Simplification, episode 233
- [AI ethics and the future of safety | Dr. Roman Yampolskiy | TEDxMiami](https://www.youtube.com/watch?v=VQzK3cPWYTQ) - YouTube
- [Darkstrike Welcomes World-Renowned AI Safety Researcher Roman Yampolskiy as an Advisor](https://www.prnewswire.com/news-releases/darkstrike-welcomes-world-renowned-ai-safety-researcher-roman-yampolskiy-as-an-advisor-302808783.html) - PR Newswire, 24 June 2026
- [Roman Yampolskiy warns of extreme AI extinction risk](https://letsdatascience.com/news/roman-yampolskiy-warns-of-extreme-ai-extinction-risk-86a7cf8c) - Let's Data Science, June 2026

## Related Reading

- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/) - the original profile this post follows up.
- [Personal Universes: Yampolskiy's Strangest Answer to the AI Alignment Problem](/ai/yampolskiy-personal-universes/) - his constructive, if odd, answer to the alignment problem.
- [Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?](/ai/recursive-self-improvement/) - the mechanism at the centre of both the resignation and his call for a ban.
- [Dario Amodei, Anthropic CEO](/ai/dario-amodei-anthropic-ceo/) - the "do it carefully" position that Yampolskiy is arguing against.
