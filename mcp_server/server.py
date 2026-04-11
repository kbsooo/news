"""MCP server exposing world news wiki as structured tools for simulation and prediction."""

import json
from mcp.server.fastmcp import FastMCP

from wiki_parser import (
    load_page,
    list_pages,
    search_pages,
    extract_wikilinks,
    extract_english_section,
    extract_causal_sentences,
    build_link_graph,
)

mcp = FastMCP("world-wiki")


@mcp.tool()
def wiki_index() -> str:
    """Return a structured overview of all wiki pages, grouped by type.

    Use this to get an overview of what knowledge is available before
    searching or reading specific pages.
    """
    pages = list_pages(exclude={"index", "log"})
    # Exclude simulation pages from main index grouping — they go in their own section
    by_type: dict[str, list] = {}
    for p in pages:
        t = p.type or "uncategorized"
        by_type.setdefault(t, []).append(p)

    lines = ["# Wiki Index\n"]
    for typ in ["entity", "event", "concept", "simulation", "synthesis", "uncategorized"]:
        group = by_type.get(typ, [])
        if not group:
            continue
        lines.append(f"\n## {typ.title()} ({len(group)})\n")
        for p in group:
            tags = ", ".join(p.tags) if p.tags else ""
            lines.append(f"- **{p.title}** (`{p.slug}`) [{tags}] — updated {p.updated}")
    return "\n".join(lines)


@mcp.tool()
def wiki_search(query: str) -> str:
    """Search wiki pages by keyword across titles, tags, and content.

    Args:
        query: Search term (case-insensitive). Searches page titles, tags, slugs, and body text.

    Returns matching pages with relevant context lines.
    """
    results = search_pages(query)
    if not results:
        return f"No results for '{query}'."

    lines = [f"# Search results for '{query}' ({len(results)} pages)\n"]
    for page, matches in results:
        lines.append(f"\n## {page.title} (`{page.slug}`) — {page.type}")
        for m in matches:
            lines.append(f"  - {m}")
    return "\n".join(lines)


@mcp.tool()
def wiki_read(page: str) -> str:
    """Read a specific wiki page by slug (filename without .md).

    Args:
        page: Page slug, e.g. 'iran', 'great-power-rivalry', 'iran-war-and-ceasefire-2026'.

    Returns the full English content including frontmatter summary.
    """
    p = load_page(page)
    if not p:
        return f"Page '{page}' not found. Use wiki_index() or wiki_search() to find available pages."

    english = extract_english_section(p.content)
    header = (
        f"# {p.title}\n"
        f"Type: {p.type} | Updated: {p.updated}\n"
        f"Tags: {', '.join(p.tags)}\n"
        f"Sources: {len(p.sources)} articles\n"
    )
    return f"{header}\n{english}"


@mcp.tool()
def wiki_graph(page: str, depth: int = 1) -> str:
    """Map the link network around a wiki page.

    Extracts [[wikilinks]] from the page and its neighbors to show
    how topics connect. Useful for understanding relationship networks
    before running simulations.

    Args:
        page: Starting page slug.
        depth: How many link-hops to follow (1 = direct links, 2 = links of links). Max 2.
    """
    depth = min(depth, 2)
    graph = build_link_graph(page, depth)
    if not graph:
        return f"Page '{page}' not found."

    lines = [f"# Link graph from '{page}' (depth={depth})\n"]
    for node, links in graph.items():
        p = load_page(node)
        label = p.title if p else node
        lines.append(f"\n## {label} (`{node}`)")
        if links:
            for link in links:
                lp = load_page(link)
                ll = lp.title if lp else link
                lines.append(f"  → {ll} (`{link}`)")
        else:
            lines.append("  (no outgoing links)")

    # Summary stats
    all_nodes = set(graph.keys())
    for v in graph.values():
        all_nodes.update(v)
    lines.append(f"\n---\nTotal nodes: {len(all_nodes)} | Total edges: {sum(len(v) for v in graph.values())}")
    return "\n".join(lines)


