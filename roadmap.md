# Blog Post Roadmap

A structured roadmap of upcoming blog posts, organized by category and priority.

## In Progress (Drafts)

These posts are currently being written:

### AI & LLMs
- [x] **ai-agents-that-actually-work.md** - Practical guide to building reliable AI agents (published: content/ai/ai-agents-that-actually-work.md)
- [x] **ai-safety-first-principles.md** - Safety considerations in agent design (published: content/ai/ai-safety-first-principles.md)
- [x] **fine-tune-vs-rag.md** - Comparison of fine-tuning vs retrieval approaches (published: content/ai/fine-tune-vs-rag.md)
- [ ] **multimodal-ai-2026.md** - The state of multimodal AI in 2026
- [x] **prompt-caching.md** - Optimizing costs and latency with prompt caching (published: content/ai/prompt-caching.md)

### Data Engineering
- [x] **modern-lakehouse-stack.md** - Building modern lakehouse architectures (published: content/data-engineering/modern-lakehouse-stack.md)
- [x] **stream-vs-batch-processing.md** - When to choose streaming vs batch (published: content/data-engineering/stream-vs-batch-processing.md)

### Music Production
- [ ] **hybrid-systems-montage-mc-707.md** - Integrating Montage with MC-707
- [ ] **mpe-deep-dive.md** - MPE (MIDI Polyphonic Expression) in depth
- [x] **yamaha-montage-m-six-months.md** - Six months with the Montage M (published: content/music-production/yamaha-montage-m-six-months.md)

### Ideas
- [x] **what-it-means-to-be-expert-in-2030.md** - Expertise futures essay (published: content/ai/what-it-means-to-be-expert-in-2030.md)

---

## Trust Series (Published)

Informal mini-series on conditions for trusting agents in production (`series: ["Trust"]` frontmatter):

- [x] **What I'm Researching in AI Right Now** (published: content/ai/what-im-researching-in-ai-right-now.md) - research manifesto framing the trust agenda
- [x] **AI Evals Are Broken** (published: content/ai/ai-evals-are-broken.md) - why public benchmarks fail
- [x] **Securing AI Agents** (published: content/ai/securing-ai-agents.md) - MCP hardening and the confused deputy problem
- [x] **World Models: What Comes After the Language-Only Era** (published: content/ai/world-models-after-language.md)
- [x] **Evaluating Agents in Production: Trajectory Metrics** - step-level scoring sequel (published: content/ai/evaluating-agents-in-production-trajectory-metrics.md)

---

## Next Priority Posts (Top 10)

The 10 highest-value posts to write next - chosen for importance, uniqueness (no existing post or roadmap item covers them), and practical usefulness to readers.

### AI & LLMs
- [x] **Context Engineering: The Discipline That Replaced Prompt Engineering** - Managing the whole context window - retrieval, memory, tool results, and compaction - as the core production skill, not clever wording (published: content/ai/context-engineering.md)
- [x] **Securing AI Agents: Tool-Calling Risks, MCP Hardening, and the Confused Deputy Problem** - Threat models and concrete defenses for agentic systems with real-world tool and data access (published: content/ai/securing-ai-agents.md)
- [x] **World Models: What Comes After the Language-Only Era** - Why simulators of physical and causal reality are the next research frontier, and what they unlock for robotics and agents (published: content/ai/world-models-after-language.md)
- [x] **AI Evals Are Broken: Why Benchmarks Stopped Measuring Real Capability** - Saturation, contamination, and workload-specific evals (published: content/ai/ai-evals-are-broken.md)
- [x] **Evaluating Agents in Production: Trajectory Metrics, Not Just Final Answers** - Step-level scoring, replay harnesses, and regression suites for multi-step agent quality (published: content/ai/evaluating-agents-in-production-trajectory-metrics.md)

### Data Engineering
- [ ] **The Semantic Layer: Making Metrics a First-Class Citizen** - How a shared metrics layer (dbt Semantic Layer, Cube) ends dashboard drift and conflicting definitions
- [ ] **Feature Stores in 2026: The Bridge Between Data Engineering and ML** - Online/offline parity, point-in-time correctness, and whether you actually need one
- [ ] **Lakehouse Disaster Recovery: Time Travel Is Not a Backup** - Designing RPO/RTO, cross-region replication, and recovery runbooks for table-format platforms

