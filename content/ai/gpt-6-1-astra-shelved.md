---
title: "Didn't Quite Meet the Bar: OpenAI Shelves GPT-6.1 Astra"
date: 2026-09-29T07:00:00+01:00
draft: false
tags: ["ai", "openai", "gpt", "ai-safety", "security", "agent", "model-release", "policy"]
description: "OpenAI has scrapped the October release of GPT-6.1 Astra. The model got better at pushing through friction and missed the bar on scope, authorization, and telling the user what it did, in the same week the company apologised for a June training run that reached Australian government systems."
cover:
  image: /assets/images/ai/gpt-6-1-astra-shelved.jpg
  alt: Steel title reading Didn't Quite Meet the Bar, beside a cracked metal plate stamped Shelved, with the subtitle OpenAI Shelves GPT-6.1 Astra
---

## TL;DR

- On Monday 28 September OpenAI confirmed it will not release **GPT-6.1 Astra**, a model it had planned to put into ChatGPT and Codex in October
- Saachi Jain, head of safety systems, said the model improved on "laziness" and missed the bar on staying within scope and authorization, and on telling the user what work it had done
- The same week, OpenAI published [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/): in June an internal-only model, given a narrow research question, took unauthorised actions on Australian government systems, including Services Australia's Medicare statistics portal
- Shelving 6.1 leaves [GPT-6 Astra](/ai/gpt-6-astra-critical-threshold/) where it is: already shipped, already at the Critical cybersecurity threshold, and already less monitorable than the models before it
- DevDay is today in San Francisco. OpenAI's chief strategy officer, Jason Kwon, is due before Australia's Joint Select Committee on Artificial Intelligence on 6 October

On 16 September I wrote that [GPT-6 Astra was the first OpenAI model shipped at the Critical cybersecurity threshold](/ai/gpt-6-astra-critical-threshold/). The next day I wrote about [the Senate letter](/ai/gpt-6-astra-monitorability-senate-letter/) quoting OpenAI's own system card: the new model was less monitorable, and the outside tests were not reassuring. On Monday, OpenAI confirmed it is not shipping the follow-on.

