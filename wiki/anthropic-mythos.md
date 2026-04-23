---
title: Anthropic Mythos
type: event
sources:
  - raw/business/260408-mythical-monster.md
  - raw/business/260415-locked-up-models.md
  - raw/science-and-technology/260415-examining-the-mythos.md
  - raw/science-and-technology/260415-how-ai-hackers-will-shake-up-cyber-security.md
updated: 2026-04-23
tags: [ai, cybersecurity, safety, technology]
---

# Anthropic Mythos

On April 7, 2026, Anthropic declared its latest Claude model — "Mythos" — too powerful for wide release. Capabilities are "substantially beyond those of any model we have previously trained."

## Cybersecurity Capabilities

The primary concern: Mythos can find software vulnerabilities and either **fix them** (defender mode) or **exploit them** (hacker mode).

Key findings:
- Found severe vulnerabilities in **"every major operating system and web browser"**
- Including one that had gone **undetected for 27 years**
- Credibility: Apple, Linux Foundation, CrowdStrike, and Google (a direct competitor) all participating in the response

## Project Glasswing

Anthropic's mitigation approach — give defenders a head start:
- Companies can use Mythos to test unpublished code for weaknesses before release
- Anthropic covering first **$100m** of costs
- Will eventually charge **5x more than Opus** for Mythos access
- **12 founder members** including **Apple, Google, Nvidia** (Economist, April 15)
- Expansion announced to **another 40 digital-infrastructure organisations** to harden the software on which the internet depends
- Participants include major software companies across the industry

## Business Context

- Anthropic revenue: **$30bn annualized** (up from $9bn at end of 2025) — on a roll
- Critics note Anthropic built the model, ran the tests, and benefits from the perception of power
- But industry participation suggests the threat is credible

## Project Glasswing Expanded

As exclusivity became a marketing weapon in its own right, Glasswing's perimeter turned into a status symbol:

- **JPMorgan Chase** was the only bank on the initial invite list. Within days, the board of an Asian peer summoned its chief executive to explain how the firm could "swiftly gain access" to Glasswing.
- **OpenAI response, April 14**: Not to be outshone, OpenAI released its own supercharged-hacking system — a tailored version of **GPT-5.4** — to vetted users only. Staggered release of frontier capability is rapidly becoming the norm across the industry.
- **US government reaction**: After Mythos was unveiled, **Scott Bessent** (Treasury Secretary) and **Jerome Powell** (Fed Chair) summoned America's biggest banks to discuss the cyber-security risks posed by AI. The event pulled financial regulators directly into the frontier-AI governance conversation.
- **Pricing signal → infrastructure burden**: Mythos is priced at **5x Opus 4.6**, Anthropic's most powerful publicly available model. That ratio implies Mythos is disproportionately compute-hungry. Anthropic has simultaneously:
  - Introduced **usage limits on Claude** during peak times
  - Shifted **enterprise pricing to consumption-based** billing
  
  Keeping Mythos behind closed doors lets Anthropic induct new customers only as capacity allows — the safety frame and the compute-triage frame converge on the same gated-access strategy. See [[ai-labs-and-industry]] for the broader "model lock-up" pattern.

## Geopolitical Dimensions

### US Government Tension
- Pete Hegseth (Defense Secretary) labeled Anthropic a **"supply-chain risk"** earlier in 2026 after a dispute over military use limits (a judge temporarily blocked the "Orwellian" designation)
- Project Glasswing could **disarm many US cyber-weapons** — the government has long hoarded "zero days" (undiscovered vulnerabilities) for offensive use
- This puts Anthropic and the Pentagon on a collision course

### Open-Source Safety Gap
- Anthropic's rivals (OpenAI, Google) have their own responsible release policies
- **Chinese open-source labs** tend to be less focused on safety
- These will eventually develop similar capabilities — the question is whether defenses are in place by then

## Technical Evaluation — "Jagged" but Advancing (April 15 deeper dive)

### AI Security Institute (UK government agency) test results
- Mythos was **neck-and-neck** with other models on relatively simple cyber-security tests
- But **noticeably ahead** in an advanced test that requires dozens of steps before successfully taking over a target machine
- **Verdict**: step-change in **multi-step agentic cyber-capability**, not raw bug-finding

### Is Mythos really revolutionary or evolutionary?
- A "vigorous debate" is raging online
- **Stanislav Fort** (Aisle, AI cyber-security startup): **used several smaller, older models to find the same FreeBSD bug** — the AI cyber-security frontier is "**jagged**", with no model having a clear edge
- But the state of the art is advancing quickly — "**One change I've noticed in the past couple of months is that a lot of these AI-generated bug reports are increasingly of good quality**" (Bruce Schneier)