### Data Science
- [ ] **Graph Neural Networks: From PageRank to Learned Node Representations** - A practical introduction to GNNs and where they beat classic graph algorithms
- [ ] **Experimentation at Scale: A/B Testing Pitfalls and How to Avoid Them** - Peeking, network effects, variance reduction (CUPED), and trustworthy experiment design

### Personal Development
- [ ] **Staying Hands-On as a Staff Engineer** - Keeping technical depth while the role pulls toward leadership and breadth

---

## Upcoming Posts (Suggested)

### AI & LLMs
- [ ] **From Embeddings to Retrieval: Building Better RAG** - Deep dive into embedding models, similarity search, and RAG optimization
- [ ] **Agentic Workflows: When to Loop vs When to Orchestrate** - Architecture patterns for multi-step agent systems
- [ ] **The Cost of Context: Understanding Token Arithmetic** - Practical guide to optimizing token usage and cost-per-query
- [ ] **Latency Matters: Response Time Impact on UX** - Real-world performance analysis of AI API latency in production systems
- [ ] **Constitutional AI in Practice** - Building safe, aligned agent behaviors beyond prompt injection prevention

### AI & LLMs - Frontier (Ultra Futuristic)
- [ ] **Artificial General Intelligence: Timelines, Definitions, and What Actually Changes** - Cutting through hype to examine credible AGI milestones and their concrete impact on engineering work
- [ ] **Brain-Computer Interfaces Meet LLMs: The Neural Co-Processor** - How neural implants and language models could merge into a real-time cognitive layer
- [x] **Recursive Self-Improvement: Can AI Bootstrap Its Own Intelligence?** - The theory, the safety constraints, and where automated capability gains plausibly stop (published: content/ai/recursive-self-improvement.md)
- [ ] **Quantum Machine Learning: When Qubits Train Neural Networks** - Where quantum hardware genuinely accelerates learning, and where it is still marketing
- [ ] **Agent Economies: When AIs Negotiate, Transact, and Hire Each Other** - Autonomous agents with wallets, contracts, and reputation - and the infrastructure they need
- [ ] **The AI Scientist: Autonomous Research Agents That Discover, Not Just Assist** - End-to-end agents that form hypotheses, run experiments, and publish findings
- [ ] **Neuromorphic Computing: Brain-Inspired Chips for Always-On AI** - Spiking neural networks and event-driven silicon for ultra-low-power intelligence
- [ ] **Machine Consciousness: The Hard Problem Comes for AI** - What it would take to claim a model is sentient, and why the question matters for engineers
- [ ] **Digital Twins of You: Lifelong Personal AI and the Memory Problem** - Persistent personal models that learn across decades, and how to architect their memory
- [ ] **Embodied AI at Scale: Humanoid Robots and the Sim-to-Real Frontier** - Foundation models for robotics, simulation pipelines, and the leap from lab to living room

### Data Engineering
- [ ] **Building a Data Contract Layer** - Schema evolution, versioning, and governance for modern pipelines
- [ ] **Real-Time vs Eventual Consistency: The Trade-off Matrix** - When to pick each pattern with concrete examples
- [ ] **Debugging Data Lineage in Your Lakehouse** - Practical tools for tracing data quality issues end-to-end
- [ ] **Time Series at Scale: Metrics Database Design** - ClickHouse, VictoriaMetrics, or Timescale patterns

### Music Production
- [ ] **Programming Drums on the MC-707: Workflow Patterns** - Step-by-step beats with workflow optimization
- [ ] **MPE Workflow Comparison: Expressive vs Traditional MIDI** - Tangible use cases for expressive controllers
- [ ] **Integrating Montage with Your Gear: Real Setup Scenarios** - Practical routing and sequencing

### Personal Development
- [ ] **Engineering Your Sleep: Data-Driven Recovery** - Biohacking approach to sleep quality
- [ ] **Decision-Making Under Uncertainty: A Framework** - Practical mental models for big decisions

---

## Backlog (Extensive Ideas)

### AI & LLMs (40 posts)

