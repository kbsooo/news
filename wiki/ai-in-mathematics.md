---
title: AI in Mathematics
type: concept
sources:
  - raw/science-and-technology/260408-strength-in-numbers.md
updated: 2026-04-11
tags: [ai, mathematics, proof-verification, technology]
---

# AI in Mathematics

## The Core Problem: Trust

Mathematics has a "core bottleneck" — trust (Patrick Shafto, DARPA). Before a conclusion can become a proof, every step must be painstakingly checked. Thomas Hales's 1998 sphere-packing proof took over a decade of verification. AI could drastically accelerate this formalisation process.

## How LLMs Do Math

LLMs work through mathematical logic fundamentally differently from humans. Humans devise a plan of attack; LLMs run as a "stream of consciousness" (Terence Tao) — choosing next steps based on what they think should come next, not future goals. More "improv dialogue" than "scripted text." Despite this, they have recently solved long-standing open questions and novel problems.

## Key Players

### Google DeepMind
- **AlphaEvolve**: Generates proofs for optimization problems. Accessible via natural language — non-experts can work with it.
- **DeepThink AI**: Can adequately explain its reasoning (per Tao).

### Harmonic (US startup)
- **Aristotle bot**: Verifies proofs by translating them into Lean (open-source formal math language). Fixes small errors, fills in skipped steps. Result: airtight proof following the original's principles.

### Math, Inc.
- **Gauss model**: Converts human proofs to Lean code. Successfully formalised Viazovska's 8-dimensional and 24-dimensional sphere-packing proofs (originally proved 2016) within weeks.

### DARPA
- Dr. Shafto's team: Automating translation between natural language and formal languages (Lean). Goal: unify "a hot mess of papers, textbooks and human heads" into a navigable body of work.

### Notable: Knuth + Claude
Donald Knuth (Stanford) used Claude Opus 4.6 (Anthropic) on a travelling-salesman variant. Claude solved the odd-number case using several approaches but malfunctioned on the even-number case. Knuth was nonetheless impressed. Another researcher later solved the even case using ChatGPT 5.4 Pro.

## Current Limitations

1. **No transfer learning**: LLMs struggle to apply lessons from one problem to another
2. **No aesthetic sense**: Human mathematicians seek neater proofs that yield surprising results — "quite difficult for AI to emulate" (Timothy Gowers, Cambridge)
3. **Unreliability**: Models can malfunction unexpectedly (Knuth's experience)
4. **Expertise still needed**: "The AI makes mistakes, and you have to be able to figure out where" (Shafto)

## Future Potential

A model retaining the mathematical corpus could make new connections long eluding humans. Mathematical reasoning ability could transfer to economics, physics, and other quantitative fields. "The real challenge for humans will be finding the next set of problems worth tackling" (Pushmeet Kohli, DeepMind).

## Connection to Broader Trends

AI's acceleration of mathematical progress is one domain-specific instance of a broader pattern. In [[great-power-rivalry]], AI is noted as a factor that could shrink military decision time from weeks to minutes — the same underlying capability (rapid pattern processing) applied to a far more dangerous domain.

## See Also
- [[great-power-rivalry]] (AI compressing decision time)

---

# 수학에서의 AI

## 핵심 문제: 신뢰

수학에는 "핵심 병목"이 존재한다 — 바로 신뢰이다(Patrick Shafto, DARPA). 결론이 증명으로 인정받으려면 모든 단계를 꼼꼼히 검증해야 한다. Thomas Hales의 1998년 구 충전 증명(sphere-packing proof)은 검증에만 10년 이상이 걸렸다. AI는 이러한 형식화 과정을 획기적으로 가속할 수 있다.

## LLM은 어떻게 수학을 하는가

LLM은 인간과 근본적으로 다른 방식으로 수학적 논리를 처리한다. 인간은 공략 계획을 세우지만, LLM은 "의식의 흐름"처럼 작동한다(Terence Tao) — 미래 목표가 아니라 다음에 무엇이 와야 할지를 기반으로 다음 단계를 선택한다. "대본 있는 연극"보다는 "즉흥 대화"에 가깝다. 그럼에도 불구하고, 최근 오랫동안 풀리지 않던 미해결 문제와 새로운 문제들을 해결해냈다.

## 주요 플레이어

### Google DeepMind
- **AlphaEvolve**: 최적화 문제에 대한 증명을 생성한다. 자연어로 접근 가능하여 비전문가도 활용할 수 있다.
- **DeepThink AI**: 자신의 추론 과정을 적절히 설명할 수 있다(Tao 평가).

### Harmonic (미국 스타트업)
- **Aristotle 봇**: 증명을 Lean(오픈소스 형식 수학 언어)으로 번역하여 검증한다. 작은 오류를 수정하고 생략된 단계를 채운다. 결과: 원본의 원칙을 따르는 빈틈없는 증명.

### Math, Inc.
- **Gauss 모델**: 인간의 증명을 Lean 코드로 변환한다. Viazovska의 8차원 및 24차원 구 충전 증명(원래 2016년에 증명됨)을 몇 주 만에 성공적으로 형식화했다.

### DARPA
- Shafto 박사 팀: 자연어와 형식 언어(Lean) 간 번역 자동화. 목표: "논문, 교과서, 인간의 머릿속에 흩어진 혼돈"을 탐색 가능한 체계적 지식으로 통합하는 것.

### 주목할 사례: Knuth + Claude
Donald Knuth(Stanford)는 외판원 문제의 변형에 Claude Opus 4.6(Anthropic)을 사용했다. Claude는 여러 접근법을 동원해 홀수 경우를 풀었지만, 짝수 경우에서는 오작동했다. Knuth는 그럼에도 깊은 인상을 받았다. 이후 다른 연구자가 ChatGPT 5.4 Pro를 사용해 짝수 경우를 풀었다.

## 현재의 한계

1. **전이 학습 부재**: LLM은 한 문제에서 얻은 교훈을 다른 문제에 적용하는 데 어려움을 겪는다
2. **미적 감각 부재**: 인간 수학자는 놀라운 결과를 이끌어내는 더 깔끔한 증명을 추구한다 — "AI가 모방하기 상당히 어려운 부분"(Timothy Gowers, Cambridge)
3. **신뢰성 부족**: 모델이 예기치 않게 오작동할 수 있다(Knuth의 경험)
4. **전문성 여전히 필요**: "AI는 실수를 하고, 어디서 실수했는지 파악할 수 있어야 한다"(Shafto)

## 미래 가능성

수학 전체 자료를 보유한 모델은 오랫동안 인간이 발견하지 못한 새로운 연결고리를 찾아낼 수 있다. 수학적 추론 능력은 경제학, 물리학, 기타 정량적 분야로 전이될 수 있다. "인간에게 진정한 도전은 다음에 풀어야 할 가치 있는 문제를 찾는 것이 될 것이다"(Pushmeet Kohli, DeepMind).

## 더 넓은 흐름과의 연결

AI가 수학의 발전을 가속하는 것은 더 광범위한 패턴의 한 분야별 사례이다. [[great-power-rivalry]]에서 AI는 군사적 의사결정 시간을 몇 주에서 몇 분으로 단축할 수 있는 요소로 언급된다 — 동일한 근본 역량(빠른 패턴 처리)이 훨씬 더 위험한 영역에 적용된 것이다.
