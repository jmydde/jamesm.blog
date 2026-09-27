---
title: "Graph Algorithms Explained: PageRank, Centrality, and Why They Matter"
date: 2026-01-02T08:00:00+00:00
draft: false
tags: ["data-science", "graph-algorithm", "network-analysis", "neptune-analytics"]
lastmod: 2026-09-26T09:00:00+01:00
description: "A practical guide to understanding graph algorithms: how PageRank actually works, when to use centrality measures, and why these patterns matter for real-world problems like recommendation systems and fraud detection."
cover:
  image: /assets/images/data-science/data-science.jpg
  alt: Network graph visualisation representing PageRank and centrality algorithms
slug: "graph-algorithms-pagerank-centrality"
---

## TL;DR

- Graph queries answer relationship questions (paths, positions, influence) that are impossibly expensive in a relational database - the mental shift is from filtering rows to traversing paths
- PageRank measures a node's importance by the importance of the nodes pointing to it; it is recursive, typically converges in a few dozen iterations, and applies far beyond web pages - citations, influence, fraud (via personalised PageRank)
- Centrality is an umbrella term: degree (how connected), betweenness (how many paths run through you), closeness (how near everything you are), and eigenvector (whether you are connected to important nodes) each answer a different question
- Picking the right centrality measure for the question matters more than tuning any single algorithm
- Managed engines like Neptune Analytics run these at scale without you implementing the iteration loops yourself

Graph algorithms often get treated as academic curiosities - something you learn in a computer science course and then never think about again. But they're actually the hidden backbone of some of the most profitable systems on the internet.

Google's early search ranking was built on PageRank. Recommendation systems use graph proximity to suggest connections and products. Fraud teams use personalised PageRank and community structure to find accounts linked to known bad actors. And if you're working with Neptune Analytics or building graph systems in 2026, you need to understand these patterns.

The good news? They're not as complicated as they sound.

## What Makes a Graph Problem Different?

Before we dive into specific algorithms, let's clarify what we're actually solving.

In a traditional relational database, you answer questions like:
- "What are all the orders for customer ID 42?"
- "Which products were purchased most in Q1?"

In a graph, you're answering relationship questions:
- "How is person A connected to person B?"
- "Who influences the most people in this network?"
- "What's the shortest path between two nodes?"
- "Which nodes are central to the network?"

The key difference: **relational queries are about filtering rows; graph queries are about traversing paths and measuring positions**.

This is why graph algorithms matter. They let you compute things that would be impossibly expensive in a traditional database.

## PageRank: The Algorithm That Funded Google

PageRank is the most famous graph algorithm, but most explanations of it are either "simplified to uselessness" or so mathematical they lose the actual insight.

Here's what PageRank actually does: **It measures the importance of a node based on the importance of the nodes pointing to it.**

That's it. But the implications are profound.

### The Intuition

Imagine you're on a random web page. You close your eyes and click a link at random. Where are you likely to end up? If you repeat this millions of times, some pages you'll visit way more often than others. PageRank calculates the probability.

A page is important if:
1. Important pages link to it
2. Pages that link to it don't have many other links (so their "vote" is worth more)

### The Algorithm (Simplified)

The simple version of PageRank works like this:

```text
PR(A) = (1 - d)/N + d * (PR(B)/L(B) + PR(C)/L(C) + ...)
```

Where:
- PR(A) is PageRank of page A
- B, C, etc. are pages that link to A
- L(B) is the number of outgoing links on page B
- N is the number of pages, and d is the damping factor (usually 0.85), so 1 - d = 0.15 is the chance you "teleport" to a random page

With the 1/N term the scores form a probability distribution summing to 1. (The original paper's version drops the N, which scales the scores but doesn't change the ranking.) Pages with no outgoing links - "dangling nodes" - need special handling, usually by spreading their score evenly across all pages.

### Why This Matters