@mcp.tool()
def causal_chain(topic: str) -> str:
    """Extract causal relationships related to a topic from wiki pages.

    Searches for the topic, reads related pages, and extracts sentences
    containing causal language (→, caused by, led to, etc.).

    Args:
        topic: Topic to trace causal chains for, e.g. 'hormuz blockade', 'fertiliser crisis'.
    """
    results = search_pages(topic, max_results=8)
    if not results:
        return f"No pages found related to '{topic}'."

    lines = [f"# Causal chains related to '{topic}'\n"]
    all_causal: list[tuple[str, str]] = []

    for page, _ in results:
        causal = extract_causal_sentences(page.content)
        if causal:
            all_causal.extend((page.title, s) for s in causal)

    if not all_causal:
        lines.append("No explicit causal language found. Try reading the pages directly with wiki_read().")
    else:
        lines.append(f"Found {len(all_causal)} causal statements across {len(results)} pages:\n")
        current_source = ""
        for source, sentence in all_causal:
            if source != current_source:
                lines.append(f"\n## From: {source}\n")
                current_source = source
            lines.append(f"- {sentence}")

    # Also show which pages are connected
    lines.append(f"\n---\n## Related pages")
    for page, _ in results:
        lines.append(f"- {page.title} (`{page.slug}`)")
    return "\n".join(lines)


@mcp.tool()
def simulate(scenario: str, variables: list[str] | None = None) -> str:
    """Gather wiki context for a scenario simulation.

    Collects all relevant wiki knowledge for a given scenario question,
    organizes it by causal relevance, and returns a structured context
    package that the LLM can use for reasoning and prediction.

    The LLM (Claude) performs the actual analysis — this tool provides
    the structured knowledge base.

    Args:
        scenario: Natural language scenario question, e.g.
                  "What if the Hormuz blockade continues through 2026?"
        variables: Optional list of key variables to focus on, e.g.
                   ["oil price", "food security", "NATO alliance"]
    """
    variables = variables or []

    # Extract keywords from scenario for search
    # Remove common words and search for meaningful terms
    stop_words = {
        "what", "if", "the", "how", "will", "would", "could", "does",
        "when", "where", "why", "is", "are", "was", "were", "been",
        "through", "until", "about", "from", "into", "with", "that",
        "this", "than", "then", "for", "and", "but", "not", "can",
    }
    words = scenario.lower().split()
    keywords = [w.strip("?.,!") for w in words if w.strip("?.,!") not in stop_words and len(w) > 2]

    # Search for each keyword and collect unique pages
    seen_slugs: set[str] = set()
    relevant_pages = []
    for kw in keywords + variables:
        for page, matches in search_pages(kw, max_results=5):
            if page.slug not in seen_slugs:
                seen_slugs.add(page.slug)
                relevant_pages.append((page, matches))

    if not relevant_pages:
        return (
            f"No relevant wiki pages found for scenario: '{scenario}'\n"
            "Try rephrasing or check wiki_index() for available topics."
        )

    # Build the simulation context
    lines = [
        f"# Simulation Context",
        f"## Scenario: {scenario}\n",
    ]

    if variables:
        lines.append(f"## Key Variables: {', '.join(variables)}\n")

    lines.append(f"## Relevant Knowledge ({len(relevant_pages)} pages)\n")

    # Collect causal sentences across all relevant pages
    all_causal: list[tuple[str, str]] = []

    for page, _ in relevant_pages:
        english = extract_english_section(page.content)
        links = extract_wikilinks(english)
        causal = extract_causal_sentences(page.content)

        lines.append(f"\n### {page.title} (`{page.slug}`) — {page.type}")
        lines.append(f"Tags: {', '.join(page.tags)}")
        lines.append(f"Links to: {', '.join(links[:10])}")

        # Include key content (first ~40 lines of English section)
        content_lines = english.split("\n")[:40]
        lines.append("\n**Key content:**")
        lines.append("\n".join(content_lines))

        if causal:
            all_causal.extend((page.title, s) for s in causal[:5])

    # Causal chain summary
    if all_causal:
        lines.append(f"\n---\n## Causal Statements ({len(all_causal)} found)\n")
        for source, sentence in all_causal:
            lines.append(f"- [{source}] {sentence}")

    # Instructions for the LLM
    lines.append(
        "\n---\n## Instructions for Analysis\n"
        "Using the above wiki knowledge, analyze the scenario by:\n"
        "1. Identifying the primary causal chains affected\n"
        "2. Tracing second and third-order effects\n"
        "3. Considering each key actor's likely response (based on their wiki profiles)\n"
        "4. Assessing confidence levels for each projection\n"
        "5. Flagging key uncertainties and pivot points\n"
        "6. Providing a timeline of expected developments\n"
        "\n"
        "Save the result as a bilingual (EN/KO) simulation page in wiki/simulations/."
    )

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Multi-agent simulation tools
# ---------------------------------------------------------------------------

