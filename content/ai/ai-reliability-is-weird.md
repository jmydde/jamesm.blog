---
title: "AI Reliability Is Weird: Why Testing LLMs Breaks Everything You Know"
date: 2026-04-09T22:00:00+00:00
draft: false
tags: ["ai","reliability","testing","llm","agentic-engineering","verification"]
description: "Traditional testing methods are failing in the age of autonomous AI agents. We need a new approach to ensure reliability when the 'builder' is non-deterministic."
---

We've embraced the future. AI agents like [Cline](https://jamesm.blog/ai/cline/) are now the primary "builders" of software, executing complex engineering plans from high-level specifications. As I've argued in ["The Architect vs The Builder"](https://jamesm.blog/ai/architect-vs-builder/), the human role is shifting from execution to architectural oversight and defining intent.

But this shift introduces a profound, often uncomfortable, question: **How do we know it actually works?**

In a world where AI is writing the code, generating the data, and even orchestrating deployments, traditional notions of testing and reliability are breaking down. AI reliability is weird, and it demands a complete re-evaluation of our verification strategies.

## The Old Covenant: Deterministic Testing for Deterministic Code

For decades, software testing has been built on a fundamental premise: **determinism**.

*   **Unit Tests**: Given input `X`, a function `f` should always produce output `Y`. If `f(X)` doesn't equal `Y`, the test fails.
*   **Integration Tests**: When components `A` and `B` interact, the system state should transition from `S1` to `S2`.
*   **Test-Driven Development (TDD)**: Write the test first, then write the code to make the test pass. The test *defines* correctness.

This model works beautifully for traditional, human-written code. Our code is (mostly) deterministic. We expect it to behave the same way every time, given the same inputs. The "Builder" writes the code, and the tests verify that the code does what the builder intended.

## The Agentic Anomaly: When the Builder is Non-Deterministic

Now, consider the agentic workflow:

1.  A human "Architect" defines a high-level specification (e.g., "Implement a user authentication flow with OAuth2").
2.  An AI agent (like Cline) takes this specification and acts as the "Builder." It reasons, plans, uses tools (reads files, executes commands, writes code), and iterates.
3.  Eventually, it presents a solution: new code, modified configurations, deployed services.

The problem? The AI agent itself is powered by Large Language Models (LLMs), which are inherently **non-deterministic**. The same prompt, given twice, can produce slightly different outputs. The same task, given twice to Cline, might result in different code implementations, even if both are functionally correct.

This breaks the old covenant. How do you write a unit test for code that might be different every time it's generated? How do you assert `expected_output` when the "correct" output isn't a single, fixed string, but a range of semantically equivalent possibilities?

## Why Traditional Testing Fails for LLMs

1.  **Non-Determinism**: As mentioned, LLMs don't guarantee the same output for the same input. This makes direct assertion-based testing (e.g., `assert_equals(generated_code, expected_code)`) brittle and often useless.
2.  **Semantic vs. Syntactic Correctness**: An LLM might generate code that is syntactically perfect (compiles, passes basic linting) but semantically incorrect (doesn't solve the problem, introduces a subtle bug, or violates architectural principles). Traditional tests often struggle to capture deep semantic correctness without becoming overly complex themselves.
3.  **Hallucinations**: LLMs can confidently generate plausible-sounding but entirely false information or code. A unit test might pass, but the underlying logic could be fundamentally flawed due to an AI hallucination.
4.  **Context Sensitivity**: LLMs operate on vast contexts. A small change in the prompt or surrounding code can drastically alter the output. Isolated unit tests often miss these broader contextual dependencies.
5.  **The "Black Box" Problem**: While we can observe the inputs and outputs, the internal reasoning process of an LLM is opaque. Debugging *why* an LLM produced a certain output is far harder than debugging human-written code.

## The New Paradigm: Verification of Intent and Properties

In the agentic era, we must shift our focus from "testing the code" to "verifying the intent" and "validating properties" of the AI's output. This is less about specific examples and more about defining the *boundaries of correctness*.

### 1. LLM-as-a-Judge (LLM4J)

One powerful technique is to use another LLM to evaluate the output of the primary AI agent.

*   **How it works**: You provide the judge LLM with the original specification, the AI's output (e.g., generated code, extracted data), and a set of evaluation criteria. The judge then assesses whether the output meets the criteria.
*   **Advantages**: Can understand semantic nuances, adaptable to complex requirements, can provide qualitative feedback.
*   **Challenges**: Still an LLM, so it can hallucinate or be biased. Can be expensive due to multiple LLM calls. Requires careful prompt engineering for the judge itself.

### 2. Property-Based Testing

Instead of asserting `output == expected_value`, we define properties that the output *must* satisfy. This is where the concept of "Structured Outputs" becomes critical.

*   **Syntactic Properties**:
    *   "The output must be valid JSON according to this schema." (Guaranteed by structured outputs).
    *   "The generated code must compile without errors." (A key verification step for Cline).
    *   "The response must contain a valid URL."
*   **Semantic Properties**:
    *   "The extracted summary must contain the keywords 'AI' and 'reliability'."
    *   "The generated function must correctly handle edge cases like empty lists or null inputs." (This often requires running the generated code with specific test cases).
    *   "The sentiment of the generated text must be positive."

Property-based testing shifts the burden from predicting exact outputs to defining the *characteristics* of acceptable outputs.

### 3. Golden Datasets and Evals

For critical functions, maintaining a "golden dataset" of human-verified inputs and their expected outputs remains invaluable.

*   **How it works**: A curated set of examples where human experts have confirmed the correct output.
*   **Use Cases**: Regression testing (does a new model or prompt still perform well on known cases?), tracking performance metrics over time, and evaluating the impact of model updates.
*   **Crucial for**: Ensuring that improvements in one area don't degrade performance in another.

### 4. Human-in-the-Loop: The Ultimate Arbiter

Ultimately, the human "Architect" remains the final arbiter of correctness. The AI builds, the automated verification checks properties, but the human still needs to review the *outcome* against the *original intent* and "taste."

*   **Architect's Role**: Defines the high-level success criteria, the "taste" of the solution, and what "good enough" looks like.
*   **Builder's Role (Human)**: Translates architectural intent into concrete, verifiable properties and evaluation metrics. Designs the *evals* and the *verification steps* for the AI. This is the new frontier for quality assurance.

## Connecting to Structured Outputs

My previous post, "Structured Outputs: When Your AI Needs to Follow a Schema", is a perfect example of this new verification paradigm. By enforcing a JSON schema at generation time, we're applying a powerful property-based test *before* the output even reaches our application. It guarantees syntactic and basic type correctness.

However, as noted, structured outputs don't guarantee *semantic* correctness. An age of `999` might be valid JSON for an integer, but it's semantically nonsensical. This highlights the need for layered verification: structured outputs for the basics, LLM4J or custom code for deeper semantic checks, and human review for overall intent.

## The Future of Verification

The future of software quality in the agentic era is less about writing exhaustive unit tests for every line of code (which the AI might generate differently next time anyway) and more about:

*   **Designing robust evaluation frameworks.**
*   **Developing skills in defining clear, measurable properties and success criteria.**
*   **Embracing iterative refinement of evaluation metrics.**
*   **Leveraging AI itself to verify AI-generated outputs.**

AI reliability is weird because it forces us to confront the non-deterministic nature of intelligence. But by adapting our verification strategies, we can build trust in our autonomous builders and continue to push the boundaries of what's possible. It's a shift from "test what you wrote" to "verify what the AI built against your intent." This is the new frontier for software quality.

---
*How are you tackling reliability in your agentic workflows? Share your insights in the comments below!*