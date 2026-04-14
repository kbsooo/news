---
title: "Simulation: Branching outcomes of the April 11 US-Iran Islamabad talks — flow-through to Korea, US/Korea equities, and global crypto"
type: simulation
date: 2026-04-12
scenario: "Islamabad negotiations (Vance ↔ Qalibaf, brokered by Munir) opened April 11. What are the branching outcomes over the next 8 months, and how do they flow through to the Korean economy, US and Korean equities, and global crypto (BTC + ETH + altcoins)?"
variables: [iran_nuclear_decision, hormuz_transit, brent_oil, usd_krw, kospi, sp500, btc_eth_crypto, samsung_sk_hynix, us_10y_yield, gold, korean_jeonse_credit]
confidence: medium
based_on:
  - iran
  - iran-war-and-ceasefire-2026
  - donald-trump
  - south-korea
  - financial-markets-2026
  - iran-war-economic-impact
  - strait-of-hormuz
  - pakistan
  - gulf-states
  - china
  - israel
  - market-snapshot
sources:
  - raw/middle-east-and-africa/260411-third-time-the-charm.md
tags: [simulation, iran, korea, markets, crypto, equities, scenarios]
---

# Branching Scenarios of the April 11 Islamabad US-Iran Talks

## Why This Simulation

The previous version of this file (deleted 2026-04-12) was written on day 0 of the Serena hotel talks. This rewrite refreshes the analysis with a **WebSearch-grounded market snapshot** (actual S&P 500, KOSPI, Brent, BTC, gold, USD/KRW as of Apr 11-12) and extends coverage in three directions:

1. **High-frequency trajectory** — next 14 days while the two-week truce clock runs
2. **Crypto granularity** — not just BTC but ETH and altcoin correlation structure
3. **Korean ticker-level detail** with explicit jeonse/household credit amplifier

Primary source: The Economist, [raw/middle-east-and-africa/260411-third-time-the-charm.md](raw/middle-east-and-africa/260411-third-time-the-charm.md) — "America and Iran start a high-stakes negotiation" (April 11, 2026).

## Current Snapshot (2026-04-12, WebSearch anchor)

Mixed signals. Equities have priced a *ceasefire-holds-and-deal-gets-done* path too eagerly; physical oil and gold are pricing *tail risk*; FX and the won are pricing *Korea-as-epicenter*.

| Asset | Level | Note |
|---|---|---|
| S&P 500 | **6,617** | best week since Nov 2025 after ceasefire; futures sanguine |
| KOSPI | **5,778** | -1.61% Apr 10 on ceasefire uncertainty (snapped 4-day rally) |
| Nikkei 225 | positive YTD | one of three major indices with YTD gains |
| Shanghai Composite | 3,986 | +23.1% YoY; +2.7% Apr 8 on ceasefire headline |
| Brent crude | **$96.69** | futures sanguine; physical grades touched $150 at war peak |
| Gold | **$4,762.62/oz** | all-time-high zone — hedge demand has NOT unwound |
| USD/KRW | **1,479** | won sharply weaker; Korea pricing twin shocks (energy + chip-order drag) |
| US 10Y | **~4.3%** | stagflation whipsaw per [[financial-markets-2026]] |
| BTC | **~$71k** | significant pullback from late-2025 peak |
| ETH | **~$2,250** | ETH/BTC ratio at multi-year lows — beta washed out |
| US CPI | 3.3% YoY March | up from 2.4% Feb, petrol-led |

**The market divergence is the story.** SPX and KOSPI are behaving like the ceasefire will hold and a deal will come; gold at $4,762 and Brent physical at $150 disagree. Reconciling these implies the market is underpricing tail outcomes — relevant for position sizing the scenarios below.

See [[market-snapshot]] for full table. Reconciliation note: some WebSearch indices (KOSPI 5,778) are higher than wiki-internal narrative would have implied (wiki shows 2,550 post-war). This simulation uses WebSearch values as the anchor since they reflect the *actual* price of risk today.

## Scenario Matrix

| # | Scenario | P | Iran nuclear | Hormuz traffic (ships/day) | Ceasefire durability |
|---|---|---|---|---|---|
| A | **Grand Bargain** (JCPOA+) | ~12% | HEU surrendered to Kazakh/IAEA custody; cap 3.67% | Free nav, 130+ | Permanent framework |
| B | **Interim Deal → Modus Vivendi** (base) | ~50% | HEU frozen under dual US+China seal; enrichment capped 20% | Managed tolls, 40-60 | Rolling 2-wk extensions |
| C | **Talks Collapse → Limited Strikes** | ~28% | Dash to 90%+ enrichment; IAEA expelled | Re-blockaded, tolls weaponized | Broken by Q3 2026 |
| D | **Nuclear Breakout → Preemptive Strike** (tail) | ~10% | Iran declares or Israel/US strike Fordow | Shut + mining threat | Open war |

Probability rationale for changes vs old matrix:
- **A bumped 10→12%**: Khamenei's absence is a larger structural unlock than usually modeled. Vance-Qalibaf direct channel without the supreme leader's "no decisions" rule genuinely raises ceiling.
- **B trimmed 55→50%**: Gold $4,762 and oil physical $150 say the market is NOT as confident in muddle-through as the equity indices are. Tail weights deserve more mass.
- **C bumped 25→28%**: Iran added the Lebanon and $6bn frozen-oil demand **while Vance was already in the air** — classic pre-collapse signaling. Arab diplomats are preparing for the Gaza-ceasefire template (halt the fighting, never get to the hard issues) which itself is a fragile equilibrium.
- **D unchanged at 10%**: 400kg HEU + a wounded Mojtaba/IRGC faction is a real breakout path, but the IRGC is **splintering**, which cuts both ways.

### Macro Endpoints (by end-2026)

Anchored to WebSearch current levels (2026-04-12). Arrows show direction from today.

| Variable | Today (Apr 12) | A (Grand Bargain) | B (Interim, base) | C (Collapse) | D (Breakout) |
|---|---|---|---|---|---|
| Brent ($/bbl) | 96.69 | **$62** ↓ | **$84** ↓ | **$138** ↑ | **$180+** ↑ |
| USD/KRW | 1,479 | **1,330** ↓ | **1,450** ↓ | **1,590** ↑ | **1,730** ↑ |
| KOSPI | 5,778 | **6,600** ↑ | **5,850** ↑ | **4,400** ↓ | **3,600** ↓ |
| US 10Y yield | 4.3% | **3.6%** ↓ | **4.1%** ↓ | **4.9%** then **4.2%** | **5.1%** then **3.6%** |
| S&P 500 | 6,617 | **7,300** ↑ | **6,750** ↑ | **5,550** ↓ | **4,800** ↓ |
| Gold ($/oz) | 4,762 | **3,900** ↓ | **4,400** ↓ | **5,300** ↑ | **6,000+** ↑ |
| BTC ($k) | 71 | **108** ↑ | **78** ↑ | **95** ↑ | **120** ↑ |
| ETH ($) | 2,250 | **4,100** ↑ | **2,550** ↑ | **2,200** flat | **2,600** ↑ |
| ETH/BTC | 0.032 | 0.038 ↑ | 0.033 ↑ | 0.023 ↓ | 0.022 ↓ |
| Hormuz ships/day | 10 | 130 | 55 | 5 | 0 |
| Iran HEU | ~3mo to weapon | defused | frozen | 2-4 weeks | weaponized |
| Korea jeonse stress | elevated | relieved | elevated | severe | crisis |

### Key Non-Obvious Patterns

1. **BTC is positive-skew across all four states.** Every scenario delivers BTC up from $71k. Grand bargain via USD weakness + risk-on; tails via sanctions-plumbing (Iran needs to move money) + digital-gold bid. **Middle case B is BTC's worst risk-adjusted outcome** — small upside, modest vol decline, opportunity cost vs KOSPI/SPX.
2. **ETH decouples from BTC in the tails.** ETH is **beta, not hedge**. Scenarios C and D crush ETH/BTC ratio further because ETH is priced as "risk-on tech" not "alternative money." This is the cleanest pair trade in the matrix: long BTC / short ETH in collapse/breakout; long ETH / short BTC in grand bargain.
3. **Gold does NOT round-trip.** Even in Grand Bargain, gold only goes to $3,900 — not back to $2,400 pre-war. The USD's reserve-status damage from the [[nato-and-transatlantic-crisis|transatlantic divorce]] + Trump trade-war legacy + central bank EM buying makes this shift structural.
4. **Korea is asymmetric.** KOSPI upside in A is +14%; downside in D is -38%. This is not symmetric because:
   - Upside is capped by the won strengthening (KOSPI gains in local currency get eaten by FX)
   - Downside compounds through jeonse/household credit (next section)
