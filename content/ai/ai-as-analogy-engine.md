---
title: "AI as Analogy Engine: Synthesis, Invention, and the Combinatorial Frontier"
date: 2026-05-16T08:02:00+00:00
draft: false
tags: ["ai", "invention", "analogy", "discovery", "research", "intelligence"]
description: "The deepest misunderstanding about modern AI is that it merely retrieves memorised text. The more interesting truth is that large models form analogies, combine concepts, and explore conceptual relationships at a scale that may eventually industrialise parts of the invention process itself."
cover:
  image: /assets/images/ai/ai-analogy-engine.png
  alt: AI as Analogy Engine Banner
---

A common dismissal of modern AI goes like this: "It is just a fancy autocomplete. It memorises text and stitches it back together. There is no real understanding, only retrieval." It is a comforting story, and it has the shape of a critique that ought to be true. But spend enough time with frontier systems and a different picture starts to form. The thing that large models actually seem to be good at is not memorisation. It is something stranger and arguably more important: the formation of analogies, the combination of distant concepts, and the generation of conceptual relationships that were not explicitly present in any one place in the training data.

This is not a claim that AI is conscious, or that it understands the world the way humans do. It is a narrower and more interesting claim. AI is becoming an industrial-scale engine for searching the space of possible ideas. And if that capability continues to improve, it has implications for invention, science, and economic progress that most casual users of these tools have not yet fully internalised.

## TL;DR

- The "AI is just memorisation" framing is the single most common misunderstanding about what modern systems actually do.
- The deeper capability is synthesis: forming analogies between domains, combining unrelated concepts, and generating conceptual mappings that were never sitting in any one document.
- Analogy formation is one of the foundations of human intelligence. Many of our greatest inventions came from mapping one domain onto another.
- AI systems can search the space of possible analogies and concept-combinations far faster, more broadly, and more parallel than any individual human.
- This does not mean AI replaces human thought. It means AI may eventually act as a search engine over ideas, dramatically accelerating discovery in science, medicine, engineering, and beyond.

## Why analogy is the deep foundation of intelligence

