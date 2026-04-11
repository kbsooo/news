"""Generate bilingual simulation report as wiki page — no LLM calls."""

import re
from datetime import date
from pathlib import Path

from simulation.agents import Agent
from simulation.state import WorldState


WIKI_DIR = Path(__file__).parent.parent.parent / "wiki"
SIM_DIR = WIKI_DIR / "simulations"


# Mapping for auto-generating Korean state variable descriptions
STATE_VAR_KO = {
    "oil_price_brent": "브렌트 원유 가격",
    "hormuz_throughput": "호르무즈 해협 일일 선박 통행",
    "nato_cohesion": "NATO 동맹 결속력",
    "iran_nuclear_progress": "이란 핵무기 진전도",
    "us_credibility": "미국 안보 파트너 신뢰도",
    "gulf_stability": "걸프 국가 안정성",
    "china_influence": "중국 지정학적 영향력",
    "market_stress": "글로벌 금융시장 스트레스",
    "food_security": "글로벌 식량 안보 (100=안전)",
    "lebanon_tension": "이스라엘-레바논 갈등 강도",
}


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:60].rstrip("-")


def _format_en_state_table(state: WorldState) -> str:
    if not state.rounds:
        return "(No rounds completed)"
    first = state.rounds[0].state_before
    last = state.rounds[-1].state_after
    lines = ["| Variable | Initial | Final | Change |", "|----------|---------|-------|--------|"]
    for key, var in state.variables.items():
        i = first.get(key, 0)
        f_val = last.get(key, 0)
        d = f_val - i
        sign = "+" if d >= 0 else ""
        lines.append(f"| {var.description} | {i:.1f} | {f_val:.1f} | {sign}{d:.1f} |")
    return "\n".join(lines)


def _format_ko_state_table(state: WorldState) -> str:
    if not state.rounds:
        return "(라운드 없음)"
    first = state.rounds[0].state_before
    last = state.rounds[-1].state_after
    lines = ["| 변수 | 초기 | 최종 | 변화 |", "|------|------|------|------|"]
    for key, var in state.variables.items():
        i = first.get(key, 0)
        f_val = last.get(key, 0)
        d = f_val - i
        sign = "+" if d >= 0 else ""
        ko_desc = STATE_VAR_KO.get(key, var.description)
        lines.append(f"| {ko_desc} | {i:.1f} | {f_val:.1f} | {sign}{d:.1f} |")
    return "\n".join(lines)


def _format_en_rounds(state: WorldState) -> str:
    lines = []
    for r in state.rounds:
        lines.append(f"\n### Round {r.round_num}: {r.time_label}\n")
        lines.append("**Actions:**")
        for name, action in r.agent_actions.items():
            lines.append(f"- **{name}**: {action.action_type} → {action.description}")
        if r.arbiter_reasoning:
            lines.append(f"\n**Impact:** {r.arbiter_reasoning}")
        changes = []
        for key in r.state_before:
            before = r.state_before[key]
            after = r.state_after.get(key, before)
            if abs(after - before) > 0.5:
                desc = state.variables[key].description if key in state.variables else key
                sign = "+" if after > before else ""
                changes.append(f"{desc}: {sign}{after - before:.1f}")
        if changes:
            lines.append(f"Key changes: {'; '.join(changes)}")
    return "\n".join(lines)


def _format_ko_rounds(state: WorldState) -> str:
    lines = []
    for r in state.rounds:
        lines.append(f"\n### 라운드 {r.round_num}: {r.time_label}\n")
        lines.append("**행동:**")
        for name, action in r.agent_actions.items():
            lines.append(f"- **{name}**: {action.action_type} → {action.description}")
        if r.arbiter_reasoning:
            lines.append(f"\n**영향:** {r.arbiter_reasoning}")
        changes = []
        for key in r.state_before:
            before = r.state_before[key]
            after = r.state_after.get(key, before)
            if abs(after - before) > 0.5:
                ko_desc = STATE_VAR_KO.get(key, state.variables[key].description if key in state.variables else key)
                sign = "+" if after > before else ""
                changes.append(f"{ko_desc}: {sign}{after - before:.1f}")
        if changes:
            lines.append(f"주요 변화: {'; '.join(changes)}")
    return "\n".join(lines)


def generate_report(
    scenario: str,
    agents: list[Agent],
    state: WorldState,
    analysis: str = "",
    analysis_ko: str = "",
    confidence: str = "medium",
) -> Path:
    """Generate bilingual simulation report and save to wiki/simulations/.

    The analysis text (EN + KO) is provided by the host LLM.
    Round-by-round summaries are auto-generated from state data in both languages.
    """
    SIM_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    slug = f"sim-{_slugify(scenario)}-{today}"
    filepath = SIM_DIR / f"{slug}.md"

    agent_names = [a.name for a in agents]
    based_on = list(set(a.slug for a in agents))

    # --- English section ---
    en_agents = "\n".join(f"- **{a.name}** ({a.agent_type})" for a in agents)
    en_state = _format_en_state_table(state)
    en_rounds = _format_en_rounds(state)

    english = f"""# Simulation: {scenario}

## Scenario
{scenario}

## Agents ({len(agents)})
{en_agents}

## Key Variables (Initial → Final)
{en_state}

## Round-by-Round Summary
{en_rounds}

## Analysis
{analysis}

## Confidence: {confidence}

## See Also
{chr(10).join(f'- [[{s}]]' for s in based_on)}"""

    # --- Korean section ---
    ko_agents = "\n".join(f"- **{a.name}** ({a.agent_type})" for a in agents)
    ko_state = _format_ko_state_table(state)
    ko_rounds = _format_ko_rounds(state)

    # Use Korean analysis if provided, otherwise note it's pending
    ko_analysis = analysis_ko if analysis_ko else "(한국어 분석은 호스트 LLM이 제공해야 합니다. sim_save 시 analysis_ko 필드를 포함해주세요.)"

    korean = f"""# 시뮬레이션: {scenario}

## 시나리오
{scenario}

## 행위자 ({len(agents)})
{ko_agents}

## 핵심 변수 (초기 → 최종)
{ko_state}

## 라운드별 요약
{ko_rounds}

## 분석
{ko_analysis}

## 신뢰도: {confidence}"""

    # --- Assemble full file ---
    frontmatter = f"""---
title: "Simulation: {scenario}"
type: simulation
date: {today}
scenario: "{scenario}"
confidence: {confidence}
based_on: {based_on}
rounds: {len(state.rounds)}
agents: {agent_names}
---"""

    content = f"{frontmatter}\n\n{english}\n\n---\n\n{korean}"

    filepath.write_text(content, encoding="utf-8")
    return filepath
