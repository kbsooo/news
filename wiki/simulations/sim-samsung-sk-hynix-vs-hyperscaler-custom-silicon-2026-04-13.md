---
title: "Simulation: Samsung & SK Hynix outlook in the hyperscaler custom-silicon era (HBM4 + CXMT + Rubin cycle)"
type: simulation
date: 2026-04-13
scenario: "Semiconductor cycle is white-hot, but Google TPUv7, Anthropic's Broadcom/Google deal (3.5GW), Amazon Trainium 3, Microsoft Maia 200, Meta MTIA, and OpenAI's planned 2027 custom chip are eroding NVIDIA's GPU monopoly. How do Samsung Electronics and SK Hynix fare over May-Dec 2026 under branching combinations of (i) HBM demand trajectory and (ii) Samsung HBM4 execution + foundry positioning?"
variables: [hbm_tam_2026, sk_hynix_hbm_share, samsung_hbm_share, samsung_foundry_rev, samsung_005930_krw, sk_hynix_000660_krw, kospi, usd_krw, cxmt_hbm3_ramp, nvidia_inference_share]
confidence: medium
based_on:
  - south-korea
  - market-snapshot
  - china
  - donald-trump
  - financial-markets-2026
  - ai-labs-and-industry
tags: [simulation, korea, semiconductor, hbm, samsung, sk-hynix, custom-silicon, ai-infrastructure, scenarios]
---

# Samsung & SK Hynix vs. Hyperscaler Custom-Silicon Wave

## Why This Simulation

The AI compute stack is splitting in two:
- **Logic (compute)**: NVIDIA GPU monopoly eroding as Google TPUv7 Ironwood, Amazon Trainium 3, Microsoft Maia 200, Meta MTIA, and (from 2027) OpenAI's Broadcom ASIC and Anthropic's 3.5GW Broadcom/Google deal bring hyperscalers in-house. Custom ASIC CAGR is ~45%; NVIDIA inference share is projected to fall from ~90% today to 20-30% by 2028.
- **Memory (HBM)**: Every custom ASIC — TPU, Trainium, Maia, MTIA — **still needs HBM**. The oligopoly of SK Hynix (~53-62%), Samsung (~17-35%), and Micron (~11-21%) is the real chokepoint, reinforced by TSMC CoWoS packaging and US export controls that designate HBM a "choke point" (January 2026 framework).

So the central question isn't "does custom silicon kill Korean memory?" — it's "does the TAM expansion from hyperscaler ASIC proliferation plus Samsung's HBM4 catch-up into NVIDIA Rubin offset CXMT pressure, and how is the upside split between the two Korean players?"

**Asymmetry that matters**: SK Hynix is a pure-play memory house. Samsung has **two dogs in this fight** — HBM memory AND foundry. If hyperscalers shift more of the logic stack to custom ASICs and TSMC 3nm stays at 100% utilization with 3x demand overhang, Samsung Foundry becomes the only meaningful alternative. That's a hedge SK Hynix doesn't have.

## Current Snapshot (2026-04-13, WebSearch anchor)

| Asset / Metric | Level | Note |
|---|---|---|
| Samsung Electronics (005930) | **₩201,000** | Apr 13; prev close ₩206,000 (−2.4%); record-high zone on HBM4 Rubin deal |
| SK Hynix (000660) | **₩1,027,000** | Apr 12; prev ₩998,000; surged 15% to ₩1,050,000 earlier on Samsung's Q1 preview |
| KOSPI | 5,778 | −1.61% Apr 10 on ceasefire uncertainty |
| USD/KRW | 1,479 | weak on energy shock + chip-order timing |
| Brent crude | $96.69 | physical grades touched $150 at war peak |
| HBM 2026 TAM (BofA) | **$54.6B** | +58% YoY |
| DRAM rev growth 2026E | +51% | ASP +33% — worst undersupply in 15+ years (Goldman) |
| SK Hynix HBM share (Q3 2025) | 53% | Q2 was 62% (Samsung catching up on HBM3E) |
| Samsung HBM share (Q3 2025) | 35% | up from 17% in Q2 — re-qualifying on HBM3E 12-hi |
| Micron HBM share | 11-21% | variable; HBM4 challenger on Micron's 1γ node |
| Samsung HBM4 ASP target | ~$700/unit | +30% vs prior gen; 50-60% op margin at that level |
| Morgan Stanley Samsung memory 2026E profit | +310% | approaching ₩100tn mark |
| Anthropic TPU commitment | **1M TPUv7 + 3.5GW** | Broadcom/Google, ramping 2026-2027 |
| NVIDIA Rubin HBM4 suppliers | Samsung + SK Hynix exclusive | UBS: SK Hynix targeting 70% share |
| CXMT HBM3 mass production | end-2026 | 2-3 year gap to SK Hynix; US "choke point" export ban binds |

