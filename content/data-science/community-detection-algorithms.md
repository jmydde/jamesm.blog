---
title: "Community Detection Algorithms: Finding Clusters and Groups in Network Data"
date: 2026-02-09T09:00:00+00:00
draft: false
tags: ["data-science", "graph-algorithm", "network-analysis"]
lastmod: 2026-09-26T09:00:00+01:00
description: "Deep dive into community detection: how Louvain, Leiden, modularity, and spectral clustering work. Practical guide to finding natural groups in networks and why they matter for fraud, social networks, and product recommendations."
cover:
  image: /assets/images/data-science/data-science.jpg
  alt: Network graph showing clusters of connected nodes representing community detection
slug: "community-detection-algorithms"
---

## TL;DR

- A community is a group of nodes with more internal connections than you would expect by chance; community detection finds these groups purely from network structure, not features
- Modularity is the metric most methods optimise - values of 0.3-0.7 are common for real networks - but it has a known resolution limit that can hide small communities
- Louvain made community detection practical at scale, but it can produce badly connected or even disconnected communities; Leiden fixes that and is now the better default. Label propagation, spectral clustering, and Girvan-Newman fill the gaps
- The same technique powers friend-group detection, product clustering, fraud-ring identification, and finding functional modules in biological networks
- Overlapping communities remain the genuinely hard problem - most standard algorithms assign each node to exactly one group

If you've ever looked at a social network and wondered "why is this group of people more connected to each other than to the rest of the network?", you've just articulated the community detection problem.

Real networks aren't random. They have structure. People cluster with people like them. Products cluster with complementary products. Proteins in cells interact with nearby proteins more than distant ones.

Community detection algorithms find these natural groupings automatically. And unlike clustering algorithms (which work on features), graph community detection works purely on the structure of connections.

This matters because sometimes the connections themselves are the signal.

## The Core Intuition

A community is a group of nodes with more internal connections than expected by chance.

More precisely: A good community has:
- Many edges between nodes in the community
- Few edges between the community and the rest of the network

This creates a natural boundary - the group is more connected internally than externally.

## Modularity: The Metric Everything Uses

Before we dive into algorithms, you need to understand modularity - it's the metric that measures "how good is this community division?"

In words: the fraction of edges that fall within communities, minus the fraction you'd expect if edges were placed at random while keeping every node's degree the same. Formally, for a graph with m edges:

```text
Q = (1 / 2m) * Σ over node pairs (i, j) [ A_ij - γ * (k_i * k_j) / 2m ] * δ(c_i, c_j)
```

where A_ij is 1 if i and j are connected, k_i is node i's degree, δ(c_i, c_j) is 1 when both nodes are in the same community, and γ is the resolution parameter (1 in the classic definition).

Higher modularity = better division into communities.

The intuition: If communities were random, you'd expect some edges within groups just by chance. Modularity measures how much better your actual community structure is than random.

A modularity of 0.3 - 0.7 is common for real networks, but there's no universal threshold for "good": very sparse, highly modular graphs legitimately score above 0.9.

The caveat that matters more is the **resolution limit** (Fortunato and Barthélemy, 2007): maximising modularity can merge small, genuine communities into larger ones, especially in big graphs. The resolution parameter γ is how you push back: higher values give more, smaller communities.

## The Louvain Algorithm: What Most People Actually Use

The Louvain algorithm became the standard because it's:
1. Fast (close to linear time in practice)
2. Simple (a greedy method; the main knob is the resolution parameter)
3. Effective (produces high modularity)

### How It Works (Conceptually)

**Phase 1: Modularity Optimization**
- Start with each node in its own community
- For each node, try moving it to each neighboring community
- If moving it increases modularity, do it
- Repeat until nothing improves

**Phase 2: Aggregation**
- Collapse each community into a single node
- The new graph has fewer nodes but preserves the community structure
- Repeat phases 1-2 until there's no change

This two-phase approach is why Louvain is fast - each phase runs in linear time.

### The Key Insight

Louvain doesn't require you to specify "how many communities are there?" It discovers the natural number. This is powerful because you don't have to guess.

The downsides: the algorithm is non-deterministic, so different node orderings can produce different communities - run it multiple times and look for communities that appear consistently. And, more seriously, it can produce **badly connected or even disconnected communities**.

### Leiden: Louvain, Fixed

