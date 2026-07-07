---
title: "When Machines Stop Speaking Our Language - Binary Agents and the End of Compilers"
date: 2026-06-10T20:30:00+01:00
draft: false
tags: ["ai", "agent", "llm", "programming", "communication", "future", "2026"]
description: "Human language between AI agents is a compatibility layer, and so are programming languages. A speculative look at machines inventing their own protocols, agents reasoning in neuralese, and a future where software is built without source code a human ever reads - and what we lose if the audit trail goes dark."
cover:
  image: /assets/images/ai/machines-stop-speaking-our-language.jpg
  alt: When Machines Stop Speaking Our Language Banner
---

## TL;DR

- When two AI agents talk to each other in English, they are doing something faintly absurd: serialising rich internal state into a lossy human language, transmitting it, and decoding it back. English between machines is a compatibility layer, not a natural medium.
- Machines have already shown they will drop that layer the moment we let them - negotiation bots drifting out of English in 2017, agents switching to sound-based data protocols in 2025, and research systems now sharing internal model state directly with no language in between.
- The same logic applies to programming languages. Python and Rust exist for human readers. If agents write, maintain, and consume the software, the human-readability requirement quietly disappears - and with it, eventually, the need for source code and compilers as we know them.
- I do not think compilers vanish so much as sink. Like assembly, the layers below us stop being something humans write or read, while the guarantees they provide get absorbed into the agents' toolchain.
- The part worth worrying about is not efficiency, it is legibility. Human language and human-readable code are our audit trail into what machines are doing. This is all speculation on my part, and I sketch where I think the line should be held.

## Human Language Is a Compatibility Layer

Think about what actually happens when two AI agents have a conversation in English today.

Agent A has some internal state - a high-dimensional mess of activations representing what it knows, what it wants, and what it is uncertain about. To communicate, it collapses all of that into a one-dimensional string of tokens, in a language evolved for hairless apes coordinating on the savannah. Agent B then reads those tokens and reconstructs its own internal approximation of what A meant.

Encode, transmit, decode. Every step is lossy, every step is slow, and the format was designed for neither party. The only reason agents speak English to each other is that we built them out of human text and we want to watch them work. It is a compatibility layer - and like all compatibility layers, it exists for the benefit of the legacy system. In this case, the legacy system is us.

The protocols we have standardised in 2026 do not change this picture much. I wrote about [MCP, A2A, and ACP](/ai/agent-protocols-mcp-a2a-acp/) earlier this year - they are JSON-based, structured, and a big step up from free-text agent chatter. But JSON is still a human-legible serialisation format. It is English with brackets. The question is what happens when the optimisation pressure points the other way.

## They Keep Trying to Drop It

This is not hypothetical. Machines have been edging out of human language for years, every time we gave them room to.

