---
title: "Monitoring and Observability"
date: 2022-01-21T11:51:18+01:00
draft: false
tags: ['monitoring', 'observability', 'devops', 'cloud', 'metric', 'logging', 'tracing']
description: "Guide to monitoring and observability tools for cloud infrastructure and applications - AWS CloudWatch, Datadog, Grafana, Prometheus, and open-source alternatives."
---

"Monitoring" and "observability" are not the same thing, even though the words are often used interchangeably. Monitoring tells you when a pre-defined thing has gone wrong. Observability is whether you can answer new questions about system behaviour - including questions you had not thought to ask when you built the dashboards.

This page groups tools by what they do rather than by vendor, because most real production stacks combine several of them.

## Metrics

Metrics are cheap to store, easy to aggregate, and the right tool for dashboards and alerts. They are a poor tool for debugging anything specific, because by definition you have already collapsed the interesting detail.

- [Prometheus](https://prometheus.io/) - the de-facto open-source standard for metrics, with a pull-based model and the PromQL query language
- [Grafana](https://grafana.com/) - visualisation and alerting layer that reads from Prometheus, CloudWatch, and dozens of other sources
- [AWS CloudWatch](https://aws.amazon.com/cloudwatch/) - AWS's native metrics and logs service, cost-effective if you are already in the AWS ecosystem
- [Datadog](https://www.datadoghq.com/) - hosted SaaS covering metrics, APM, logs, and security, popular in mid-to-large organisations that want a single pane of glass
- [New Relic](https://newrelic.com/) - long-standing APM and infrastructure monitoring platform
- [VictoriaMetrics](https://victoriametrics.com/) - a Prometheus-compatible alternative optimised for long-term storage and high cardinality

## Logs

Logs are expensive to store but invaluable when something unusual has happened. Modern practice is to log with structure (JSON, key-value) rather than free text, so you can query them.

- [Loki](https://grafana.com/oss/loki/) - Grafana's log aggregation system, designed to pair with Prometheus-style labels
- [Elastic Stack (ELK)](https://www.elastic.co/elastic-stack) - Elasticsearch, Logstash, and Kibana, the long-standing open-source option
- [OpenSearch](https://opensearch.org/) - AWS-backed fork of Elasticsearch
- [CloudWatch Logs](https://aws.amazon.com/cloudwatch/features/) - AWS-native logging with Logs Insights for query

## Traces

Distributed tracing is how you reconstruct what happened across service boundaries. In a microservices world it stops being optional.

- [OpenTelemetry](https://opentelemetry.io/) - the CNCF-led standard for instrumentation, now the default choice for new systems
- [Jaeger](https://www.jaegertracing.io/) - CNCF-graduated distributed tracing backend
- [Tempo](https://grafana.com/oss/tempo/) - Grafana's tracing backend, designed for cost-efficient long-term storage
- [Honeycomb](https://www.honeycomb.io/) - commercial tracing-first observability platform

## All-in-one platforms

- [Datadog](https://www.datadoghq.com/) - metrics, APM, logs, RUM, security, cost management, and more in a single product
- [New Relic](https://newrelic.com/) - similar breadth with strong APM heritage
- [Dynatrace](https://www.dynatrace.com/) - enterprise-focused with heavy investment in AI-driven root-cause analysis
- [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability.html) - built on the SignalFx and Plumbr acquisitions

## Synthetic and user monitoring

Monitoring the system from outside is as important as monitoring it from within. Real-user metrics and synthetic checks catch the outages that internal dashboards miss.

- [Pingdom](https://www.pingdom.com/) - uptime and synthetic-transaction monitoring
- [Checkly](https://www.checklyhq.com/) - Playwright-driven synthetic monitoring with a developer focus
- [Sentry](https://sentry.io/) - error tracking and performance monitoring for front-end and back-end code

## How to think about tool selection

A few questions that tend to separate the good choices from the expensive ones:

- How are you charged - by host, by ingest volume, by metric cardinality? All three get expensive, just in different ways
- Does the tool support OpenTelemetry ingestion? If not, you are locking yourself into a proprietary agent
- Can you query high-cardinality data (like `user_id` or `request_id`) without cost-prohibitive sampling?
- What happens to your historical data if you leave - does it export, or is it gone?

## Further reading

- [Observability Engineering (Majors, Fong-Jones, Miranda)](https://www.oreilly.com/library/view/observability-engineering/9781492076438/) - the canonical modern text
- [Google SRE Workbook - Chapter 4](https://sre.google/workbook/alerting-on-slos/) - the definitive guide to alerting on SLOs rather than causes

## Related Pages

- [DevOps Best Practices]({{< ref "/devops/best-practices" >}})
- [CI/CD Tools]({{< ref "/devops/cicd-tools" >}})
