---
title: "Quantum Computing: A Threat to Bitcoin?"
date: 2026-05-20T09:00:00+01:00
draft: false
tags: ['bitcoin', 'blockchain', 'quantum-computing', 'cryptography', 'security', 'web3', 'post-quantum']
description: "How real is the quantum threat to Bitcoin in 2026? A grounded update on the timeline to Q-Day, how much BTC genuinely sits at risk, the recent quantum milestones, and the defences taking shape - BIP-360, BIP-361 and NIST's post-quantum cryptography standards."
cover:
  image: /assets/images/blockchain/quantum-threat.png
  alt: "Quantum Computing: A Threat to Bitcoin? Banner"
---

## TL;DR

- Quantum computers threaten Bitcoin because [Shor's algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm) can derive a private key from an exposed public key, breaking the ECDSA and Schnorr signatures that authorise transactions.
- The threat is **real but not imminent**. Credible estimates put a cryptographically relevant quantum computer somewhere between **2029 and 2035**. Research cited by Google and Bitcoin security analysts suggests a roughly **10% chance** of a break by 2032.
- Around **6.9 million BTC** - close to a third of all supply - sit in addresses with exposed public keys, including roughly **1 million BTC believed to belong to Satoshi Nakamoto**. These are the coins most at risk.
- Mining (SHA-256) is **far less exposed**. Grover's algorithm only offers a quadratic speed-up, which higher network difficulty can absorb.
- Bitcoin's defences are forming: **BIP-360** adds a quantum-resistant address type, **BIP-361** proposes a controversial migrate-or-freeze deadline, and **NIST** has finalised post-quantum standards (ML-DSA, SLH-DSA) for future signature schemes to draw on.
- The safest action for an ordinary holder today: **use a modern address and never reuse it**, so your public key stays hidden behind a hash until you spend.

## Overview

Quantum computing is one of the most significant theoretical threats to modern cryptography. For Bitcoin, the core concern is that a sufficiently powerful quantum computer could run **Shor's algorithm** to solve the elliptic curve discrete logarithm problem - the hard maths that secures Bitcoin's public-key cryptography.

This is not a new debate, but it has moved from the fringe to the mainstream over the past year. In April 2026, Nobel Prize-winning physicist [John M. Martinis](https://www.coindesk.com/business/2026/04/07/bitcoin-quantum-threat-is-real-and-closer-than-it-looks-says-nobel-physicist), who helped build Google's early quantum processors, warned that Bitcoin could be one of the earliest real-world targets of a quantum attack, calling cryptography "the low-hanging fruit" for the technology. A panel of cryptographers convened by Coinbase reached a similar conclusion: a machine capable of breaking blockchain encryption will eventually be built, and the industry should begin migrating now.

The good news is that "eventually" is still years away, and Bitcoin has time to adapt. The bad news is that the migration itself will take years - so the preparation has to start well before the threat arrives.

## How Bitcoin Cryptography Works

Bitcoin relies on two distinct cryptographic primitives, and they face very different levels of quantum risk.

- **Digital signatures** - Bitcoin uses the **secp256k1** elliptic curve with ECDSA, and since the Taproot upgrade also Schnorr signatures. These prove that the owner of a private key authorised a transaction. Both are vulnerable to Shor's algorithm.
- **Hashing** - Bitcoin uses **SHA-256** for mining (proof-of-work) and to derive most address formats. Hash functions are only weakened, not broken, by quantum computers.

The distinction matters. The realistic quantum threat is against signatures, not against mining or hashing.

### The Vulnerabilities

- **ECDSA and Schnorr signatures** - Both are built on the discrete logarithm problem. A large, fault-tolerant quantum computer running Shor's algorithm could derive a private key from its corresponding public key, allowing an attacker to spend coins they do not own.
- **Public key exposure** - This is the crux of the problem. Bitcoin addresses are typically a *hash* of a public key, and a hash gives no useful information to a quantum attacker. The risk only appears once the public key itself is visible on-chain - which happens with legacy P2PK outputs, any address that has been reused, and, notably, Taproot outputs, which expose a public key the moment they are funded.
- **The transaction window** - When you spend from a hashed address, your public key is revealed in the transaction. Between broadcast and confirmation - often around ten minutes - a quantum attacker could in principle derive the key and broadcast a competing transaction. This is a much harder, time-boxed attack than draining a long-dormant address with a permanently exposed key.
- **Mining (SHA-256)** - [Grover's algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm) could speed up the search for valid blocks, but only quadratically rather than exponentially. That effectively halves SHA-256's security margin (256-bit to a still-comfortable 128-bit) and can be offset by rising difficulty and hash rate. Mining is not where the danger lies.

## How Close Is Q-Day?

"Q-Day" is the informal name for the point at which a quantum computer can break the cryptography securing real assets. We are not there, but the trend line has steepened.

- **Hardware milestones** - Google's *Willow* chip (December 2024) and Microsoft's *Majorana 1* (February 2025) showed meaningful progress on error correction, the hardest part of scaling. Today's machines still measure in the low hundreds of qubits.
- **The first real attacks** - In September 2025, researcher Steve Tippeconnic broke a 6-bit elliptic curve key on quantum hardware. In April 2026, Giancarlo Lelli [broke a 15-bit key](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech) to win Project Eleven's "Q-Day Prize" of 1 BTC - a 512x jump in just seven months. Bitcoin uses 256-bit keys, so this is still a long way from a real break, but the direction of travel is clear.
- **Falling resource estimates** - Just as important, the cost of a full attack keeps dropping. A 2025 estimate put a break of RSA-2048 at roughly a million qubits; a Google whitepaper in April 2026 estimated under 500,000 physical qubits for a 256-bit elliptic curve attack, and a follow-up from Caltech researchers suggested a neutral-atom architecture could need as few as ~10,000. Algorithms are improving faster than hardware.
- **The consensus timeline** - Most credible estimates now place the risk window between **2029 and 2035**. Project Eleven puts a greater-than-50% likelihood of a capable machine by 2033. Tellingly, [Google has committed to migrating its own infrastructure](https://www.coindesk.com/tech/2026/03/28/watch-out-bitcoin-devs-google-says-post-quantum-migration-needs-to-happen-by-2029) to post-quantum cryptography by 2029 - a useful signal of how seriously the people building these machines take the deadline.

The honest summary: a quantum computer that can break Bitcoin is still at least two major engineering leaps away, but "not imminent" is not the same as "not urgent."

## How Much Bitcoin Is Actually at Risk?

Estimates vary, but research broadly converges on **around 6.9 million BTC** - close to a third of the circulating supply - sitting in addresses whose public keys are already exposed on-chain. Several categories make up that figure:

- **Satoshi-era P2PK coins** - The earliest blocks paid directly to raw public keys. An estimated **~1 million BTC attributed to Satoshi Nakamoto** sits in this format, untouched since 2009 and fully exposed.
- **Reused addresses** - Any address that has spent funds has revealed its public key. Reusing it afterwards leaves the remaining balance exposed.
- **Taproot outputs** - Because P2TR commits to a public key directly, those funds are exposed from the moment they are received.

It is worth keeping perspective. A widely cited [CoinDesk analysis](https://www.coindesk.com/markets/2026/04/23/the-usd145-billion-math-why-bitcoin-s-quantum-threat-is-manageable-not-existential) argued the threat is "manageable, not existential": even a large tranche of vulnerable coins represents only a couple of months of typical long-term-holder selling, which the market could absorb if released gradually. The deeper problem is less about price and more about governance - what the network should do about coins their owners can no longer protect, or in Satoshi's case, may no longer be around to move.

## Mitigation and Post-Quantum Bitcoin

The Bitcoin community is well aware of these risks, and 2026 has been the year concrete proposals finally landed in the official Bitcoin Improvement Proposal (BIP) repository.

### BIP-360: A Quantum-Resistant Address Type

[BIP-360](https://bip360.org/) introduces a new output type, **Pay-to-Merkle-Root (P2MR)**. It behaves much like a Taproot output but removes the quantum-vulnerable key-path spend, committing only to the Merkle root of a script tree. Authored by Hunter Beast, Ethan Heilman and Isabel Foxen Duke, it was [merged into the BIP repository](https://bitcoinmagazine.com/news/bitcoin-advances-toward-quantum-resistance) in February 2026 - though as a draft, not an active soft fork. The proposal has evolved through several names (P2QRH, then P2TSH, now P2MR), and BTQ Technologies has already shipped a working implementation on a Bitcoin Quantum testnet. The full specification lives in the [BIP-360 document](https://github.com/bitcoin/bips/blob/master/bip-0360.mediawiki).

### BIP-361: The Controversial Migrate-or-Freeze Plan

A quantum-safe address type is useless if nobody moves their coins to it. **BIP-361**, co-authored by Casa CTO Jameson Lopp and others, tackles that with a three-phase soft fork: first wallets stop sending to legacy address types, then legacy signatures become invalid at the consensus layer, **freezing any coins that did not migrate** in time - roughly a five-year window. A possible third phase would let frozen-coin holders recover funds via a zero-knowledge proof tied to their seed phrase.

It is deeply contentious. Critics see freezing unmigrated coins as a violation of Bitcoin's core promise that valid coins stay spendable, with early community sentiment running heavily negative. Supporters argue the alternative - leaving millions of BTC for a quantum attacker to harvest - is worse. Expect this debate to run for years.

### NIST Post-Quantum Standards

Bitcoin does not have to invent new cryptography from scratch. In August 2024, [NIST finalised its first post-quantum standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards): **ML-KEM** (FIPS 203) for key exchange, and **ML-DSA** (FIPS 204) and **SLH-DSA** (FIPS 205) for digital signatures. SLH-DSA, a stateless hash-based scheme, is especially relevant to Bitcoin because its security rests only on hash functions. Future quantum-resistant signature schemes for Bitcoin are likely to build on these NIST-vetted designs. The full programme is documented on the [NIST Post-Quantum Cryptography project page](https://csrc.nist.gov/projects/post-quantum-cryptography).

### What Holders Can Do Now

- **Use a modern address and never reuse it.** A native SegWit (`bc1q...`) address keeps your public key hidden behind a hash until the moment you spend, removing you from the "permanently exposed" category.
- **Consolidate coins out of legacy P2PK and reused addresses** if you still hold any.
- **Follow the BIP-360 and BIP-361 discussions** rather than panic-selling on quantum headlines - the timeline gives ample room to migrate calmly.

## Video Explainers

### Quantum Computers Explained - Limits of Human Technology

{{< youtube JhHMJCUmq28 >}}

Kurzgesagt's animated primer on how quantum computers work and why they differ fundamentally from classical machines - the best starting point if the concept is new to you.

### What Makes Quantum Computers SO Powerful?

{{< youtube -UrdExQW0cs >}}

Veritasium digs into superposition, interference and why a quantum computer is not simply a faster classical one - useful context for understanding why Shor's algorithm is such a leap.

### Will Quantum Computing Kill Bitcoin?

{{< youtube rjYFcElfA_s >}}

Physicist Sabine Hossenfelder gives a clear-eyed, hype-free assessment of whether quantum computers really threaten Bitcoin, and how far away the danger actually is.

### Bitcoin's Quantum Countdown

{{< youtube Ykwi-3S1bYs >}}

Coin Bureau breaks down the value at risk, the Q-Day timeline and how different networks are responding - a solid overview of the 2026 state of play.

### Bitcoin Q&A: Is Quantum Computing a Threat?

{{< youtube wlzJyp3Qm7s >}}

Andreas Antonopoulos explains why hashed addresses provide a buffer and why the threat is often overstated in the press.

### Bitcoin Q&A: Migrating to Post-Quantum Cryptography

{{< youtube dkXKpMku5QY >}}

A companion talk from Andreas on how the Bitcoin protocol can evolve, via soft fork, to adopt quantum-resistant signatures without breaking the network.

## Further Reading

- [What Is Q-Day? The Quantum Threat to Bitcoin Explained](https://decrypt.co/resources/what-q-day-quantum-threat-bitcoin-explained) - Decrypt
- [Researcher wins 1 BTC bounty for the largest quantum attack on elliptic curve cryptography to date](https://www.coindesk.com/tech/2026/04/24/researcher-wins-1-bitcoin-bounty-for-largest-quantum-attack-on-underlying-tech) - CoinDesk
- [Google says post-quantum migration needs to happen by 2029](https://www.coindesk.com/tech/2026/03/28/watch-out-bitcoin-devs-google-says-post-quantum-migration-needs-to-happen-by-2029) - CoinDesk
- [Bitcoin developers propose freezing coins that skip quantum-safe migration under BIP-361](https://news.bitcoin.com/bitcoin-developers-propose-freezing-coins-that-skip-quantum-safe-migration-under-bip-361/) - Bitcoin.com News
- [The $145 billion math: why Bitcoin's quantum threat is manageable, not existential](https://www.coindesk.com/markets/2026/04/23/the-usd145-billion-math-why-bitcoin-s-quantum-threat-is-manageable-not-existential) - CoinDesk
- [BIP 360: Pay-to-Merkle-Root (P2MR)](https://bip360.org/) - the proposal's official site

## Related Reading

- [The State of Blockchain in 2026](/blockchain/state-of-blockchain-2026/)
- [Private Keys in Cryptocurrency](/blockchain/private-keys/)
- [Cryptocurrency Hardware Wallets](/blockchain/hardware-wallets/)
- [Real World Asset Tokenisation: The Slow Revolution in 2026](/blockchain/real-world-asset-tokenisation/)