5. **The S&P-KOSPI correlation breaks.** In A and B, both rally. In C and D, S&P loses ~16% and ~28% respectively, but KOSPI loses ~24% and ~38% — Korea has more residual Iran-exposure beta than the US because of energy intensity + geographic proximity of supply chains.

---

## Scenario A — Grand Bargain (~12%)

### Geopolitical Path
Vance and Qalibaf use the **Khamenei-gone** structural unlock — the 37-year first-ever direct talks without the supreme leader's "no decisions" constraint. Within 8-10 weeks: IAEA re-enters Fordow, 400kg HEU shipped to Kazakhstan (or to China under IAEA seal), enrichment capped at 3.67%, missile range voluntarily limited to 2,000km, all pre-war sanctions lifted in phases. [[gulf-states|MBS]] normalizes with Tehran; Israel gets an explicit US nuclear umbrella and a 30,000-troop permanent presence in Syria/Iraq as offset. [[donald-trump|Trump]] claims the deal publicly, Vance banks it for 2028. [[china|Xi]] co-signs as guarantor at the May summit — this is the fork where China becomes a **top-tier security architect** of the Gulf, matching its already-dominant economic role.

**Early triggers (next 14 days) that would move P(A) from 12% to 25%**:
- US confirms $6bn Qatar unfreeze + signals $150bn broader phased relief
- Israel accepts 60-day Lebanon freeze (hard ask; Netanyahu would need a coalition partner swap)
- Iran releases US-Iranian dual nationals held in Evin
- IAEA delegation receives Fordow visa within 21 days

### South Korea Impact
- **Immediate (within 2 weeks)**: KOSPI gaps up +4-5% on announcement; Won to 1,420, then to 1,330 over 3 months as current-account stress reverses.
- **Chips**: [[south-korea|Samsung/SK Hynix]] multiple re-rate hard. Helium from a reopening Ras Laffan flows by Q4; bromine from Israel secured as a side-effect of Lebanon de-escalation. Samsung Electronics: est. +22%; SK Hynix: est. +28% over 6 months. 3nm/2nm roadmap unblocked. Yongin cluster Phase 1 accelerates. Equipment suppliers (HPSP, Wonik IPS, PSK, EO Technics) outperform large-caps by ~15pp.
- **Refiners/petrochem**: S-Oil / SK Innovation / Lotte Chemical rally +18% on margin normalization, then give back half as crack spreads compress with Brent at $62. Net positive.
- **LNG importers (KOGAS)**: Immediate relief on spot cargo costs; long-term $10bn US LNG emergency contract signed in March is now "over-hedged" → political pushback from opposition.
- **Shipping & aviation**: HMM +30%, Korean Air +22%, Asiana +18% on lower bunker costs and insurance normalization.
- **Defense (Hanwha Aerospace, KAI, LIG Nex1, Hyundai Rotem)**: Give back the 2025-26 war premium (-15%). Structurally strong on European orders from [[european-defence-industry|post-NATO-crisis rearmament]] but cyclical top near-term.
- **Financials (KB, Shinhan, Hana)**: Won strength + normalizing rates = modest positive (+8%). Jeonse/household credit risk defuses; cheonsei landlords unwind gracefully.
- **Growth/CPI**: 2027 GDP revised +0.4pp (to ~2.8%); CPI back under 2.5% YoY by Q4.

### Global Equity Impact
- **S&P 500 → 7,300** by year-end (+10% from here). Tech (Nvidia, AMD, Broadcom, Marvell benefit from AI capex cycle un-disrupted), homebuilders (lower long yields), airlines, consumer discretionary lead. Energy sector craters ~20%. Defense names give back.
- **Nikkei 225 → 42,500** as BOJ hikes resume on confirmed disinflation path.
- **DAX → 22,800** on EU-Iran trade revival + cheaper LNG.
- **Shanghai → 4,400** as China harvests "peace-maker" diplomatic win; property stocks lift on stimulus room.

### Crypto Impact
- **BTC → $108k** on USD weakness + risk-on + renewed stablecoin flows into EM. This is **not a tail-driven rally** — it's liquidity-driven. Stablecoin cap grows toward $350bn.
- **ETH → $4,100**. Clear decoupled upside — Grand Bargain is the one world where ETH outperforms BTC because it's risk-on beta. ETH/BTC ratio recovers to 0.038 (from 0.032).
- **Altcoins**: Solana, Sui, Aptos +80-150%. Meme-coin cycle revival. DeFi TVL doubles.
- **Stablecoin regulation accelerates** in US Congress as post-deal environment allows bipartisan tech legislation.

---

## Scenario B — Interim Deal → Modus Vivendi (~50%, BASE CASE)

### Geopolitical Path
The Economist's "likeliest" outcome. Over 10-14 days: Iran commits to allowing 40-60 ships/day through Hormuz with capped tolls ($500k/vessel, down from $2m); America unfreezes $6bn Qatari-held assets, modest secondary-sanctions relief on refined products. The two-week ceasefire is extended by rolling two-week increments. **HEU is "frozen" under dual US+China observation** at Esfahan — not surrendered — which Gulf states call a "Gaza-ceasefire redux" (halts the fighting, never resolves the hard issues).

By Q3, talks enter a second phase addressing missile range and comprehensive sanctions architecture. By year-end, no breakthrough but no collapse. Iran regime consolidates around Qalibaf faction; IRGC splinters further (a stability positive).

**Canary indicators that flip this to C**:
- Hormuz traffic stalls at <20 ships/day by week 4 (tolls weaponized)
- Iran misses the first IAEA inspection window (Q2)
- Israel conducts another Lebanon strike during talks (Netanyahu spoiler path per [[israel]])

### South Korea Impact
- **KOSPI**: Grinds higher to 5,850-6,000 over 6 months. No re-rating event. Sector rotation is the game, not index beta.
- **Samsung/SK Hynix**: +8%/+12% as helium partially normalizes but at elevated cost (40% premium to pre-war). Yongin Phase 1 proceeds on schedule; Phase 2 pushed 6 months to Q4 2027.
- **Refiners**: Mixed. Margins stable but volumes lower. S-Oil flat; SK Innovation +5%.
- **KOGAS**: Stuck with expensive US LNG contract; earnings drag through 2027. Regulated utility → limited downside but no upside.
- **Shipping**: HMM +12%; insurance (war-risk premiums) stay elevated but traffic resumes enough to restore earnings.
- **Defense**: Stays elevated — rolling ceasefire extensions keep the war premium on.
- **Jeonse/household credit**: **Elevated but manageable**. BOK can't cut (imported inflation from oil at $84 + won at 1,450). Jeonse rollover stress builds through 2026H2 but no systemic break.
- **Growth/CPI**: 2027 GDP ~2.3%, CPI ~2.8% YoY (sticky above target).

### Global Equity Impact
- **S&P 500 → 6,750** (+2%). Boring positive. Tech re-leads as AI capex narrative resumes but no euphoria. Energy sector gradually de-rates as Brent drifts to $84. Defense keeps premium.
- **KOSPI stays Korean-specific alpha game** — avoid the index, pick tickers.
- **Shanghai → 4,200**. China benefits modestly as the implicit deal-guarantor at the May summit.

### Crypto Impact — **WORST RISK-ADJUSTED SCENARIO FOR CRYPTO**
- **BTC → $78k**. Small upside, but not compensating for vol. USD doesn't weaken enough; risk-on isn't risk-on enough for alt assets.
- **ETH → $2,550**. ~13% upside — token-supply inflation drags; no meaningful thematic catalyst.
- **Altcoins**: Choppy. Meme-coin revival aborted. DeFi TVL flat.
- **Opportunity cost**: KOSPI mid-caps, Korean chip equipment suppliers, and European defense names offer better Sharpe than crypto in this scenario.

---

## Scenario C — Talks Collapse → Limited Strikes (~28%)

