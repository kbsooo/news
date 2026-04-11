# World News Knowledge Wiki

The Economist 기사를 기반으로 세계 뉴스를 체계적으로 정리하고, 정보 간의 관계를 추적하여 세상의 흐름을 이해하고 미래를 예측하는 지식 위키.

A knowledge wiki built from The Economist articles — tracking causal chains between global events, mapping relationships across domains, and building a compounding understanding of how the world works.

## How It Works

이 프로젝트는 [LLM Wiki 패턴](llm-wiki.md)을 따릅니다. 사람이 소스를 큐레이션하고 분석을 지시하면, LLM(Claude Code)이 위키를 유지 관리합니다.

```
raw/ (소스 기사)          →  LLM이 읽고 분석
wiki/ (위키 페이지)       ←  LLM이 생성·업데이트·교차참조
CLAUDE.md (스키마)        →  위키 운영 규칙
```

## Structure

```
raw/                            # The Economist 원문 기사 (불변)
├── leaders/                    # 사설
├── briefing/                   # 브리핑 (심층 분석)
├── finance-and-economics/      # 금융·경제
├── business/                   # 비즈니스
├── science-and-technology/     # 과학·기술
├── middle-east-and-asia/       # 중동·아시아
├── culture/                    # 문화
└── the-world-this-week/        # 금주의 세계

wiki/                           # LLM이 유지하는 위키 페이지
├── index.md                    # 전체 목차
├── log.md                      # 작업 기록
├── iran.md                     # Entity: 이란
├── great-power-rivalry.md      # Concept: 강대국 경쟁
├── iran-war-and-ceasefire-2026.md  # Event: 이란 전쟁
└── ...                         # 22개 이중 언어 페이지
```

## Wiki Pages

모든 위키 페이지는 **영어/한국어 이중 언어**로 작성됩니다. [Obsidian](https://obsidian.md)에서 `[[wikilinks]]`와 그래프 뷰로 탐색할 수 있습니다.

### Entities
**Iran** · **China** · **Donald Trump** · **Israel** · **Gulf States** · **Strait of Hormuz** · **South Korea** · **Monte dei Paschi di Siena**

### Events
**Iran War & Ceasefire (2026)** · **Anthropic Mythos**

### Concepts
**Great Power Rivalry** · **Iran War Economic Impact** · **Iran War Damage Assessment** · **Fertiliser & Food Crisis** · **Financial Markets 2026** · **NATO & Transatlantic Crisis** · **European Defence Industry** · **Japanese Auto Industry** · **Maritime Law & Chokepoints** · **Global Poverty Reduction** · **AI in Mathematics** · **Assisted Dying (UK)**

## Key Insight: The Causal Chain

이 위키에서 발견된 핵심 인과 사슬:

```
Iran War (Feb 28, 2026)
├─ Hormuz Blockade → 715 vessels stranded, 172m barrels trapped
│  ├─ Oil: Dated Brent $144 peak, $25bn infrastructure damage
│  ├─ Gas: Ras Laffan 17% destroyed, South Korea days from exhaustion
│  ├─ Fertiliser: urea +70%, 45m more in acute hunger
│  └─ Downstream: aluminium, helium, petrochemicals disrupted
├─ Geopolitics
│  ├─ NATO at 77-year low → European self-defence imperative
│  ├─ China exploiting US weakness → May 2026 Xi-Trump summit
│  ├─ Gulf states' assumptions shattered → alliance diversification
│  └─ Israel sidelined from peace → Lebanon escalation
├─ Finance
│  ├─ Bond markets: stagflation tug-of-war
│  ├─ Trump trades: DJT -80%, Peak Trump mid-2025
│  └─ Private credit: Blackstone/KKR -33%, redemption freezes
└─ Nuclear risk: 400kg HEU remains, proliferation incentive increased
```

## Operations

| Command | Description |
|---------|-------------|
| **Ingest** | 새 기사를 `raw/`에 넣고 LLM에게 ingest 요청 → 5-15개 위키 페이지 생성/업데이트 |
| **Query** | 위키에 대해 질문 → LLM이 관련 페이지를 읽고 종합 답변 |
| **Lint** | 위키 건강 점검 → 모순, 고아 페이지, 누락된 교차 참조 탐지 |

## Tools

- **[Claude Code](https://claude.ai/code)** — 위키 유지 관리 LLM
- **[Obsidian](https://obsidian.md)** — 위키 브라우징 및 그래프 뷰
- **Git** — 버전 관리 및 히스토리
