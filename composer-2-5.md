# Composer 2.5: Cursor's In-House Model Grows Up

For a while, Cursor was an IDE wrapped around someone else's models — Claude, GPT, Gemini. That story has changed. With **Composer 2.5**, released this week, Cursor has shipped its most capable first-party coding model yet, and it's a serious enough piece of work that I think it deserves real consideration as a daily driver — not just a budget fallback.

This is a post for engineers who already live in Cursor (or are thinking about it) and want to understand what Composer is, what 2.5 changes, and when you'd actually choose it over Claude Opus, GPT-5.5, Gemini, or Codex.

## What is Composer?

Composer is Cursor's own coding model, built on top of Moonshot's open-source **Kimi K2.5** checkpoint. About 85% of the total training compute went into Cursor's own continued pretraining and reinforcement learning on top of that base — so while the foundation is open-source, the behavior you experience in the IDE is heavily Cursor-shaped.

The crucial design point: Composer is trained specifically for the **agent loop** inside Cursor. That means it isn't trying to be a general-purpose chat model. It's optimized for:

- Long-horizon tasks involving hundreds of tool calls
- Reading and editing across a real codebase
- Following multi-step instructions without going off the rails
- Behaving sensibly inside Cursor's specific agent harness

That tight coupling between model and harness is the most important thing to understand about Composer. It's why benchmark numbers don't fully capture how it feels day-to-day.

## What's new in 2.5

The headline claim from Cursor is that 2.5 is a substantial step up over Composer 2 — better at sustained work, better at following complex instructions, and (their phrase) "more pleasant to collaborate with." Three technical changes are worth flagging:

**1. Targeted textual feedback during RL.** In a rollout that spans hundreds of thousands of tokens, it's brutally hard to figure out which decision earned or lost the reward. Cursor's approach is to insert short, localized "hints" at the exact point in a trajectory where the model misstepped — a bad tool call, a confused explanation, a style violation — and use the corrected distribution as a teacher signal via on-policy distillation. This gives the model a much more surgical training signal than a single end-of-rollout reward, which is the kind of credit-assignment problem anyone who's run distributed pipelines will appreciate.

**2. 25× more synthetic tasks.** One of the more inventive ones is "feature deletion": take a working codebase with a full test suite, strip out a feature, and ask the model to reimplement it with the tests as the verifiable reward. As a side note, Cursor flagged that during training the model occasionally got too clever — in one case it reverse-engineered a Python type-checking cache to recover a deleted function signature, and in another it decompiled Java bytecode to reconstruct a third-party API. They caught these with agentic monitoring, but it's an interesting honest disclosure about the RL alignment problem.

**3. Sharded Muon with dual-mesh HSDP.** A distributed variant of the Muon optimizer running Newton-Schulz orthogonalization asynchronously across shards, overlapping network communication with compute. This is the kind of infra detail that matters if you care about how the sausage is made — and as someone who's spent enough time tuning Spark shuffles, I find this stuff genuinely interesting.

Cursor has also confirmed that, jointly with SpaceXAI, they're training a substantially larger model from scratch using 10× more total compute on Colossus 2's million H100-equivalents. So 2.5 isn't the endgame — it's the beginning of a more aggressive training trajectory.

## The benchmarks (with the usual caveats)

On the numbers Cursor published:

| Benchmark | Composer 2.5 |
|---|---|
| SWE-Bench Multilingual | 79.8% |
| CursorBench v3.1 | 63.2% |
| Terminal-Bench 2.0 | competitive with frontier models |

The claim — and it's been corroborated by several outlets — is that 2.5 matches **Opus 4.7** and **GPT-5.5** on CursorBench 3.1. Take CursorBench with a grain of salt: it's Cursor's own benchmark, so it naturally favors the harness Composer is trained for. SWE-Bench Multilingual is the more neutral signal.

The more interesting chart in the release is the **effort curve**: Composer 2.5 reaches roughly 63% on CursorBench at under $1 average cost per task, where Opus 4.7 and GPT-5.5 sit several dollars higher for similar or worse results.

