---
title: "From BASIC in 1981 to Claude Code in 2026: What Programming Has Always Been About"
date: 2026-04-02T09:00:00+00:00
draft: false
tags: ['programming', 'history', 'AI', 'retro-computing', 'philosophy', 'development']
description: "A 45-year thread from typing BASIC on a ZX Spectrum to using Claude Code: what hasn't changed about programming, and what fundamentally has."
slug: "basic-to-claude-code-2026"
---

I'm sitting at a desk with two machines.

One is a 1981 ZX Spectrum, 16KB of RAM, sitting on a desk in my garage. The other is a 2026 MacBook running Claude Code. Between them lie 45 years of computing history.

And here's the thing that struck me recently: **I'm still doing the same thing.**

On the Spectrum, I'm typing:

```basic
10 PRINT "HELLO WORLD"
20 INPUT A$
30 IF A$ = "YES" THEN GOTO 50
40 GOTO 10
50 PRINT "YOU SAID YES"
```

On Claude Code, I'm typing:

```
@roadmap.md write a blog post about why programming fundamentally hasn't changed
```

Different syntaxes. Same act.

## What Programming Actually Is

When you strip away the hype - the frameworks, the agile ceremonies, the Kubernetes, the LLMs - programming is still this:

**You describe the problem. The computer solves it. You check if you were right.**

The loop hasn't changed since 1981.

On BASIC, the loop was:
1. Type code
2. Type RUN
3. See what breaks
4. Fix it
5. Repeat

On Claude Code, the loop is:
1. Describe what you want
2. Hit enter
3. See what breaks
4. Ask Claude to fix it
5. Repeat

The *timing* is different. The *interface* is different. The *abstraction level* is radically different.

But the core act - "I have a problem, I will articulate it, I will see if a solution works" - that's unchanged.

## What Changed (And Why It Had To)

### 1981: You Own the Machine

On the ZX Spectrum, the machine was simple enough that you could understand it completely.

You knew:
- How the CPU worked (Z80 processor, you could learn the instruction set)
- What the memory looked like (16K was 16,384 bytes; you could almost memorize it)
- How graphics worked (each pixel was a bit)
- The order of operations (you understood execution flow completely)

There was no magic. There was no gap between what you wrote and what the machine did.

You typed BASIC code. The BASIC interpreter converted it to Z80 machine code. The CPU executed it. You understood the path.

### 2026: You Understand Almost Nothing