PageRank's genius is that it's recursive - a page's importance depends on pages that link to it, which themselves depend on their inbound links. You can't compute it with a simple SQL query. You need graph algorithms.

In practice, you run PageRank iteratively (power iteration) - each iteration refines the scores based on the previous one. The error shrinks roughly by the damping factor each iteration, so you stop when the total change falls below a tolerance; with d = 0.85 that is typically a few dozen iterations.

The real-world applications go way beyond web pages:

- **Citation networks**: Which research papers are most influential?
- **Social networks**: Whose endorsement carries weight, not just who has the most followers?
- **Recommendation systems**: Which products are most "recommended by recommendations"?
- **Academic hiring**: Which universities produce researchers cited most often?

## Centrality Measures: Different Kinds of Importance

PageRank is one way to measure importance, but it's not the only way. "Centrality" is the umbrella term for "how central is this node to the network?"

Different centrality measures answer different questions:

### Degree Centrality: How Connected Are You?

The simplest centrality measure - just count the number of connections.

```text
degree(A) = number of nodes connected to A
```

**When to use it:** Social networks ("who has the most followers?"), friendship graphs, basic influence metrics.

**Why it matters:** High degree nodes are often hubs or influencers, but degree centrality can mislead. A celebrity with 1 million followers has high degree, but being connected to the celebrity doesn't make you important.

### Betweenness Centrality: How Many Paths Run Through You?

Measures how often a node appears on the shortest path between other nodes.

**Intuition:** If you're the only bridge between two parts of a network, you have high betweenness centrality. You're a bottleneck.

```text
BC(A) = sum over all pairs (X, Y) of:
        (shortest paths from X to Y that pass through A) / (all shortest paths from X to Y)
```

**The catch:** summing over every pair is expensive. Brandes' algorithm computes exact betweenness in O(V·E) time, which is fine for thousands of nodes and hopeless for billions of edges. At scale you estimate it from a random sample of source nodes.

**When to use it:**
- **Fraud detection**: Suspicious intermediaries in transaction networks
- **Supply chain**: Which warehouses are critical bottlenecks?
- **Infrastructure**: Which bridges, roads, or routers are most critical to keep functioning?
- **Epidemiology**: Which people bridge otherwise separate groups?

**Why it matters:** A node with low degree but high betweenness is often more important than it appears. Think of a small airport that connects two major cities - it's not the biggest airport, but it's critical.

### Closeness Centrality: How Close Are You to Everything?

Measures the average distance from a node to all other nodes.

```text
CC(A) = 1 / (average shortest path distance from A to all other nodes)
```

**Intuition:** Someone who can reach anyone in 2-3 hops is more central than someone who needs 5-6 hops.

**When to use it:**
- **Communication networks**: Who can spread information fastest?
- **Social influence**: Whose ideas can reach the widest audience?
- **Routing optimization**: Where should you place a delivery hub?

### Eigenvector Centrality: Are You Connected to Important People?

Similar to PageRank - your importance depends on your neighbors' importance.

```text
EC(A) = constant * Σ EC(neighbor) for all neighbors
```

It is PageRank's older cousin, with two differences: PageRank divides each node's contribution by its out-degree (so a node linking to everything passes on little), and PageRank adds the random jump. Eigenvector centrality is also computed by iteration, and on directed graphs it misbehaves - nodes with no incoming links from a strongly connected core score zero - which is exactly the problem PageRank's teleportation fixes.

**When to use it:** Undirected, connected networks where you want "connected to important nodes" without PageRank's degree normalisation.

### Harmonic Centrality: The Version That Doesn't Break on Disconnected Graphs