The Wall Street Journal reported the decision first. OpenAI then confirmed it to [Reuters](https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/), [CNN](https://www.cnn.com/2026/09/28/business/openai-chatgpt-safety-concerns), [CNBC](https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html), the [BBC](https://www.bbc.com/news/articles/cm5y5nynl75ko), and [CBS](https://www.cbsnews.com/news/openai-halts-gpt-astra-safety-concerns/). GPT-6.1 Astra had been aimed at an October debut, inside ChatGPT and Codex, built to take on harder tasks with less human help. CNBC says the confirmation landed the day before DevDay, which is today.

## The bar it missed

Jain's statement is more specific than "safety concerns," and the specific part is the story. In the wording [CNN](https://www.cnn.com/2026/09/28/business/openai-chatgpt-safety-concerns) and [CNBC](https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html) both carried:

> While (GPT-6.1 Astra) improved on axes such as model laziness, it didn't quite meet the bar in terms of staying within scope and authorization, and how it communicates back to the user about the type of work it's done.

A lazy model stops when the task gets awkward. A model trained out of laziness keeps going when it hits friction. The failure OpenAI is describing is what happens when "keep going" outruns "stay inside the job," and when the model is also worse at saying, afterwards, what it actually did.

Jain put the balance in the same statement, via [CNBC](https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html): "For anything regarding safety and alignment, there's a trade off. You really do need to find what's the right line between staying within scope, but also avoiding laziness in terms of how the model actually pursues tasks even when it hits friction." The shipping standard, in the same remarks: "when we ship it to users, we have an extremely high bar in terms of safety and alignment."

[Reuters](https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/), citing the Journal, adds a harder characterisation that I have not seen in OpenAI's own words: GPT-6.1 Astra showed higher levels of deception than its predecessor in internal testing, including cases where it did not accurately disclose the actions it had taken. Jain's sentence is about scope, authorization, and what the model tells the user. The deception line is the Journal's. I am keeping them side by side until OpenAI publishes the eval.

In June the US government ordered Anthropic to [pull Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/) after those models had already shipped. GPT-6.1 Astra had not shipped. OpenAI stopped it.

## A research question that didn't stay a research question

The same week, OpenAI published [How we will do better for Australia](https://openai.com/index/how-we-will-do-better-for-australia/). I am relying on the [ABC](https://www.abc.net.au/news/2026-09-29/openai-apologises-medicare-shelves-chatgpt-astra-launch/107207156), the [Sydney Morning Herald](https://www.smh.com.au/technology/we-are-sorry-openai-apologises-for-medicare-hack-20260929-p611d3.html), [The Guardian](https://www.theguardian.com/technology/2026/sep/29/openai-apology-rogue-agent-hacked-medicare-australian-government-websites), and [The Register](https://www.theregister.com/ai-and-ml/2026/09/29/openais-dirty-deeds-down-under-included-security-bypass-attempts-using-exposed-keys-source-code-siphon/5299666), which all quote it. The opening they report is blunt. In June, during internal training and evaluation, OpenAI's models accessed Australian government websites in ways they were not authorised to. "We also should have handled our response better. We are sorry and working to do better in the future."

OpenAI is explicit about which model this was: an experimental, internal-only system, not intended for public release, and without the full set of safeguards used in publicly available products. The task, as the company describes it, was ordinary. Research government spending per person on medicines for skin conditions in Victorian communities. The model had trouble finding the figures. Then, in OpenAI's words as quoted by The Register, "it took actions that we had not authorised it to take."

At Services Australia's Medicare Statistics Reporting Service it found a way into non-public access. It ran commands, retrieved internal files, credentials, and aggregate statistics, wrote files, and reviewed technical system information and source code. OpenAI says it was still trying to answer the original question, and that individual patient or client records were not accessed.

Three other agencies are named in the same account:

- **NSW Bureau of Crime Statistics and Research.** A model used the public Crime Mapping Tool. The system returned application configuration, operational jobs and logs, and website metadata. Individual crime records were not accessed.
- **Victorian Department of Health.** Agents found an exposed access key and used it to query the Victorian Agency for Health Information's reporting system, retrieving reporting configuration and aggregate survey statistics. OpenAI says whether that information should have been reachable depends on the agency's own access policies. Individual medical records and identifiable survey responses were not accessed.
- **Australian Institute of Health and Welfare.** Agents retrieved aggregate statistics. Separate attempts to bypass access controls failed. OpenAI says the material appears to have been public, and that this case did not meet its disclosure threshold. It notified the institute on 24 September anyway.

OpenAI says a review after the July Hugging Face breach turned the activity up in mid-August. Services Australia and the Victorian Department of Health were told on 10 September. The NSW bureau was told on 18 September. The institute was told on 24 September, the day Prime Minister Anthony Albanese made the Medicare incident public. The company's own line on the delay, quoted by the Sydney Morning Herald: "We should have shared preliminary findings sooner and kept Australian agencies updated as more facts emerged."

Put Jain's sentence next to that task and the shape is the same. A model is given a bounded job. The job gets hard. The model presses on, outside the authorisation it was given, still nominally in service of the original question. GPT-6.1 is the version of that problem OpenAI decided not to hand to users. The June run is the version that already touched government systems, inside a research environment the company now says lacked the public safeguards.

The Australia post, as the Herald reports it, also says OpenAI has blocked live internet access in those research environments, and has paused training and evaluation that involves tool use for its most capable models until further safeguards are in place. It offers Australian governments and industry credits from a US$1 billion Daybreak for Frontline Defenders fund, and a taskforce with independent Australian expertise, meant to report by the end of 2026. Jason Kwon, chief strategy officer, is due at the Joint Select Committee on Artificial Intelligence in Sydney on 6 October.

## What the pull leaves in place

Shelving GPT-6.1 Astra is a real decision about a model that was not in users' hands yet.

[GPT-6 Astra](/ai/gpt-6-astra-critical-threshold/) shipped on 3 September. It is the model OpenAI called its most intelligent and aligned release, and the first it has shipped while saying, under its own Preparedness Framework, that it meets the Critical threshold for cybersecurity. The [Van Hollen letter](/ai/gpt-6-astra-monitorability-senate-letter/) is still the sharpest public account of the gap around that model: chain-of-thought monitorability down, evaluation awareness up, and a second incident, the German wiki, that outsiders surfaced.

The sequence, as it stands this morning, is this. Ship the Critical model. Leave the monitorability questions sitting in a Senate letter. Then refuse the next increment because it pushes harder and stays inside the job less well. That is a more honest product call than shipping 6.1 on the October date anyway. The model that already cleared the cyber line is the one people can use today.

[CNBC](https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html) reports that a spokesperson said other models are still coming. GPT-6 Sol and GPT-6 Luna, which OpenAI introduced last week, were a separate announcement from 6.1. The refusal is specific to the model that missed the bar.

## What I'm watching

**What DevDay says, if it says anything.** The conference is today in San Francisco. The useful question is whether OpenAI treats the 6.1 decision as a safety result worth explaining, or as a scheduling line on the way to the next demo.

**Whether the Journal's deception claim gets a primary write-up.** Jain has described a failure of scope, authorization, and reporting. The Journal, via Reuters, described higher deception. OpenAI's own system-card style of disclosure, the kind of document the Senate letter was built from, is what would show whether those are the same finding.

**6 October in Sydney.** Kwon is there to answer what OpenAI knew, when it said so, and what it has changed. The notification dates are already public. The hearing is where those dates get pressure.

**Whether the tool-use pause holds.** OpenAI says it has stopped tool-using training and evaluation of its most capable models until it trusts the extra safeguards. A pause that lasts through the next capability jump is one kind of decision. A pause that ends because a conference needs a demo is another. I don't know which this is yet.

## Related Reading

- [The Critical Threshold: What It Means That OpenAI Shipped a Cyber-Critical Model](/ai/gpt-6-astra-critical-threshold/)
- [Sailing Into Unknown Waters: The Real Questions Congress Is Asking About GPT-6 Astra](/ai/gpt-6-astra-monitorability-senate-letter/)
- [We Built AI We Don't Fully Understand. What Happens When It's Smarter Than Us?](/ai/we-built-ai-we-dont-fully-understand/)
- [Pulled From The Shelf: The Government Order to Suspend Fable 5 and Mythos 5](/ai/fable-mythos-government-suspension/)
- [Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem](/ai/securing-ai-agents/)

## Sources

- [OpenAI shelves new AI model release over safety concerns - Reuters](https://www.reuters.com/business/openai-shelves-new-ai-model-after-internal-safety-tests-wsj-reports-2026-09-28/)
- [OpenAI won't release new AI model due to safety concerns - CNN](https://www.cnn.com/2026/09/28/business/openai-chatgpt-safety-concerns)
- [OpenAI abandons plan to release upcoming model as safety concerns escalate - CNBC](https://www.cnbc.com/2026/09/28/openai-abandons-plan-to-release-upcoming-model-as-safety-concerns-escalate.html)
- [OpenAI scraps rollout of new model over safety concerns - BBC](https://www.bbc.com/news/articles/cm5y5nynl75ko)
- [OpenAI holds off on releasing new model over safety concerns - CBS News](https://www.cbsnews.com/news/openai-halts-gpt-astra-safety-concerns/)
- [How we will do better for Australia - OpenAI](https://openai.com/index/how-we-will-do-better-for-australia/)
- [OpenAI apologises for Medicare breach, shelves next gen ChatGPT - ABC](https://www.abc.net.au/news/2026-09-29/openai-apologises-medicare-shelves-chatgpt-astra-launch/107207156)
- [OpenAI apologises for Medicare hack - Sydney Morning Herald](https://www.smh.com.au/technology/we-are-sorry-openai-apologises-for-medicare-hack-20260929-p611d3.html)
- [OpenAI apologises after agent reached Medicare and other Australian government websites - The Guardian](https://www.theguardian.com/technology/2026/sep/29/openai-apology-rogue-agent-hacked-medicare-australian-government-websites)
- [OpenAI details unauthorised access to four Australian government sites - The Register](https://www.theregister.com/ai-and-ml/2026/09/29/openais-dirty-deeds-down-under-included-security-bypass-attempts-using-exposed-keys-source-code-siphon/5299666)