### Geopolitical Path
Talks break down in week 2 over the Lebanon precondition + $6bn frozen-oil demand. Iran reimposes full Hormuz blockade within 72 hours; Israel strikes Iranian missile sites (not Fordow) with US tacit approval. Iran retaliates against Gulf infrastructure — Ras Laffan gets hit again (-40% capacity vs current -17%); Al Taweelah restart delayed another 18 months. **No open US-Iran war**, but proxy escalation: Houthis resume Red Sea attacks at 2x 2024 rate, Hizbullah fires on Haifa, Iraqi militias strike Ain al-Asad.

Iran accelerates enrichment to 90%+ openly (regime survival calculus: nuclear insurance is the only deterrent). IAEA expelled in late May. HEU stockpile grows to 600kg+ by Q3 — 4-5 bomb equivalents.

**Path back to B requires**: China intervenes forcefully (unlikely given Xi's "never interrupt your enemy" strategy per [[china]]).

### South Korea Impact
- **KOSPI → 4,400** (-24% from here). Won to 1,590. Near-recession in H2 2026 (two consecutive -GDP quarters).
- **Chips**: Samsung -22%; SK Hynix -28%. Helium rationing returns at pre-ceasefire severity. Bromine crisis re-opens (97% Israel import). 3nm yields falter; 2nm node pushed out.
- **Refiners**: Massive mark-to-market loss on inventory; margin squeeze as Korean export demand drops faster than import cost rises. S-Oil -35%; SK Innovation -30%.
- **KOGAS**: Now the $10bn US LNG contract is "barely enough" — saves Korea from blackouts. Stock +15% as a defensive utility.
- **Shipping**: HMM -45% (ships stuck); Korean Air -30% (jet fuel cost + demand).
- **Defense**: **Massive winners**. Hanwha Aerospace +55%, KAI +40%, LIG Nex1 +35%. [[european-defence-industry]] + Gulf emergency orders.
- **Jeonse/household credit**: **Severe.** BOK forced to hike to defend the won (25-50bp emergency); jeonse rollovers at 2x rate → forced sales → 10-15% apartment price drop in greater Seoul. KB/Shinhan/Hana -20-30%. This is where [[financial-markets-2026|private credit]] stress spreads to Korean bank balance sheets. **Hidden amplifier**: Korean household debt-to-GDP is 105% — highest in OECD. FX + rates shock transmits directly into consumption collapse.
- **Growth/CPI**: 2027 GDP -0.5% (recession); CPI 4.8% YoY (stagflation).

### Global Equity Impact
- **S&P 500 → 5,550** (-16%). 10Y spikes to 4.9% on oil shock, then drops to 4.2% as recession prices in. Energy +60%; everything else down 15-25%. Defense +40%. Nvidia holds better than expected (defensive AI bid). DJT continues [[financial-markets-2026|80% drawdown]] deeper; no political tailwind.
- **Nikkei 225 → 35,000** (-18%). Japanese autos — already "on brink of survival" per [[japanese-auto-industry]] — face existential pressure.
- **Shanghai → 4,500**. **China outperforms** — self-reliance narrative wins; oil import margin loss offset by windfall Iranian crude at $50 discount.

### Crypto Impact
- **BTC → $95k** (+34%). **Digital-gold thesis activates.** Iran needs payment rails; sanctioned-state plumbing drives exchange flows through BTC/stablecoins. Russia, NK front-run. Stablecoin cap to $420bn.
- **ETH → $2,200** (~flat). Beta trade; ETH is risk-on tech, not refuge. ETH/BTC ratio to 0.023 (new lows).
- **Altcoins**: Massacred. -40% average. Privacy coins (Monero, Zcash) +80% on use-case.
- **Policy response**: Bipartisan crackdown on crypto-as-sanctions-evasion; Treasury designates mixers; Korea (under Lee administration) tightens won-stablecoin rails.

---

## Scenario D — Nuclear Breakout → Preemptive Strike (~10%, TAIL)

### Geopolitical Path
Within 4-8 weeks: Iran either declares a weapon or is within 2 weeks of one. Israel strikes Fordow with US bunker-busters (or independently with US acquiescence). Iran retaliates against US bases in Iraq + Gulf + (possibly) Jerusalem. Oil infrastructure burns: Ras Laffan, Al Taweelah, Dhahran refineries, Saudi Ghawar field systems. Hormuz **mined**, not just blockaded — takes 60+ days to clear with US 5th Fleet assets.

Korea, Japan, Taiwan activate energy emergency protocols. US reinstates WPR vote; Congress authorizes expanded strike package. **Mojtaba Khamenei may or may not resurface** as figurehead for hardline faction. Regime change becomes a US policy goal by Q3.

**Path probability rises** if: Qalibaf loses internal faction battle to hardliners; IRGC splinter attempts HEU seizure; Israel-Lebanon escalation spirals independently.

### South Korea Impact
- **KOSPI → 3,600** (-38%). Won to 1,730 (breach 1,700 for first time ever). Full-blown recession; 2027 GDP -1.8%.
- **Chips**: Samsung -40%; SK Hynix -45%. 3nm/2nm roadmap frozen. US CHIPS Act co-investment uncertainty — does US prioritize DC fabs over Korea's domestic Yongin cluster under wartime? Unclear.
- **Refiners**: Emergency rationing. Government-directed supply. Share prices pinned by political intervention.
- **KOGAS**: Strategic national asset mode. Un-investable.
- **Shipping**: HMM -70%. Korean Air -55%. Operations suspended on key routes.
- **Defense**: **Epic re-rating.** Hanwha Aerospace +120%; KAI +90%; LIG Nex1 +75%. Korea becomes Europe's + Gulf's defense arsenal. Side effect: K2 Black Panther order book blows past 2,000 units.
- **Jeonse/household credit**: **Crisis.** 20-25% apartment price drop greater Seoul; 10-15% nationwide. Forced deleveraging. KB/Shinhan/Hana -40-50%. Government must intervene (jeonse refund guarantee fund, moratorium on foreclosures). Korean financial system stress approaches 1998 echo — not collapse but visible strain.
- **Growth/CPI**: 2027 GDP -1.8%; CPI peaks 6.5% YoY H2 2026 before demand destruction pulls it to 3.5% by Q4 2027.

### Global Equity Impact
- **S&P 500 → 4,800** (-28%). 10Y spikes to 5.1% on supply shock, then collapses to 3.6% on recession. Most sectors -25-40%. Defense +80%. Oil majors +70% (but refiner margin compression offsets). Gold miners +100%.
- **Nikkei 225 → 28,000**. Japanese automakers go from "brink" to **bankruptcy watchlist** — Nissan, Mazda, some Subaru/Mitsubishi lines face restructuring.
- **Shanghai**: Complicated. -15% on global risk-off, but China's energy diversification + Iranian discount crude buffers. Ends flat to -5%.
- **DAX -25%**. European defense names +80%.

### Crypto Impact
- **BTC → $120k** (+69%). **Peak flight-to-alternative-money.** Central bank EM reserves shift modestly. Retail + institutional flows. Stablecoin cap past $500bn.
- **ETH → $2,600** (+16%). Underperforms BTC massively; same beta-not-hedge story as C, but some upside from general rate-cutting expectations.
- **Altcoins**: Bifurcated. Privacy + BTC-proxy names (LTC, BCH) +50%; everything else -50%. Memecoins annihilated.
- **Regulatory**: Emergency measures; Korea + US likely coordinate on sanctions-evasion crackdown while preserving core crypto infrastructure.
- **Hidden risk**: **Stablecoin depeg event** probability rises sharply if oil + USD dynamics get non-linear. Historical 2023 USDC pattern suggests even fully-backed stables can lose peg in severe shocks.

---

## Korea-Specific Deep Dive: The Jeonse Amplifier

This is the **feature that makes Korea asymmetric** in the matrix. Korea has three structural vulnerabilities that compound in C and D:

1. **Energy intensity**: Korea imports 97% of energy. Brent at $138 (C) or $180 (D) directly hits CPI and current account. USD/KRW breakdown to 1,590-1,730 imports inflation on top.
2. **Chip supply-chain concentration**: 97% of industrial bromine from Israel; helium from Ras Laffan (Qatar). War-damaged or blockaded Gulf = direct fab yield loss. Also [[south-korea|$530bn Yongin chip cluster]] needs 13 new gas turbines — delayed in C, cancelled in D.
3. **Household debt leverage**: 105% debt-to-GDP (OECD highest). Jeonse (chonsei) is a unique Korean instrument — 2-year lump-sum deposit instead of rent. In an FX + rate shock, jeonse rollover cycles force landlord fire-sales, which feed into apartment price drops, which feed into bank collateral erosion.

**Jeonse stress is the transmission belt** from geopolitical shock to consumer demand collapse. Unlike the US (where household deleveraging is slow), Korea's feedback loop is **fast** — jeonse contracts mature every 2 years, so a 6-month shock can trigger 25-30% of the housing stock into stress.

**Implication for Korean investors**: Position sizing by scenario, not just direction. If you think C+D ≥ 35% probability combined, KOSPI long is fine but hedged with:
- Long KRW puts (1,600 strike, 6-month)
- Long Hanwha Aerospace / KAI (scenario-insurance if stress hits)
- Small allocation to BTC (hedges both A via risk-on and C/D via digital-gold)
- Short KB/Shinhan/Hana if leveraged (financial-amplifier exposure)

## What to Watch — 14-Day High-Frequency Signals

The next two weeks (April 12-26, through the first ceasefire-extension decision) will heavily update probabilities. Key signals in order of information value:

1. **Day 3-5 (April 14-17)**: Does Iran release the first US-Iranian dual nationals? Yes → bumps P(A+B) by ~8pp. No → P(C) to 32%.
2. **Day 5-7**: IAEA delegation visa granted for Fordow? Granted → P(A) rises meaningfully. Stonewalled → P(C) rises.
3. **Day 7**: First Hormuz traffic reading — does tanker transit recover above 30 ships/day? Yes → managed-tolls regime confirmed (B entrenched). No → C is forming.
4. **Day 10**: US Treasury confirms $6bn Qatar unfreeze? Yes → good faith bid. No → Iran walks.
5. **Day 12-14**: Israel strikes during talks? If yes → Netanyahu-as-spoiler path activates; P(C) to 35%+.
6. **Hormuz war-risk insurance rates**: Watch Lloyds numbers weekly. Below 2% of hull value = B consolidating. Above 4% = C pricing in.
7. **Korean won**: 1,420 = A pricing in; 1,480-1,500 = B; past 1,530 = C; past 1,600 = D.
8. **Brent $/bbl**: Below $85 = B confirming; above $110 = C loading; above $140 = D priced.
9. **BTC/ETH ratio**: Rising above 33-34 = tail-hedging demand; below 28 = risk-on ETH outperforming = A path.
10. **KOSPI breadth**: If defense stocks + KOGAS lead while large-cap chips lag → market pricing C. Reverse = A.

## Uncertainty Flags

- **Khamenei succession**: The simulation assumes Qalibaf-led pragmatist consolidation holds. If Mojtaba Khamenei resurfaces with IRGC backing, scenario weights shift toward C/D by ~5pp.
- **Trump's inconsistency**: [[donald-trump|Trump's]] own positions on Hormuz tolls have flipped four times. A mid-talk Truth Social outburst (precedent: "Open the Fuckin' Strait" on April 5) can collapse talks in hours.
- **Netanyahu's calculation**: If Israeli domestic politics push [[israel|Netanyahu]] toward striking during talks (scapegoat path per existing analysis), C activates.
- **Xi's passive strategy**: [[china|China]]'s "never interrupt your enemy" approach means Xi won't actively preserve B. If talks wobble, China watches.
- **Crypto structural regime**: Stablecoin regulation + Treasury sanctions posture could change mid-scenario in ways that invalidate BTC's positive skew across states. Monitor US Congress actions on GENIUS Act / FIT21 variants.