**Market divergence**: Samsung (005930) sold off on Apr 13 even as SK Hynix ramped — suggesting the market is pricing **SK Hynix as the cleaner HBM4-Rubin play** and Samsung as still having execution risk + foundry/consumer drag. This is the market's current *prior* that the scenarios below stress-test.

See [[market-snapshot]] for the broader context.

## Scenario Matrix

Two axes. HBM demand trajectory (y) × Samsung execution (x).

|  | **Samsung HBM4 + foundry STRONG** | **Samsung HBM4 + foundry WEAK** |
|---|---|---|
| **HBM TAM supercycle (custom silicon additive)** | **A. Korea Inc. twin peaks** (~25%) | **B. SK Hynix winner-take-most** (~40% base) |
| **HBM TAM moderates (efficiency + CXMT nibble)** | **C. Samsung balanced recovery** (~20%) | **D. Cycle top 2026, painful 2027** (~15%) |

### Scenario A — Korea Inc. Twin Peaks (~25%)

**Trigger chain**: Rubin HBM4 qualification completes for both suppliers in Q2; SK Hynix keeps ~60% share, Samsung lands ~35%. Anthropic's 3.5GW Broadcom/Google commitment plus Amazon's Trainium 3 build-out means every additional ASIC shipped **adds 4-8 HBM stacks** on top of GPU demand, not substituting. TSMC CoWoS remains bottlenecked, Samsung's advanced packaging (SAINT-S) wins overflow orders. Critically, Samsung Foundry wins back TPU-class or Trainium-class custom ASIC volume from TSMC as hyperscalers seek dual-sourcing against the 3x demand overhang at TSMC 3nm.

**End-2026 variables**:
- HBM TAM: **$58-62B** (above BofA baseline)
- SK Hynix HBM share: 58-62%
- Samsung HBM share: 32-38%
- Samsung Foundry rev: +45-60% YoY (TPU-class overflow)
- Samsung (005930): **₩260-290k** (+29-44%)
- SK Hynix (000660): **₩1.35-1.50M** (+31-46%)
- KOSPI: 6,400-6,800
- USD/KRW: 1,360-1,400 (BoK tightening + export surge)

**Characterization**: Both Korean giants hit all-time highs. Samsung re-rates as its foundry finally earns a premium multiple; SK Hynix continues as the cleanest pure-play. KOSPI leadership is narrow but intense (Samsung + SK Hynix alone ~35% of index weight).

### Scenario B — SK Hynix Winner-Take-Most (~40%, base case)

**Trigger chain**: This is what the Apr 13 price action is already pricing. SK Hynix holds 65-70% of HBM4 volume (UBS forecast); Samsung HBM4 passes qualification but with yield/cost handicap, keeping share at 25-30%. Samsung Foundry wins some custom ASIC volume but not at the scale needed to offset lower memory share. CXMT contained by export controls (HBM3 only, 3-year gap).

**End-2026 variables**:
- HBM TAM: **$54-58B** (BofA baseline holds)
- SK Hynix HBM share: 65-70%
- Samsung HBM share: 25-30%
- Samsung Foundry rev: +15-25% YoY (modest wins)
- Samsung (005930): **₩220-250k** (+9-24%)
- SK Hynix (000660): **₩1.30-1.50M** (+27-46%)
- KOSPI: 6,100-6,500
- USD/KRW: 1,420-1,460

