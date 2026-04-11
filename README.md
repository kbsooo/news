# World News Knowledge Wiki + Multi-Agent Simulation

The Economist 기사를 기반으로 세계 뉴스 지식 위키를 구축하고, 그 위키를 기반으로 다중 에이전트 시뮬레이션을 실행하여 미래 시나리오를 예측하는 시스템.

Build a knowledge wiki from Economist articles, then run multi-agent simulations where each geopolitical actor — grounded in its wiki page — independently decides its actions, producing emergent outcomes.

## Core Idea

```
기사 수집 → 위키 구축 → 시뮬레이션 → 예측
               ↑                        │
               └────── 피드백 ──────────┘
```

위키가 쌓일수록 에이전트가 풍부해지고, 시뮬레이션이 정교해지고, 결과가 다시 위키를 강화합니다.

## Architecture

```
┌───────────────���─────────────────────────────────────────┐
│  호스트 LLM (Claude Code / Codex / Gemini CLI / ...)    │
│                                                         │
│  Orchestrator                    Subagents (병렬)       │
│  ┌─────────────┐    ┌──────────────────────────────┐    │
│  │ sim_setup   │    │ Agent("이란")  → 독립 판단   │    │
│  │ sim_advance │    │ Agent("중국")  → 독립 판단   │    │
│  │ sim_save    │    │ Agent("트럼프") → 독립 판단  │    │
│  │ (arbiter)   │    │ (서로 안 보임 — 창발적 행동) │    │
│  └──────┬──────┘    └──────────────────────────────┘    │
│         │                                               │
│         ▼  MCP 도구 호출                                │
│  ┌─────────────────────────────────────────────┐        │
│  │  MCP Server (상태 머신 — LLM 호출 0, API KEY 0)│     │
│  │  위키 검색 / 에이전트 추출 / 상태 추적 / 저장  │     │
│  └──────┬──────────────────────────────────────┘        │
│         │                                               │
│         ▼                                               │
│  ┌─────────────────────────────────────────────┐        │
│  │  wiki/*.md (지식 기반)                       │        │
│  │  이란.md → 에이전트 "이란"의 자아가 됨        │        │
│  │  트럼프.md → 에이전트 "트럼프"의 자아가 됨    │        │
│  │  ... (24개 이중 언어 페이지)                  │        │
│  └─────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────┘
```

**핵심**: API KEY 없음. 외부 서비스 없음. 구독 중인 LLM이 모든 추론을 수행합니다.

## Why Wiki + Simulation

일반적인 LLM 역할극:
```
"너는 이란이야. 행동을 결정해." → 얕고 일반적인 응답
```

우리 시스템:
```
"너는 이란이야. 여기 너에 대한 모든 팩트가 있어:
 - 하메네이가 2/28 사망, 칼리바프 실용파가 실권 장악
 - 강경파는 해협 봉쇄 유지 주장, 개혁파는 외국인 투자 유치 주장
 - 400kg 고농축 우라늄 보유 (핵폭탄 10개 분량)
 - IRGC 현장 사령관이 독자적으로 공격 중 (명령 체계 분열)
 - 중국이 주요 파트너, 걸프 국가들에게 통행료 부과 중
 ..."
→ 위키에 축적된 구체적 팩트 기반의 깊은 추론
```

그리고 위키가 성장할수록 에이전트도 자동으로 풍부해집니다.

## Quick Start

### 1. 설치

```bash
# Python 3.11-3.12 권장
uv pip install --python 3.12 mcp pyyaml

# Claude Code를 이 디렉토리에서 실행하면 MCP 자동 연결
cd /path/to/news
claude
```

### 2. 기사 Ingest

```
> 새 기사 추가했어. ingest 해줘
```

기사를 `raw/` 에 넣으면 → LLM이 5-15개 위키 페이지를 생성/업데이트합니다.

### 3. 시뮬레이션 실행

```
> 호르무즈 해협 봉쇄가 2026년 말까지 지속되면 어떤 일이 벌어질지 시뮬레이션 해줘
```

## Simulation: 상세 사용법

### Mode A: Subagent 시뮬레이션 (추천 — 창발적 행동)

각 에이전트가 **독립된 subagent**로 실행됩니다. 서로의 결정을 볼 수 없어서 진짜 독립적인 판단이 이루어집니다.

```
Step 1  sim_setup(scenario, rounds, slugs)
        → 위키에서 에이전트 자동 추출, 상태 변수 초기화

Step 2  sim_agents_decide()
        → 에이전트별 독립 프롬프트 생성

Step 3  병렬 subagent 생성 (Agent 도구)
        → 이란 agent: "통행료를 올리겠다" (트럼프 결정 모름)
        → 트럼프 agent: "폭격을 재개한다" (이란 결정 모름)
        → 중국 agent: "정상회담을 제안한다" (둘 다 모름)
        ← 창발: 트럼프가 폭격 재개 + 중국이 정상회담 제안 = 예상 못한 충돌

Step 4  sim_advance(combined_actions + state_deltas)
        → 메인 LLM이 Arbiter로서 모든 행동을 종합하여 상태 업데이트

        (Step 2-4를 라운드 수만큼 반복)

Step 5  sim_save(analysis)
        → wiki/simulations/*.md 에 리포트 저장
```

### Mode B: 단일 패스 (빠르지만 창발성 없음)

메인 LLM이 모든 에이전트를 직접 결정합니다. subagent 없이 빠르게 시뮬레이션.

