---
title: "DHH on AI: From Hand-Chiselled Code to 'P-Bloom' in Under a Year"
date: 2026-10-05T20:30:00+01:00
draft: false
tags: ["ai", "agent", "agentic-engineering", "coding", "programming", "software-engineering", "business", "productivity", "interview", "youtube", "people", "2026"]
description: "David Heinemeier Hansson, creator of Ruby on Rails and co-founder of 37signals, went from refusing AI autocomplete to declaring hand-written code 'an exceptional state' in under a year. Here is what changed, what he thinks it means for programmers and startups, and why he rejects AI doom."
---

David Heinemeier Hansson spent a quarter of a century making the case for code as craft. He created Ruby on Rails, the framework behind Shopify, GitHub and Airbnb, and he wrote it by hand, line by line, for the joy of it. As recently as the start of December 2025 he was still doing that, and telling people who had gone all-in on AI that the tools were not good enough yet. Ten months later he stood on stage at Rails World and told a room of Rails developers that 37signals had gone "pencils down" on writing code by hand.

His new long-form interview with Will Cannon on Decoded Genius is the most complete account yet of how that flip happened and where he thinks it leads - for programmers, for small software companies, and for the doom debate. This post pulls that conversation together with his own writing and talks from this year.

## TL;DR

- DHH (@dhh) disliked AI autocomplete from the start, comparing it to someone constantly interrupting you mid-sentence. The shift to autonomous agents in terminal harnesses, around Claude Opus 4.5 in late November 2025, changed his mind almost overnight
- Since December he says he has not started a single new piece of code without a prompt first. At Rails World on 23 September 2026 he said writing code by hand at 37signals is now "an exceptional state", like a bug showing up in Sentry
- He thinks agents open software entrepreneurship to people who can't code and don't have money - and that the same fact makes the market far more competitive and pure-software VC money much harder to come by
- His warning for builders: when implementation stops being the bottleneck, the temptation is to build every idea, and that is the fastest way to make bad software. Constraints still win
- On job losses he is sympathetic and clear-eyed: individually tragic, societally necessary, and not something any one country can vote away
- On existential risk he puts AI in a long line of doomsday stories, from judgment day to nuclear war, and argues for "P-Bloom instead of oh so much P-Doom"

## "Like someone constantly interrupting you"

The interesting thing about DHH's conversion is that his taste didn't change - the tools did. He never liked the in-editor autocomplete style popularised by GitHub Copilot and Cursor. On Decoded Genius he describes it bluntly: "It was like someone constantly interrupting you. I'm trying to finish a thought here and you're constantly interrupting me."

What changed his mind was the move from autocomplete to agents: you hand over a task, the agent works in the terminal, runs the tests, and comes back with a result. He told Cannon that a week after an interview in early December where he defended hand-writing code, a new Claude Opus model and better harnesses - he names OpenCode, Pi, Codex and Claude Code - produced code "I wanted to keep, code I wanted to merge into my code base. And I flipped like 180 degrees." (In the interview he hesitates over which Opus version it was. In his January blog post and his Rails World keynote he is specific: Claude Opus 4.5, released on 24 November 2025.)

