---
title: "The Junior Developer Pipeline Problem: Where Do Tomorrow's Seniors Come From?"
date: 2026-04-28T00:12:00+01:00
draft: false
tags: ["ai", "career", "learning", "apprenticeship", "future-of-work", "leadership"]
description: "Most of the AI-and-developers conversation assumes a steady supply of senior engineers who can curate, review, and judge. But the work that used to produce those seniors is the work AI now does. Where does the next generation come from?"
cover:
  image: assets/images/ai/junior-developer-pipeline.jpg
  alt: Junior Developer Pipeline Problem Banner
---

*The views in this post are my own personal reflections on the industry as a whole, written in my own time. They are not about any specific employer, team, or colleague, past or present.*

Almost every confident take on the future of software engineering assumes a particular kind of person at the centre of it. A senior. Someone who can read a generated diff and feel which line is wrong before they can articulate why. Someone with taste, judgement, and a working theory of the system in their head. Someone who can curate, review, and steer fleets of agents.

I have written posts that lean on exactly this assumption. So has almost everyone else.

The question I keep getting stuck on is this. The work that produced those people - the boring tickets, the bug hunts, the weeks spent tracing a request through five services to figure out why a date was off by an hour - is the work AI now does in seconds. So what is the path? How does a 22-year-old in 2026 become the kind of engineer the next decade is supposedly going to need?

This post is me trying to think it through honestly rather than reach for a comforting answer.

## The bottom rungs of the ladder were load-bearing

For a long time, our profession had an unspoken apprenticeship. You joined as a junior, you got handed work that was important enough to matter and small enough to not break too much, and you learned by doing it badly and then less badly. You read a lot of code you did not write. You broke production once and remembered the lesson forever. You sat near someone better than you and absorbed how they thought.

The work itself was the curriculum. The boilerplate taught you patterns. The bug hunts taught you systems thinking. The code reviews taught you taste. Pair programming taught you the moves that nobody writes down. None of this was efficient and most of it was not even visible. It was just what happened when you were paid to be confused for two years.

Take that work away and the curriculum disappears with it. You can ship a feature with an agent on day one. You cannot become a senior engineer with an agent on day one, because the activity that made you one has been outsourced to the thing standing in for you.

This is the part that nobody who promises "AI just makes everyone 10x more productive" wants to address. Productivity for whom, on what timescale, at the cost of which feedback loop?

## What the boring work was actually teaching

It is worth being specific about what the lower rungs of the ladder were quietly producing. If we want to replace them, we should at least know what we are replacing.

- **Pattern recognition.** Writing your hundredth CRUD endpoint is dull, but it is also how you stop having to think about CRUD endpoints. The mental cost of routine work falls to zero, freeing your attention for the parts that are not routine. The first time you see a real architectural problem, you have the bandwidth to actually see it.
- **Systems intuition.** Tracing a bug through unfamiliar code, especially code written by people who are no longer around, is how you build a model of how systems decay, where seams form, and which abstractions survive contact with reality.
- **Taste.** Reading enough mediocre code teaches you what good code feels like, in a way that no style guide ever will. You learn to flinch at certain shapes.
- **Calibration.** The first few times you confidently shipped something that broke, you learned how often you are wrong, in which directions, and under what conditions. Without this, every engineer is permanently overconfident.
- **Trust.** Seniors trust each other because they have watched each other work through hard things. That social capital is built one shared bug at a time.

Each of these is built by doing, not by reading. And the doing is exactly what is now cheapest to delegate.

## The honest version of the new apprenticeship

I think the honest answer is that the apprenticeship is not gone, but it has moved. The activities that used to produce a senior engineer are not the same activities that will produce one in 2030. Pretending they are is a recipe for a generation of people with impressive output and no foundation.

If I had to sketch what the new path actually looks like, it is something like this.

**Reading replaces writing as the primary craft.** The volume of code a junior produces matters less than the volume they read, critique, and improve. The skill of the future is not "can I generate this" but "can I tell whether this is right". That is a reading skill. It is also a much harder one to teach, because it requires exposure to a lot of bad code and a lot of subtle bugs.

**Debugging is the new boilerplate.** When the agent writes the first draft, the human's job starts at the moment something does not work. Debugging is where systems intuition lives, and it is the one part of the loop that AI is still genuinely poor at when the failure modes are not in its training distribution. A junior who learns to debug agent output across unfamiliar systems is building the exact muscle the next decade needs.

**Architecture moves earlier in the career.** The first real decisions a junior used to make were about variable names and method boundaries. Now they are about what to ask the agent to build, where to draw a service boundary, and which tradeoff to accept. The architectural conversation arrives at year one rather than year five. That is either a gift or a disaster, depending on whether anyone is teaching the underlying concepts.

