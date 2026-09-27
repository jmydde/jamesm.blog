---
title: "Structured Outputs: When Your AI Needs to Follow a Schema"
date: 2026-04-12T06:17:00+00:00
draft: false
tags: ["llm", "schema"]
lastmod: 2026-09-26T09:00:00+01:00
description: "Why guaranteeing output format matters more than you think, and when to use structured outputs in production"
cover:
  image: /assets/images/ai/ai-augmented-design-workflow.jpg
  alt: Structured outputs and schema design for LLMs
---

## TL;DR

- **Structured outputs** constrain an LLM's response to match a JSON schema during generation, eliminating the entire class of JSON parse and missing-field failures that free-form output produces
- They produce simpler code and more reliable pipelines, and the real cost saving is fewer retries rather than cheaper tokens
- Use structured outputs for data extraction, classification, entity recognition, and API payload generation - not for creative writing or open-ended reasoning
- Common mistakes include over-constraining schemas with too-strict enums, forgetting that the response format changes, and mistaking schema validity for semantic correctness
- The trajectory is toward structured outputs becoming the default: schemas will be inferred from English descriptions, and TypeScript types will auto-generate schemas

For years, extracting structured data from LLMs meant post-processing their text output: parse JSON, handle edge cases where the model forgot to close a bracket, write validation code to check if the output matched your schema, implement fallback logic when parsing failed.

Then came structured outputs - a way to constrain LLM responses to match a JSON schema before they're returned to you.

Structured outputs sound simple but represent a fundamental shift in how to build production LLM systems. And yet, most teams are still extracting data the old way - waiting for the post-processing disasters that guaranteed outputs prevent. They also pair naturally with [prompt caching](/ai/prompt-caching/) - the schema is part of the static prefix you want to cache - and with the verification disciplines I cover in ["AI agents that actually work"](/ai/ai-agents-that-actually-work/).

## What Structured Outputs Actually Do

Structured outputs guarantee that an LLM's response matches a schema you define. Instead of:

```json
{
  "name": "John Smith",
  "age": 35,
  "email": "john@example.com",
  // ...sometimes the model forgets fields, returns wrong types, or violates constraints
}
```

With structured outputs, the LLM's response is *constrained during generation* to never produce invalid JSON, missing required fields, or values that violate your type definitions. The model can't return a response unless it's schema-compliant.

This changes everything about error handling in production systems.

## The Pre-Structured-Output Reality

Before guaranteed output formats, extracting data from LLMs required defensive code at every step:

```javascript
try {
  const response = await llm.generate(prompt);
  const parsed = JSON.parse(response); // Fails whenever the model strays from valid JSON
  
  if (!parsed.name || !parsed.email) {
    // Handle missing fields
    return await retryWithMoreExplicitPrompt(prompt);
  }
  
  if (typeof parsed.age !== 'number') {
    // Handle type mismatches
    parsed.age = parseInt(parsed.age);
  }
  
  // Validate constraints (max length, allowed values, etc.)
  if (parsed.email.length > 254) {
    return await retryOrHandleError();
  }
  
  return parsed;
} catch (e) {
  // Retry logic, fallbacks, alerting
}
```

This code exists in production systems because LLMs sometimes hallucinate structure. Not often - but often enough that ignoring it costs you data quality or crashed pipelines.

Structured outputs eliminate this entire class of failure modes.

## Why This Matters More Than It Sounds

**1. Reliability Without Post-Processing**

The most obvious benefit: your code is simpler. You can trust the shape of what you receive. No `if (typeof value === 'string')` defensive checks. No field existence validation. The contract is enforced by the LLM itself.

In production systems running thousands of requests daily, even a 1% failure rate in parsing adds up. You might see:

- Customer complaints about incomplete data extraction
- Retries that overload your LLM API quota
- Cascading failures downstream when consumers expect specific fields
- Monitoring alerts that fire when your post-processing error rate spikes

Structured outputs eliminate the "silent failure" patterns where data is partially extracted but your validation doesn't catch it until it's caused damage downstream.

**2. Fewer Retries**

Constrained decoding doesn't make individual tokens cheaper - every token still costs a forward pass, and masking invalid tokens adds a little overhead. The saving comes from what you stop doing: no retry calls when parsing fails, no "please return valid JSON" repair prompts, and no verbose formatting instructions padding every request. For high-volume extraction, eliminating retries is where the money is.

**3. Deterministic Behavior for Reproducibility**

LLMs are inherently non-deterministic - the same prompt can produce slightly different outputs. Structured outputs don't eliminate this randomness, but they do eliminate variability in *structure*.

This matters for:

- **Testing**: You can verify that an extraction works by checking the structure, not by parsing fragile text patterns
- **Monitoring**: You can track data quality using schema compliance, not error rates in downstream validation
- **Iteration**: When you change a schema, you can measure the impact immediately rather than waiting for post-processing errors to surface

