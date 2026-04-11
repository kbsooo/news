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
# Multi-agent simulation tools (no LLM calls — host LLM does all reasoning)
# ---------------------------------------------------------------------------

@mcp.tool()
def sim_setup(
    scenario: str,
    rounds: int = 8,
    slugs: list[str] | None = None,
    variables: dict[str, float] | None = None,
    start_date: str = "May 2026",
) -> str:
    """Initialize a multi-agent geopolitical simulation.

    Reads wiki entity pages, extracts agent personas (no LLM calls),
    sets up world state, and returns everything needed for Round 1.

    YOU (the host LLM) do all the reasoning — this tool just provides
    the structured game board.

    Workflow: sim_setup → [sim_advance × N rounds] → sim_save

    Args:
        scenario: Scenario question, e.g. "What if the Hormuz blockade
                  continues through end of 2026?"
        rounds: Number of rounds (1-10), each ≈ 1 month.
        slugs: Entity page slugs for agents. Default: auto-select
               geopolitical entities.
        variables: Override initial state values, e.g.
                   {"oil_price_brent": 100.0}.
        start_date: Time label for round 1. Default: "May 2026".
    """
    from simulation.engine import setup_simulation
    try:
        return setup_simulation(scenario, rounds, slugs, variables, start_date)
    except Exception as e:
        return f"Setup error: {e}"


@mcp.tool()
def sim_advance(decisions_json: str) -> str:
    """Submit your decisions for the current round and advance.

    YOU decide what each agent does and how state variables change.
    This tool records your decisions and returns the prompt for the
    next round (or a completion summary if done).

    Args:
        decisions_json: JSON string with your decisions:
            {
              "actions": {
                "Agent Name": {
                  "action_type": "negotiate|escalate|...",
                  "target": "who/what",
                  "description": "one sentence"
                }
              },
              "state_deltas": {"oil_price_brent": 5.0, "nato_cohesion": -3.0},
              "reasoning": "Why these changes make sense."
            }
    """
    from simulation.engine import advance_round
    try:
        return advance_round(decisions_json)
    except Exception as e:
        return f"Advance error: {e}"


@mcp.tool()
def sim_save(analysis_json: str) -> str:
    """Save the completed simulation as a wiki report.

    Call this after all rounds are complete. Provide your analysis
    and the report will be saved to wiki/simulations/.

    Args:
        analysis_json: JSON string:
            {
              "analysis": "3-5 paragraphs of your analysis...",
              "confidence": "low|medium|high"
            }
    """
    from simulation.engine import save_report
    try:
        return save_report(analysis_json)
    except Exception as e:
        return f"Save error: {e}"


@mcp.tool()
def sim_status() -> str:
    """Check simulation status — active session and completed reports."""
    from simulation.engine import get_status
    return get_status()


if __name__ == "__main__":
    mcp.run()