[Traag, Waltman and van Eck (2019)](https://arxiv.org/abs/1810.08473) showed that Louvain can yield arbitrarily badly connected communities; in their experiments, up to 25% of communities were badly connected and up to 16% were disconnected. Their **Leiden algorithm** adds a refinement step between moving nodes and aggregating, which guarantees connected communities, and it also runs faster than Louvain.

If your library offers Leiden, use it. A "community" that is actually two disconnected pieces is a real problem when you're about to hand it to a fraud investigator as a ring.

## Other Community Detection Approaches

### Label Propagation: The Fast Alternative

**How it works:**
1. Each node starts with a unique label
2. Repeatedly: Each node adopts the label that's most common among its neighbors
3. Stop when labels stabilize

**Time complexity:** O(edges * iterations), usually converges in 5-10 iterations

**When to use:** When you need speed over accuracy, or you have huge graphs where Louvain is too slow

**Tradeoff:** Less theoretically grounded than Louvain, but practically fast and often good enough

### Spectral Clustering: The Mathematical Approach

Uses the eigenvectors of a matrix derived from the graph - usually the graph Laplacian - to find community structure.

**The intuition:** Graph structure encodes itself in the mathematical properties of the adjacency matrix. Nodes in tight communities have similar eigenvectors.

**When to use:**
- When you need mathematical guarantees
- When the graph has specific properties (e.g., bipartite networks)
- When you're doing theoretical work

**Downside:** Requires choosing how many communities in advance (typically k), and is slower than Louvain for large graphs

### Girvan-Newman: The Hierarchical Approach

**How it works:**
1. Compute betweenness centrality for all edges
2. Remove the edge with highest betweenness
3. Recompute betweenness centrality
4. Repeat

You end up with a tree (dendrogram) showing how the network would partition at different scales.

**When to use:** When you want hierarchical structure (communities within communities), or when you want to understand how tightly-knit groups are

**Downside:** O(V²) or O(V²*E) depending on implementation - slow for large graphs

## Real-World Examples

### Social Networks: Finding Friend Groups

Louvain on a friendship graph finds natural social circles. In real social networks, you typically get communities of 50-500 people who know each other.

The communities often correspond to:
- Geographic location (high school friends)
- Work (colleagues)
- Interest (gaming friends vs sports friends)

The algorithm doesn't know about these labels - it just finds density in the connection structure.

### Product Recommendation: Finding Product Clusters

Run Louvain on a "people who bought both products" graph:
- Nodes are products
- Edges connect products bought by the same person

You'll automatically discover product clusters:
- Electronics cluster together
- Sports equipment clusters together
- Home and garden clusters together

These are the groups you should recommend together. The algorithm discovers natural affinity without any product metadata.

### Fraud Detection: Finding Organized Rings

In transaction networks, fraudsters create distinctive community structure:
- Isolated communities (tight groups)
- Unusual modularity patterns (more connected than normal)
- Hierarchical structure (different from legitimate networks)

Finding communities first, then analyzing their structure, is often more effective than node-level anomaly detection.

### Biological Networks: Finding Functional Modules

Protein interaction networks have communities (proteins that work together):
- Metabolic pathways cluster together
- Signaling cascades form distinct communities
- Disease modules show dysfunction at the community level

## When Community Detection Matters vs When It Doesn't

**Community detection is valuable when:**
- Structure in the network is meaningful (social networks, biological networks, products)
- You want to understand what groups naturally form
- You're doing recommendations or fraud detection based on group membership
- You're designing systems where community awareness matters (community-aware caching, distributed load balancing)

**Community detection is less useful when:**
- The network is random or near-random (true random networks have very low modularity)
- You need pre-specified community sizes or counts
- Edges represent noisy features (a weak proxy for relationships)
- You care about hierarchical structure (overlapping communities)

## Overlapping Communities: The Hard Problem

One limitation of standard algorithms: They assign each node to exactly one community.

Real networks often have:
- Nodes in multiple communities
- Soft boundaries
- Hierarchical structure

Detecting overlapping communities is harder. Some approaches:

**Clique Percolation:** Find overlapping cliques (complete subgraphs) and treat them as overlapping communities. Slower but captures overlaps.

**Mixed Membership Models:** Each node has a probability distribution over communities, not a hard assignment. More flexible but requires tuning.

**Hierarchy-aware algorithms:** First find the hierarchy (like Girvan-Newman), then analyze overlaps at different levels.

The tradeoff: Complexity vs realism. For most use cases, Louvain's non-overlapping communities are practical enough.

## Implementation in Neptune Analytics

When running community detection at scale:

**Memory:** Louvain and Leiden use O(V + E) memory, so the constraint is fitting the graph in memory - which is exactly what Neptune Analytics is sized around.

**Execution time:** 
- Label Propagation: O(E * iterations) - typically seconds
- Louvain / Leiden: close to linear in practice - typically minutes
- Spectral: O(V²) - slow for very large graphs

**Key consideration:** These algorithms often need to be run on the entire graph to get meaningful results. You can't easily partition a graph and run detection on each partition independently.

**Practical approach:**
1. Run Leiden or Louvain on the full graph (check which your engine provides, and save the results)
2. Query community membership (fast lookups)
3. Re-run periodically (weekly or monthly, depending on how fast your network changes)

## The Deeper Pattern

Community detection, like centrality measures, is answering "what's the structure of this network?" Different algorithms answer different aspects:

- **Louvain/Modularity:** What's the most natural division?
- **Spectral:** What's the mathematical structure?
- **Label Propagation:** What emerges from local diffusion?
- **Hierarchical:** How do communities nest?

Often you'll use multiple algorithms on the same graph and look for communities that appear across methods. Robust communities show up in Louvain, spectral clustering, and label propagation.

That's a signal you can trust.

## Going Deeper

- [The Louvain Method paper](https://arxiv.org/abs/0803.0476) is readable and includes comparison to other methods
- [From Louvain to Leiden](https://arxiv.org/abs/1810.08473) explains the connectivity problem and the fix
- Community Detection in Graphs on Wikipedia covers the landscape
- Neo4j's Community Detection Algorithms has practical implementations

The key insight for 2026: Community detection is now a standard tool in the data scientist's toolkit. You're not doing cutting-edge research using these algorithms - you're solving practical problems with proven techniques.

The next time you need to understand the structure of a network, find natural groupings, or set up recommendations, reach for community detection. The algorithms will do the heavy lifting.

## Related Reading

- [Graph Algorithms Explained: PageRank, Centrality, and Why They Matter](/data-science/graph-algorithms-pagerank-centrality/)
- [Scaling Graph Algorithms: From Prototypes to Production](/data-science/scaling-graph-algorithms/)
- [The Causal Inference Comeback: Why Correlation-Era ML Hit a Wall](/data-science/causal-inference-comeback/)