@mcp.tool()
def sim_agents(scenario: str = "", slugs: list[str] | None = None) -> str:
    """Preview agents that would participate in a simulation.

    Extracts agent personas from wiki entity pages using LLM analysis.
    Use this to review agents before running a full sim_run().

    Requires env vars: LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_NAME

    Args:
        scenario: Optional scenario context to focus agent extraction.
        slugs: Optional list of specific page slugs to use as agents.
               Default: auto-select geopolitical entities.
    """
    try:
        from simulation import extract_agents
    except ImportError:
        return "Error: simulation package not found. Check mcp_server/simulation/ directory."

    try:
        agents = extract_agents(slugs=slugs, scenario_context=scenario)
    except Exception as e:
        return f"Error extracting agents: {e}"

    if not agents:
        return "No agents extracted. Check that wiki has entity pages with geopolitical tags."

    lines = [f"# Simulation Agents ({len(agents)})\n"]
    for a in agents:
        lines.append(f"## {a.name} (`{a.slug}`) — {a.agent_type}")
        lines.append(a.to_prompt_block())
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def sim_run(
    scenario: str,
    rounds: int = 8,
    slugs: list[str] | None = None,
    variables: dict[str, float] | None = None,
    start_date: str = "May 2026",
) -> str:
    """Run a multi-agent geopolitical simulation.

    Extracts agent personas from wiki, runs multi-round simulation where
    each agent makes decisions that affect world state variables, and
    generates a bilingual report in wiki/simulations/.

    Requires env vars: LLM_API_KEY, LLM_BASE_URL, LLM_MODEL_NAME
    Token budget: ~150K tokens for 8 agents × 8 rounds.

    Args:
        scenario: The scenario question, e.g.
                  "What if the Hormuz blockade continues through 2026?"
        rounds: Number of simulation rounds (1-10). Each round ≈ 1 month.
        slugs: Wiki entity page slugs to use as agents. Default: auto-select.
        variables: Override initial state variable values, e.g.
                   {"oil_price_brent": 100.0}.
        start_date: Starting time label for round 1. Default: "May 2026".
    """
    try:
        from simulation import run_simulation
    except ImportError:
        return "Error: simulation package not found."

    try:
        report_path, final_state, agents = run_simulation(
            scenario=scenario,
            rounds=rounds,
            slugs=slugs,
            variable_overrides=variables,
            start_date=start_date,
        )
    except Exception as e:
        return f"Simulation error: {e}"

    # Summary for Claude
    agent_names = ", ".join(a.name for a in agents)
    snap = final_state.snapshot()
    state_summary = "\n".join(
        f"  - {final_state.variables[k].description}: {v:.1f}"
        for k, v in snap.items()
    )

    return (
        f"# Simulation Complete\n\n"
        f"**Scenario:** {scenario}\n"
        f"**Agents:** {agent_names}\n"
        f"**Rounds:** {len(final_state.rounds)}\n"
        f"**Report saved:** `{report_path.relative_to(report_path.parent.parent.parent)}`\n\n"
        f"## Final State\n{state_summary}\n\n"
        f"Read the full report with `wiki_read` or open in Obsidian."
    )


@mcp.tool()
def sim_status() -> str:
    """List completed simulations in wiki/simulations/.

    Returns metadata for each simulation report that has been generated.
    """
    from pathlib import Path
    sim_dir = Path(__file__).parent.parent / "wiki" / "simulations"
    if not sim_dir.exists():
        return "No simulations directory found."

    files = sorted(sim_dir.glob("*.md"))
    if not files:
        return "No simulations have been run yet."

    lines = [f"# Completed Simulations ({len(files)})\n"]
    for f in files:
        # Try to extract scenario from frontmatter
        text = f.read_text(encoding="utf-8")
        scenario = "Unknown"
        sim_date = "Unknown"
        for line in text.split("\n")[:15]:
            if line.startswith("scenario:"):
                scenario = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("date:"):
                sim_date = line.split(":", 1)[1].strip()
        lines.append(f"- **{f.stem}** ({sim_date}): {scenario}")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