Most of what we call insight, in retrospect, is analogy. A new problem is solved by recognising that it is structurally similar to an old, already-solved problem in a different domain. The mathematician Henri Poincaré called this the perception of "unsuspected relations between facts long known". Douglas Hofstadter spent a career arguing that [analogy is the core of cognition](https://www.basicbooks.com/titles/douglas-hofstadter/surfaces-and-essences/9780465018475/), not a peripheral feature.

The pattern shows up everywhere once you start looking for it. [Velcro was invented](https://en.wikipedia.org/wiki/Velcro) after George de Mestral examined burrs sticking to his dog's fur under a microscope and saw a mechanism worth copying. The Wright brothers studied [the mechanics of bird flight](https://en.wikipedia.org/wiki/Wright_brothers) before building wings that could carry a person. Artificial [neural networks were inspired by](https://en.wikipedia.org/wiki/Artificial_neural_network) the rough structure of biological neurons. [Sonar and radar](https://en.wikipedia.org/wiki/Sonar) draw on the same underlying idea as bat echolocation. [Evolutionary algorithms](https://en.wikipedia.org/wiki/Evolutionary_algorithm) borrow directly from natural selection. [Swarm intelligence algorithms](https://en.wikipedia.org/wiki/Swarm_intelligence) borrow from the collective behaviour of ants and bees.

In each case, a hard problem in one domain was cracked by noticing that it looked, at a structural level, like an already-solved problem in another domain. The invention was the mapping. The execution came afterwards.

This is what makes analogy so important. It is not decoration on top of reasoning. It is one of the primary engines of new ideas. And it is a kind of reasoning that, until very recently, no machine could do at scale.

## What synthesis actually means

To take this claim seriously, we need to be precise about the distinction between memorisation and synthesis. Memorisation is straightforward: a system stores a piece of training data and reproduces it on demand. Search engines do this. Older retrieval systems do this. It is useful but bounded - you can only get out what was put in.

Synthesis is different. It is the construction of something that was not present, as a unit, anywhere in the training data, by combining patterns from many places. A model that has read about both transformers and reservoirs of water can be asked to explain attention mechanisms in terms of dynamic memory, and produce a description that no specific source wrote. The mapping is new. The component concepts were familiar. The combination is the work.

The technical reason this is possible is roughly that modern LLMs do not store text verbatim in any practical sense. They store a vast set of statistical relationships between tokens and concepts, organised into a high-dimensional space where related ideas sit near each other. Generating output is closer to navigating that space than to looking up a record. When you ask a question, the model is not searching for a memorised answer. It is constructing a path through a conceptual geometry that was learned, not stored.

That geometry is the part that matters. It contains relationships between concepts that no single human laid out, because no single human read everything the model was trained on. The model did. And the structure that emerged is something genuinely new: a compressed representation of the relationships between very large numbers of ideas, available to be queried.

## What AI-generated analogies actually look like

This is easier to see in concrete examples. Ask a strong model to explain technical concepts and the analogies that come back are often compositional rather than copied. Three examples that illustrate the point:

- "A database index is like a book's table of contents - it does not contain the content itself, only the locations where each topic can be found, sorted so that finding any topic takes a number of steps proportional to the depth of the index rather than the size of the book."
- "Vector embeddings are coordinates in a conceptual space. Words and ideas with similar meanings end up near each other, and the geometry of the space encodes relationships - the direction from 'king' to 'queen' is roughly the same as the direction from 'man' to 'woman', because both directions encode the same conceptual shift."
- "Transformer attention mechanisms behave somewhat like a form of dynamic contextual memory. At each step the model decides which earlier parts of the input are relevant to the current decision, weighting them accordingly, rather than treating the input as a fixed-length state."

These are not phrases that were sitting somewhere in the training data waiting to be retrieved. They are constructions: mappings from one domain (databases, geometry, working memory) onto another (indexes, embeddings, attention). The mapping is the new thing. And the model is producing thousands of such mappings every second, across millions of conversations, for users in every imaginable domain.

It is worth pausing on the scale of that. Even if only a small fraction of these mappings are novel and useful, the absolute number is large. The space of plausible analogies between any two domains is vast, and most of it has never been explored by humans, because no individual human has had time to study both domains deeply enough. Models are starting to explore that space at industrial volume.

## The invention pipeline

A useful way to think about where this matters is to break invention down into its steps. Roughly, invention looks like:

1. **Observe patterns.** Notice regularities in some part of the world.
2. **Form analogies.** Map those regularities onto patterns from elsewhere.
3. **Combine concepts.** Construct a candidate new idea by composing existing ones.
4. **Generate hypotheses.** Turn the candidate into a testable proposal.
5. **Test ideas.** Run experiments, simulations, or arguments to see whether the proposal survives contact with reality.
6. **Refine successful outputs.** Iterate on what survived and discard what did not.

Look at where AI is today. Steps 1 to 4 are already being done by frontier models in domains as diverse as software architecture, organic chemistry, mathematics, and materials science. Step 5 remains mostly human, but is increasingly assisted by automated experimentation, simulation, and verification systems. Step 6 is still firmly in human hands for most fields, but the pattern is clear: the early conceptual stages of invention are the part that AI is best suited to scale.

This is exactly the part of the pipeline that has historically been the bottleneck. Experiments are expensive but tractable. Refinement is laborious but doable. The hard, scarce step has always been the leap - the moment when someone notices that this domain looks like that domain, and a new idea becomes possible. If that step can be partially automated, the throughput of the whole pipeline goes up.

## Why people underestimate this

The "AI is just retrieval" framing persists for understandable reasons. Most people's first encounter with these systems is asking them factual questions, and the answers sound suspiciously like things you could have looked up. The cases where models hallucinate look like retrieval failures, which reinforces the mental model that retrieval is what they were trying to do.

But this mistakes the failure mode for the underlying mechanism. A model hallucinating a paper that does not exist is not failing at lookup. It is succeeding at construction - generating a plausible-sounding paper from the statistical regularities of how papers are written - in a context where construction was the wrong tool. The same machinery that produces the hallucination is what produces the genuinely useful analogy when pointed at a problem where construction is what was needed. Hallucination and insight are powered by the same engine.

Once you see this, a lot of the public commentary about AI starts to look mis-aimed. "It is just predicting the next token" is technically true and almost completely misleading, in the same sense that "the brain is just firing neurons" is technically true and misses the level at which the interesting behaviour happens. Prediction at the token level, done well enough, requires the model to develop internal structure that captures relationships between concepts. That internal structure is the thing doing the work.

## AI as a search engine over ideas

The most useful framing I have found is this: a sufficiently capable AI system is, in effect, a search engine over the space of possible ideas. Not a search engine over documents, which is what we built in the previous era. A search engine over conceptual relationships, analogies, combinations, hypotheses.

This framing has consequences. It suggests that the most valuable use of AI is not to produce a single best answer to a question, but to explore the neighbourhood around a question. Generate twenty analogies and pick the one that opens the right door. Ask for the ten most distant fields whose techniques might apply to the current problem. Have the system propose mappings between disciplines that no individual has studied together. The output is not authoritative. It is a set of candidate paths through idea-space, most of which are dead ends but a small minority of which are valuable.

In this framing, the human role is judgment. AI proposes; humans dispose. AI suggests directions; humans evaluate which are worth pursuing. The throughput of the system depends on both sides. The proposal engine has scaled enormously in the last few years. The evaluation engine - humans, plus their tools - is now the bottleneck.

## Implications across domains

Several fields are starting to look different through this lens.

**Science.** [DeepMind's AlphaFold work](https://deepmind.google/discover/blog/alphafold-a-solution-to-a-50-year-old-grand-challenge-in-biology/) was the headline example of AI accelerating a specific scientific problem, but the broader pattern is more important. AI systems are increasingly used to propose hypotheses, suggest experimental designs, and connect findings across sub-disciplines that humans rarely span. The pace of hypothesis generation is no longer the limiting factor in many fields. The limiting factor is experimental capacity.

**Medicine.** [Drug discovery pipelines](https://en.wikipedia.org/wiki/Drug_discovery) increasingly use AI to propose candidate molecules by combining structural features from very different known compounds. The combinatorial space is too large for human chemists to search exhaustively. AI does not eliminate the wet lab - it directs it.

**Software engineering.** This is the field most software engineers can see directly. Modern coding assistants are not just typing faster. They propose architectural patterns by mapping the current problem onto similar problems they have seen across many codebases. The good ones are doing analogy formation at the architectural level. The job of the engineer shifts towards evaluating proposals, not generating them from scratch.

**Physics and mathematics.** AI systems are starting to suggest [proof strategies](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), conjecture new mathematical relationships, and propose connections between sub-fields that mathematicians rarely study together. The role of automated theorem provers as collaborators is no longer hypothetical.

**Economics and business.** Strategy is, in part, an exercise in analogy. "This market looks like that market." "This competitor's playbook resembles the one that worked in another industry." AI systems can hold many more such comparisons in mind simultaneously than any single strategist, which changes what kinds of strategic analysis are economically feasible.

**Education.** If AI is good at explaining one thing in terms of another, then education - which is largely the practice of finding the right analogy for the learner - is one of the natural beneficiaries. Personalised analogies, generated on demand, for each student's existing mental model, is a capability that did not exist before.

## What to be careful about

This is not a claim that AI is going to invent things on its own with no human in the loop. The proposal-evaluation distinction matters. AI systems will continue to produce many plausible-but-wrong ideas alongside the genuinely useful ones. Filtering remains hard. The cost of a confidently-asserted bad idea is real, and in some domains - medicine, safety-critical engineering, scientific publishing - the cost of pollution from low-quality machine-generated proposals is already a serious problem.

It is also not a claim that current AI has human-like understanding. It does not need to. The argument here is much weaker: that the geometry of concept-space encoded in large models is rich enough to support useful analogy formation, even without anything that we would recognise as subjective experience. Whether systems will eventually develop something more is a separate question. The combinatorial argument does not depend on it.

And it is not a claim that this will be fast or smooth. The history of technology is full of capabilities that took longer than expected to translate into impact, because the surrounding infrastructure - tools, institutions, skills, trust - took time to catch up. AI as an idea-search engine is in roughly the position that early electronic computing was in the 1950s: clearly powerful, obviously transformative in the long run, awkward and partial in the short run.

## The combinatorial frontier

Here is the part that I find the hardest to fully take in. The number of possible combinations of two concepts from a large knowledge base is roughly the square of the number of concepts. The number of three-way combinations is the cube. The space of possible analogies between pairs of domains, each with their own internal structure, is larger still. Almost all of that space has never been explored by anyone, because no individual human has had time.

What changes when a system can, in some sense, walk through that space at machine speed? Most of what it generates will be uninteresting. A small fraction will be genuinely valuable. The fraction does not need to be large. The space is so big that even a low hit rate, multiplied by enormous throughput, produces a meaningful flow of new ideas.

That is the real argument for why AI may matter more than the current discourse suggests. Not because it will replace what humans do, but because it will let us explore parts of idea-space that we previously could not reach. Many of the inventions that defined the last several centuries came from someone noticing a hidden relationship between two domains. The most interesting question about the next few decades is what becomes possible when that pattern-noticing is industrialised.

Humanity's greatest breakthroughs have often come from discovering hidden relationships between ideas. The story of the next century may well be the story of what happens when the search for those relationships stops being bounded by how many of them a single mind can hold at once.

## Related Reading

- [AI in Scientific Research: From AlphaFold to the Long Tail](/ai/ai-in-scientific-research-2026/)
- [Taste Is the New Scarcity](/ai/taste-is-the-new-scarcity/)
- [The Architect vs The Builder](/ai/architect-vs-builder/)
- [The Next Decade of AI](/ai/the-next-decade-of-ai/)
- [AI Hallucinations: Understanding and Mitigating](/ai/ai-hallucinations-understanding-and-mitigating/)