**Prompt Engineering & Techniques**
- [ ] **Prompt Engineering Patterns That Actually Scale** - Modular prompts, templates, and reusable components
- [ ] **Chain of Thought vs Tree of Thought: When to Branch** - Comparing reasoning strategies for complex problems
- [ ] **Few-Shot Learning: Selecting Optimal Examples** - How to choose in-context examples for best performance
- [ ] **In-Context Learning vs Fine-Tuning: A Cost-Benefit Analysis** - Trade-offs in model adaptation approaches
- [ ] **System Prompts: The Invisible Architect** - Designing robust system prompts for production systems
- [ ] **Self-Consistency and Vote Aggregation** - Improving reasoning through multiple reasoning paths
- [ ] **Temperature, Top-P, and Sampling: Controlling Randomness** - Practical tuning of generation parameters
- [ ] **Prompt Injection: Attack Vectors and Defenses** - Real-world vulnerability patterns and mitigation

**Model Evaluation & Benchmarking**
- [ ] **Evaluating Language Models Beyond Accuracy** - Latency, cost, bias, hallucination, and safety metrics
- [ ] **Building Custom Evaluation Harnesses** - Testing models on domain-specific tasks
- [ ] **Benchmark Gaming: When Metrics Mislead** - Understanding and avoiding evaluation pitfalls
- [ ] **Human Evaluation Loops: Scaling Feedback** - Setting up annotation workflows for quality improvement

**Model Architecture & Optimization**
- [ ] **Quantization for Production: Int8, Int4, and Beyond** - Reducing model size without significant quality loss
- [ ] **Knowledge Distillation: Teaching Smaller Models** - Compressing large models into lightweight versions
- [ ] **Model Merging and Ensemble Techniques** - Combining multiple models for better performance
- [ ] **Inference Optimization: KV Cache, Flash Attention** - Production performance tuning techniques
- [ ] **Mixture of Experts: Scaling without Full Activation** - Efficient large model architecture patterns
- [ ] **Adapter Modules and LoRA: Efficient Fine-Tuning** - Low-rank adaptation for parameter-efficient tuning

**Tool Use & Function Calling**
- [ ] **Designing Function Calling APIs for LLMs** - Schema design patterns that maximize model reliability
- [ ] **Error Recovery in Multi-Step Tool Chains** - Handling failures gracefully in agentic workflows
- [ ] **Grounding Models with Real-Time Data** - Integrating live APIs and databases into model outputs
- [ ] **Building Reliable Reasoning with Structured Output** - JSON, XML, and schema validation for LLM outputs

**Vector Databases & Retrieval**
- [ ] **Vector Database Comparison: Pinecone vs Weaviate vs Milvus** - Feature and performance analysis
- [ ] **Hybrid Search: Keyword + Semantic** - Combining BM25 and vector similarity for better retrieval
- [ ] **Reranking: The Hidden Performance Multiplier** - Using a second model to improve retrieval quality
- [ ] **Chunking Strategies for RAG** - Optimal document segmentation for retrieval systems
- [ ] **Dense vs Sparse Retrieval Patterns** - When to use each retrieval strategy

**Deployment & Production**
- [ ] **Model Serving at Scale: vLLM, TGI, TensorRT** - Production inference frameworks compared
- [ ] **Canary Deployments for LLMs** - Safely rolling out model updates in production
- [ ] **Monitoring LLM Quality in Production** - Detecting degradation and drift over time
- [ ] **Multi-Region LLM Deployment** - Latency optimization and failure recovery strategies
- [ ] **Cost Attribution in Multi-Tenant LLM Systems** - Billing and usage tracking

**Safety & Alignment**
- [ ] **Detecting and Mitigating Hallucinations** - Techniques to identify and reduce false information
- [ ] **Adversarial Testing for Language Models** - Red-teaming and robustness evaluation
- [ ] **Watermarking LLM Outputs** - Detecting machine-generated text
- [ ] **Content Filtering and Moderation at Scale** - DLP and safety guardrails for LLM applications
- [ ] **RLHF in Production: Feedback Loops** - Continuous improvement from user feedback

### Data Engineering (35 posts)

