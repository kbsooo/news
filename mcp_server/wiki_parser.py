"""Wiki markdown parsing utilities for the MCP server."""

import re
import yaml
from pathlib import Path
from dataclasses import dataclass, field


WIKI_DIR = Path(__file__).parent.parent / "wiki"

CAUSAL_PATTERNS = re.compile(
    r"→|->|caused by|led to|as a result|resulting in|triggered|"
    r"because of|due to|which meant|forcing|prompting|enabling|"
    r"driving|fueling|exacerbating|undermining|accelerating",
    re.IGNORECASE,
)

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


@dataclass
class WikiPage:
    path: Path
    slug: str
    title: str = ""
    type: str = ""
    tags: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    updated: str = ""
    content: str = ""
    frontmatter: dict = field(default_factory=dict)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from a markdown file."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    body = parts[2].strip()
    return fm, body


def load_page(slug: str) -> WikiPage | None:
    """Load a single wiki page by slug (filename without .md)."""
    path = WIKI_DIR / f"{slug}.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    return WikiPage(
        path=path,
        slug=slug,
        title=fm.get("title", slug),
        type=fm.get("type", ""),
        tags=fm.get("tags", []),
        sources=fm.get("sources", []),
        updated=str(fm.get("updated", "")),
        content=body,
        frontmatter=fm,
    )


def list_pages(exclude: set[str] | None = None) -> list[WikiPage]:
    """List all wiki pages, optionally excluding some slugs."""
    exclude = exclude or set()
    pages = []
    for f in sorted(WIKI_DIR.glob("*.md")):
        slug = f.stem
        if slug in exclude:
            continue
        page = load_page(slug)
        if page:
            pages.append(page)
    return pages


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[wikilink]] targets from text."""
    return list(dict.fromkeys(WIKILINK_RE.findall(text)))


def extract_english_section(body: str) -> str:
    """Extract only the English section (before the --- separator for Korean)."""
    # Split on horizontal rule that separates EN/KO sections
    # The separator is a line that is just "---" preceded by a blank line
    lines = body.split("\n")
    english_lines = []
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            # Check if the next non-empty line starts with # and contains Korean
            rest = "\n".join(lines[i + 1 :]).strip()
            if rest and re.match(r"^#\s+.*[\uac00-\ud7a3]", rest):
                break
        english_lines.append(line)
    return "\n".join(english_lines).strip()


def search_pages(query: str, max_results: int = 10) -> list[tuple[WikiPage, list[str]]]:
    """Search wiki pages by keyword. Returns (page, matching_lines) pairs."""
    query_lower = query.lower()
    results = []
    for page in list_pages(exclude={"index", "log"}):
        english = extract_english_section(page.content)
        matches = []
        for line in english.split("\n"):
            if query_lower in line.lower():
                matches.append(line.strip())
        # Also match on title, tags, slug
        if query_lower in page.title.lower() or query_lower in page.slug:
            if not matches:
                matches.append(f"(matched on title/slug: {page.title})")
        if any(query_lower in t.lower() for t in page.tags):
            if not matches:
                matches.append(f"(matched on tag)")
        if matches:
            results.append((page, matches[:5]))
    results.sort(key=lambda x: len(x[1]), reverse=True)
    return results[:max_results]


def extract_causal_sentences(text: str) -> list[str]:
    """Extract lines/sentences that contain causal language."""
    english = extract_english_section(text)
    causal = []
    # Process line-by-line (wiki content is mostly bullet/line-based)
    for line in english.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Strip markdown bullet prefix for matching
        clean = re.sub(r"^[-*]\s+(\*\*.*?\*\*:?\s*)?", "", line)
        if CAUSAL_PATTERNS.search(clean) and len(clean) > 20:
            causal.append(line)
    return causal


def build_link_graph(slug: str, depth: int = 1) -> dict[str, list[str]]:
    """Build a link graph starting from a page, up to a given depth."""
    graph: dict[str, list[str]] = {}
    visited: set[str] = set()
    queue = [(slug, 0)]
    while queue:
        current, d = queue.pop(0)
        if current in visited or d > depth:
            continue
        visited.add(current)
        page = load_page(current)
        if not page:
            continue
        links = extract_wikilinks(extract_english_section(page.content))
        graph[current] = links
        if d < depth:
            for link in links:
                if link not in visited:
                    queue.append((link, d + 1))
    return graph
