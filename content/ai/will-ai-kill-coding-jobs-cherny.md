---
title: "Will AI Kill Coding Jobs? Reacting to Claude Code's Creator and Three Charts"
date: 2026-05-26T08:00:00+01:00
draft: false
tags: ["ai", "coding", "anthropic", "future-of-work", "claude-code"]
description: "Boris Cherny, creator of Claude Code, sits down with Sky News and reacts to three charts about AI, jobs, and the future of software. A look at what is genuinely new in his argument, what is well-worn, and where the printing press analogy actually holds up."
cover:
  image: /assets/images/ai/will-ai-kill-coding-jobs-cherny.png
  alt: Will AI Kill Coding Jobs Banner
---

The "is the software engineer dead" genre has been running long enough that you can predict most of the takes before you read them. The interesting interviews are the ones where the person being interviewed is in a position to know something the rest of us do not. Boris Cherny, the creator of Claude Code at Anthropic, is one of those people. Sky News got him in front of three charts and asked him to react.

The conversation is worth watching not because it settles the question, but because it shows you which parts of the question are now actually settled in his head, and which parts he still treats as genuinely open.

## Video

### Will AI kill coding jobs? Claude Code's creator reacts to 3 charts

{{< youtube KRJzonECIY4 >}}

*Rowland Manthorpe of Sky News interviews Boris Cherny on coding's printing-press moment, the real demand driving the AI boom, and the AI risk that worries him most.*

## TL;DR

- Cherny is not predicting that software engineering goes away - he is predicting that it broadens, the way reading broadened after the printing press
- His personal anchor data point is that he has not hand-edited code in months and ships dozens of PRs a day from his phone; he is describing his own workflow, not a forecast
- The "coding is solved" framing is a deliberately strong claim and only makes sense if you read "coding" narrowly - the typing-out-of-known-patterns layer, not the design layer
- The job-title argument - "software engineer" giving way to "builder" - is the part that will age either very well or very poorly depending on how the next eighteen months go
- The risk he flags is not unemployment; it is the gap between what the tools can do and what the workforce is set up to do with them

## The printing press argument, made honestly

It is hard to talk about AI and coding without somebody reaching for the printing press analogy, and most of the time the reach is lazy. Cherny's version is sharper than most. Before the printing press, somewhere around 10% of Europeans could read and write. The technology did not destroy the scribe profession by holding scribes' wages flat. It destroyed the scribe profession by making literacy ordinary, and in doing so it created a much larger economy of writing than the scribes had ever served.

The claim he is making about coding is structurally the same. The set of people who can describe a working program in enough detail for a machine to execute it expands by an order of magnitude. The total volume of software produced goes up by more than that, because the unmet demand was always enormous. The people who used to be the bottleneck - professional engineers - do not disappear, but their role moves further up the stack.

The honest critique of this argument is not that the analogy is wrong. It is that the transition was not painless for the scribes who lived through it, and the transition will not be painless for the engineers who live through this one. He says as much in the interview.

## The "I have not edited code by hand" claim

This is the part that gets quoted, and it gets quoted for the wrong reason. The interesting thing is not the dramatic-sounding statement. The interesting thing is what kind of workflow makes that statement true.

What he is describing is an environment where the agent runs many tasks in parallel, where the human spends their time specifying, reviewing, and intervening, and where the medium of work is review-and-direct rather than write-and-debug. That is not a prediction about the future. That is how he works now. Whether that workflow generalises - whether the tooling, the model capability, the codebase characteristics, and the team norms exist to support it across the industry - is a separate question.

The shape of his workday is the artifact worth paying attention to, not the soundbite about phones and PR counts.

## What "coding is solved" actually means

The phrase is provocative on purpose, and it only holds up if you read "coding" in a specific narrow sense. The activity that is now largely solved is the bit between "I know what I want this code to do" and "the code does it". That is real progress. It is not the whole job.

The bits that are not solved by current tooling, even in his telling: deciding what to build, understanding why the previous attempt failed, integrating across systems that nobody has the full picture of, sustaining a codebase across years of changing requirements, and arguing with stakeholders about what is actually wanted. None of these go away because the typing bit got fast. Some of them get harder, because the typing bit being fast means more code gets produced and more decisions have to be made about it.

If you want a useful frame: the cost of writing code went down a lot. The cost of being wrong about what to write did not.

## The job title question

His prediction that "software engineer" gives way to "builder" inside a year is the cleanest forecast in the interview, and it is the one most likely to age badly. Job titles change slowly even when the underlying work has changed quickly, because they are anchored in HR systems, in hiring norms, and in the self-image of the people doing the work.

What is more likely than the title disappearing is the title fragmenting. The senior end - the people doing system design, architectural judgment, cross-team integration - keeps the engineer title and the engineer salary. The junior end - the people who used to be hired to write code - either gets absorbed into the agent-driven workflow, or it gets repriced down to where small businesses that never had a developer can now have one.

This is consistent with the broader [agent-first architecture](/ai/agent-first-architecture-engineer-as-curator/) shift the field has been moving toward for the last eighteen months, and it is more interesting than the binary "engineers are dead" framing.

## The risk he actually flags

The thing he singles out as the risk he worries about is not unemployment. It is the gap between the tools and the workforce. If the tools improve faster than the workforce can adapt, the people who already know how to use them well capture a disproportionate share of the value, and the people who do not are left behind not because they cannot do the work but because the way the work is done has changed under them.

That is a workforce problem, not a technology problem, and the remedies for it are unglamorous: retraining, accessible tooling, hiring practices that do not gatekeep on prior agent experience, and education systems that adapt fast enough to matter. None of those are things Anthropic can fix from inside Anthropic.

## The reaction

The substance of what Cherny is saying is not really controversial inside the industry any more. The shape of the workday he describes is recognisable to anyone who has spent the last year actually using these tools well. The disagreement, when there is disagreement, is about the timing - whether the transition arrives this year, next year, or over the next five.

The interview is most useful as a snapshot of where the conversation has moved to. Eighteen months ago this would have been a debate about whether AI could write code at all. Now it is a debate about which parts of the engineering role survive in something resembling their current form. That shift is the actual news, even if no single soundbite in the segment captures it.

## Related Reading

- [Agent-First Architecture: The Engineer as Curator](/ai/agent-first-architecture-engineer-as-curator/)
- [Architect vs Builder: Where the Job Title Goes Next](/ai/architect-vs-builder/)
- [The Automation Paradox: Why More AI Makes Human Judgment More Valuable](/ai/automation-paradox/)
- [The Junior Developer Pipeline Problem](/ai/junior-developer-pipeline-problem/)
- [Top 5 Human In-Demand Jobs in 10 Years](/ai/human-in-demand-jobs/)