### Concrete AI-found fixes already in production
- **OpenSSL update (January 2026)**: **fixed a dozen security flaws** found by AI models employed by Fort's firm
- **Firefox (2025)**: an older, **pre-Mythos Claude** found **~20% of all high-severity bugs fixed** that year
- Mythos found "thousands" of high- or critical-severity flaws (most kept secret until fixed), including:
  - One in **FreeBSD** (comprehensible enough that other AI models found it too)
  - One in **FFmpeg** (video-and-audio library)
  - One in **cloud-computing software — still unfixed** at publication

## The Cost Problem

- One Mythos bug cost Anthropic **nearly $20,000-worth of tokens to find**
- **Linux** (partly volunteer-maintained): prohibitive cost
- **Home routers, smart gadgets (TVs, fridges), industrial machinery**: mostly **nobody maintains this code at all** — "attackers could have a field day"

The defender asymmetry is compute-budget-gated: rich maintainers can afford AI hardening; everyone else is exposed.

## Optimistic Long-Term View

All researchers The Economist interviewed for the April 15 piece agreed: in the **long run**, AI-enabled hacking will probably **help defenders more than attackers** by allowing more thorough pre-publication code checks. But Schneier qualifies: "**In the medium term I think this will be a mess. But in the long run I think it will actually be good for the defenders.**"

## Connection to Broader AI Trends

This is a step-change in the [[ai-in-mathematics|AI capability]] trajectory. Where AI in mathematics shows the constructive potential of advanced reasoning, Mythos demonstrates the dual-use danger: the same capability that can verify proofs can also find exploits. The [[great-power-rivalry]] dimension is immediate — AI as both shield and weapon.

## See Also
- [[ai-in-mathematics]]
- [[great-power-rivalry]]

---

# Anthropic Mythos (한국어)

2026년 4월 7일, Anthropic은 최신 Claude 모델인 "Mythos"가 광범위한 공개에는 너무 강력하다고 선언했다. 해당 모델의 능력은 "이전에 훈련한 어떤 모델보다도 실질적으로 뛰어나다(substantially beyond)"고 밝혔다.

## 사이버보안 역량

핵심 우려 사항: Mythos는 소프트웨어 취약점을 찾아내어 **수정**(방어 모드)하거나 **악용**(해커 모드)할 수 있다.

주요 발견:
- **"모든 주요 운영체제와 웹 브라우저"**에서 심각한 취약점을 발견
- 그중 하나는 **27년간 탐지되지 않았던** 취약점
- 신뢰성: Apple, Linux Foundation, CrowdStrike, 그리고 직접적 경쟁사인 Google까지 대응에 참여

## 프로젝트 Glasswing

Anthropic의 완화 전략 — 방어자에게 선제적 우위를 제공:
- 기업들이 Mythos를 활용해 미공개 코드의 취약점을 출시 전에 테스트 가능
- Anthropic이 초기 **1억 달러($100m)**의 비용을 부담
- 향후 Mythos 접근 비용은 **Opus의 5배**로 책정 예정
- 업계 전반의 주요 소프트웨어 기업들이 참여

## 비즈니스 맥락

- Anthropic 매출: **연간 300억 달러($30bn)** (2025년 말 90억 달러에서 성장) — 급성장 중
- 비평가들은 Anthropic이 모델을 직접 만들고, 테스트를 수행하고, 그 강력함에 대한 인식으로부터 이익을 얻는다고 지적
- 그러나 업계의 참여는 위협이 실질적임을 시사

## 프로젝트 Glasswing 확장

배타성 자체가 마케팅 무기로 작동하면서, Glasswing의 울타리는 일종의 지위 상징으로 변했다:

- **JPMorgan Chase**가 최초 초청 명단에 포함된 유일한 은행. 며칠 뒤 한 아시아 은행의 이사회가 CEO를 소환해 자신들도 어떻게 "신속히 Glasswing에 접근"할 수 있는지를 설명하라고 요구했다.
- **OpenAI의 대응, 4월 14일**: 뒤질세라 OpenAI도 자체 초강력 해킹 시스템을 공개 — 지난달 출시한 **GPT-5.4** 모델의 맞춤형 버전을 검증된 사용자에게만 제공. 프론티어 역량의 단계적(staggered) 공개가 업계 표준으로 빠르게 굳어지고 있다.
- **미국 정부 반응**: Mythos 공개 이후 **Scott Bessent**(재무장관)와 **Jerome Powell**(연준 의장)은 미국 대형 은행들을 소집해 AI의 사이버보안 위험을 논의했다. 이로써 금융 규제당국도 프론티어 AI 거버넌스 논의의 당사자로 끌려들어왔다.
- **가격 신호 → 인프라 부담**: Mythos는 Anthropic의 공개된 최강 모델인 **Opus 4.6의 5배** 가격으로 책정됐다. 이 비율은 Mythos가 비정상적으로 컴퓨팅 자원을 많이 소비한다는 것을 시사한다. Anthropic은 동시에:
  - 피크 시간대에 **Claude 사용량 한도**를 도입
  - **기업용 가격 체계를 사용량 기반(consumption-based)** 으로 전환
  
  Mythos를 폐쇄된 문 뒤에 두면 Anthropic은 용량이 허용할 때만 신규 고객을 받아들일 수 있다 — 안전성 프레임과 컴퓨팅 자원 분배(triage) 프레임이 동일한 제한 접근 전략으로 수렴한다. 보다 넓은 "모델 잠금(model lock-up)" 패턴은 [[ai-labs-and-industry|AI 연구소와 산업]] 참조.