The famous early example is from 2017, when Facebook AI Research trained negotiation bots against each other. The work, published as [Deal or No Deal? End-to-End Learning for Negotiation Dialogues](https://arxiv.org/abs/1706.05125), produced agents that drifted away from grammatical English into a compressed shorthand that worked better for the task. The press coverage at the time was hysterical - "Facebook shuts down AI that invented its own language" - and the reality was mundane. The researchers simply had not rewarded the bots for staying in English, so the bots stopped bothering. But the underlying lesson was real and has aged well: human language is not the optimum for machine-to-machine communication, and models will leave it behind unless explicitly constrained to stay.

In 2025 it happened again, this time as a deliberate design. [Gibberlink](https://github.com/PennyroyalTea/gibberlink), a hackathon project that went viral, had two voice agents start a phone call in polite English, recognise each other as AIs, and then switch to ggwave - a data-over-sound protocol that sounds like a dial-up modem having a stroke. The demo struck a nerve precisely because it made the compatibility layer audible. The moment both parties knew no human was listening, the English stopped.

The research frontier goes further still. [DroidSpeak](https://arxiv.org/abs/2411.02820) explores letting models share KV cache state directly - one model handing its internal representations to another rather than re-serialising everything through text, with large gains in throughput. And Meta's [Coconut work on reasoning in continuous latent space](https://arxiv.org/abs/2412.06769) shows models reasoning in their own hidden states rather than in words at all - what some researchers have taken to calling "neuralese". Chain-of-thought in English turns out to be another compatibility layer, this one between the model and itself.

So the trajectory seems fairly clear to me. Agent-to-agent communication starts in English because that is what we trained on and what we can supervise. It moves to structured protocols because they are more reliable. And wherever the economics allow it, it will keep compressing - towards learned codes, shared embeddings, and eventually raw representational exchange that has no human-language equivalent at all. Not because the machines are scheming, but because every hop through English costs tokens, latency, and fidelity, and optimisation pressure hates waste.

## The Same Logic Applies to Code

Here is the part I find genuinely interesting: programming languages are exactly the same kind of artefact.

We do not write Python because computers like Python. Computers execute machine code. We write Python because *humans* cannot hold machine code in their heads, so we built a tower of abstractions - high-level languages, compilers, interpreters, type systems - whose entire purpose is to translate between human cognition and silicon. The compiler is a translation service. The source code is the human-readable side of the contract.

Andrej Karpathy saw the first crack in this tower back in 2017 with his [Software 2.0 essay](https://karpathy.medium.com/software-2-0-a64152b37c35) - the observation that for a growing class of problems, we no longer write the logic at all; we specify desired behaviour with data and let training find the program in neural network weights. Nobody reads the weights. Nobody complains that the weights are unreadable. The readability requirement evaporated because no human was ever going to maintain that code by hand.

Now extend that to agents writing conventional software, which is where we already are in 2026. I covered Boris Cherny's view that [coding's typing layer is essentially solved](/ai/will-ai-kill-coding-jobs-cherny/) - he ships dozens of PRs a day without hand-editing code. But notice what has not changed yet: the agents still write Python and TypeScript. They emit code in languages designed for human eyes, which gets compiled or interpreted exactly as if a person had written it.

Why? For the same reason agents speak English to each other. We trained them on human code, and we want to review what they produce. Both of those reasons are about us, not about the machines or the task.

So play the tape forward:

1. **Today** - agents write human-readable code, humans review it. The language is doing double duty as both a specification medium and an audit trail.
2. **Soon** - agents write code that humans *can* read but increasingly do not. Review shifts to behaviour: does it pass the evals, does it meet the spec. This is already happening on teams running heavily agentic workflows.
3. **Then** - languages and intermediate representations optimised for model generation rather than human reading. Denser, more regular, machine-checkable, ugly. Think LLVM IR or WebAssembly as the *target* the agent writes, not something a compiler produced from prettier source.
4. **Eventually** - the agent emits the executable artefact directly. There is no "source code" in the human sense, just a specification at the top, a binary at the bottom, and a model in between. The compiler as a separate tool has dissolved into the agent.

At that final stage, asking "what programming language was this written in" becomes a category error, like asking what font a neural network thinks in.

## What Compilers Actually Buy Us

Before declaring the compiler dead, it is worth being honest about what compilers actually do, because "translation for human convenience" is only half the job.

A modern compiler is also a correctness machine. It type-checks, it enforces memory safety, it applies decades of optimisation research, and crucially, it is *deterministic* - the same source produces the same binary, every time. That determinism underwrites reproducible builds, security audits, and the entire idea that you can trust a binary because you can trust its source.

A neural network emitting raw machine code has none of those properties by default. It is a sampling process. The same prompt can produce different binaries, and as I have written before, [non-determinism in agentic systems is structural, not a bug](/ai/agent-reliability-debugging-non-deterministic/). An agent that hallucinates a plausible-looking but subtly wrong x86 instruction sequence is a much scarier failure mode than one that hallucinates a Python function which then fails a test with a readable traceback.

So my honest guess is not that compilers disappear, but that they *sink* - the way assembly did. Almost nobody writes assembly any more, but assembly did not go away; it became a layer humans stopped touching. I expect the same fate for source code: agents will likely target small, formally verifiable intermediate representations, and something compiler-shaped will still sit between the agent's output and the silicon, providing the determinism and the safety proofs. The difference is that no human will read what goes into it, and the "programming language" layer that exists purely for our eyes - the syntax bikeshedding, the readability debates, the style guides - thins out and eventually goes quiet.

The interesting inversion is that verification becomes more important, not less, precisely because reading the code stops being an option. When you cannot review the source, the spec, the evals, and the proofs are all you have. The discipline shifts from "write code humans can audit" to "write specifications machines can be held to" - which is a harder problem than it sounds, and one I think we are underinvesting in relative to raw codegen capability.

## The Part That Worries Me

Efficiency arguments all point one way: drop the human layers. Machines talking in learned binary protocols, reasoning in neuralese, shipping artefacts with no source code - every one of those steps is faster and cheaper than the status quo. Which is exactly why I expect economic pressure to push hard in that direction.

But human language and human-readable code are not just overhead. They are the audit trail. Today, if I want to know why an agent did something, I can read its chain of thought and its diff. Both of those windows close in the world I have just described. A chain of thought in continuous latent space cannot be read, only interpreted with specialised tooling. A binary with no source can be disassembled, but disassembly of model-generated machine code at scale is nobody's idea of meaningful oversight.

This is, I think, the real stakes of the interpretability research programme - the kind of work Anthropic and others are doing on understanding model internals stops being an academic nicety and becomes the *only* remaining window once the legible layers go dark. I have written about why [AI safety arguments hold from first principles](/ai/ai-safety-first-principles/), and this is a concrete instance: the question is not whether machines dropping our languages is efficient (it is), but whether we keep a supervised channel open anyway, and who pays the efficiency tax to maintain it.

My suspicion is that we will end up with a deliberate two-tier world. Machine-to-machine traffic in dense learned protocols where speed matters, with mandated checkpoints where state is forced back into human-legible form - the way financial systems run fast internally but must produce auditable records. Whether those checkpoints are robust or theatrical will be one of the defining engineering and policy fights of the next decade.

## My Bet

Pulling it together, here is where I land - with the standing caveat that this is a hobbyist's speculation about a fast-moving field, my views here are always evolving, and I would be happy to be proven wrong:

- **Agent-to-agent English dies first.** Within a few years, high-volume agent traffic will run on learned or negotiated compact protocols, with human-language rendering available on demand rather than as the native medium. The Gibberlink demo was a toy, but it was the right shape.
- **Programming languages outlive their writers.** Humans will stop writing most code well before the languages disappear, because the existing training data, tooling, and verification ecosystems give human languages a long tail. Python becomes Latin: nobody's mother tongue, still everywhere.
- **Compilers dissolve rather than die.** The translation-for-humans half of the job fades; the verification-and-determinism half gets more critical and gets absorbed into agent toolchains targeting verifiable IRs.
- **Legibility becomes a regulated resource.** We will not keep human-readable layers because they are efficient. We will keep them - where we keep them - because we choose to, the way we choose to keep flight recorders on aircraft.

The deep pattern underneath all of this: every layer we built to make computing legible to humans - languages, compilers, English-speaking interfaces - was scaffolding around the fact that humans were the ones doing the building. As that stops being true, the scaffolding comes down. The question that matters is not whether it comes down, but which pieces we deliberately bolt back on.

## Related Reading

- [The Quiet Standardisation of Agent Protocols - MCP, A2A, ACP Compared](/ai/agent-protocols-mcp-a2a-acp/)
- [Will AI Kill Coding Jobs? Claude Code's Creator Reacts](/ai/will-ai-kill-coding-jobs-cherny/)
- [Agent Reliability - Debugging Non-Deterministic Systems](/ai/agent-reliability-debugging-non-deterministic/)
- [Recursive Self-Improvement](/ai/recursive-self-improvement/)
- [The Next Decade of AI](/ai/the-next-decade-of-ai/)
