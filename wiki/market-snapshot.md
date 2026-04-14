---
title: Market Snapshot
type: reference
updated: 2026-04-12 (WebSearch refreshed)
tags: [market, finance, reference]
---

# Market Snapshot

A rolling reference of volatile market indicators used as shared context for simulations. Wiki-native alternative to having each simulation agent make redundant web searches.

**When simulating finance/market/crypto scenarios**: Claude Code should first check this page for recency. If stale (>7 days), run WebSearch to refresh, then update this page.

## Guidance for Updates

- Keep entries terse — one line per indicator, focus on numerical value
- Include date stamp per indicator when they diverge
- Cite source if non-obvious (Bloomberg, FRED, CoinGecko, etc.)
- Archive previous snapshots as a dated subsection if useful for trend analysis
- Do NOT delete indicators — stale values are better than missing ones for simulation context

## Current Snapshot (as of 2026-04-12)

*Refreshed via WebSearch on 2026-04-12. Reconciliation note below: WebSearch real-world data diverges in places from wiki-internal narrative (wiki depicts deeper Iran-war market shock — e.g. wiki-internal post-war KOSPI ~2,550). Simulations should use WebSearch values as anchor and flag where wiki narrative would imply lower.*

### Equities
- **S&P 500**: 6,616.85 (Apr 11-12, +0.08% d/d) — best week since Nov 2025 after ceasefire
- **KOSPI**: 5,778 (Apr 10 close, -1.61% d/d; snapping 4-day rally on ceasefire uncertainty)
- **Nikkei 225**: positive YTD through Apr 6 (one of three major indices with gains YTD)
- **DAX**: (partial data; roughly flat YTD)
- **Shanghai Composite**: 3,986 (Apr 10, +0.51% d/d; -3.56% 1-month; +23.10% YoY) — SSE gapped +2.7% Apr 8 on ceasefire

### Commodities
- **Brent crude**: $96.69 (prev close $95.92) — futures sanguine vs physical spot that touched $150 at war peak
- **Gold**: $4,762.62/oz (Apr 11, 8:37 AM EDT) — all-time high zone as war/inflation hedge
- **Natural gas (TTF)**: (to be updated; elevated due to Gulf LNG disruption)

### Currencies (vs USD)
- **EUR/USD**: (to be updated)
- **USD/JPY**: (to be updated)
- **USD/KRW**: 1,479.07 (prev 1,478.35) — won sharply weaker vs wiki's 1,380 late-2025 baseline
- **INR/USD**: 94.65 (wiki narrative)
- **DXY**: (to be updated)

### Rates & Yields
- **US 10Y Treasury**: ~4.3% (Apr 9, FRED/CNBC)
- **US 2Y**: (to be updated)
- **Fed funds rate**: (to be updated)
- **ECB deposit rate**: (to be updated)
- **BOK base rate**: (to be updated)

### Crypto
- **Bitcoin (BTC)**: ~$71,448 (Yahoo Finance, +4.15% d/d) — significant pullback from late-2025 peaks; treat with caution, cross-check before sim
- **Ethereum (ETH)**: $2,249.92 (Apr 10, Fortune)
- **Total crypto market cap**: (to be updated)

### Macro Data
- **US CPI (YoY)**: 3.3% (wiki, March 2026; up from 2.4% Feb)
- **US unemployment**: (to be updated)
- **Eurozone HICP**: (to be updated)
- **China CPI**: (to be updated)

### Notable Earnings / Corporate
- **Samsung / SK Hynix**: stable but helium rationing (from south-korea.md)
- **Foxconn Q1**: +30% YoY (AI rack demand)
- **DJT (Trump Media)**: down ~80% from peak
- **TSMC**: Q1 +35% YoY, shares +25% YTD

## How to Use This Page

1. Before launching a market/finance simulation, call `wiki_read("market-snapshot")`
2. Check `updated:` frontmatter — if fresh enough, copy relevant indicators into the scenario context
3. If stale, run WebSearch for specific indicators your scenario needs, update this page, then proceed
4. Do not let agents search independently — always go through this central snapshot

## See Also
- [[financial-markets-2026]]
- [[iran-war-economic-impact]]
- [[south-korea]]
- [[india]]

---

# 시장 스냅샷

시뮬레이션의 공유 컨텍스트로 사용할 변동성 시장 지표의 롤링 참조 페이지. 각 시뮬레이션 에이전트가 중복 웹검색하는 것에 대한 위키 네이티브 대안.