In disconnected networks (where some nodes can't reach others), closeness centrality breaks because the distance is infinite.

Harmonic centrality fixes this by summing the reciprocals of the distances (an unreachable node contributes 1/∞ = 0) instead of averaging the distances.

## When to Use Each Algorithm

Here's a quick decision tree:

**You want to rank importance by incoming links** → PageRank

**You want to find bottlenecks and bridges** → Betweenness centrality

**You want to find who spreads information fastest** → Closeness centrality

**You want to find influencers (connected to other influencers)** → Eigenvector centrality or PageRank

**You need something simple and cheap** → Degree centrality (but verify it answers your question)

**You have a disconnected network** → Harmonic centrality (for closeness-type questions)

## Real-World Example: Finding Hidden Leaders

Imagine you're a fraud team and you've built a transaction network:
- Nodes are people
- Edges are money transfers

You want to find the people running the operation.

Using degree centrality, you'd find the busiest traders - but legitimate traders are busy too.

Using betweenness centrality, you'd find the intermediaries - the people who connect different parts of the network. These are often the ones coordinating the scheme.

Using PageRank on the money-flow graph, you'd find the accounts where money ultimately collects - often the top of the scheme.

Using **personalised PageRank**, seeded from accounts already confirmed as fraudulent, you'd rank everyone else by how closely they're connected to those accounts. This is usually the most useful of the four in practice, because it starts from what you already know.

You'd probably use **all three** and compare:
- High degree but low betweenness? Probably a normal trader
- High betweenness but low degree? Likely a coordinator
- High PageRank but low in other measures? Possibly the person at the top

## Implementation Considerations in Neptune Analytics

If you're using AWS Neptune or a similar graph database, here's what you need to know:

**Most graph databases offer built-in algorithms** - don't implement PageRank yourself. Neptune Analytics holds the whole graph in memory and runs its algorithm library in-engine, callable from openCypher. Check its algorithm reference for exactly which centrality measures and variants are available before designing around one.

**Execution time depends on:**
- Number of nodes (N)
- Number of edges (E)
- Number of iterations (for PageRank)

PageRank is O(V + E) per iteration. Degree is a single pass. Exact betweenness and closeness are the expensive ones - O(V·E) - so sample them on large graphs.

**Memory considerations:** Storing centrality scores for all nodes requires O(V) space. For billion-node networks, this matters.

**Iterate carefully:** Don't compute PageRank for "are nodes A and B important?" Run it once for the whole graph, then query the results.

## The Pattern Nobody Explains

Here's what most explanations miss: These algorithms are all measuring similar things from different angles.

PageRank, eigenvector centrality, and several others are all measuring "recursive importance" - your value depends on your neighbors' values. They differ in:
- The starting assumption (uniform vs PageRank's random jump)
- The damping or normalization
- The computational approach

Betweenness centrality is asking "how often am I needed?" It's the control measure - if PageRank says you're important, betweenness explains why (are you a hub, a bridge, or just lucky in your connections?).

Once you see that pattern, you can reason about designing custom centrality measures for your specific problem. Should importance flow through edges? Should it decay with distance? Should being connected to important nodes matter? These are the questions driving algorithm design.

## Going Deeper

If you want to understand the math:
- Brin and Page's original PageRank paper is surprisingly readable
- [Centrality in Networks](https://en.wikipedia.org/wiki/Centrality) on Wikipedia has the math without drowning in it
- Neo4j's Graph Data Science library documentation has good practical explanations of each algorithm, even if you're using Neptune

The key insight for 2026 is: **graph algorithms are no longer academic**. They're the standard way to solve relationship problems in data. Understanding PageRank and centrality measures isn't just theoretical knowledge - it's foundational to building modern data systems.

The next time you're designing a recommendation system, fraud detection pipeline, or network analysis project, you'll know exactly which algorithm to reach for.

## Related Reading

- [Scaling Graph Algorithms: From Prototypes to Production](/data-science/scaling-graph-algorithms/)
- [Community Detection Algorithms: Finding Clusters and Groups in Network Data](/data-science/community-detection-algorithms/)
- [The Causal Inference Comeback: Why Correlation-Era ML Hit a Wall](/data-science/causal-inference-comeback/)