**Data Modeling & Quality**
- [ ] **Fact and Dimension Tables: Dimensional Modeling Patterns** - Building robust star schemas
- [ ] **Data Validation Frameworks: Great Expectations and Beyond** - Automated quality checks at scale
- [ ] **Data Contracts: The Modern Data Agreement** - Schema governance and producer-consumer contracts
- [ ] **Handling Missing Data: Strategies at Scale** - Imputation, removal, and marking patterns
- [ ] **Referential Integrity in Data Warehouses** - Maintaining consistency across distributed systems
- [ ] **Slowly Changing Dimensions: Handling Updates** - Type 1, Type 2, and Type 3 patterns

**ETL & Pipelines**
- [ ] **ELT vs ETL: When Schema-on-Read Wins** - Advantages of moving transformation downstream
- [ ] **Incremental Loading Patterns** - Change Data Capture, watermarks, and state tracking
- [ ] **Idempotency in Data Pipelines** - Ensuring safe reruns and retries
- [ ] **Error Handling in Data Pipelines** - Dead letter queues, retry policies, and notifications
- [ ] **Data Pipeline Orchestration: Airflow, Prefect, Dagster** - Workflow scheduling and dependency management
- [ ] **Building Resilient Batch Processors** - Handling failures, backpressure, and recovery

**Streaming & Real-Time**
- [ ] **Exactly-Once Processing Semantics** - Achieving reliability in streaming systems
- [ ] **Windowing Patterns: Tumbling, Sliding, Session** - Aggregation strategies for time series
- [ ] **Stream Joins: Stateful Transformations** - Correlating events from multiple streams
- [ ] **Backpressure and Flow Control** - Handling upstream data rate mismatches
- [ ] **Event Time vs Processing Time** - Handling late and out-of-order data
- [ ] **Building Event Streaming Platforms** - Architecture patterns for high-volume event systems

**Distributed Systems & Architecture**
- [ ] **Eventual Consistency: Models and Trade-offs** - Causal, session, and read-your-write consistency
- [ ] **Partitioning Strategies: Range, Hash, Composite** - Scaling data systems horizontally
- [ ] **Replication and High Availability** - Master-slave, multi-master, and quorum patterns
- [ ] **Distributed Transactions: When You Need Them** - 2PC, saga patterns, and alternatives
- [ ] **Building Data Warehouses vs Data Lakes** - Strengths and weaknesses compared
- [ ] **Data Mesh: Decentralized Data Architecture** - Domain-driven data ownership
- [ ] **Building Data Catalogs** - Metadata management and discovery at scale

**Analytics & BI**
- [ ] **Star Schema vs Snowflake: Schema Design Patterns** - Trade-offs in dimensional design
- [ ] **Materialized Views and Incremental Refresh** - Pre-aggregation strategies
- [ ] **Query Optimization: Indexes, Statistics, Execution Plans** - Performance tuning techniques
- [ ] **OLAP Cubes and Pre-aggregation** - Building fast analytical systems
- [ ] **Real-Time Analytics Architectures** - Balancing freshness and performance

**Specific Technologies**
- [ ] **DuckDB: SQL on Data Files** - In-process analytics and ETL
- [ ] **Apache Iceberg: Time Travel and Schema Evolution** - Modern table formats explained
- [ ] **Delta Lake: ACID Transactions** - Building reliable data lakes
- [ ] **Apache Flink: Streaming and Batch Unified** - Complex event processing
- [ ] **Kafka: Event Streaming Architecture** - Building event-driven systems

### Music Production (20 posts)

**Sound Design & Synthesis**
- [ ] **Subtractive Synthesis: Oscillators to Filters** - Fundamentals of sound sculpting
- [ ] **Additive Synthesis: Building Tones from Harmonics** - Complex sound construction
- [ ] **Wavetable Synthesis: Modern Sound Design** - Creating and morphing waveforms
- [ ] **FM Synthesis: Creating Bell Tones and Bells** - Frequency modulation principles
- [ ] **Granular Synthesis: Texture and Ambient** - Advanced sound manipulation
- [ ] **Physical Modeling: Emulating Real Instruments** - String and wind modeling
- [ ] **Wavetable Automation: Dynamic Sound Evolution** - Movement and expression
- [ ] **Harmonics and Overtones: Building Rich Tones** - Understanding frequency content