## Strategic Recommendations (Not Investment Advice)

### For Korean equity investors
- **Core**: KOSPI index tracker at 40% of planned allocation. Remaining 60% in scenario-hedged individual names.
- **Barbell**: Long Samsung + SK Hynix + equipment suppliers (A/B upside) + Long Hanwha Aerospace + KAI (C/D insurance).
- **Avoid unless scenario clears**: HMM, Korean Air (clean B+/A bet, but ±30% volatility); defense if C clears (would fade).

### For US equity investors
- S&P 500 is priced somewhere between A and B already. **Under-owned in the tails.** Consider:
  - Defense (LMT, NOC, RTX) as C/D insurance
  - Energy (XOM, CVX) as bifurcated — call options are cheapest insurance
  - Nvidia is resilient across A/B/C — the AI capex cycle survives 3 of 4 scenarios

### For crypto investors
- **Rebalance away from ETH-heavy toward BTC-heavy**. ETH only outperforms in A.
- Privacy coins for C tail is a known trade but liquidity-constrained.
- Stablecoin protocols with transparent reserves + US domicile win regulatory tailwinds in A; lose in D.

### Korean-specific portfolio
- **USD hedge** 30% of Korean equity exposure via KRW short / USD long. Cheap insurance.
- **Jeonse stress = KB/Shinhan short as tail-hedge** if exposed to residential real estate.
- **Small BTC allocation** (2-5%) as cross-state hedge.

## Confidence: Medium