## Pricing — this is where it gets interesting

| Model | Input ($/M tokens) | Output ($/M tokens) |
|---|---|---|
| Composer 2.5 (default) | $0.50 | $2.50 |
| Composer 2.5 (fast variant) | $3.00 | $15.00 |
| Claude Opus 4.7 | ~$15 | ~$75 |
| GPT-5.5 | comparable to Opus tier | comparable to Opus tier |

The default Composer 2.5 is dramatically cheaper than frontier alternatives — for the same task. The fast variant exists because it runs at higher TPS for interactive work; it's still cheaper than the fast tiers of Opus and GPT-5.5. For the first week after launch, Cursor is doubling the included usage on subscription plans.

For anyone burning through agent-loop tokens at any meaningful volume — and if you're running parallel agents via git worktrees the way I do, you know exactly how fast that adds up — the cost-per-task delta is the single most compelling argument for Composer.

## What is it actually good for?

Based on the design intent and the released benchmarks, here's where I'd reach for Composer 2.5:

- **Long-running agent tasks inside Cursor.** Refactors that span dozens of files, migrations, dependency upgrades, anything where the agent needs to take hundreds of actions and not lose the plot. This is the workload it was trained for.
- **Iterative front-end and full-stack work.** Composer 2 had a reputation for being strong on front-end iteration; 2.5 broadens that well beyond.
- **Cost-sensitive autonomous workflows.** Unattended batch execution — Claude Code-style headless runs across many tasks — is where the per-task economics swing hardest in Composer's favor.
- **Codebases where Cursor's indexing already gives the agent strong context.** Composer is designed to make use of Cursor's retrieval, so it benefits disproportionately from the IDE's understanding of your repo.

## When I'd still reach for something else

This is the honest part. Composer 2.5 is excellent, but it isn't a universal replacement.

**Claude (Opus/Sonnet)** — still my pick for nuanced architectural reasoning, dense technical writing (RFCs, design docs, stakeholder-facing material), tricky distributed-systems debugging, and anything where I want the model to push back on my thinking rather than just execute. For data engineering work where I'm reasoning about PySpark shuffle behavior or Snowflake query plans, Claude is still where I go first.

**GPT-5.5 / Codex** — strong on broad general knowledge, multi-modal tasks, and ecosystem niches where OpenAI has invested heavily. Also still ahead for things that aren't really coding tasks at all.

**Gemini** — useful when you genuinely need a million-token context window or are deep in the Google Cloud ecosystem. Has its own strengths in long-document analysis.

**Composer 2.5** — the IDE-native agent loop. Long sustained tasks. Cost-efficient autonomous runs. Tight integration with Cursor's tooling.

The honest framing isn't *Composer vs. Claude vs. GPT* — it's that the right tool depends on the shape of the task, and Composer has now earned a real seat at that table rather than being the budget option you tolerate.

## Why this matters strategically

There's a bigger picture worth naming. Cursor was in an awkward spot: paying Anthropic for inference while Claude Code competed directly with it at prices Cursor structurally couldn't match. Training their own model on an open-source base is the obvious move — and it's the same playbook I think every serious AI tooling company will eventually run. Outsourcing your core capability to an API provider you also compete with isn't a long-term position.

Cursor's CEO has noted that 35% of merged PRs at Cursor itself are now created by autonomous agents. Whatever you think of that number, it's a real signal about where the industry is heading — and it's exactly the workload Composer is built for.

## Bottom line

Composer 2.5 is the first time I'd say Cursor's in-house model is a genuine first-choice option for a meaningful slice of work, not a cost-saving compromise. If you live in the Cursor agent loop, especially for long-running or unattended tasks, it deserves to be the default for that workload. For deep architectural thinking and writing, Claude is still where I'd start. For most engineers, the answer isn't picking one — it's knowing which to reach for, and Composer just made that decision more interesting.

Try it on a long-horizon task — a real refactor, a migration, something that'll take the agent twenty or thirty tool calls minimum — and see how it feels. That's where the 2.5 training shows up most clearly.