**Audio Processing & Effects**
- [ ] **Compression: Threshold, Ratio, Attack, Release** - Dynamics control fundamentals
- [ ] **EQ Techniques: Surgical to Creative** - Additive and subtractive equalization
- [ ] **Reverb Types: Room, Hall, Plate, Spring** - Creating depth and space
- [ ] **Delay and Timing: Rhythmic Effects** - Syncing effects to tempo
- [ ] **Saturation and Distortion: Adding Warmth and Grit** - Harmonic enhancement
- [ ] **Sidechain: Creating Movement and Pumping** - Modulation from external sources
- [ ] **Parallel Compression: Thick and Full Mixes** - Blending compressed and dry signals
- [ ] **Multiband Processing: Frequency-Specific Effects** - Targeted signal shaping

**Mixing Techniques**
- [ ] **Gain Staging: Setting Levels Correctly** - Foundation for mixing
- [ ] **Panning and Stereo Width: Creating Space** - Spatial arrangement of tracks
- [ ] **Bussing and Group Processing** - Organizing and processing tracks together
- [ ] **Automation: Bringing Life to Mixes** - Dynamic parameter control
- [ ] **Submixes and Color** - Creative use of busses for cohesion
- [ ] **Checking Your Mix: Reference Tracks** - Comparing and calibration

**Production Workflow**
- [ ] **Arrangement: Structure and Pacing** - Song forms and development
- [ ] **Chord Progressions: Building Emotional Arcs** - Harmony fundamentals
- [ ] **Melody Writing: Singability and Catchiness** - Crafting memorable hooks
- [ ] **Drum Programming: Groove and Pocket** - Humanizing drum patterns
- [ ] **Layering: Building Depth and Texture** - Combining elements effectively

### Personal Development (15 posts)

**Learning & Skill Building**
- [ ] **Deliberate Practice: Efficient Skill Development** - The 10,000-hour myth and reality
- [ ] **Spaced Repetition: Science of Long-Term Memory** - Building retention systems
- [ ] **Learning in Public: Building an Audience** - Sharing progress and learning together
- [ ] **Teaching Others: The Best Way to Learn** - Learning through explanation
- [ ] **Building Deep Technical Expertise** - T-shaped and specialized knowledge

**Productivity & Time Management**
- [ ] **Time Blocking: Protecting Deep Work** - Scheduling focused work sessions
- [ ] **Context Switching Costs: Why Interruptions Hurt** - Minimizing disruption
- [ ] **Batching Work: Minimizing Setup Cost** - Grouping similar tasks
- [ ] **Energy Management: Beyond Time Management** - Working with natural rhythms
- [ ] **The 2-Minute Rule and Task Momentum** - Getting started and maintaining flow

**Mental Models & Thinking**
- [ ] **Systems Thinking: Understanding Feedback Loops** - Seeing interconnections
- [ ] **Bayesian Thinking: Updating Beliefs** - Probabilistic reasoning in practice
- [ ] **First Principles: Breaking Down Complex Problems** - Reasoning from fundamentals
- [ ] **Occam's Razor: Simplicity in Explanations** - When less is more
- [ ] **Cognitive Biases in Decision Making** - Common thinking errors and mitigation

**Health & Wellness**
- [ ] **Sleep Optimization: Temperature, Light, Timing** - Improving sleep quality
- [ ] **Exercise for Cognitive Performance** - Physical activity and brain health
- [ ] **Nutrition for Focus and Energy** - Food impacts on productivity
- [ ] **Stress Management Techniques** - Reducing chronic stress
- [ ] **Building Sustainable Habits** - Creating lasting change

### Gaming & Game Technology (12 posts)

- [ ] **Game Technology in 2026: Inside the Stack Behind a Live Service Game** - The five layers of a modern live game and how they fit together (published: content/gaming/game-technology-2026.md)
- [ ] **Game Telemetry at Scale: The Data Pipeline Behind a Live Game** - Ingesting billions of player events a day and serving every consumer from one stream
- [ ] **Netcode Explained: Rollback, Lockstep, and Client-Side Prediction** - The techniques that hide the speed of light in multiplayer games
- [ ] **Matchmaking Systems: Skill Rating and the Math of a Fair Match** - Balancing match quality, queue time, and connection quality in real time
- [ ] **Anti-Cheat in 2026: Kernel Drivers, Server Authority, and ML Detection** - How studios detect and deter cheating, and the trade-offs of each approach
- [ ] **Game Engines Compared: Unreal 5, Unity, Godot, and the In-House Question** - Choosing who owns the hardest bugs
- [ ] **LiveOps: Running a Game as a Service** - Seasons, events, and steering a live game with data
- [ ] **The Economics of Free-to-Play: Monetisation and Player Lifetime Value** - How free games make money and what the data looks like
- [ ] **Cloud Gaming in 2026: Latency, Streaming, and Whether It Finally Works** - The infrastructure behind game streaming and its real constraints
- [ ] **Procedural Generation: From Noise Functions to Infinite Worlds** - Algorithms for generating game content at scale
- [ ] **AI in Games: NPC Behaviour, Generative Content, and Player Modelling** - Where machine learning is changing how games are built and played
- [ ] **Player Analytics: Funnels, Retention, and Reading Behaviour From Events** - Turning raw telemetry into design and business decisions

