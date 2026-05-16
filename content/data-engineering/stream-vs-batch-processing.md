---
title: "Real-Time Data Processing: Stream Processing vs Batch Processing"
date: 2026-05-10T08:00:00+01:00
draft: false
tags: ["streaming", "batch", "data-engineering", "kafka", "spark", "architecture"]
description: "A direct comparison of stream and batch processing as architectural choices, the operational and cost tradeoffs that the marketing material does not mention, and the patterns that work when you need both."
cover:
  image: assets/images/data-engineering/stream-vs-batch-processing.jpg
  alt: Stream vs Batch Processing Banner
---

If you spend enough time in data engineering, you will eventually encounter the conviction that batch processing is dying and streaming is the future. This is the third or fourth time the industry has had this conversation in my career, and the answer has been the same every time. Streaming is not the future. Batch is not the past. They are different tools with different operational profiles, and the systems that age well use both, with discipline about which is the right choice for which problem.

This post is the working comparison I would have with an engineer who has been told by a vendor or a thought leader that the future is real-time and is wondering whether they should be tearing out their batch jobs.

## What we actually mean by each term

The words batch and streaming have suffered the kind of definition drift that happens to terms that get used in marketing.

For this post, I will use them in their precise senses. **Batch processing** is processing in which a finite, bounded set of data is consumed end-to-end, transformed, and the result emitted. The job has a defined start and end, runs on a schedule or trigger, and operates on data that is at rest at the moment of execution.

**Stream processing** is processing in which an unbounded, continuously-arriving set of data is consumed in flight. The job is conceptually always running, has no defined end, and operates on data that is in motion. State and windowing are concerns, because the job has to make sense of "what counts as a result" without the natural completion that batch gives you for free.

The terms "real-time", "near-real-time", and "micro-batch" are deliberately vague and I am going to avoid them. They mostly describe the latency the user experiences, which is a property of the whole system rather than of the processing model.

## The latency-vs-cost trade-off

The first thing to understand is the underlying economic shape of the choice.

A batch job that runs once a day on a meaningful volume of data is, on most modern engines, dramatically cheaper per row processed than the equivalent streaming job. The reasons are mechanical: you can use spot instances, you can size the cluster to the work, you can take advantage of vectorised execution and partition-aware scheduling, and you can amortise startup costs across the entire job. Most importantly, you only run when there is work to do.

A streaming job that processes the same data over the course of the day is paying for a continuously-running cluster, has weaker batching opportunities, has higher per-event overhead, and typically runs on warmer (more expensive) compute. The cost ratio between batch and streaming for the same volume of data is often something like five to ten times in batch's favour.

What you get for that cost is latency. Batch's per-record latency is bounded below by the schedule cadence. If you run a job once an hour, you have at minimum thirty minutes of average latency from event arrival to result. If you run it once a day, you have twelve hours. Streaming, by contrast, can produce per-record latencies in the hundreds of milliseconds, sometimes lower.

The honest framing of the choice is: how much are you willing to pay to reduce latency? If the answer is "the latency does not actually matter to anyone, we just like the idea of real-time", you should be running a batch job. If the answer is "every minute of latency genuinely costs us money or quality of service", you might need streaming. The space in between is more interesting than the extremes.

## Where streaming actually earns its keep

There are use cases where streaming is the right architectural choice and the cost premium is justified. They share a common shape: the value of an event decays sharply with time, or the system has a hard latency requirement that batch cannot meet.

**Fraud detection.** A fraudulent transaction blocked in 100 milliseconds is prevented. A fraudulent transaction caught in an hourly batch is reported. The economic value is in the prevention, and the prevention requires streaming.

**Personalisation in a live session.** If a user is browsing your site right now, the recommendation system has to reflect what they have just done. Yesterday's batch model was correct yesterday. It is not correct for the current session.

**Operational monitoring and alerting.** A system that is failing now needs to be observed now. The latency between a problem and an alert is often a hard SLA on the platform team, and that SLA pushes you into streaming.

**Real-time dashboards for genuinely operational decisions.** I want to be careful here, because most "real-time dashboards" are aesthetic rather than operational. But there are dashboards that drive minute-to-minute decisions - in a network operations centre, in a trading desk, in a logistics control room - and those genuinely need streaming.

**Event-driven architectures where data movement is the integration pattern.** If your system is built such that events flowing between services are the contract, streaming is not a choice you make about analytics. It is a property of the architecture.

In all of these cases, the value of low latency is meaningful, observable, and worth paying for.

## Where batch is the right answer and people choose streaming anyway

The far more common case is teams choosing streaming for use cases where batch would be cheaper, simpler, and entirely sufficient. The patterns repeat.

**Reports that nobody looks at after the morning.** A daily executive dashboard does not need streaming. The decision being made off it is monthly at best. A nightly batch refresh is the right architecture and is dramatically cheaper.