His January essay, [Promoting AI agents](https://world.hey.com/dhh/promoting-ai-agents-3ee04945), is worth reading as a snapshot of that moment, because it is far more cautious than where he ended up:

> Yet pure vibe coding remains an aspirational dream for professional work for me, for now. Supervised collaboration, though, is here today.

In the same post he wrote that he was "nowhere close to the claims of having agents write 90%+ of the code", at least not "if I hold the line on quality and cohesion." By August, in an essay called [Endless execution](https://world.hey.com/dhh/endless-execution-4157e065), the hedging was gone: "For people with endless ideas, this is nirvana." He added that "AGI is a nefarious concept to pin down, but I'm not sure how different whatever definition we eventually settle on will look from what I'm already experiencing on the daily."

## A bionic arm, not a project manager's job

The thing DHH says he feared most was becoming a project manager for robots. He doesn't enjoy managing human programmers, and assumed agents would feel the same. On Decoded Genius he explains why they don't: the feedback loop. A human team might take weeks or months to come back with a substantial feature. An agent often comes back in minutes. That changes the relationship:

> It's more like an extension of myself. Like I get a bionic arm. Like I'm extending that arm, but suddenly I can crush 4,000 pounds instead of whatever a human hand can crush.

His summary of the current state is simple: "Now I haven't started a single new piece of code that didn't start as a prompt first." He still drops in and writes code himself when an agent heads in the wrong direction, but everything starts with a prompt.

He is also careful to keep a distinction that gets lost in a lot of the hype. On the [Lex Fridman Podcast in August](https://lexfridman.com/dhh-2-transcript/) he defined vibe coding narrowly: "you tell an agent to build software for you. You do not look at the implementation. That, to me, is what separates vibe coding from programming or, let's say, agent-accelerated development." What he is doing is the second thing. He reviews the output, and much of his original resistance was aesthetic - early agents made things work "in a really ugly way." The change in December was that the code, "with a little bit of nudging, looked like my code."

He is also happy to pick his battles. In his [Rails World 2026 keynote](https://www.youtube.com/watch?v=vDjW_dRyKXY), describing a new Rust backend for HEY, he says he hates looking at Rust but is happy for agents to write it: "I'll tell you what to do. You'll write it in Rust. I never have to look at it."

## What he says happens to programmers

DHH doesn't pretend everyone will enjoy this. He separates programmers into those who learned to code because they wanted the programs, and those who loved the mechanics of turning a requirement into working code without caring much about either end. The second group, he says, is struggling, "because it is clear that the agents are eating more and more" of that work. He sympathises with the sense of loss - a year ago they were "the tight resource" everyone had to go through - and says it is fair to wonder whether anyone will need programmers at all if the trend continues.

For himself, he describes it as being returned to where he started: "I learned programming, not because I wanted to lovingly type out programs, but because I wanted the programs."

At Rails World he went further, and this is the strongest version of his position on record. 37signals, he said, had decided a couple of weeks earlier that "we're done writing code by hand":

> Writing code by hand at 37signals is now an exceptional state. It is like seeing a bug in Sentry. Something here went wrong. Why was the agent not able to produce what we wanted?

He told the audience that writing code by hand "is no longer an economically productive enterprise for the vast majority of programmers working at the vast majority of companies", predicted it would be true of "virtually all domains" by the end of the year, and said he wrote 150,000 lines of code in August - about 60 times his long-run average, though he notes much of it is verbose Rust.

There is another thoughtful angle in his April conversation with Gergely Orosz on [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code). In Orosz's summary, DHH's view is that senior engineers benefit from agents much more than juniors, because seniors can tell whether an agent's output is actually production-ready.
## Constraints still beat resources

The 37signals story is about small teams and no investor control, and DHH thinks agents make that philosophy more relevant, not less. His argument on Decoded Genius is that the old bottleneck - you had to be able to build, or be rich enough to pay builders - is gone. "I have absolutely already seen people who just had great ideas and not a lot of money be able to, with a $20 a month cloud subscription, build at the very least a prototype."

The catch is that everyone else can do the same, which makes the market "100X worse than what it was 20 years ago" for breaking through. Distribution, and protecting an idea from ten clones by tomorrow, matter more than ever.

His most useful warning is about what happens inside a team that suddenly has unlimited capacity. He has always argued that small teams build better software because they are forced to cut ideas. Agents remove that constraint:

> If implementation is no longer your bottleneck, you can do every idea you have. But if you do, it's going to turn to shit.

He compares it to the original Star Wars trilogy against the later films made with vastly bigger budgets. The point lands: when the cost of building drops towards zero, saying no becomes the main skill. It ties into his comments on work hours too. Asked whether founders need to grind, he answers no: "You're not supposed to be grinding... Grinding is for computers."

On money, he thinks this is one of the worst times to raise as a pure software company. SaaS valuations relied on projecting recurring revenue 15 or 20 years out, and "this AI joker has been played and we don't even know what the world is going to look like in six months." He calls the end of easy seed money "a blessing" because it forces founders down the bootstrapped path - which, he adds, "is easier than ever."

## Jobs, ATMs and tractors

Cannon pushes him on the people aged 35 to 55 who don't know how to use the tools and see AI as something taking their jobs. DHH's answer is one of the most thoughtful parts of the interview. He calls job losses from data centres and automation "individually tragic and societally absolutely necessary", and leans on familiar historical cases: ATMs made bank branches cheaper to open, so retail banking employment rose; tractors ended an economy where almost everyone farmed, and nobody wants to go back.

He doesn't wave the distribution problem away. He argues that a lot of current political discontent in the US and Europe comes from what he calls "a very elitist glib response" to de-industrialisation - the cheaper iPhone did nothing for people who lost their jobs. "To have a well-functioning society, you need to lift all boats." But he is clear that he doesn't think any single country can opt out:

> We have an obligation, I think, as societies... to try to nudge it, steer it. We don't get to put it in reverse.

His test case is the US banning AI to protect jobs, and asking whether China would follow. His answer: "No, it never happens like that."

## Doom, nuclear power and 42,000 road deaths

The most direct disagreement in the interview comes when Cannon cites [Roman Yampolskiy](/ai/roman-yampolskiy/) and others who worry less about jobs than about a handful of labs building something capable of killing everyone. Cannon says he is an optimist too, but that ignoring the risk would do his children a disservice.

DHH's reply has three parts. First, worrying only helps if you can change the outcome. Second, humanity has always had a doomsday story - judgment day, then the nuclear standoff, then climate - and he argues the nuclear threat was more immediate than AI's, because it needed only "one misstep from one individual." By contrast:

> What we have right now with AI is we have a fear that requires a fair amount of extrapolation. I'm not saying it's not a scenario you should worry about. I'm certainly not saying that the people working on AI shouldn't be taking it seriously.

Third, he points to the one time he thinks the West really did slow a technology down - nuclear power - and calls it "a big mistake", arguing that the current panic over data centre energy wouldn't exist if the West had kept building reactors the way France did in the 1980s. He frames AI safety as the same kind of trade-off we already make with cars, citing 42,000 US road deaths a year that we could prevent with a five-kilometre-an-hour speed limit, and choose not to. And he adds a geopolitical point: "if someone's going to have this super capacity, this super technology, it should be us" - meaning, he says, the West.

At Rails World he put the same position in one coined phrase, urging developers to lean in "with a little bit of P-Bloom instead of oh so much P-Doom", on the grounds that "the chances of this panning out and us getting abundance and joy is so vastly greater than us getting the doom."

He also applies the same Stoic logic to his own company. He says he has already made peace with the possibility that AGI wipes out Basecamp and the rest of SaaS - even within three months - because he has had a 22-year run and can only control what he builds next.

## Watch

Most recent first.

### Decoded Genius: WARNING: We're Not Ready for The AI Revolution (30 September 2026)
{{< youtube nNx1D54wVEM >}}

The interview this post is built around, at just over two hours. The first hour is the AI material: the December flip, what agents mean for programmers and startups, jobs, and the doom argument. The second half covers the 37signals story - the Jeff Bezos minority stake, leaving the cloud (a cloud bill of about $3.2 million a year cut to about $800,000), the fight with Apple, banning politics at work, and Stoicism.

### Ruby on Rails: Rails World 2026 Opening Keynote - DHH (23 September 2026)
{{< youtube vDjW_dRyKXY >}}

The fullest and most energetic version of his position, delivered to a Rails audience in Austin. Opus 4.5 as "the Kodak Brownie of our era", the "pencils down" announcement, HEY's move to native clients and a Rust backend, his demand that every app ship a CLI agents can drive, and the P-Bloom close. Infectiously enthusiastic from start to finish.

### Lex Fridman Podcast #501: DHH: Future of Programming, AI, Agentic Engineering, Vibe Coding & Linux (26 August 2026)
{{< youtube NYFGCESmikA >}}

Over five hours, and the most technical of the three. Best for his distinction between vibe coding and agentic engineering, his day-to-day setup with many agents running in parallel, how the Omarchy Linux distribution is now built almost entirely by agents, and his comparisons of AI coding models and harnesses.

## My read

This was a genuinely good interview, and a refreshingly positive one. DHH is energised in a way that is hard to fake - someone who has loved computers for forty years and is clearly having the most fun he has ever had with them. In a year full of anxious conversations about AI, it was a pleasure to listen to two hours of curiosity, optimism and practical wisdom. Well worth your time.

## Sources

- [Decoded Genius: WARNING: We're Not Ready for The AI Revolution (YouTube)](https://www.youtube.com/watch?v=nNx1D54wVEM) - the interview, uploaded 30 September 2026
- [Decoded Genius episode transcript - Exa](https://exa.ai/library/podcast/32xzp74d6k0/episode/wr7r7vstvz6) - automated transcript, source of the interview quotes
- [Decoded Genius - Listen Notes](https://www.listennotes.com/podcasts/decoded-genius-decoded-genius-xzn9UpI3aV4/) - podcast listing and episode date
- [Promoting AI agents - David Heinemeier Hansson](https://world.hey.com/dhh/promoting-ai-agents-3ee04945) - 7 January 2026
- [Endless execution - David Heinemeier Hansson](https://world.hey.com/dhh/endless-execution-4157e065) - 9 August 2026
- [Rails World 2026 Opening Keynote - DHH (YouTube)](https://www.youtube.com/watch?v=vDjW_dRyKXY)
- [Rails World 2026 Opening Keynote - Hraness summary and transcript](https://hraness.com/reading/rails-world-2026-opening-keynote-dhh)
- [Rails World 2026 Opening Keynote - RubyEvents.org](https://www.rubyevents.org/talks/opening-keynote-rails-world-2026) - date and location
- [DHH's Rails World 2026 Keynote: Building Software When Agents Write the Code - Makers' Den](https://makersden.io/blog/dhh-rails-world-2026-ai-agents)
- [Transcript: Lex Fridman Podcast #501 with DHH](https://lexfridman.com/dhh-2-transcript/) - source of the vibe coding definition
- [DHH's new way of writing code - The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code) - 8 April 2026

## Related Reading

- [Roman Yampolskiy: The Researcher Who Thinks AI Cannot Be Controlled](/ai/roman-yampolskiy/) - the view Will Cannon put to DHH in the interview
- [Connor Leahy: From EleutherAI to ControlAI, and Why He Now Wants Superintelligence Banned](/ai/connor-leahy/) - another builder's perspective on whether AI can be paused
- [Scott Galloway on AI: The Marketing Professor's Case That the Rich Don't Need You Anymore](/ai/scott-galloway-on-ai/) - another angle on the jobs and inequality question DHH answers with ATMs and tractors
- [The Automation Paradox: Why More AI Makes Human Judgment More Valuable](/ai/automation-paradox/) - the "saying no is the skill" argument in general form
- [Agent-First Architecture: The Engineer as System Curator](/ai/agent-first-architecture-engineer-as-curator/) - what DHH's "pencils down" workflow looks like as an engineering practice
- [Token Economics: Why Your AI Bill Isn't Going Down](/ai/token-economics-why-costs-arent-going-down/) - the Jevons paradox behind his "cheaper software means more demand" argument