- **High confidence**: Direction of BTC (positive across states); direction of defense stocks (positive in B/C/D); jeonse amplifier mechanism works as described.
- **Medium confidence**: Scenario probabilities (±5pp each); specific endpoint levels (±15% for equity targets).
- **Lower confidence**: ETH trajectory (depends on catalyst absence/presence); Shanghai index (China's positioning is discretionary); stablecoin depeg tail in D.

## See Also

- [[iran-war-and-ceasefire-2026]]
- [[iran-war-economic-impact]]
- [[donald-trump]]
- [[south-korea]]
- [[financial-markets-2026]]
- [[strait-of-hormuz]]
- [[pakistan]]
- [[china]]
- [[israel]]
- [[gulf-states]]
- [[market-snapshot]]
- [[simulations/sim-what-if-us-iran-ceasefire-negotiations-succeed-or-collapse-h-2026-04-11|Sister sim: 8-round multi-agent Korea investment outlook]]
- [[simulations/sim-what-if-the-strait-of-hormuz-blockade-continues-through-end-2026-04-11|Sister sim: Hormuz blockade path]]

---

# 2026년 4월 11일 이슬라마바드 미·이란 협상 — 분기 시나리오

## 이 시뮬레이션을 다시 하는 이유

이전 버전(2026-04-12 삭제)은 Serena 호텔 회담 0일 차에 작성됨. 이번 재작성은 다음 세 방향으로 확장:

1. **WebSearch 기반 시장 앵커** (실제 S&P 500, KOSPI, 브렌트, BTC, 금, USD/KRW, 2026-04-11~12 기준)
2. **고주파 경로** — 2주 휴전 카운트다운 동안의 14일 단위 신호
3. **암호화폐 세분화** — BTC뿐 아니라 ETH + 알트코인의 상관구조
4. **한국 개별 종목 수준 디테일** + 전세/가계부채 증폭제 메커니즘

일차 출처: The Economist, [raw/middle-east-and-africa/260411-third-time-the-charm.md](raw/middle-east-and-africa/260411-third-time-the-charm.md) — "미국과 이란, 이 전쟁을 끝내기 위한 고위험 협상 개시" (2026-04-11).

## 현재 스냅샷 (2026-04-12, WebSearch 앵커)

신호가 엇갈림. 주식은 *휴전 유지 + 딜 성사* 경로를 너무 일찍 반영했고, 현물 원유와 금은 *꼬리 리스크*를 반영 중이며, FX와 원화는 *한국-진앙* 리스크를 반영하고 있음.

| 자산         | 수준               | 해석                                 |              |
| ---------- | ---------------- | ---------------------------------- | ------------ |
| S&P 500    | **6,617**        | 휴전 후 2025년 11월 이후 최고의 주간; 선물 안정    |              |
| KOSPI      | **5,778**        | 4/10 휴전 불확실성에 -1.61% (4일 연속 상승 중단) |              |
| Nikkei 225 | YTD 플러스          | 양호 YTD 성과 3개 주요 지수 중 하나            |              |
| 상하이 종합     | 3,986            | 연간 +23.1%; 4/8 휴전에 +2.7%           |              |
| 브렌트유       | **$96.69**       | 선물 안정; 일부 현물 등급은 전쟁 고점 $150 터치     |              |
| 금          | **$4,762.62/oz** | 사상 최고치 구간 — 헤지 수요 아직 풀리지 않음        |              |
| USD/KRW    | **1,479**        | 원화 대폭 약세; 에너지 + 반도체 수요 둔화 이중 충격 반영 |              |
| 미국 10년물    | **~4.3%**        | [[financial-markets-2026           | 스태그플레이션 시소]] |
| BTC        | **~$71k**        | 2025년 말 고점 대비 상당폭 조정               |              |
| ETH        | **~$2,250**      | ETH/BTC 비율 다년 저점 — 베타 탈락           |              |
| 미국 CPI     | 3.3% YoY 3월      | 2월 2.4%에서 상승, 휘발유 주도               |              |

**핵심 스토리는 시장 간 괴리.** S&P와 KOSPI는 휴전 유지 + 딜 성사를 가격에 반영. 금 $4,762와 브렌트 현물 $150은 이에 반박. 이를 종합하면 시장이 꼬리 결과를 저평가 중 — 아래 시나리오 포지션 사이징에 중요.

전체 표는 [[market-snapshot]] 참조. 조정 노트: 일부 WebSearch 지수(KOSPI 5,778)는 위키 내부 서사(위키는 전후 2,550)가 시사하는 수준보다 높음. 이 시뮬레이션은 WebSearch 값을 앵커로 사용 — 현재 *실제* 리스크 가격을 반영하기 때문.

## 시나리오 매트릭스

| # | 시나리오 | 확률 | 이란 핵 | 호르무즈 통행(일간 척수) | 휴전 지속성 |
|---|---|---|---|---|---|
| A | **대합의** (JCPOA+) | ~12% | HEU 카자흐스탄/IAEA 이관; 3.67% 상한 | 자유 통항, 130+ | 영구 프레임워크 |
| B | **잠정 협정 → 모두스 비벤디** (기저) | ~50% | HEU 미·중 공동 봉인 동결; 농축 20% 상한 | 관리형 통행료, 일간 40-60척 | 롤링 2주 연장 |
| C | **협상 결렬 → 제한적 공습** | ~28% | 90% 이상 농축 돌진; IAEA 추방 | 재봉쇄, 통행료 무기화 | 2026년 3분기 파탄 |
| D | **핵 돌파 → 선제타격** (꼬리) | ~10% | 이란 선언 또는 이스라엘/미국의 포르도 타격 | 봉쇄 + 기뢰 위협 | 전면전 |

이전 매트릭스 대비 확률 변경 근거:
- **A 10→12% 상향**: 하메네이 부재는 통상 모델링보다 큰 구조적 해제. 바인스-칼리바프 직접 채널 (최고지도자 "결정 금지" 규칙 없이)이 실제로 상한을 올림.
- **B 55→50% 하향**: 금 $4,762, 원유 현물 $150은 주식 지수만큼 B에 확신하지 않음을 의미. 꼬리에 더 많은 질량이 필요.
- **C 25→28% 상향**: 이란은 바인스가 이륙 후 레바논 + 60억 달러 동결 자산 해제 요구 추가 — 전형적 결렬 전조 신호. 아랍 외교관들은 가자식 템플릿 (전투는 멈추되 난제는 영영 해결 안 됨) 에 대비 중 — 이 또한 취약한 균형.
- **D 10% 유지**: 400kg HEU + 부상당한 모즈타바/IRGC 분파는 실제 돌파 경로이지만, IRGC의 **분열**은 양방향 효과.

### 연말(2026) 거시 엔드포인트

2026-04-12 WebSearch 현 수준 기준. 화살표는 현재 대비 방향.

| 변수 | 현재 (4/12) | A (대합의) | B (잠정, 기저) | C (결렬) | D (돌파) |
|---|---|---|---|---|---|
| 브렌트 ($/배럴) | 96.69 | **$62** ↓ | **$84** ↓ | **$138** ↑ | **$180+** ↑ |
| USD/KRW | 1,479 | **1,330** ↓ | **1,450** ↓ | **1,590** ↑ | **1,730** ↑ |
| KOSPI | 5,778 | **6,600** ↑ | **5,850** ↑ | **4,400** ↓ | **3,600** ↓ |
| 미국 10년물 | 4.3% | **3.6%** ↓ | **4.1%** ↓ | **4.9%** 후 **4.2%** | **5.1%** 후 **3.6%** |
| S&P 500 | 6,617 | **7,300** ↑ | **6,750** ↑ | **5,550** ↓ | **4,800** ↓ |
| 금 ($/oz) | 4,762 | **3,900** ↓ | **4,400** ↓ | **5,300** ↑ | **6,000+** ↑ |
| BTC ($천) | 71 | **108** ↑ | **78** ↑ | **95** ↑ | **120** ↑ |
| ETH ($) | 2,250 | **4,100** ↑ | **2,550** ↑ | **2,200** 보합 | **2,600** ↑ |
| ETH/BTC | 0.032 | 0.038 ↑ | 0.033 ↑ | 0.023 ↓ | 0.022 ↓ |
| 호르무즈 일간 척수 | 10 | 130 | 55 | 5 | 0 |
| 이란 HEU | ~3개월 내 무기화 | 해체 | 동결 | 2-4주 | 무기화 |
| 한국 전세 스트레스 | 고조 | 해소 | 고조 | 심각 | 위기 |

### 비자명한 핵심 패턴

1. **BTC는 4개 상태 모두에서 양의 왜도(positive-skew).** 모든 시나리오에서 $71k 대비 상승. 대합의는 USD 약세 + 리스크온, 꼬리는 제재 회피 플러밍(이란의 자금 이동 필요) + 디지털 금 매수. **기저 B가 BTC 최악의 리스크 조정 결과** — 소폭 상승, 변동성 하락, KOSPI/S&P 대비 기회비용.
2. **ETH는 꼬리에서 BTC와 디커플링.** ETH는 **베타지 헤지가 아님**. C와 D는 ETH/BTC 비율을 더 짓누름 — ETH는 "위험자산 기술주"로 가격 책정되지 "대체 화폐"가 아니기 때문. 이 매트릭스에서 가장 깔끔한 페어 트레이드: 결렬/돌파 시 롱 BTC / 숏 ETH; 대합의 시 롱 ETH / 숏 BTC.
3. **금은 되돌림 안 됨.** 대합의에서도 금은 $3,900까지만 하락 — 전쟁 전 $2,400로 돌아가지 않음. USD 준비자산 지위 훼손([[nato-and-transatlantic-crisis|대서양 이혼]] + 트럼프 무역전 유산 + EM 중앙은행 매수)은 **구조적 이동**.
4. **한국은 비대칭.** A 상승 +14%; D 하락 -38%. 비대칭 이유:
   - 상승은 원화 강세에 의해 상쇄(로컬 통화 KOSPI 수익이 FX로 잠식)
   - 하락은 전세/가계 신용 경로로 복리(다음 섹션)
5. **S&P-KOSPI 상관관계 붕괴.** A, B에서는 둘 다 상승. C, D에서 S&P는 ~16%, ~28% 하락, KOSPI는 ~24%, ~38% 하락 — 한국이 에너지 집약도 + 공급망 지리적 근접성으로 이란 잔여 베타가 미국보다 더 큼.

---

## 시나리오 A — 대합의 (~12%)

### 지정학 경로
바인스와 칼리바프가 **하메네이 부재** 구조적 해제를 활용 — 최고지도자의 "결정 금지" 제약 없이 진행되는 37년 만의 첫 직접 회담. 8-10주 이내: IAEA 포르도 재진입, 400kg HEU 카자흐스탄(혹은 IAEA 봉인 하 중국)으로 이송, 농축 3.67% 상한, 미사일 사거리 자발적 2,000km 제한, 전쟁 전 모든 제재 단계적 해제. [[gulf-states|MBS]] 테헤란과 정상화; 이스라엘은 미국 핵우산 + 시리아/이라크 영구 주둔 3만 병력 상쇄. [[donald-trump|트럼프]] 딜 대외 홍보, 바인스 2028 자산화. [[china|시진핑]] 5월 정상회담 때 보증자로 공동 서명 — 여기가 포크 지점: 중국이 걸프의 **최상급 안보 설계자**가 되어 이미 지배적인 경제적 역할에 매칭.

**다음 14일 초기 트리거 — P(A)를 12%→25%로 이동시킬 수 있는 신호**:
- 미국이 60억 달러 카타르 해제 확인 + 1,500억 달러 단계별 확대 시사
- 이스라엘이 60일 레바논 동결 수용 (어려운 요청; 네타냐후는 연정 교체 필요)
- 이란이 에빈 교도소 미국-이란 이중 국적자 석방
- IAEA 사찰단 21일 내 포르도 비자 접수

### 한국 영향
- **즉각 (2주 이내)**: 발표에 KOSPI +4-5% 갭상승; 원화 1,420 거쳐 3개월에 걸쳐 경상수지 스트레스 반전되며 1,330으로.
- **반도체**: [[south-korea|삼성/SK하이닉스]] 멀티플 강하게 재평가. 라스 라판 재개로 Q4까지 헬륨 공급; 이스라엘 레바논 디에스컬레이션 부수효과로 브로민 확보. 삼성전자: 약 +22%; SK하이닉스: 약 +28% (6개월). 3nm/2nm 로드맵 해제. 용인 클러스터 1기 가속화. 장비 업체(HPSP, 원익IPS, PSK, 이오테크닉스)가 대형주 대비 ~15%p 아웃퍼폼.
- **정유/석유화학**: S-Oil / SK이노베이션 / 롯데케미칼 마진 정상화로 +18% 상승 후, 브렌트 $62로 크랙 스프레드 압축되며 절반 반납. 순증.
- **LNG 수입자(KOGAS)**: 현물 카고 비용 즉각 해소; 3월 긴급 체결된 100억 달러 미국 LNG 장기 계약은 "과잉 헤지" → 야당 정치적 역풍.
- **해운·항공**: 벙커 비용 + 보험 정상화로 HMM +30%, 대한항공 +22%, 아시아나 +18%.
- **방산(한화에어로, KAI, LIG넥스원, 현대로템)**: 2025-26 전쟁 프리미엄 반납 (-15%). 유럽 주문 + [[european-defence-industry|NATO 위기 후 재무장]]으로 구조적 견조하나 단기 사이클 고점.
- **금융(KB, 신한, 하나)**: 원화 강세 + 금리 정상화 = 소폭 플러스(+8%). 전세/가계 신용 리스크 해소; 전세 임대인 순조롭게 디레버리징.
- **성장률/CPI**: 2027 GDP +0.4%p 상향(~2.8%); CPI Q4까지 2.5% YoY 이하 복귀.

### 글로벌 주식 영향
- **S&P 500 → 7,300** 연말(여기서 +10%). 기술주(엔비디아, AMD, 브로드컴, 마벨 AI 자본지출 사이클 무중단 수혜), 주택(장기금리 하락), 항공, 경기소비재 선도. 에너지 섹터 ~20% 급락. 방산 프리미엄 반납.
- **Nikkei 225 → 42,500** 디스인플레이션 경로 확인에 BOJ 금리인상 재개.
- **DAX → 22,800** EU-이란 교역 부활 + 저렴한 LNG.
- **상하이 → 4,400** 중국이 "평화 설계자" 외교 승리 수확; 부동산 주식 부양 여력에 반등.

### 암호화폐 영향
- **BTC → $108k** USD 약세 + 리스크온 + EM 스테이블코인 흐름 재개. **꼬리 주도 반등이 아님** — 유동성 주도. 스테이블코인 시총 3,500억 달러 돌파.
- **ETH → $4,100**. 명확한 디커플 상승 — 대합의는 ETH가 BTC를 아웃퍼폼하는 유일한 세계, 리스크온 베타이기 때문. ETH/BTC 비율 0.038 회복 (0.032에서).
- **알트코인**: 솔라나, 수이, 앱토스 +80-150%. 밈코인 사이클 부활. DeFi TVL 두 배.
- **스테이블코인 규제** 포스트 딜 환경이 초당적 기술 입법을 허용하며 미 의회 가속화.

---

## 시나리오 B — 잠정 협정 → 모두스 비벤디 (~50%, 기저 케이스)

### 지정학 경로
이코노미스트의 "가장 유력한" 결과. 10-14일에 걸쳐: 이란은 호르무즈를 통한 일간 40-60척 통항 허용, 통행료 상한 (선박당 $2m에서 $500k); 미국은 60억 달러 카타르 보유 자산 해제, 정제품 2차 제재 소폭 완화. 2주 휴전은 롤링 2주 단위로 연장. **HEU는 Esfahan에서 미·중 공동 관찰 하 "동결"** — 양도 아님 — 이를 걸프 국가들은 "가자 휴전 재탕"(전투는 멈추되 난제는 미해결)이라 부름.

Q3까지 회담은 미사일 사거리 + 포괄 제재 아키텍처 다루는 2단계 진입. 연말까지 돌파구는 없지만 결렬도 없음. 이란 정권 칼리바프 분파 중심 공고화; IRGC 추가 분열(안정성 측면 플러스).

**C로 전환 트리거**:
- 4주 차 호르무즈 통항 <20척/일 (통행료 무기화)
- 이란이 첫 IAEA 사찰 창(Q2) 미준수
- 이스라엘이 회담 중 또 레바논 공습 ([[israel|네타냐후 스포일러 경로]])

### 한국 영향
- **KOSPI**: 6개월 5,850-6,000으로 완만 상승. 재평가 이벤트 없음. 섹터 로테이션이 게임, 지수 베타 아님.
- **삼성/SK하이닉스**: 헬륨 부분 정상화(전쟁 전 대비 40% 프리미엄)로 +8%/+12%. 용인 1기 일정대로; 2기는 6개월 지연(Q4 2027).
- **정유**: 혼합. 마진 안정, 물량 감소. S-Oil 보합; SK이노베이션 +5%.
- **KOGAS**: 비싼 미국 LNG 계약 고착; 2027까지 수익 드래그. 규제 유틸리티 → 하방 제한, 상방도 없음.
- **해운**: HMM +12%; 전쟁 리스크 보험료 높지만 교통량 회복 충분해 수익 복구.
- **방산**: 롤링 휴전 연장이 전쟁 프리미엄 유지 → 방산 프리미엄 유지.
- **전세/가계신용**: **고조되나 관리 가능.** BOK 금리 인하 불가(원유 $84 + 원화 1,450에서 수입 인플레). 전세 롤오버 스트레스 2026H2 내내 축적되나 시스템적 파열 없음.
- **성장률/CPI**: 2027 GDP ~2.3%, CPI ~2.8% YoY (목표 위 점착).

### 글로벌 주식 영향
- **S&P 500 → 6,750** (+2%). 지루한 플러스. AI 자본지출 내러티브 재개되며 기술주 재선도, 그러나 희열은 없음. 에너지 섹터 점진 디레이트 (브렌트 $84 향). 방산 프리미엄 유지.
- **KOSPI는 한국 특화 알파 게임** — 지수 회피, 개별 종목 선택.
- **상하이 → 4,200**. 5월 정상회담 딜 암묵 보증자로 중국이 소폭 수혜.

### 암호화폐 영향 — **암호화폐 최악의 리스크 조정 시나리오**
- **BTC → $78k**. 소폭 상승, 변동성 대비 보상 부족. USD 약세 불충분; 리스크온도 대체자산 상승 유도할 만큼 리스크온 아님.
- **ETH → $2,550**. ~13% 상승 — 토큰 공급 인플레이션 발목; 의미 있는 테마 촉매 없음.
- **알트코인**: 변동. 밈코인 부활 중단. DeFi TVL 보합.
- **기회비용**: KOSPI 중소형, 한국 반도체 장비 업체, 유럽 방산 이름이 이 시나리오에서 암호화폐보다 나은 샤프비율 제공.

---

## 시나리오 C — 협상 결렬 → 제한적 공습 (~28%)

### 지정학 경로
레바논 전제조건 + 60억 달러 동결 자산 요구로 2주 차 회담 결렬. 이란은 72시간 내 호르무즈 완전 재봉쇄; 이스라엘은 미국 암묵 승인으로 이란 미사일 기지 (포르도 아님) 타격. 이란 걸프 인프라 보복 — 라스 라판 재피격 (-40% 용량, 현재 -17% 대비); 알 타웨엘라 재가동 18개월 추가 지연. **전면 미·이란 전쟁은 아님**, 그러나 대리전 확대: 후티 홍해 공격 2024년 2배 속도로 재개, 히즈볼라 하이파 발사, 이라크 민병대 아인 알 아사드 타격.

이란 농축 90%+로 공개 가속화 (정권 생존 계산: 핵 보험만이 유일 억지력). 5월 말 IAEA 추방. Q3까지 HEU 재고 600kg+ 증가 — 핵폭탄 4-5발 상당.

**B 복귀 경로**: 중국 강력 개입 필요 (시진핑의 [[china|"적 방해 말라"]] 전략 감안 시 가능성 낮음).

### 한국 영향
- **KOSPI → 4,400** (여기서 -24%). 원화 1,590. 2026H2 준경기침체 (두 분기 연속 -GDP).
- **반도체**: 삼성 -22%; SK하이닉스 -28%. 헬륨 배급 휴전 전 강도로 복귀. 브로민 위기 재발 (97% 이스라엘 수입). 3nm 수율 흔들림; 2nm 노드 연기.
- **정유**: 재고 대규모 시가 평가 손실; 한국 수출 수요가 수입 비용 상승보다 빨리 하락하며 마진 압박. S-Oil -35%; SK이노베이션 -30%.
- **KOGAS**: 이제 100억 달러 미국 LNG 계약이 "겨우 충분" — 한국을 정전에서 구함. 방어 유틸리티로 +15%.
- **해운**: HMM -45% (선박 고립); 대한항공 -30% (제트연료 + 수요).
- **방산**: **대규모 승자**. 한화에어로 +55%, KAI +40%, LIG넥스원 +35%. [[european-defence-industry]] + 걸프 긴급 주문.
- **전세/가계신용**: **심각.** BOK 원화 방어 위해 강제 인상 (25-50bp 긴급); 전세 롤오버 2배 속도 → 강제 매각 → 수도권 아파트 가격 10-15% 하락. KB/신한/하나 -20-30%. 여기서 [[financial-markets-2026|프라이빗 크레딧]] 스트레스가 한국 은행 대차대조표로 확산. **숨은 증폭제**: 한국 가계부채 105% GDP — OECD 최고. FX + 금리 쇼크가 소비 붕괴로 직접 전달.
- **성장률/CPI**: 2027 GDP -0.5% (침체); CPI 4.8% YoY (스태그플레이션).

### 글로벌 주식 영향
- **S&P 500 → 5,550** (-16%). 10년물 원유 쇼크에 4.9%로 급등 후 침체 반영하며 4.2%로 하락. 에너지 +60%; 나머지 모두 15-25% 하락. 방산 +40%. 엔비디아 예상보다 선방(방어적 AI 매수세). DJT는 [[financial-markets-2026|80% 드로다운]] 더 깊어짐; 정치 순풍 부재.
- **Nikkei 225 → 35,000** (-18%). 일본 자동차 — 이미 [[japanese-auto-industry|"생존의 벼랑 끝"]] — 실존 압박 직면.
- **상하이 → 4,500**. **중국 아웃퍼폼** — 자립 내러티브 승; 원유 수입 마진 손실을 $50 할인 이란 원유 횡재로 상쇄.

### 암호화폐 영향
- **BTC → $95k** (+34%). **디지털 금 테제 작동.** 이란 결제 레일 필요; 제재 회피 플러밍이 BTC/스테이블코인 교환 흐름 구동. 러시아, 북한 선행. 스테이블코인 시총 4,200억 달러.
- **ETH → $2,200** (~보합). 베타 트레이드; ETH는 리스크온 기술주, 피난처 아님. ETH/BTC 비율 0.023 (신저점).
- **알트코인**: 대학살. 평균 -40%. 프라이버시 코인 (모네로, Z캐시) 용례로 +80%.
- **정책 대응**: 초당적 암호화폐-제재회피 단속; 재무부 믹서 지정; 한국(이재명 정부) 원화-스테이블코인 레일 조임.

---

## 시나리오 D — 핵 돌파 → 선제 타격 (~10%, 꼬리)

### 지정학 경로
4-8주 이내: 이란 무기 선언 또는 2주 내 무기화 가능. 이스라엘이 미국 벙커버스터로 포르도 타격(혹은 미국 묵인 하 독자 타격). 이란 이라크 + 걸프 + (가능) 예루살렘 미군 기지 보복. 석유 인프라 화염: 라스 라판, 알 타웨엘라, 다란 정유소, 사우디 가와르 필드 시스템. 호르무즈 **기뢰 부설** — 단순 봉쇄 아님 — 미국 5함대 자산으로 60일+ 소요 해제.

한국, 일본, 대만 에너지 비상 프로토콜 가동. 미국 WPR 표결 재개; 의회 확대 타격 패키지 승인. **모즈타바 하메네이** 강경파 분파 명목상 복귀 가능성. Q3까지 정권 교체가 미국 정책 목표로.

**상승 경로**: 칼리바프 내부 분파전 패배; IRGC 분파 HEU 탈취 시도; 이스라엘-레바논 독립 확대.

### 한국 영향
- **KOSPI → 3,600** (-38%). 원화 1,730 (사상 첫 1,700 돌파). 본격 경기침체; 2027 GDP -1.8%.
- **반도체**: 삼성 -40%; SK하이닉스 -45%. 3nm/2nm 로드맵 동결. 미 CHIPS 법 공동투자 불확실 — 전시 미국이 DC 팹을 한국 용인 클러스터보다 우선시할까? 불투명.
- **정유**: 비상 배급. 정부 지시 공급. 주가는 정치적 개입으로 고정.
- **KOGAS**: 전략적 국가 자산 모드. 투자 불가.
- **해운**: HMM -70%. 대한항공 -55%. 주요 노선 영업 중단.
- **방산**: **서사시적 재평가.** 한화에어로 +120%; KAI +90%; LIG넥스원 +75%. 한국이 유럽 + 걸프의 방산 무기고가 됨. 부수효과: K2 흑표 주문량 2,000대 돌파.
- **전세/가계신용**: **위기.** 수도권 아파트 20-25% 하락; 전국 10-15%. 강제 디레버리징. KB/신한/하나 -40-50%. 정부 개입 필수(전세 환급 보증 기금, 경매 모라토리엄). 한국 금융 시스템 스트레스가 1998 메아리에 근접 — 붕괴 아니지만 가시적 부담.
- **성장률/CPI**: 2027 GDP -1.8%; CPI 2026H2 6.5% YoY 정점 후 수요 파괴에 2027 Q4까지 3.5%로.

### 글로벌 주식 영향
- **S&P 500 → 4,800** (-28%). 10년물 공급 쇼크에 5.1% 급등 후 침체에 3.6%로 붕괴. 대부분 섹터 -25-40%. 방산 +80%. 정유 메이저 +70% (정제 마진 압축 상쇄). 금광 +100%.
- **Nikkei 225 → 28,000**. 일본 자동차가 "벼랑" 에서 **파산 감시 목록**으로 — 닛산, 마쓰다, 일부 스바루/미쓰비시 라인 구조조정 직면.
- **상하이**: 복잡. 글로벌 리스크오프에 -15%, 그러나 중국 에너지 다각화 + 이란 할인 원유 완충. 보합~-5%.
- **DAX -25%**. 유럽 방산주 +80%.

### 암호화폐 영향
- **BTC → $120k** (+69%). **대체 화폐로의 도피 정점.** EM 중앙은행 준비금 소폭 이동. 리테일 + 기관 흐름. 스테이블코인 시총 5,000억 달러 돌파.
- **ETH → $2,600** (+16%). BTC 대비 대폭 언더퍼폼; C와 동일한 베타-아닌-헤지 스토리, 그러나 일반 금리 인하 기대에 일부 상승.
- **알트코인**: 이분화. 프라이버시 + BTC 대리(LTC, BCH) +50%; 나머지 -50%. 밈코인 전멸.
- **규제**: 긴급 조치; 한국 + 미국이 제재회피 단속을 조율하되 핵심 암호화폐 인프라는 보존.
- **숨은 리스크**: 원유 + USD 역학이 비선형으로 가면 **스테이블코인 디페깅 이벤트** 가능성 급상승. 2023 USDC 역사적 패턴 — 완전히 담보된 스테이블도 심각 쇼크에 페그 이탈 가능.

---

## 한국 특화 심층: 전세 증폭제

이것이 매트릭스에서 **한국을 비대칭으로 만드는 특성**. 한국은 C와 D에서 복리화되는 세 가지 구조적 취약점 보유:

1. **에너지 집약도**: 한국은 에너지 97% 수입. 브렌트 $138 (C) 혹은 $180 (D)는 CPI + 경상수지 직격. USD/KRW 1,590-1,730 돌파가 인플레이션을 추가 수입.
2. **반도체 공급망 집중**: 산업용 브로민 97%가 이스라엘; 헬륨은 라스 라판(카타르). 전쟁으로 손상되거나 봉쇄된 걸프 = 팹 수율 직접 손실. 또한 [[south-korea|530억 달러 용인 반도체 클러스터]]는 13개 신규 가스 터빈 필요 — C에서 지연, D에서 취소.
3. **가계부채 레버리지**: 105% GDP (OECD 최고). 전세는 한국 특유 수단 — 월세 대신 2년 일시불 보증금. FX + 금리 쇼크에서 전세 롤오버 사이클이 임대인 급매를 강제, 아파트 가격 하락으로 이어지고, 은행 담보 침식으로 연결.

**전세 스트레스는 지정학적 쇼크에서 소비 수요 붕괴로 가는 전달 벨트.** 미국(가계 디레버리징이 느림)과 달리 한국의 피드백 루프는 **빠름** — 전세 계약이 2년마다 만기, 따라서 6개월 쇼크가 주택 재고의 25-30%를 스트레스 상태로 촉발 가능.

**한국 투자자 시사점**: 방향이 아닌 시나리오별 포지션 사이징. C+D 확률 합이 ≥ 35%라고 본다면, KOSPI 롱은 괜찮지만 다음으로 헤지:
- KRW 풋 롱 (1,600 행사가, 6개월)
- 한화에어로 / KAI 롱 (스트레스 발생 시 시나리오 보험)
- BTC 소액 배분 (A의 리스크온과 C/D의 디지털 금 모두 헤지)
- 레버리지 노출된 경우 KB/신한/하나 숏 (금융 증폭제 노출)

## 지켜봐야 할 것 — 14일 고주파 신호

다음 2주 (4/12-4/26, 첫 휴전 연장 결정까지)는 확률을 크게 업데이트할 것. 정보 가치 순 핵심 신호:

1. **3-5일차 (4/14-17)**: 이란이 첫 미국-이란 이중 국적자 석방? 예 → P(A+B) ~8%p 상승. 아니오 → P(C) 32%로.
2. **5-7일차**: IAEA 사찰단 포르도 비자 발급? 발급 → P(A) 의미 있게 상승. 차단 → P(C) 상승.
3. **7일차**: 첫 호르무즈 교통량 확인 — 일간 30척 이상 회복? 예 → 관리 통행료 체제 확정(B 정착). 아니오 → C 형성 중.
4. **10일차**: 미 재무부 60억 달러 카타르 해제 확인? 예 → 신뢰 입찰. 아니오 → 이란 이탈.
5. **12-14일차**: 회담 중 이스라엘 공습? 예 → 네타냐후 스포일러 경로 활성화; P(C) 35%+.
6. **호르무즈 전쟁 리스크 보험료**: Lloyds 수치 주간 관찰. 선체가액 2% 이하 = B 정착. 4% 이상 = C 가격화.
7. **원화**: 1,420 = A 가격화 중; 1,480-1,500 = B; 1,530 돌파 = C; 1,600 돌파 = D.
8. **브렌트 $/배럴**: $85 이하 = B 확인; $110 이상 = C 적재; $140 이상 = D 가격화.
9. **BTC/ETH 비율**: 33-34 이상 상승 = 꼬리 헤지 수요; 28 이하 = 리스크온 ETH 아웃퍼폼 = A 경로.
10. **KOSPI 등락 종목 수**: 방산 + KOGAS 선도, 대형 반도체 후행 → 시장 C 가격화. 반대 = A.

## 불확실성 플래그

- **하메네이 후계**: 시뮬레이션은 칼리바프 주도 실용파 공고화 유지 가정. 모즈타바 하메네이가 IRGC 지지 받아 재부상하면 시나리오 가중치 C/D로 ~5%p 이동.
- **트럼프의 일관성 부재**: [[donald-trump|트럼프]]의 호르무즈 통행료 입장은 4번 뒤집힘. 회담 중 Truth Social 폭발(4/5 "Open the Fuckin' Strait" 선례)이 몇 시간 내에 회담 붕괴 가능.
- **네타냐후 계산**: 이스라엘 국내 정치가 [[israel|네타냐후]]를 회담 중 공습으로 밀면 (기존 분석상 희생양 경로), C 활성화.
- **시진핑 수동 전략**: [[china|중국]]의 "적 방해 말라" 접근은 시진핑이 B를 능동적으로 보존하지 않음을 의미. 회담 흔들리면 중국은 지켜봄.
- **암호화폐 구조적 체제**: 스테이블코인 규제 + 재무부 제재 자세가 시나리오 중간에 바뀌어 BTC의 양의 왜도 전체 상태 무효화 가능. 미 의회 GENIUS 법 / FIT21 변형 조치 모니터링.

## 전략 권고 (투자 조언 아님)

### 한국 주식 투자자
- **코어**: 계획 배분의 40%를 KOSPI 지수 추종. 나머지 60%는 시나리오 헤지된 개별 종목.
- **바벨**: 롱 삼성 + SK하이닉스 + 장비 업체(A/B 상승) + 롱 한화에어로 + KAI (C/D 보험).
- **시나리오 정리 전까진 회피**: HMM, 대한항공(깔끔한 B+/A 베팅, 그러나 ±30% 변동성); C 정리 시 방산(페이드).

### 미국 주식 투자자
- S&P 500은 이미 A-B 중간 어딘가 가격화. **꼬리에서 언더-오너드.** 고려:
  - 방산(LMT, NOC, RTX)을 C/D 보험으로
  - 에너지(XOM, CVX)를 이분화 — 콜옵션이 가장 싼 보험
  - 엔비디아는 A/B/C에서 회복탄력 — AI 자본지출 사이클은 4개 시나리오 중 3개에서 생존

### 암호화폐 투자자
- **ETH 비중에서 BTC 비중으로 리밸런싱.** ETH는 A에서만 아웃퍼폼.
- C 꼬리용 프라이버시 코인은 알려진 트레이드지만 유동성 제약.
- 투명 준비금 + 미국 도메인 스테이블코인 프로토콜이 A에서 규제 순풍; D에서 역풍.

### 한국 특화 포트폴리오
- **USD 헤지** 한국 주식 노출의 30%를 KRW 숏 / USD 롱으로. 저렴한 보험.
- **전세 스트레스 = 주거용 부동산 노출 시 KB/신한 숏** 꼬리 헤지로.
- **소액 BTC 배분** (2-5%) 상태 간 교차 헤지로.

## 신뢰도: 중간

- **높은 신뢰도**: BTC 방향(상태 전반 상승); 방산주 방향(B/C/D 상승); 전세 증폭제 메커니즘 설명대로 작동.
- **중간 신뢰도**: 시나리오 확률(각 ±5%p); 특정 엔드포인트 레벨(주식 목표 ±15%).
- **낮은 신뢰도**: ETH 궤적(촉매 부재/존재에 의존); 상하이 지수(중국 포지셔닝 재량); D에서 스테이블코인 디페깅 꼬리.

## 관련 문서

- [[iran-war-and-ceasefire-2026]]
- [[iran-war-economic-impact]]
- [[donald-trump]]
- [[south-korea]]
- [[financial-markets-2026]]
- [[strait-of-hormuz]]
- [[pakistan]]
- [[china]]
- [[israel]]
- [[gulf-states]]
- [[market-snapshot]]
- [[simulations/sim-what-if-us-iran-ceasefire-negotiations-succeed-or-collapse-h-2026-04-11|자매 시뮬: 8라운드 멀티에이전트 한국 투자 전망]]
- [[simulations/sim-what-if-the-strait-of-hormuz-blockade-continues-through-end-2026-04-11|자매 시뮬: 호르무즈 봉쇄 경로]]