I don't understand my MacBook. I understand:
- It has many cores (I don't know the exact architecture)
- It has GPU acceleration (I couldn't explain it)
- It runs an operating system (I don't understand the kernel)
- My code compiles somehow (I know it involves LLVM, but I couldn't debug the compiler)
- I'm using someone else's AI model (I understand transformers in theory, but couldn't reimplement one)

The gap between "I typed code" and "the computer solved it" is now enormous. Incomprehensibly large.

**This is not a problem. This is progress.**

The Spectrum was simple because it *had to be*. 16K of RAM means you can't have layers of abstraction. You have to build close to metal.

Modern systems have abstraction layers because they *need* them to be usable at all. A modern CPU has more transistors than the entire world had computers in 1981. You cannot understand it directly.

So we built abstractions on top.

- **Assembly** on top of circuits
- **BASIC/FORTRAN** on top of assembly
- **C** on top of that
- **Python** on top of that
- **Frameworks** (Rails, React, Django) on top of that
- **AI agents** on top of that

Each layer makes the machine more useful and the programmer more removed from how it actually works.

And that's been the trajectory of all 45 years.

## What Stayed the Same

### The Core Problem-Solving Loop

Every programming paradigm, every decade, every generation of hardware has followed the same pattern:

1. **I want to build something.**
2. **I articulate what it should do.**
3. **I create or request a solution.**
4. **I run it and check.**
5. **I iterate when it's wrong.**

In 1981:
```basic
10 PRINT "ENTER YOUR NAME: "
20 INPUT N$
30 PRINT "HELLO " + N$
40 GOTO 10
```

Run it. Name misaligned? Change line 30. Run again.

In 2026:
```
"Build a CLI that asks for a name and greets them"
```

Got it? Try it. Greeting misaligned? Describe the problem. Claude fixes it.

**Same loop. Different resolution.**

### The Debugging Mindset

Debugging hasn't changed either.

In 1981, if your BASIC program crashed:
- You looked at the line number
- You read the code
- You thought: "What could go wrong here?"
- You added a PRINT statement to check
- You ran it again

In 2026, if your Python program crashes:
- You read the stack trace
- You think: "What could go wrong here?"
- You add a print statement or use a debugger to check
- You run it again

Same process. The tools are better (real debuggers vs PRINT statements), but the *method* is identical.

### The Feeling of Not Knowing

In 1981, you'd write code and not know if it would work until you typed RUN.

In 2026, you'll write a prompt, hit enter, and not know if Claude understood what you meant until you run it.

The uncertainty is the same. It's just delayed or distributed differently.

## What Genuinely Changed

### Abstraction Inversion

This is huge, and I don't think people appreciate how strange it is.

In 1981, you were abstracting *upward*. You took raw machine language and created BASIC so you didn't have to think about registers and memory addresses.

Fewer people needed to understand the machine. Most of us could just live in BASIC land.

In 2026, something inverted.

Younger programmers understand *less* about the machine than I do. They've never seen assembly. They've never thought about CPU cache. They don't know what a pointer is.

But they can do more. They can build web apps, mobile apps, ML systems - things I couldn't touch at their age.

The abstraction is so high now that you don't need to understand what's below. You just need to understand the problem you're solving.

The machine has become more opaque, and this made programming more accessible.

### The Illusion of Choice

In 1981, you had one language: BASIC. (Or machine code if you were brave.)

You had no decisions to make about syntax or paradigm. You just wrote code.

In 2026, you can choose from 500 languages, 50 frameworks, 100 deployment options, 20 package managers.

But this is an illusion of choice. For most problems, 5–10 combinations are actually reasonable. The rest are premature optimization or hype.

Interestingly, Claude Code partially reverses this. You describe what you want. Claude picks the technology.

"Build me a CLI app." Claude picks Python, maybe Go.

"Build me a web app." Claude picks React, or Vue, or Next.js.

You don't choose. Claude does. And most of the time, Claude's choice is perfectly reasonable.

We've come full circle. 1981: no choices (only BASIC). 2026: too many choices (500 languages), so AI makes them for you.

### Speed

This is the one thing that's genuinely different.

In 1981, you'd type a line of BASIC, hit RUN, and wait 10 seconds for your program to crash.

In 2026, you describe a feature to Claude, and 30 seconds later, you have working code.

The speed has compressed the feedback loop from "type RUN, wait, see" to "describe, paste, see."

This matters. A faster feedback loop changes how you think. You can iterate faster. You can experiment more. You can afford to be wrong.

But it's still the same loop. Just compressed.

## A Hypothesis: Programming Will Keep Feeling the Same

I think in 2046, someone will write an article like this comparing 2026 Claude Code to whatever comes next - probably some mental interface or quantum system or something I can't imagine.

And they'll say:

"The machine is incomprehensibly more powerful, the interface is unrecognizable, the problems I solve are different in every way.

But underneath it all, I'm still doing the same thing: describing a problem and iterating when I'm wrong."

Because that's what programming *is*. It's not about the syntax or the paradigm or the hardware. It's about closing the gap between "what I want to exist" and "what actually exists."

And as long as we're building software, that gap will exist, and we'll be closing it.

## Why This Matters Right Now

We're in a moment where it's tempting to think everything is changing.

"AI will replace programmers."
"The entire profession is disrupted."
"No one will write code anymore."

Maybe. But I doubt it.

Because what's changing is the *interface* to programming, not programming itself. The abstraction level is rising. The feedback loop is compressing.

This has happened before.

In 1980, coders thought the move from assembly to BASIC would end programming. "Why would anyone write machine code if they can write BASIC?"

But assembly didn't die. It evolved. Some people stopped writing it, and others started writing it in new contexts (embedded systems, performance-critical code).

Same with BASIC to C, C to Python, Python to AI agents.

The interface rose. The profession didn't die. It redistributed.

**I think the same thing will happen now.**

Some jobs will disappear (junior developers writing boilerplate). New jobs will appear (people who know how to prompt effectively, how to evaluate AI output, how to integrate AI into systems).

The core act of programming - iteration, testing, debugging, improving - remains.

The tool just changed.

## The Real Constant

What's actually unchanged about programming across 45 years:

1. **Taste.** Some code is elegant, some is hacky. That distinction predates and will postdate AI.

2. **Judgment.** Whether a solution is right isn't determined by the tool; it's determined by whether it solves the problem. This required judgment in 1981 and 2026.

3. **Iteration.** You will be wrong. You will fix it. This is the constant.

4. **Responsibility.** When your code breaks, you own it. This doesn't change with AI.

5. **Curiosity.** Good programmers want to understand. Some want to understand the hardware (assembly), some the algorithm (theory), some the system (architecture). That drive is constant.

## Where I Land

I started with BASIC on a ZX Spectrum because it was the only tool available. I didn't choose the language or the environment. I learned what I could.

I'm ending with Claude Code because it makes my iteration faster. I chose this tool.

But the core activity - figuring out how to make the computer do what I want - is identical.

The abstraction has risen. The feedback loop has compressed. The machine is incomprehensibly more powerful.

But I'm still typing, running, failing, fixing.

That's what programming is.

And I suspect that will remain true for the next 45 years, even though I won't be here to see it.

---

*Last Updated: April 7, 2026*