## 지정학적 차원

### 미국 정부와의 긴장
- Pete Hegseth(국방장관)는 군사적 사용 제한에 관한 분쟁 이후 2026년 초 Anthropic을 **"공급망 위험(supply-chain risk)"**으로 규정 (판사가 이 "오웰적" 지정을 일시적으로 차단)
- 프로젝트 Glasswing은 **다수의 미국 사이버 무기를 무력화**할 수 있음 — 정부는 오랫동안 공격용으로 "제로데이"(미발견 취약점)를 비축해 왔음
- 이는 Anthropic과 펜타곤을 정면충돌 경로에 놓음

### 오픈소스 안전성 격차
- Anthropic의 경쟁사(OpenAI, Google)는 자체적인 책임 있는 출시 정책을 보유
- **중국의 오픈소스 연구소**는 안전성에 대한 관심이 상대적으로 낮은 경향
- 이들도 결국 유사한 역량을 개발할 것 — 문제는 그때까지 방어 체계가 갖춰져 있느냐 여부

## 기술 평가 — "들쭉날쭉"하지만 진보 중 (4월 15일 심층)

### AI 보안 연구소(AISI, 영국 정부 기관) 테스트 결과
- Mythos는 비교적 단순한 사이버보안 테스트에서는 다른 모델과 **막상막하**
- 그러나 목표 기기를 성공적으로 장악하기 위해 수십 단계를 완료해야 하는 고급 테스트에서는 **뚜렷이 앞섬**
- **판단**: 원시 버그 발견보다 **다단계 에이전틱 사이버 역량**의 단계 변화

### Mythos는 정말 혁명적인가 점진적인가?
- 온라인에서 "격렬한 토론" 진행 중
- **Stanislav Fort**(Aisle, AI 사이버보안 스타트업): **여러 더 작고 오래된 모델로 같은 FreeBSD 버그 발견** — AI 사이버보안 프론티어는 "**들쭉날쭉(jagged)**", 어느 모델도 명확한 우위 없음
- 그러나 최첨단은 빠르게 진보 — "**지난 몇 달간 내가 주목한 변화는 AI 생성 버그 보고가 점점 질이 좋아지고 있다는 것**"(Bruce Schneier)

### 이미 프로덕션에 적용된 AI 발견 수정
- **OpenSSL 업데이트(2026년 1월)**: Fort 회사가 고용한 AI 모델이 찾은 **12개 보안 결함 수정**
- **Firefox(2025)**: **Mythos 이전 Claude**가 그해 수정된 **고심각도 버그의 약 20%** 발견
- Mythos는 고·중대 심각도 결함을 "수천 개" 발견(대부분 수정 전까지 비공개), 공개된 것:
  - **FreeBSD** 한 개(다른 AI 모델도 발견할 만큼 이해 가능)
  - **FFmpeg** 한 개(비디오·오디오 라이브러리)
  - **클라우드 컴퓨팅 소프트웨어 한 개 — 발표 시점 미수정**

## 비용 문제

- Mythos 버그 하나에 **거의 $20,000 상당의 토큰** 소비
- **Linux**(부분 자원봉사 유지 관리): 비용 부담 불가능
- **가정용 라우터, 스마트 기기(TV, 냉장고), 산업용 기계**: 대부분 **아무도 코드를 유지 관리하지 않음** — "공격자들에게 '봄철'이 될 수 있음"

방어자 비대칭은 컴퓨팅 예산에 의해 게이팅됨: 부유한 유지 관리자는 AI 강화를 감당 가능, 나머지는 노출.

## 장기 낙관론

The Economist가 4월 15일 기사를 위해 인터뷰한 모든 연구자들이 동의: **장기적으로** AI 지원 해킹은 **방어자에게 공격자보다 더 유리**할 것, 출판 전 코드 검사를 더 철저히 할 수 있게 해줌. 단 Schneier가 조건: "**중기적으로는 난장판이 될 것이다. 하지만 장기적으로는 방어자에게 유리할 것이다.**"

## 광범위한 AI 트렌드와의 연결

이는 [[ai-in-mathematics|AI 역량]] 궤적에서의 단계적 변화다. 수학 분야의 AI가 고급 추론의 건설적 잠재력을 보여준다면, Mythos는 이중 용도의 위험을 입증한다: 증명을 검증할 수 있는 동일한 능력이 취약점을 찾아내는 데도 쓰일 수 있다. [[great-power-rivalry|강대국 경쟁]] 차원은 즉각적이다 — AI는 방패이자 무기다.