### Security & Cybersecurity (12 posts)

- [x] **Threat Modeling for Engineers: Finding the Flaws Before Attackers Do** - A structured way to find design flaws before writing code (published: content/security/threat-modeling-for-engineers.md)
- [ ] **The Software Supply Chain: SBOMs, Dependency Risk, and Lessons From xz** - Securing what you depend on, not just what you write
- [ ] **Secrets Management: Vaults, Rotation, and Why .env Files Keep Leaking** - Handling credentials without scattering them across the codebase
- [ ] **Zero Trust Explained: Identity as the New Perimeter** - What zero trust actually means beyond the marketing
- [ ] **Cryptography for Engineers: What to Use and What to Never Touch** - Practical crypto choices without rolling your own
- [ ] **OAuth and OIDC Demystified: Tokens, Flows, and Common Mistakes** - The protocols behind modern auth, explained clearly
- [ ] **Securing AI Agents: Tool-Calling Risks and the Confused Deputy Problem** - Threat models and defenses for agentic systems (cross-referenced with the AI section)
- [ ] **The Anatomy of a Data Breach: How Attacks Actually Unfold** - Walking a real breach from initial access to exfiltration
- [ ] **Container and Kubernetes Security: Hardening the Stack** - Securing the layers from image to cluster
- [ ] **Security for Data Pipelines: Access Control, PII, and Exfiltration** - Protecting data systems specifically
- [ ] **Passkeys and the End of Passwords** - How passkeys work and why they replace passwords
- [ ] **Red Team vs Blue Team: How Security Testing Actually Works** - Offensive and defensive security testing in practice

### Software Engineering (12 posts)

- [x] **System Design Fundamentals: Making Trade-offs You Won't Regret** - The core axes every design decision moves along (published: content/software-engineering/system-design-fundamentals.md)
- [ ] **API Design That Lasts: REST, gRPC, and the Contract Mindset** - Designing interfaces that survive their first version
- [ ] **Rust for the Curious: When It Earns Its Complexity** - Where Rust's guarantees are worth the learning curve
- [ ] **Go in Practice: Why It Keeps Winning Backend Work** - The language design choices behind Go's staying power
- [ ] **Testing Strategy: The Pyramid, the Trophy, and What to Actually Test** - Choosing what to test and at which level
- [ ] **Debugging as a Discipline: From Print Statements to Systematic Diagnosis** - Turning debugging from luck into method
- [ ] **Code Review That Improves Code, Not Just Catches Bugs** - Making review a tool for design and learning
- [ ] **Design Patterns Worth Knowing in 2026 (and the Ones to Forget)** - Which classic patterns still earn their place
- [ ] **Concurrency Models Compared: Threads, Async, Actors, and CSP** - Choosing a concurrency model for the problem
- [ ] **Technical Debt: Naming It, Measuring It, Paying It Down** - Making debt visible and manageable
- [ ] **Reading Code: The Underrated Engineering Skill** - Getting fast and accurate at understanding code you did not write
- [ ] **The Art of the Interface: Abstraction Boundaries That Don't Leak** - Designing boundaries that hide the right things

---

## Notes

- Posts follow the metadata requirements in [README.md](README.md)
- All posts require cover images and proper YAML frontmatter
- Links must be verified before publication
- Tags should use singular form (e.g., `ai` not `ai-tools`)
- Dates use ISO 8601 format with timezone (e.g., 2026-04-28T14:30:00+01:00)