**금융/시장/암호화폐 시나리오 시뮬레이션 시**: Claude Code는 먼저 이 페이지의 최신성을 확인해야 함. 7일 이상 지났으면 WebSearch로 갱신 후 이 페이지를 업데이트.

## 업데이트 가이드

- 간결하게 — 지표당 한 줄, 숫자 값에 집중
- 값이 분기할 경우 지표별 날짜 스탬프 포함
- 출처가 명확하지 않으면 표기 (Bloomberg, FRED, CoinGecko 등)
- 트렌드 분석에 유용할 경우 이전 스냅샷을 날짜별 하위 섹션으로 보관
- 지표를 삭제하지 말 것 — 시뮬레이션 컨텍스트에는 오래된 값이 누락된 값보다 낫다

## 현재 스냅샷 (2026-04-12 기준)

*2026-04-12 WebSearch로 갱신. 참고: 실제 WebSearch 값이 위키 내부 서사(이란전으로 인한 더 깊은 시장 충격, 예: 위키 내부 전후 KOSPI ~2,550)와 일부 괴리됨. 시뮬레이션은 WebSearch 값을 앵커로 사용하되, 위키 서사가 더 낮은 값을 암시하는 경우 명시할 것.*

### 주식
- **S&P 500**: 6,616.85 (4/11-12, 일간 +0.08%) — 휴전 후 2025년 11월 이후 최고의 주간
- **KOSPI**: 5,778 (4/10 종가, 일간 -1.61%; 휴전 불확실성에 4일 연속 상승 중단)
- **Nikkei 225**: 4/6까지 YTD 상승 (양호 YTD 성과를 보인 3개 주요 지수 중 하나)
- **DAX**: (일부 데이터; YTD 거의 보합)
- **상하이 종합지수**: 3,986 (4/10, 일간 +0.51%; 1개월 -3.56%; 연간 +23.10%) — 4/8 휴전 소식에 +2.7% 갭업

### 원자재
- **브렌트유**: $96.69 (전일 종가 $95.92) — 선물 시장 안정, 그러나 현물 일부 등급 전쟁 고점 $150 터치
- **금**: $4,762.62/oz (4/11, 8:37 AM EDT) — 전쟁/인플레 헤지로 사상 최고치 구간
- **천연가스 (TTF)**: (업데이트 필요; 걸프 LNG 차질로 고공행진)

### 통화 (USD 대비)
- **EUR/USD**: (업데이트 필요)
- **USD/JPY**: (업데이트 필요)
- **USD/KRW**: 1,479.07 (전일 1,478.35) — 위키의 2025년 말 1,380 기준 대비 원화 대폭 약세
- **INR/USD**: 94.65 (위키 서사)
- **DXY**: (업데이트 필요)

### 금리 및 수익률
- **미국 10년물 국채**: ~4.3% (4/9, FRED/CNBC)
- **미국 2년물**: (업데이트 필요)
- **연방기금금리**: (업데이트 필요)
- **ECB 예금금리**: (업데이트 필요)
- **한국은행 기준금리**: (업데이트 필요)

### 암호화폐
- **비트코인 (BTC)**: ~$71,448 (Yahoo Finance, 일간 +4.15%) — 2025년 말 고점 대비 상당폭 조정; 시뮬 전 재확인 필요
- **이더리움 (ETH)**: $2,249.92 (4/10, Fortune)
- **전체 암호화폐 시가총액**: (업데이트 필요)

### 거시 지표
- **미국 CPI (YoY)**: 3.3% (위키, 2026년 3월; 2월 2.4%에서 상승)
- **미국 실업률**: (업데이트 필요)
- **유로존 HICP**: (업데이트 필요)
- **중국 CPI**: (업데이트 필요)

### 주요 실적 / 기업
- **삼성 / SK하이닉스**: 안정적이나 헬륨 배급 (south-korea.md 기준)
- **폭스콘 Q1**: 전년 대비 +30% (AI 랙 수요)
- **DJT (트럼프 미디어)**: 고점 대비 약 -80%
- **TSMC**: Q1 전년 대비 +35%, 주가 YTD +25%

## 사용 방법

1. 시장/금융 시뮬레이션 실행 전 `wiki_read("market-snapshot")` 호출
2. `updated:` 프런트매터 확인 — 충분히 최신이면 관련 지표를 시나리오 컨텍스트에 복사
3. 오래되었으면 시나리오에 필요한 특정 지표를 WebSearch로 조회, 이 페이지 업데이트 후 진행
4. 에이전트가 독립적으로 검색하게 두지 말 것 — 항상 이 중앙 스냅샷을 경유
