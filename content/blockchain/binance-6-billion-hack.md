---
title: "The $6.3 Billion Binance Hack: What We Know, What We Don't, and Why Hot Wallets Keep Failing"
date: 2026-11-01T21:30:00+00:00
draft: false
tags: ['blockchain', 'cryptocurrency', 'security', 'bitcoin', 'ethereum', 'news']
description: "Binance says hackers took more than $6 billion on 29 October 2026, likely the largest crypto theft on record. What is confirmed, what is only attributed, what has been frozen, and what is still unknown."
cover:
  image: /assets/images/blockchain/binance-6-billion-hack.jpg
  alt: The $6.3 Billion Binance Hack Banner
---

## TL;DR

- On **29 October 2026**, attackers drained roughly **$6.3 billion** of crypto from Binance wallets. Estimates run from about $5.9 billion (Chainalysis, per CoinDesk) to about $6.36 billion (TRM Labs, at transfer-time prices).
- Binance says it will **cover all losses**, and about **$3 billion** has been frozen so far.
- TRM Labs and Chainalysis both attribute it to **TraderTraitor**, a North Korean state-sponsored group. That is an attribution by blockchain-analytics firms. Binance has said only that it is working with law enforcement to confirm the attackers' identities.
- **The root cause is not public.** Binance's first account pointed to a compromised laptop. Later it said there were more "points of breach".

Coverage is still moving. Everything below reflects reporting as of 31 October and 1 November 2026, and some figures will change.

## What happened

According to TRM Labs, most of the money left in about 20 minutes, starting at 20:05 UTC on 29 October, across **ten blockchains**. The first theft hit the XRP Ledger, a Bitcoin hot wallet followed about 15 minutes later, and a second wave reached Avalanche and Polygon around 23:05 UTC.

TRM's breakdown of what moved:

| Chain | Roughly |
|---|---|
| Ethereum | $3.79 billion (including 200,630 ETH, 1.875 billion USDT, 823 million USDC) |
| Bitcoin | 18,270 BTC (about $1.47 billion) |
| Tron | about $628 million |
| XRP Ledger | about $296 million |
| Solana | about $96 million |
| Arbitrum, Optimism, Base | about $39 million combined |
| Avalanche, Polygon | about $28 million and $10 million |

For scale, TRM calls it about four times the $1.5 billion Bybit hack of February 2025. CoinDesk puts the stolen funds at roughly 4% of the $144 billion in assets Binance held before the attack (DefiLlama figure).

## How they got in: what is known and what is guessed

This is the part that matters most for anyone holding crypto on an exchange, and it is the part nobody has confirmed.

**What Binance has said.** CoinDesk reports that Binance's initial investigation pointed to a compromised DevOps engineer's laptop, which the attacker allegedly used to reach a service container and submit unauthorised withdrawals, and that Binance found no evidence of a wallet private key leak. PBS/AP reports that a later review found additional "points of breach". Co-CEO Richard Teng said Binance's own hot wallet was affected, that most user assets sit in offline cold wallets and move to hot wallets only for withdrawals, and that the attack used complex tactics including a "self-destruct mechanism" that complicates the investigation.

**What TRM Labs assesses.** TRM's view is that the most likely explanation is a compromise of Binance's hot wallet **signing infrastructure**, because funds moved across chains with different key types and signing schemes within about half an hour. On Ethereum, TRM says the attacker used an EIP-7702 delegation to turn a Binance hot wallet into a sweeper contract, using 50 pre-signed authorisations prepared in advance. On the other nine chains, it says Binance wallets sent funds through ordinary signed transfers. TRM also notes that Binance had yet to publish a root cause.

**One outside guess.** PBS/AP quotes NyxLab's Kok Tin Gan speculating that a single signature may have granted an attacker a never-expiring, full-access token to a hot wallet. That is an expert's interpretation of the pattern, not a finding.

My read, and it is only that: the common thread across these accounts is that the weak point looks like **the operational layer around the keys** (engineer machines, internal services, signing pipelines), not the cryptography. That would match how large exchange thefts have tended to go. But until Binance publishes a post-mortem, treat any specific mechanism as unconfirmed.

## Who did it

TRM Labs attributes the attack to TraderTraitor "with high confidence" and cites on-chain and off-chain intelligence. It points to features shared with earlier heists: small Tornado Cash funding, staging well ahead (it says preparation began at least 36 hours earlier), and signatures collected in advance. TRM notes the FBI attributed the Bybit hack to the same group. Chainalysis CEO Jonathan Levin said the firm assessed the attack was likely carried out by TraderTraitor. CoinDesk adds that ZachXBT named the Lazarus Group as the likely attacker.