**The classroom is the codebase, not the course.** Bootcamps and degrees lose their grip on what counts as a good developer faster than they can update their syllabus. The actual training happens inside the codebase you ship to, and only if someone there is willing to let you struggle on purpose. Which brings us to the harder problem.

## A coordination problem the industry has not really named

Step back to the industry level for a moment. There is a structural tension that the sector as a whole has not yet thought through carefully. Across the industry, the short-term economics of agent-augmented seniors look more attractive per output unit than the cost of training juniors who need years of investment to become productive. Any individual organisation, looking only at this quarter, can rationally take the cheaper path.

The catch is that the cost of *not* training juniors is paid by the industry collectively, several years later, when the senior pipeline starts to thin. This is a classic coordination problem rather than a failure of any one employer. It is the kind of thing that is easy to spot in the abstract and hard to act on inside any particular budget cycle.

Two readings of this are both plausible. The pessimistic reading is that the incentives drift the industry into under-investment by default, and we only really notice in the early 2030s. The optimistic reading is that the organisations that figure out how to keep developing juniors during this transition will quietly accumulate a hiring advantage for the next decade. I find both readings worth taking seriously.

## What I would actually do if I were starting today

If I were 22 and entering this market, here is the version of the advice I would believe, rather than the version that flatters anyone.

- **Optimise for proximity to good engineers.** More than salary, more than title. The job that puts you next to one excellent senior who will let you watch them think is worth more than three jobs that pay better and stick you on a team of agents. Pick the human, not the brand.
- **Read more code than you write.** Every week, pick a real production system you respect and read it. Open source is full of these. Trace a feature end to end. Write down what you would have done differently and why. This is the closest thing to the old apprenticeship that you control yourself.
- **Practice debugging deliberately.** Most juniors learn debugging by accident, when their own code breaks. Now that the agent's code breaks instead, you have to seek out the practice. Take broken pull requests, broken builds, broken tests, and treat them as exercises. The skill compounds violently.
- **Build one thing without an agent every quarter.** Not because agents are bad, but because the muscles atrophy fast and you need to know what they feel like at full strength. Pick something small enough to finish and big enough to hurt.
- **Get good at writing.** Spec-writing, design docs, post-mortems. The bottleneck of a curator is communication, and the people who can write clearly about systems will be disproportionately valuable. This was always true. It is now table-stakes.
- **Learn one layer below where you work.** If you write web apps, learn how the runtime actually executes them. If you write SQL, learn how the query planner thinks. The layer below is where most production-grade bugs live, and it is the layer agents are weakest at, because there is less training data for it.

None of this is novel advice. It is mostly the same advice good engineers gave good juniors twenty years ago. What has changed is the urgency, because the default path no longer produces it as a side effect.

## Questions worth the industry asking out loud

If I were thinking about this purely as an industry-wide design problem, with no specific organisation in mind, the questions I think the sector will eventually have to engage with are roughly these.

- How does the industry as a whole make sure entry-level hiring does not quietly drift toward zero in the agent era?
- When juniors are hired, what kind of work produces future engineers, as distinct from work that simply produces tickets?
- How should organisations recognise mentorship and pairing as real engineering work rather than as an unmeasured tax on velocity?
- What new metrics, if any, capture the activities that produce future seniors - reading, debugging, design participation - rather than only current output?
- What does a modern apprenticeship actually look like, and who is responsible for designing one?

None of these have neat answers. They are the kind of questions that get easier with several years of collective experimentation across the industry, and harder the longer they go unasked.

## The part I am not sure about

I am genuinely uncertain whether the new apprenticeship can produce engineers as deep as the old one did, or whether something is being lost that we will only notice in retrospect. There is a version of this story where the loss is real and permanent, and a version where the new path produces a different but equally capable kind of senior, just trained on different signals.

I lean towards the second, but only just, and only if the industry collectively keeps investing in juniors during a period when the short-term spreadsheet does not always reward it. That is not really a technological question. It is a cultural and structural one, and the sector has historically been better at the technological kind.

The good news is that the pipeline is not a force of nature. It is something the industry builds, deliberately, and stops building when no one is paying attention. The encouraging version of this story is that enough people across enough teams notice the question early, and the apprenticeship reinvents itself rather than disappearing.

If you are a senior reading this, it is worth asking, in a personal capacity, whether the engineers who will eventually replace you are being trained anywhere at all. If you are a junior reading this, it is worth asking whether the path you are on is one that will turn you into the engineer you want to be, or whether you need to seek the missing parts deliberately on the side.

Neither question is comfortable. Both are worth sitting with.
