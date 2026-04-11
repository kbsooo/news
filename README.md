# World News Knowledge Wiki

The Economist 기사를 기반으로 세계 뉴스를 체계적으로 정리하고, 정보 간의 관계를 추적하여 세상의 흐름을 이해하고 미래를 예측하는 지식 위키.

A knowledge wiki built from The Economist articles — tracking causal chains between global events, mapping relationships across domains, and building a compounding understanding of how the world works.

## How It Works

이 프로젝트는 [LLM Wiki 패턴](llm-wiki.md)을 따릅니다. 사람이 소스를 큐레이션하고 분석을 지시하면, LLM(Claude Code)이 위키를 유지 관리합니다.

```
raw/ (소스 기사)          →  LLM이 읽고 분석
wiki/ (위키 페이지)       ←  LLM이 생성·업데이트·교차참조
mcp_server/ (MCP 서버)   →  위키 지식을 도구로 노출 (검색, 그래프, 시뮬레이션)
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
├── china/                      # 중국
├── culture/                    # 문화
├── the-world-this-week/        # 금주의 세계
└── the-world-in-brief/         # 일일 브리핑

wiki/                           # LLM이 유지하는 위키 페이지
├── index.md                    # 전체 목차
├── log.md                      # 작업 기록
├── simulations/                # 시나리오 시뮬레이션 결과
├── iran.md                     # Entity: 이란
├── great-power-rivalry.md      # Concept: 강대국 경쟁
├── iran-war-and-ceasefire-2026.md  # Event: 이란 전쟁
└── ...                         # 24개 이중 언어 페이지

mcp_server/                     # MCP 서버 (Python)
├── server.py                   # 6개 도구 정의
├── wiki_parser.py              # 위키 마크다운 파싱
└── requirements.txt            # 의존성
```

## Wiki Pages

모든 위키 페이지는 **영어/한국어 이중 언어**로 작성됩니다. [Obsidian](https://obsidian.md)에서 `[[wikilinks]]`와 그래프 뷰로 탐색할 수 있습니다.

### Entities
**Iran** · **China** · **Donald Trump** · **Israel** · **Gulf States** · **Strait of Hormuz** · **South Korea** · **Monte dei Paschi di Siena**

### Events
**Iran War & Ceasefire (2026)** · **Anthropic Mythos** · **Artemis II**

### Concepts
**Great Power Rivalry** · **Iran War Economic Impact** · **Iran War Damage Assessment** · **Fertiliser & Food Crisis** · **Financial Markets 2026** · **NATO & Transatlantic Crisis** · **European Defence Industry** · **Japanese Auto Industry** · **Maritime Law & Chokepoints** · **AI Labs & Industry** · **AI in Mathematics** · **Global Poverty Reduction** · **Assisted Dying (UK)**

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

## MCP Server: Simulation & Prediction

위키 지식을 구조화된 도구로 노출하는 MCP 서버. Claude Code가 자동으로 연결하여 시나리오 시뮬레이션과 예측을 수행합니다.

### Setup

```bash
# Python 3.11-3.12 권장 (uv 사용 시)
uv pip install --python 3.12 mcp pyyaml

# 또는 직접 설치
pip install mcp pyyaml
```

`.mcp.json`이 프로젝트 루트에 있으므로, Claude Code를 이 디렉토리에서 실행하면 MCP 서버가 자동 연결됩니다.

### MCP Tools (6개)

| Tool | Description | Example |
|------|-------------|---------|
| `wiki_index` | 전체 위키 목록 (타입별) | 어떤 페이지들이 있는지 확인 |
| `wiki_search(query)` | 키워드 검색 (제목/태그/본문) | `wiki_search("fertiliser")` |
| `wiki_read(page)` | 특정 페이지 전문 읽기 | `wiki_read("iran")` |
| `wiki_graph(page, depth)` | 링크 네트워크 매핑 | `wiki_graph("iran", depth=2)` |
| `causal_chain(topic)` | 인과 관계 추출 | `causal_chain("oil price")` |
| `simulate(scenario, variables)` | 시뮬레이션 컨텍스트 수집 | 아래 예시 참조 |

### Simulation 사용 예시

Claude Code에서 자연어로 질문하면 됩니다:

```
"호르무즈 해협 봉쇄가 2026년 말까지 지속되면 어떻게 되는가?"
```

MCP 도구가 자동으로:
1. 관련 위키 페이지를 검색·수집 (15+ 페이지)
2. 인과 사슬을 추출
3. 행위자별 프로필을 조합
4. 구조화된 컨텍스트를 Claude에게 전달

Claude가 이 컨텍스트를 기반으로 시나리오 분석을 수행하고, 결과를 `wiki/simulations/`에 이중 언어 페이지로 저장합니다.

## Operations

| Operation | Description |
|-----------|-------------|
| **Ingest** | 새 기사를 `raw/`에 넣고 LLM에게 ingest 요청 → 5-15개 위키 페이지 생성/업데이트 |
| **Query** | 위키에 대해 질문 → LLM이 관련 페이지를 읽고 종합 답변 |
| **Simulate** | 시나리오 질문 → MCP 도구로 지식 수집 → 인과 분석 → 예측 리포트 생성 |
| **Lint** | 위키 건강 점검 → 모순, 고아 페이지, 누락된 교차 참조 탐지 |

## Tools

- **[Claude Code](https://claude.ai/code)** — 위키 유지 관리 + 시뮬레이션 LLM
- **[Obsidian](https://obsidian.md)** — 위키 브라우징 및 그래프 뷰
- **MCP Server** — 위키 지식을 구조화된 도구로 노출
- **Git** — 버전 관리 및 히스토리