## When Structured Outputs Actually Matter

Structured outputs aren't universally better - they're better for specific tasks.

**Use structured outputs for:**

- **Data extraction**: Pulling fields from documents, forms, or natural language
- **Classification**: Choosing from a defined set of categories
- **Entity recognition**: Identifying and categorizing named entities
- **API generation**: Creating JSON payloads to send to downstream services
- **Validation pipelines**: Ensuring data meets constraints before it enters your system

In these tasks, the output schema is known in advance and non-compliance is a failure, not a feature.

**Don't use structured outputs for:**

- **Creative writing**: A schema would be silly for generating blog posts
- **Open-ended reasoning**: When you don't know the output shape in advance
- **Exploratory analysis**: When you're iterating and the output format keeps changing
- **Streaming UIs**: You can stream a structured response, but partial JSON is only useful to a UI that can render it incrementally

## The Implementation Reality

Using structured outputs is straightforward with modern LLM APIs:

With Anthropic's API, you pass the schema in [`output_config.format`](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), and the response text is JSON that matches it:

```python
import json
from anthropic import Anthropic

client = Anthropic()

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "integer"},
        "tags": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["name", "email"],
    "additionalProperties": False,
}

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Extract contact info from this text: ..."}],
    output_config={"format": {"type": "json_schema", "schema": schema}},
)

contact = json.loads(response.content[0].text)  # parses, and matches the schema's shape
print(contact["name"])
```

The SDKs also have a `messages.parse()` helper that takes a Pydantic (Python) or Zod (TypeScript) model and does the schema generation and validation for you.

Two things the guarantee does **not** cover:

- **Every JSON Schema keyword.** Constrained decoding enforces structure: types, required fields, enums, `additionalProperties: false`. Providers support different subsets of JSON Schema, and value constraints such as numeric ranges or string lengths may be unsupported or only partly enforced. Check your provider's supported-features list, and validate those rules in code.
- **Correctness.** A schema-valid response can still contain the wrong name.

JSON Schema itself is a standard, so the schema is mostly portable, but each provider's supported subset and request shape differ (OpenAI uses `response_format`, for example). Expect small adjustments when you switch.

## Common Mistakes When Using Structured Outputs

**1. Over-constraining with too-strict schemas**

If your schema requires exact string matches for a field like "category," but the model might reasonably return variations ("customer service," "Customer Service," "customer-service"), your schema will fail.

Better: Use enums for truly finite choices, but allow flexibility for natural language fields.

**2. Forgetting to handle the response format**

The response structure changes when you use structured outputs. Make sure your code accesses `response.content[0].parsed` (or the equivalent in your SDK), not `response.content[0].text`.

**3. Making schemas so large that models struggle**

If your schema has 50 fields with complex nested validation, the model's focus is split between answering the question and conforming to the schema. Simpler schemas get better results. If you need many fields, consider multiple extraction passes.

**4. Not validating the semantic quality**

Structured outputs guarantee valid JSON that matches your schema. They don't guarantee the data makes sense. "age": 999 is technically valid even if it's nonsensical. Layer semantic validation on top of schema validation.

## The Future of Output Structuring

Structured outputs are becoming the default rather than a special feature. The trajectory is clear:

- **Better schema inference**: Defining schemas will become easier (describe the output in English, let the model infer the schema)
- **Tighter integration**: Structured outputs will integrate with type systems (TypeScript types automatically generate schemas)
- **Runtime optimization**: Models will become better at guided generation as the infrastructure matures
- **Composition**: Combining multiple structured outputs in sequence will become the norm (extract entities, then extract relationships between them)

The teams that adopt structured outputs early build more reliable systems. The teams that stick with post-processing handwaves will spend engineering time on error handling they didn't need to write.

## For Further Exploration

- [Anthropic Structured Outputs Documentation](https://docs.claude.com/en/docs/build-with-claude/structured-outputs) - Full guide with examples
- [JSON Schema Reference](https://json-schema.org/) - The schema standard
- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) - Alternative implementation
- [Pydantic for Schema Definition](https://docs.pydantic.dev/) - Python library for defining schemas programmatically

## Related Reading

- [AI Reliability Is Weird: Why Testing LLMs Breaks Everything You Know](/ai/ai-reliability-is-weird/)
- [AI Hallucinations: Understanding and Mitigating False Outputs](/ai/ai-hallucinations-understanding-and-mitigating/)
- [When to Fine-Tune vs When to RAG: Choosing Your AI Architecture](/ai/fine-tune-vs-rag/)
- [Prompt Caching: The Quiet Performance Win for LLM Applications](/ai/prompt-caching/)
- [The LLM Context Window Arms Race: Does It Actually Matter?](/ai/llm-context-window-arms-race/)
