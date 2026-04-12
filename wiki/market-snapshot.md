---
title: Market Snapshot
type: reference
updated: 2026-04-12
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

*This is a seed page. Claude Code should populate with fresh WebSearch data before the next market simulation.*

### Equities
- **S&P 500**: (to be updated)
- **KOSPI**: (to be updated)
- **Nikkei 225**: (to be updated)
- **DAX**: (to be updated)
- **Shanghai Composite**: (to be updated)

### Commodities
- **Brent crude**: ~$95/barrel (from wiki — post-ceasefire baseline)
- **Gold**: (to be updated)
- **Natural gas (TTF)**: (to be updated)

### Currencies (vs USD)
- **EUR/USD**: (to be updated)
- **USD/JPY**: (to be updated)
- **USD/KRW**: ~1,380 (wiki reference, late 2025)
- **INR/USD**: 94.65 (from india.md, post-war depreciation)
- **DXY**: (to be updated)

### Rates & Yields
- **US 10Y Treasury**: ~4.4% (wiki, post-Iran war peak; 2.4-pp below 5.1% UK)
- **US 2Y**: (to be updated)
- **Fed funds rate**: (to be updated)
- **ECB deposit rate**: (to be updated)
- **BOK base rate**: (to be updated)

### Crypto
- **Bitcoin (BTC)**: (to be updated)
- **Ethereum (ETH)**: (to be updated)
- **Total crypto market cap**: (to be updated)

### Macro Data
- **US CPI (YoY)**: 3.3% (from wiki, March 2026)
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

*시드 페이지임. 다음 시장 시뮬레이션 전에 Claude Code가 WebSearch로 채워야 함.*

### 주식
- **S&P 500**: (업데이트 필요)
- **KOSPI**: (업데이트 필요)
- **Nikkei 225**: (업데이트 필요)
- **DAX**: (업데이트 필요)
- **상하이 종합지수**: (업데이트 필요)

### 원자재
- **브렌트유**: ~$95/배럴 (위키 참조 — 휴전 후 기준값)
- **금**: (업데이트 필요)
- **천연가스 (TTF)**: (업데이트 필요)

### 통화 (USD 대비)
- **EUR/USD**: (업데이트 필요)
- **USD/JPY**: (업데이트 필요)
- **USD/KRW**: ~1,380 (위키 참조, 2025년 말)
- **INR/USD**: 94.65 (india.md 기준, 전쟁 후 하락)
- **DXY**: (업데이트 필요)

### 금리 및 수익률
- **미국 10년물 국채**: ~4.4% (위키, 이란전 후 피크; 영국 5.1%보다 2.4%p 낮음)
- **미국 2년물**: (업데이트 필요)
- **연방기금금리**: (업데이트 필요)
- **ECB 예금금리**: (업데이트 필요)
- **한국은행 기준금리**: (업데이트 필요)

### 암호화폐
- **비트코인 (BTC)**: (업데이트 필요)
- **이더리움 (ETH)**: (업데이트 필요)
- **전체 암호화폐 시가총액**: (업데이트 필요)

### 거시 지표
- **미국 CPI (YoY)**: 3.3% (위키, 2026년 3월)
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