```
Step 1  sim_setup(scenario)
Step 2  sim_advance(all_decisions)  × N 라운드
Step 3  sim_save(analysis)
```

### 커스터마이징

```
# 특정 에이전트만 선택
sim_setup(slugs=["iran", "china", "donald-trump", "gulf-states"])

# 초기 상태 변수 오버라이드
sim_setup(variables={"oil_price_brent": 110.0, "nato_cohesion": 50.0})

# 라운드 수 조절 (1-10, 각 1개월)
sim_setup(rounds=6, start_date="June 2026")
```

### 상태 변수 (10개)

| Variable | 초기값 | 단위 | 설명 |
|----------|--------|------|------|
| oil_price_brent | 95.0 | $/barrel | 브렌트 원유가 |
| hormuz_throughput | 10.0 | ships/day | 호르무즈 해협 일일 선박 통과 |
| nato_cohesion | 30.0 | 0-100 | NATO 결속력 |
| iran_nuclear_progress | 40.0 | 0-100 | 이란 핵무기 진행도 |
| us_credibility | 35.0 | 0-100 | 미국 안보 파트너 신뢰도 |
| gulf_stability | 25.0 | 0-100 | 걸프 국가 안정성 |
| china_influence | 60.0 | 0-100 | 중국 지정학적 영향력 |
| market_stress | 65.0 | 0-100 | 글로벌 금융 시장 스트레스 |
| food_security | 40.0 | 0-100 | 세계 식량 안보 |
| lebanon_tension | 80.0 | 0-100 | 이스라엘-레바논 긴장도 |

## MCP Tools (11개)

### Wiki 도구 (7개)

| Tool | 설명 |
|------|------|
| `wiki_index` | 전체 위키 페이지 목록 (타입별) |
| `wiki_search(query)` | 키워드 검색 (제목/태그/본문) |
| `wiki_read(page)` | 특정 페이지 전문 읽기 |
| `wiki_graph(page, depth)` | 링크 네트워크 매핑 (depth 1-2) |
| `causal_chain(topic)` | 인과 관계 문장 추출 |
| `simulate(scenario, variables)` | 시나리오 컨텍스트 수집 (단일 패스 분석용) |

### Simulation 도구 (5개)

| Tool | 설명 |
|------|------|
| `sim_setup(scenario, rounds, slugs, variables)` | 시뮬레이션 초기화, 에이전트 추출 |
| `sim_agents_decide()` | 에이전트별 독립 프롬프트 생성 (subagent용) |
| `sim_advance(decisions_json)` | 라운드 결정 기록, 상태 업데이트 |
| `sim_save(analysis_json)` | 최종 리포트를 wiki/simulations/에 저장 |
| `sim_status()` | 활성/완료 시뮬레이션 목록 |

## Structure

```
raw/                              # The Economist 원문 기사 (불변)
├── leaders/                      # 사설
├── briefing/                     # 브리핑 (심층 분석)
├── finance-and-economics/        # 금융·경제
├── business/                     # 비즈니스
├── science-and-technology/       # 과학·기술
├── middle-east-and-asia/         # 중동·아시아
├── china/                        # 중국
├── culture/                      # 문화
├── the-world-this-week/          # 금주의 세계
└── the-world-in-brief/           # 일일 브리핑

wiki/                             # LLM이 유지하는 위키 (이중 언어)
├── index.md                      # 전체 목차
├── log.md                        # 작업 기록
├── simulations/                  # 시뮬레이션 결과
└── *.md                          # 24개 entity/event/concept 페이지

mcp_server/                       # MCP 서버 (Python, LLM 호출 없음)
├── server.py                     # 11개 도구 정의
├── wiki_parser.py                # 위키 마크다운 파싱
├── simulation/                   # 다중 에이전트 시뮬레이션 엔진
│   ├── engine.py                 # 상태 머신 (setup → advance → save)
│   ├── agents.py                 # 위키 → 에이전트 페르소나 추출
│   ├── state.py                  # 세계 상태 변수 추적
│   └── report.py                 # 리포트 생성
└── requirements.txt              # mcp, pyyaml
```

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

| Operation | Description |
|-----------|-------------|
| **Ingest** | 새 기사를 `raw/`에 넣고 LLM에게 요청 → 5-15개 위키 페이지 생성/업데이트 |
| **Query** | 위키에 대해 질문 → LLM이 관련 페이지를 읽고 종합 답변 |
| **Simulate** | 시나리오 질문 → 다중 에이전트 시뮬레이션 → 예측 리포트 저장 |
| **Lint** | 위키 건강 점검 → 모순, 고아 페이지, 누락된 교차 참조 탐지 |

## Inspired By

- **[LLM Wiki](llm-wiki.md)** by Andrej Karpathy — 위키 패턴의 원형
- **[MiroFish](https://github.com/666ghj/MiroFish)** — 다중 에이전트 시뮬레이션 엔진의 참조 아키텍처. MiroFish가 독립 LLM 호출로 1000개 에이전트를 시뮬레이션하는 것처럼, 우리는 Claude Code의 subagent를 활용하여 추가 API KEY 없이 동일한 패턴을 구현합니다.

## Tools

- **[Claude Code](https://claude.ai/code)** — 위키 관리 + Orchestrator + Subagent 인프라
- **[Obsidian](https://obsidian.md)** — 위키 브라우징, 그래프 뷰, `[[wikilinks]]` 탐색
- **MCP Server** — 위키 지식을 구조화된 도구로 노출 (Python, 외부 의존성 없음)
- **Git** — 버전 관리, 위키 히스토리 추적