**Machine learning training pipelines.** Training a model is a batch operation, fundamentally. Streaming feature extraction is sometimes necessary for online inference, but model training is offline by nature and trying to make it incremental usually adds complexity for little benefit.

**Most data warehousing.** A warehouse for BI and ad-hoc analysis is well served by hourly or daily batch refreshes for the vast majority of use cases. The exceptions exist but they are rarer than the marketing makes them sound. The shape of the underlying platform - covered in [The modern lakehouse stack](/data-engineering/modern-lakehouse-stack/) - is built for exactly this kind of bounded refresh cadence.

**Compliance and regulatory reporting.** Reports that have to be correct, complete, and auditable are easier to produce as batch jobs because the bounded input gives you natural checkpoints for validation. Streaming compliance reporting is possible but expensive in engineering effort.

The rule of thumb I use when someone proposes a streaming architecture is: what specifically goes wrong if this runs once an hour instead? If the answer is a vague feeling that real-time is better, batch is probably the right choice.

## The hidden costs of streaming

Streaming systems have operational costs that are not visible when you are evaluating them on the whiteboard. They are worth knowing about, because they show up reliably in production.

**State management is harder.** Streaming jobs that aggregate, join, or window data have to maintain state, and that state has to survive restarts. Tools like [Apache Flink](https://flink.apache.org/) and [Kafka Streams](https://kafka.apache.org/documentation/streams/) have made this much better than it used to be, but state management remains a frequent source of operational pain.

**Schema evolution is more painful.** Adding a column to a batch job's input is straightforward: you change the schema, the next batch picks it up. Adding a column to a streaming job's input typically requires a coordinated change across the producer, the consumer, and the state store, sometimes with a window of dual-running. Open table formats like [Apache Iceberg](/data-engineering/apache-iceberg-2026/) make the batch side of this dramatically less painful than it used to be.

**Debugging is harder.** A batch job that produced wrong output has a finite, replayable input that you can re-run with diagnostics. A streaming job's failure modes are temporal: you have to reconstruct what the state was at a specific moment to understand why the output was wrong.

**Backfills are non-trivial.** When something needs to be recomputed from history, batch makes this easy. Streaming requires explicit replay infrastructure, careful state reset, and often a coordinated handoff between historical and live data.

**Observability is more complex.** Watching a streaming job for "is it healthy" requires more sophisticated monitoring than watching a batch job for "did it complete successfully". The healthy-vs-unhealthy distinction is continuous rather than binary.

None of these are show-stoppers. They are real engineering costs that should be on the balance sheet when you are deciding which paradigm to use.

## The hybrid pattern that works

The architecture that I have seen succeed most often when both latency and correctness matter is the [lambda](https://en.wikipedia.org/wiki/Lambda_architecture)-style hybrid: streaming for the operational fast path, batch for the system of record.

The shape is something like this. Events flow into a streaming system that produces approximate, low-latency results for whatever needs them right now. The same events also land in object storage. A periodic batch job re-processes the historical events into the system of record, and the system of record is treated as authoritative.

The streaming side is allowed to be slightly wrong. The batch side is correct. Downstream consumers that need low latency read the streaming output. Consumers that need correctness read the batch output. Where you need both, you read the batch up to the watermark and the streaming output for events after.

This is not novel. It is the architecture every large-scale data system that needs both real-time and correctness has converged on, in some form. The variations are in how clean the integration is between the two paths and how much shared logic you can avoid duplicating.

The [kappa architecture](https://en.wikipedia.org/wiki/Kappa_architecture) - streaming-only with replay - is the cleaner alternative on paper and has more enthusiasts than working examples in production. It can work, but it requires the streaming system to be authoritative, which puts a higher operational bar on the platform than most teams can sustain. For most organisations in 2026, lambda-shaped hybrids are still the realistic answer.

## What I would tell someone starting today

If you are building a new data platform in 2026, default to batch and add streaming where you have a specific use case that genuinely requires it. The default is the cheaper, simpler, more recoverable architecture, and the cost of moving from batch to streaming later when you have a real reason is much lower than the cost of running a fully streaming platform that nobody actually needed.

When you do need streaming, be honest about which use cases require it. The four or five use cases I described above are genuine. Most of the rest are aesthetic preferences for "real-time" dressed up as requirements.

Build the hybrid lambda architecture from the start, even if you only need batch initially. This means landing events in object storage in their raw form, treating that as the authoritative input, and running batch jobs over it. Adding a streaming path later is then a matter of attaching a stream processor to the same event source, not re-architecting from scratch. On Databricks, [Lakeflow declarative pipelines](/data-engineering/lakeflow-declarative-pipelines-2026/) make this kind of shared-source-of-truth pattern noticeably cleaner than it used to be.

The thing to avoid is the trap of treating streaming and batch as a religious choice. They are tools. Each is the right answer for some problems. The skill is knowing which is which and being willing to use both.