**Characterization**: SK Hynix is the 2026 market darling — stock doubles off its 2025 lows, valuation stretched but defensible on earnings. Samsung delivers the promised Morgan Stanley +310% memory profit but gets *de-rated* relative to SK Hynix because the foundry/consumer segments drag. Wealth effect concentrated: SK Hynix shareholders win big, Samsung retail investors (Korea's "Donghak ants" heavily long 005930) underperform.

### Scenario C — Samsung Balanced Recovery (~20%)

**Trigger chain**: HBM cycle moderates in H2 2026 as AI efficiency gains (smaller effective models, better HBM bandwidth reuse in software stacks, inference batching optimizations) + capacity additions from all three players close the undersupply faster than expected. TAM growth slows to ~+35% vs BofA's +58%. *But* Samsung's HBM4 qualification is cleaner than expected, and Samsung Foundry wins a visible TPU-class or Maia-class customer — validating the two-horse strategy.

**End-2026 variables**:
- HBM TAM: **$48-52B** (below BofA)
- SK Hynix HBM share: 55-60%
- Samsung HBM share: 35-40% (gains on a smaller pie)
- Samsung Foundry rev: +35-50% YoY
- Samsung (005930): **₩240-270k** (+20-35%)
- SK Hynix (000660): **₩950k-1.15M** (−7% to +12%)
- KOSPI: 5,900-6,300
- USD/KRW: 1,440-1,480

**Characterization**: Crossover year. SK Hynix flattens as the cycle matures and it faces tougher comps; Samsung re-rates as the market prices in its diversification. This is the scenario where *relative* performance flips: Samsung outperforms SK Hynix from mid-2026 onward.

### Scenario D — Cycle Top 2026, Painful 2027 (~15%)

**Trigger chain**: HBM supercycle peaks earlier than expected. Hyperscaler capex digestion begins in Q4 2026 after the 2024-2026 build-out sprint. CXMT's HBM3 ramp forces Micron (and Samsung, the weakest HBM4 player among the big three) to defend share on HBM3E with margin-destructive pricing. Samsung's HBM4 gains remain stuck at 25-30%. A Trump-era 2027 tariff on Korean memory (retaliation for EU-Korea alignment or Yongin subsidy dispute) compresses multiples further.

**End-2026 variables**:
- HBM TAM: **$45-50B** (below BofA)
- SK Hynix HBM share: 60-65% (defends via HBM4 Rubin exclusivity)
- Samsung HBM share: 22-28%
- Samsung Foundry rev: +5-15% YoY
- Samsung (005930): **₩160-195k** (−20% to −3%)
- SK Hynix (000660): **₩900k-1.05M** (−12% to +2%)
- KOSPI: 5,200-5,600
- USD/KRW: 1,500-1,550

**Characterization**: The 2017-2019 memory-down-cycle rhymes. SK Hynix still more resilient (HBM4 Rubin lock-in + pure-play premium) but de-rates. Samsung underperforms severely — consumer/mobile segment drag + foundry still not at scale + HBM share compressed. Korean retail investors capitulate.

## Probability-Weighted End-2026 Targets

| Variable | Weighted mid | Distribution |
|---|---|---|
| HBM TAM 2026 | **~$54B** | A:60 · B:56 · C:50 · D:48 |
| Samsung (005930) | **~₩230k** (+14%) | A:275 · B:235 · C:255 · D:180 |
| SK Hynix (000660) | **~₩1.25M** (+22%) | A:1,425 · B:1,400 · C:1,050 · D:975 |
| KOSPI | ~6,200 | A:6,600 · B:6,300 · C:6,100 · D:5,400 |

**Key observation**: The weighted return for SK Hynix (~+22%) is higher than for Samsung (~+14%) even though both have strong upside in scenario A. Reason: Samsung's downside in D is much deeper (−20%) while SK Hynix holds up better. **SK Hynix is the higher-expected-return, narrower-risk play**; Samsung is the *optionality* play — same upside in A but cheaper entry with more downside risk in D.

## What Would Move the Scenario Probabilities

- **Up for A/C (Samsung strong)**: Clean HBM4 12-hi yield report in Q2 earnings; a named hyperscaler foundry customer announcement (most likely: Google TPU dual-source, Amazon Trainium overflow).
- **Up for B (base case)**: Confirmation that SK Hynix is the sole HBM4 lead validator for NVIDIA Rubin at launch; continued Samsung HBM4 delays or re-qualification cycles.
- **Up for D (downside)**: Meta or Microsoft explicitly cutting 2027 capex guidance; CXMT HBM3 volume surprising to the upside; a Trump 25%+ tariff on Korean semiconductors.
- **Tail risk not modeled**: A TSMC/SK Hynix JV for CoWoS (would compress Samsung foundry opportunity); a US ban on *Samsung foundry* serving any Chinese AI accelerator customer (already partially true, but an expansion would hit).

## Energy/Supply Chain Wildcard

From [[south-korea]]: Korea imports 70% of oil and 20% of natural gas from the Middle East; Samsung/SK Hynix depend on **97% Israeli bromine** (chip etching) and **65% Qatari helium** (wafer cooling). Samsung and SK Hynix have months of stock. Small probability (~5-8%) that a second Iran-Israel flare-up cuts input supplies, forcing a weeks-long Yongin production slowdown. This would hit scenarios symmetrically (TAM falls but so does supply) — probably neutral for relative share, but **negative in absolute terms** for both stocks by 10-15% on the input-cost shock.

## Strategic Implications

**For Samsung Electronics (005930)**:
1. The **foundry is the strategic hedge**, not a distraction. Weighted expected value depends on whether hyperscaler custom silicon volume spills over to Samsung 2nm/3nm from TSMC.
2. HBM4 Rubin validation is table-stakes. Missing this locks Samsung into the "lagging supplier" narrative for the entire Rubin cycle (through ~2028).
3. Consumer/mobile segment is dead weight in an AI memory bull market. Expect activist pressure for a spin-off within 18 months if scenarios B or D play out.

**For SK Hynix (000660)**:
1. Currently priced for scenario B. Upside exists in A but valuation is stretched.
2. No foundry hedge. Pure-play memory means the stock rides the memory cycle both directions.
3. The **CXMT endgame** is the quiet 2027-2028 threat — US export controls are the moat, and any loosening (e.g., a Trump-Xi grand bargain on AI chips) would be the bear catalyst.

**For Korean macro**:
- Samsung + SK Hynix combined are ~35% of KOSPI weight. A scenario A/B regime lifts KOSPI materially despite energy shock drag.
- USD/KRW convergence back toward 1,400 requires export surge + BOK staying hawkish; scenario D keeps KRW weak.
- Lee Jae Myung's $530B Yongin mega-cluster has a ~2029-2030 payoff window — today's scenarios are mostly about the **existing** Samsung/SK Hynix fabs, not the mega-cluster.

**For hyperscaler custom silicon**:
- The Korean memory duopoly is **not** the bottleneck the hyperscalers worry about — they worry about TSMC CoWoS packaging and fab capacity. Memory is supply-tight but available.
- Anthropic's 3.5GW Broadcom/Google commitment implies roughly **15-25 million HBM stacks** lifetime — every watt of custom silicon is incremental HBM demand. Korea is a structural beneficiary of the custom silicon trend *despite* it being a threat to NVIDIA.

## Confidence: Medium

The HBM4 qualification question and Samsung foundry thesis are the biggest sources of uncertainty. HBM TAM direction is more confident — the custom silicon migration adds demand, it doesn't subtract. CXMT timing and US export policy are the binary tail risks.

## See Also
- [[south-korea]]
- [[market-snapshot]]
- [[financial-markets-2026]]
- [[ai-labs-and-industry]]
- [[china]]
- [[donald-trump]]
- [[simulations/sim-us-iran-talks-korea-crypto-equities-2026-04-12|Previous Korea markets sim]]

---

# 삼성전자와 SK하이닉스 — 하이퍼스케일러 커스텀 실리콘 시대의 전망 (HBM4 + CXMT + Rubin 사이클)

## 왜 이 시뮬레이션인가

AI 컴퓨팅 스택이 둘로 갈라지고 있다:
- **로직 (연산)**: NVIDIA GPU 독점이 잠식되고 있다. Google TPUv7 Ironwood, Amazon Trainium 3, Microsoft Maia 200, Meta MTIA, 그리고 2027년부터 OpenAI의 Broadcom ASIC과 Anthropic의 3.5GW Broadcom/Google 딜이 하이퍼스케일러들을 자체 실리콘으로 끌어들이고 있다. 커스텀 ASIC CAGR은 약 45%; NVIDIA 인퍼런스 점유율은 현재 ~90%에서 2028년 20-30%로 하락 전망.
- **메모리 (HBM)**: 모든 커스텀 ASIC — TPU, Trainium, Maia, MTIA — 은 **여전히 HBM을 필요로 한다**. SK하이닉스(~53-62%), 삼성(~17-35%), 마이크론(~11-21%)의 과점은 실제 초크포인트이며, TSMC CoWoS 패키징과 HBM을 "choke point"로 지정한 미국 수출 통제(2026년 1월 프레임워크)가 이를 강화한다.

따라서 핵심 질문은 "커스텀 실리콘이 한국 메모리를 죽이는가?"가 아니다 — "하이퍼스케일러 ASIC 확산에 따른 TAM 확장 + 삼성의 NVIDIA Rubin HBM4 추격이 CXMT 압력을 상쇄하는가, 그리고 업사이드가 두 한국 업체에 어떻게 분배되는가?"이다.

**중요한 비대칭**: SK하이닉스는 순수 메모리 업체다. 삼성은 **이 싸움에서 두 마리 개를 갖고 있다** — HBM 메모리 **그리고** 파운드리. 하이퍼스케일러들이 로직 스택을 더 많이 커스텀 ASIC으로 이전하고 TSMC 3nm가 수요 3배 초과 상태로 100% 가동을 유지한다면, 삼성 파운드리는 유일한 의미있는 대안이 된다. SK하이닉스에게는 없는 헤지다.

## 현재 스냅샷 (2026-04-13, WebSearch 앵커)

| 자산/지표 | 수준 | 비고 |
|---|---|---|
| 삼성전자 (005930) | **₩201,000** | 4/13; 전일 ₩206,000 (−2.4%); HBM4 Rubin 딜로 사상 최고가 구간 |
| SK하이닉스 (000660) | **₩1,027,000** | 4/12; 전일 ₩998,000; 삼성 Q1 프리뷰에 한때 ₩1,050,000까지 +15% 급등 |
| KOSPI | 5,778 | 4/10 휴전 불확실성에 −1.61% |
| USD/KRW | 1,479 | 에너지 쇼크 + 칩 주문 타이밍으로 약세 |
| 브렌트유 | $96.69 | 현물 일부 등급 전쟁 고점 $150 터치 |
| HBM 2026 TAM (BofA) | **$54.6B** | YoY +58% |
| DRAM 매출 증가율 2026E | +51% | ASP +33% — 15년+ 최악의 공급부족 (Goldman) |
| SK하이닉스 HBM 점유율 (Q3 '25) | 53% | Q2는 62% (삼성 HBM3E 추격) |
| 삼성 HBM 점유율 (Q3 '25) | 35% | Q2 17% 대비 상승 — HBM3E 12단 재자격 |
| 마이크론 HBM 점유율 | 11-21% | 변동성; Micron 1γ 노드 HBM4 도전자 |
| 삼성 HBM4 ASP 목표 | ~$700/유닛 | 이전 세대 대비 +30%; 해당 가격에서 영업이익률 50-60% |
| Morgan Stanley 삼성 메모리 2026E 이익 | +310% | ₩100조 수준 근접 |
| Anthropic TPU 커밋 | **100만 TPUv7 + 3.5GW** | Broadcom/Google, 2026-2027 램프 |
| NVIDIA Rubin HBM4 공급사 | 삼성 + SK하이닉스 독점 | UBS: SK하이닉스 70% 점유 목표 |
| CXMT HBM3 양산 | 2026년 말 | SK하이닉스와 2-3년 격차; 미국 "choke point" 수출 금지 구속 |

**시장 다이버전스**: 삼성(005930)은 4/13 하락, SK하이닉스는 상승 — 시장은 **SK하이닉스를 더 깨끗한 HBM4-Rubin 플레이**로 가격 매기고 있고 삼성은 여전히 실행 리스크 + 파운드리/소비자 드래그가 있다고 보고 있다. 이것이 아래 시나리오들이 스트레스 테스트하는 시장의 현재 *사전 확률*이다.

광범위한 맥락은 [[market-snapshot|시장 스냅샷]] 참조.

## 시나리오 매트릭스

두 축. HBM 수요 궤적 (y) × 삼성 실행력 (x).

|  | **삼성 HBM4 + 파운드리 강세** | **삼성 HBM4 + 파운드리 약세** |
|---|---|---|
| **HBM TAM 슈퍼사이클 (커스텀 실리콘 가산적)** | **A. Korea Inc. 쌍봉 정점** (~25%) | **B. SK하이닉스 승자독식** (~40% 기본) |
| **HBM TAM 둔화 (효율 개선 + CXMT 잠식)** | **C. 삼성 균형 회복** (~20%) | **D. 2026 사이클 고점, 2027 고통** (~15%) |

### 시나리오 A — Korea Inc. 쌍봉 정점 (~25%)

**트리거 체인**: Rubin HBM4 자격이 Q2에 두 공급사 모두 완료; SK하이닉스 ~60% 점유, 삼성 ~35% 확보. Anthropic의 3.5GW Broadcom/Google 커밋 + Amazon Trainium 3 증설로 추가 ASIC 한 대당 **HBM 스택 4-8개가 GPU 수요 위에 가산**됨 (대체가 아닌 보완). TSMC CoWoS가 병목 유지, 삼성 첨단 패키징(SAINT-S)이 오버플로 수주. 결정적으로, 삼성 파운드리가 TSMC 3nm의 수요 3배 초과분에 대한 듀얼 소싱으로 TPU급 또는 Trainium급 커스텀 ASIC 물량을 TSMC로부터 되찾음.

**2026년 말 변수**:
- HBM TAM: **$58-62B** (BofA 기준치 상회)
- SK하이닉스 HBM 점유: 58-62%
- 삼성 HBM 점유: 32-38%
- 삼성 파운드리 매출: YoY +45-60% (TPU급 오버플로)
- 삼성 (005930): **₩260-290k** (+29-44%)
- SK하이닉스 (000660): **₩1.35-1.50M** (+31-46%)
- KOSPI: 6,400-6,800
- USD/KRW: 1,360-1,400 (BoK 긴축 + 수출 급증)

**특징**: 양대 한국 대기업 모두 사상 최고가 기록. 파운드리가 마침내 프리미엄 배수를 얻으며 삼성 재평가; SK하이닉스는 가장 깨끗한 순수 메모리 플레이로 지속. KOSPI 리더십은 좁지만 강렬 (삼성 + SK하이닉스 단독으로 지수 가중치 ~35%).

### 시나리오 B — SK하이닉스 승자독식 (~40%, 기본 케이스)

**트리거 체인**: 이것이 4/13 가격 움직임이 이미 반영하고 있는 시나리오. SK하이닉스가 HBM4 물량의 65-70% 보유 (UBS 전망); 삼성 HBM4는 자격 통과하나 수율/원가 핸디캡으로 25-30% 유지. 삼성 파운드리는 일부 커스텀 ASIC 물량 확보하나 낮은 메모리 점유율을 상쇄할 규모는 아님. CXMT는 수출 통제로 억제(HBM3만, 3년 격차).

**2026년 말 변수**:
- HBM TAM: **$54-58B** (BofA 기준치 유지)
- SK하이닉스 HBM 점유: 65-70%
- 삼성 HBM 점유: 25-30%
- 삼성 파운드리 매출: YoY +15-25% (소폭 수주)
- 삼성 (005930): **₩220-250k** (+9-24%)
- SK하이닉스 (000660): **₩1.30-1.50M** (+27-46%)
- KOSPI: 6,100-6,500
- USD/KRW: 1,420-1,460

**특징**: SK하이닉스가 2026년 시장의 총아 — 주가는 2025년 저점 대비 더블, 밸류에이션은 부담되지만 이익 근거로 방어 가능. 삼성은 Morgan Stanley가 약속한 메모리 이익 +310%를 달성하지만 파운드리/소비자 세그먼트 드래그로 SK하이닉스 대비 *디레이팅*. 부의 효과 집중: SK하이닉스 주주 대승, 삼성 개미(005930을 대량 보유한 "동학개미") 언더퍼폼.

### 시나리오 C — 삼성 균형 회복 (~20%)

**트리거 체인**: HBM 사이클이 2026년 하반기에 둔화 — AI 효율 개선(모델 경량화, 소프트웨어 스택에서의 HBM 대역폭 재사용 개선, 인퍼런스 배칭 최적화) + 3사 모두의 증설이 예상보다 빠르게 공급부족을 해소. TAM 성장률이 BofA의 +58%에서 ~+35%로 둔화. *그러나* 삼성의 HBM4 자격이 예상보다 깔끔하고, 삼성 파운드리가 가시적인 TPU급 또는 Maia급 고객 수주 — 두 마리 전략 검증.

**2026년 말 변수**:
- HBM TAM: **$48-52B** (BofA 하회)
- SK하이닉스 HBM 점유: 55-60%
- 삼성 HBM 점유: 35-40% (작아진 파이에서 점유 상승)
- 삼성 파운드리 매출: YoY +35-50%
- 삼성 (005930): **₩240-270k** (+20-35%)
- SK하이닉스 (000660): **₩950k-1.15M** (−7% ~ +12%)
- KOSPI: 5,900-6,300
- USD/KRW: 1,440-1,480

**특징**: 크로스오버의 해. SK하이닉스는 사이클이 성숙해지고 비교 기저가 높아지면서 횡보; 삼성은 다각화가 가격 반영되며 재평가. 이 시나리오가 *상대적* 성과가 역전되는 구간: 2026년 중반부터 삼성이 SK하이닉스를 아웃퍼폼.

### 시나리오 D — 2026 사이클 고점, 2027 고통 (~15%)

**트리거 체인**: HBM 슈퍼사이클이 예상보다 이른 시기에 고점. 2024-2026 구축 스프린트 이후 하이퍼스케일러 CapEx 소화 국면이 Q4 2026에 시작. CXMT HBM3 램프가 마이크론(과 빅3 중 HBM4 최약체인 삼성)으로 하여금 HBM3E에서 마진 파괴적 가격으로 점유 방어를 강요. 삼성 HBM4 점유율은 25-30%에 정체. Trump 행정부의 2027년 한국 메모리 관세(EU-한국 동조화 또는 용인 보조금 분쟁 보복)가 멀티플을 추가 압축.

**2026년 말 변수**:
- HBM TAM: **$45-50B** (BofA 하회)
- SK하이닉스 HBM 점유: 60-65% (HBM4 Rubin 독점으로 방어)
- 삼성 HBM 점유: 22-28%
- 삼성 파운드리 매출: YoY +5-15%
- 삼성 (005930): **₩160-195k** (−20% ~ −3%)
- SK하이닉스 (000660): **₩900k-1.05M** (−12% ~ +2%)
- KOSPI: 5,200-5,600
- USD/KRW: 1,500-1,550

**특징**: 2017-2019 메모리 다운사이클과 운율. SK하이닉스는 여전히 더 견고(HBM4 Rubin 락인 + 순수 플레이 프리미엄)하나 디레이팅. 삼성은 심하게 언더퍼폼 — 소비자/모바일 드래그 + 파운드리 규모 미달 + HBM 점유 압축. 한국 개미 항복 구간.

## 확률 가중 2026년 말 타겟

| 변수 | 가중 중간값 | 분포 |
|---|---|---|
| HBM TAM 2026 | **~$54B** | A:60 · B:56 · C:50 · D:48 |
| 삼성 (005930) | **~₩230k** (+14%) | A:275 · B:235 · C:255 · D:180 |
| SK하이닉스 (000660) | **~₩1.25M** (+22%) | A:1,425 · B:1,400 · C:1,050 · D:975 |
| KOSPI | ~6,200 | A:6,600 · B:6,300 · C:6,100 · D:5,400 |

**핵심 관찰**: SK하이닉스의 가중 기대수익률(~+22%)이 삼성(~+14%)보다 높다. 시나리오 A에서 둘 다 업사이드가 강한데도 말이다. 이유: 삼성의 D 시나리오 하방(−20%)이 훨씬 깊은 반면 SK하이닉스는 더 잘 방어한다. **SK하이닉스는 더 높은 기대수익 + 좁은 리스크 플레이**; 삼성은 *옵셔널리티* 플레이 — A에서 같은 업사이드지만 더 싼 진입가 + D에서 더 큰 하방 리스크.

## 시나리오 확률을 움직일 요인

- **A/C 상향 (삼성 강세)**: Q2 실적에서 깔끔한 HBM4 12단 수율 보고; 지목된 하이퍼스케일러 파운드리 고객 발표(가장 유력: Google TPU 듀얼 소스, Amazon Trainium 오버플로).
- **B 상향 (기본 케이스)**: SK하이닉스가 NVIDIA Rubin 런칭 시점의 유일한 HBM4 리드 검증자로 확정; 삼성 HBM4 지연 또는 재자격 사이클 지속.
- **D 상향 (다운사이드)**: Meta 또는 Microsoft가 2027 CapEx 가이던스를 명시적으로 삭감; CXMT HBM3 물량이 상방으로 서프라이즈; Trump가 한국 반도체에 25%+ 관세.
- **모델링 안 한 꼬리 리스크**: TSMC/SK하이닉스 CoWoS JV (삼성 파운드리 기회 압축); 미국이 *삼성 파운드리*가 중국 AI 가속기 고객을 전면 제공하는 것을 금지(이미 부분적으로 존재, 확대는 타격).

## 에너지/공급망 와일드카드

[[south-korea|한국]]에서: 한국은 석유의 70%, 천연가스의 20%를 중동에서 수입; 삼성/SK하이닉스는 **이스라엘 브롬 97%**(칩 식각) 및 **카타르 헬륨 65%**(웨이퍼 냉각)에 의존. 삼성과 SK하이닉스는 수 개월치 재고 보유. 소확률(~5-8%)로 이란-이스라엘 2차 충돌이 투입 공급을 차단, 용인 생산을 수 주간 감속시킬 수 있다. 이는 시나리오들에 대칭적으로 타격(TAM 하락, 공급도 하락) — 상대적 점유에는 중립, **절대값에서는 부정적** — 양 주식 모두 투입 비용 쇼크로 10-15% 하락.

## 전략적 함의

**삼성전자 (005930)에게**:
1. **파운드리는 전략적 헤지**이지 산만함이 아니다. 가중 기대가치는 하이퍼스케일러 커스텀 실리콘 물량이 TSMC에서 삼성 2nm/3nm로 넘어오는지에 달려있다.
2. HBM4 Rubin 검증은 테이블 스테이크. 이걸 놓치면 Rubin 사이클 전체(~2028까지) "후행 공급사" 내러티브에 갇힌다.
3. 소비자/모바일 세그먼트는 AI 메모리 불마켓에서 사중. 시나리오 B 또는 D 전개 시 18개월 내 분할 요구 행동주의 압력 예상.

**SK하이닉스 (000660)에게**:
1. 현재 시나리오 B 기준으로 가격 반영. A의 업사이드는 존재하나 밸류에이션은 부담.
2. 파운드리 헤지 없음. 순수 메모리 플레이는 주가가 메모리 사이클을 양방향으로 탐.
3. **CXMT 엔드게임**이 조용한 2027-2028 위협 — 미국 수출 통제가 해자이며, 어떤 완화(예: Trump-Xi AI 칩 그랜드 바겐)도 베어 촉매.

**한국 매크로에게**:
- 삼성 + SK하이닉스 합산 KOSPI 가중치 ~35%. 시나리오 A/B 레짐은 에너지 쇼크 드래그에도 불구하고 KOSPI를 상당히 들어올림.
- USD/KRW가 1,400대로 수렴하려면 수출 급증 + BoK 매파 유지 필요; 시나리오 D는 원화 약세 지속.
- 이재명의 $530B 용인 메가 클러스터는 ~2029-2030 회수 구간 — 오늘의 시나리오들은 대부분 **기존** 삼성/SK하이닉스 팹에 대한 것이지 메가 클러스터가 아님.

**하이퍼스케일러 커스텀 실리콘에게**:
- 한국 메모리 듀오폴리는 하이퍼스케일러들이 걱정하는 병목이 **아님** — 그들은 TSMC CoWoS 패키징과 팹 캐파시티를 걱정. 메모리는 공급 타이트하지만 조달 가능.
- Anthropic의 3.5GW Broadcom/Google 커밋은 대략 **1,500-2,500만 HBM 스택** 생애 수요를 시사 — 커스텀 실리콘의 매 와트가 HBM 증분 수요. 한국은 NVIDIA에는 위협이지만 커스텀 실리콘 트렌드의 *구조적* 수혜자.

## 신뢰도: 중간

HBM4 자격 문제와 삼성 파운드리 명제가 가장 큰 불확실성 원천. HBM TAM 방향은 더 자신 있음 — 커스텀 실리콘 이전은 수요를 더하지, 빼지 않는다. CXMT 타이밍과 미국 수출 정책이 이진적 꼬리 리스크.

## See Also
- [[south-korea|한국]]
- [[market-snapshot|시장 스냅샷]]
- [[financial-markets-2026|2026 금융시장]]
- [[ai-labs-and-industry|AI 연구소 및 산업]]
- [[china|중국]]
- [[donald-trump]]
- [[simulations/sim-us-iran-talks-korea-crypto-equities-2026-04-12|이전 한국 시장 시뮬레이션]]
