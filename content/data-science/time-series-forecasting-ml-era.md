---
title: "Time Series Forecasting in the ML Era: What Actually Works"
date: 2026-05-13T02:30:00+01:00
draft: true
tags: ["data", "forecasting", "time-series", "machine-learning", "statistics"]
description: "Forecasting is one of the oldest statistical problems and one where the deep-learning revolution has produced mixed results. A practical look at the state of time-series forecasting in 2026, where neural approaches actually beat classical statistics, and where they do not."
cover:
  image: /assets/images/data-science/time-series-forecasting-ml-era.jpg
  alt: Time Series Forecasting in the ML Era Banner
---

Time series forecasting is the statistical problem with the longest pedigree and one of the most uneven track records for the deep-learning revolution. For most prediction problems - image classification, natural language, recommendation - neural networks have decisively beaten classical statistical approaches. For forecasting, the picture is much more complicated. Some forecasting problems yield to neural methods; many do not. Some of the biggest forecasting competitions of the last few years have been won by ensembles of classical methods rather than by deep learning approaches.

The 2026 state of the field has stabilised enough to talk honestly about where each kind of method actually wins.

## What forecasting actually is

Time-series forecasting is the problem of predicting future values of a sequence based on its past values, possibly with covariates. The classical examples - demand forecasting, energy load forecasting, financial markets, climate projections - are areas where good forecasts have direct economic value and where the field has been actively developed for decades.

The naive expectation in 2017-2018 was that neural networks would eat forecasting the way they had eaten everything else. The papers were published, the benchmarks were claimed, and the deep-learning approach was declared the future. The honest assessment a few years later is that the takeover did not happen, or rather, that it happened in specific places and not in others.

## Where classical methods still win

A few categories where the well-tuned classical approach is still hard to beat:

**Short univariate series.** A few hundred to a few thousand data points, one variable, possibly with covariates. ARIMA, ETS, and the more recent statistical models from the [Hyndman ecosystem](https://otexts.com/fpp3/) consistently produce competitive or better results than neural approaches on this kind of data. The neural methods are over-parameterised for the size of the problem and tend to overfit.

**Series with strong seasonal patterns and limited history.** Classical models that explicitly decompose into trend, seasonal, and residual components are very efficient at this kind of data. Neural approaches can match them but rarely beat them.

**The M-competition lineage.** The recurring forecasting competitions run by Makridakis and colleagues have consistently shown that simple methods, well-tuned ensembles, and the new statistical methods (theta, Naïve, MAPA, and similar) remain competitive with neural approaches across a wide range of forecasting tasks.

**Cases where interpretability matters.** Classical methods produce models that can be inspected, decomposed, and reasoned about. Neural forecasts are essentially black boxes. For regulated industries, audit-requiring contexts, and any case where understanding why the forecast is what it is matters, classical methods retain a real advantage.

## Where neural methods win

The places where neural approaches have genuinely advanced the state of the art:

**Very large multivariate problems.** When you have thousands of related time series - product demand across a large retail chain, energy demand across many regions, traffic flow across a transport network - the neural approaches scale better than classical methods. The ability to share information across series through learned embeddings is a real advantage.

**Long sequences with complex dependencies.** Series with several thousand data points, with both short-term and long-term patterns. Transformer-based approaches handle this kind of structure well, and the recent foundation models for time-series (TimesFM, Chronos, Moirai) have produced credible results on this category.

**Problems with rich covariates.** When the forecast needs to incorporate many external variables - weather, calendar events, marketing spend, market conditions - neural methods can integrate these in ways that classical approaches struggle with.

**Zero-shot or few-shot forecasting.** The recent time-series foundation models can produce reasonable forecasts on new series they have never seen, without any fitting. This is genuinely new and useful for applications that involve forecasting many short series.

## The 2026 foundation models

The newest development in forecasting is the arrival of time-series foundation models. These are pre-trained transformer models that have been trained on large corpora of diverse time series and can produce forecasts on new series in a zero-shot or few-shot setting.

The major ones in 2026:

**TimesFM** (Google) - one of the earlier serious entries, trained on a large corpus of time series with good zero-shot performance across many domains.

**Chronos** (Amazon) - takes the language-model approach, treating time series as token sequences. Competitive performance with the advantage of leveraging existing transformer infrastructure.

**Moirai** (Salesforce) - explicitly designed for the heterogeneous-series case where different forecasts have different lengths, frequencies, and structures.

**Various open-source contributions** - several smaller foundation models with strong performance in specific domains.

The honest assessment of these is that they are useful but not transformative. For series that fit the patterns the foundation model has seen during training, they produce competitive forecasts with no fitting effort. For series with unusual patterns, they often do not beat well-tuned classical methods. The use case where they shine is when you need reasonable forecasts on many series with no per-series modelling effort.

## What this means in practice

The practical advice for forecasting in 2026:

**Start with a good classical baseline.** Theta, exponential smoothing, ARIMA - whichever fits your data. These often produce results that are within a few percent of the best neural method, at a fraction of the complexity.

**Use neural methods when the problem actually warrants them.** Large multivariate problems, long sequences with complex dependencies, rich covariate sets. The selection criterion is whether the data has the structure that neural methods exploit, not whether neural methods are fashionable.

**Use foundation models for zero-shot scenarios.** When you have many short series and want reasonable forecasts without per-series fitting, the foundation models are the right tool.

**Ensemble classical and neural methods where both are competitive.** The best results often come from combining methods. The ensemble dominates either approach alone on many real-world forecasting problems.

**Be honest about uncertainty.** Forecasts without uncertainty estimates are barely forecasts. Classical methods give you well-calibrated prediction intervals for free; neural methods require explicit work to produce useful uncertainty estimates.

## The interesting cultural shift

The deeper interesting thing about forecasting in 2026 is that the data science culture has become more honest about the limits of deep learning in this domain. For a few years after the deep-learning boom, presenting "neural network for forecasting" results was the easy path - it sounded modern, the marketing favoured it, and the audiences were not always equipped to ask whether the baseline was strong.

That has changed. Forecasting practitioners now routinely demand strong classical baselines, ensemble comparisons, and honest assessment of where each method excels. The field has matured into a more diverse methodological ecosystem rather than collapsing onto a single approach.

This is, in a way, a model for how other ML-adjacent fields might develop. The hype phase produces over-claims; the maturity phase produces appropriate use of multiple methods for the problems they are each suited to. Forecasting has reached the maturity phase, and the practitioners working on it are doing better work as a result.

## Related Reading

- [The Causal Inference Comeback](/data-science/causal-inference-comeback/)
- [Graph Algorithms: PageRank and Centrality](/data-science/graph-algorithms-pagerank-centrality/)
- [Community Detection Algorithms](/data-science/community-detection-algorithms/)
- [Scaling Graph Algorithms](/data-science/scaling-graph-algorithms/)
- [Fine-Tune vs RAG](/ai/fine-tune-vs-rag/)