Two cautions. First, these are private analytics firms, and their judgement is not a government finding. I did not find a confirmed FBI statement on this specific attack in the reports I read. Second, Binance itself did not confirm North Korean involvement. PBS/AP reports that when asked about North Korea, President Trump said officials are "looking at that".

## The money: frozen, moved, and still at large

- **Frozen.** Binance and partners froze about $3 billion. TRM's on-chain count is around $2.7 billion, including Tether (about 1.77 billion USDT), Circle (about 825 million USDC), Ripple (40.5 million RLUSD) and World Liberty Financial (27.8 million USD1), plus an Arbitrum Security Council action on about $30 million. Figures differ between outlets because they are snapshots taken at different times.
- **Laundering has started.** TRM says the attacker sold about 325 million USDT to market makers via UniswapX for about 122,300 ETH, at a discount of more than 10%, and supplied 60 million USDT to Aave to borrow about 19,760 ETH. CoinDesk, citing Arkham, reports the attacker also moved funds through Uniswap.
- **What cannot be frozen.** CNBC's explainer makes the key point: stablecoins can be frozen, burned and reissued by their issuers, but Bitcoin and ether have no issuer that can do that, so recovery depends on tracing funds to cooperating exchanges. TRM's Ari Redbord put it this way: "A freeze stops the money from moving, and recovery follows through legal process."

TRM expects future movement through bridges, swap services and OTC brokers. A caution on one number: TRM's article says the attacker still holds more than 420,000 ETH, but that does not reconcile with the 200,630 ETH it counts in the theft on Ethereum, so I would not repeat that figure.

## Are users safe?

Binance says deposits were unaffected and has promised to cover all losses. PBS/AP reports it has reserved more than $6.34 billion of company funds for that purpose. CoinDesk reports co-CEO Yi He said the platform would cover "all hacking losses", and that founder CZ said "User funds are safe".

On solvency, CNBC quotes Fundstrat's Farrell, who said the attack does not currently appear to create meaningful solvency risk and that "the key tell will be how quickly withdrawals resume and whether outflows stay orderly". He estimated the roughly $1.2 billion SAFU emergency fund could cover about a third of the remaining losses, with the rest coming from Binance's own funds. He also warned that a shortfall could force reserve sales and wider selling, though he did not think that was happening.

Withdrawals were suspended while Binance investigated, and PBS/AP says Binance expected them to resume within a day or two. I could not confirm that they have resumed.

## Market reaction

Per CoinDesk, Bitcoin fell 4.8% to below $77,000, ether fell 5.7%, BNB fell 8% and AAVE fell 11%. CNBC had Bitcoin trading below $78,000 on Friday.

## What I'm watching

- **A real post-mortem from Binance.** The difference between a compromised engineer laptop and a compromised signing system is the difference between a lesson for every exchange and a lesson for one.
- **Whether a government confirms attribution.** Analytics firms are confident. An official finding is a separate thing.
- **How much of the Bitcoin and ether gets cashed out.** The frozen stablecoins are the recoverable part. The rest depends on who is willing to touch the funds.
- **Withdrawal behaviour.** If outflows stay orderly after reopening, the solvency worry fades.

## The practical lesson

This is another case for not keeping more on an exchange than you are prepared to have frozen or delayed, and for holding long-term savings in your own custody. My earlier posts on [private keys](/blockchain/private-keys/) and [hardware wallets](/blockchain/hardware-wallets/) cover the basics. Even so, self-custody is no cure for everything: the people who lost the most here were the ones whose security depended on a company's internal systems.

## Related Reading

- [Private Keys in Cryptocurrency](/blockchain/private-keys/)
- [Hardware Wallets](/blockchain/hardware-wallets/)
- [The State of Blockchain in 2026](/blockchain/state-of-blockchain-2026/)

## Sources

- [North Korea Steals USD 6.36 Billion From Binance in the Largest Hack in History - TRM Labs](https://www.trmlabs.com/resources/blog/north-korea-steals-usd-6-36-billion-from-binance-in-the-largest-hack-in-history)
- [Binance's $6.3 billion hack: What we know and what comes next - CNBC](https://www.cnbc.com/2026/10/30/billions-in-crypto-frozen-in-binance-hack-heres-what-happens-next-.html)
- [Binance loses over $6 billion in the largest crypto hack to date - CoinDesk](https://www.coindesk.com/business/2026/10/29/potential-multi-billion-binance-hack-hitting-crypto-markets)
- [What to know about the $6.3B hack on Binance, likely the biggest-ever crypto theft - PBS NewsHour](https://www.pbs.org/newshour/world/what-to-know-about-the-6-3b-hack-on-binance-likely-the-biggest-ever-crypto-theft)
