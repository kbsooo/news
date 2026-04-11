# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a **world news knowledge wiki** following the [LLM Wiki pattern](llm-wiki.md). The goal is to curate high-quality global news, organize it into an interlinked wiki, find relationships between events, and build understanding of global trends to better anticipate the future.

The human curates sources and directs analysis. The LLM maintains the wiki — summarizing, cross-referencing, updating, and synthesizing.

## Architecture

Three layers:

- **`raw/`** — Immutable source articles from **The Economist**. Organized by category subdirectories that mirror The Economist's sections (e.g., `leaders/`, `finance-and-economics/`, `middle-east-and-asia/`, `culture/`, `science-and-technology/`). Named as `YYMMDD-slug.md` (e.g., `260410-the-price-of-passage.md`). Never modify these.
- **`wiki/`** — LLM-generated and LLM-maintained markdown pages. Entity pages, concept pages, topic summaries, comparisons, synthesis. All interlinked with `[[wikilinks]]`. The LLM owns this layer entirely.
- **`CLAUDE.md`** (this file) — Schema and conventions governing how the wiki operates.

## Wiki Conventions

### Page Types
- **Entity pages**: Countries, organizations, people, treaties (e.g., `iran.md`, `donald-trump.md`, `unclos.md`)
- **Concept pages**: Recurring themes and dynamics (e.g., `nationalism-and-great-power-rivalry.md`, `ai-in-mathematics.md`)
- **Event pages**: Specific events or developments (e.g., `iran-war-ceasefire-2026.md`)
- **Synthesis pages**: Cross-cutting analysis connecting multiple topics (e.g., `global-power-shifts-q2-2026.md`)

### Page Format
```markdown
---
title: Page Title
type: entity | concept | event | synthesis
sources:
  - raw/category/YYMMDD-slug.md
updated: YYYY-MM-DD
tags: [tag1, tag2]
---

# Page Title

Content with [[wikilinks]] to related pages.

## See Also
- [[related-page]]
```

### File Naming
- Wiki pages: `kebab-case.md` in `wiki/`
- Source files: `YYMMDD-slug.md` in `raw/{category}/`

### Special Files in `wiki/`
- **`wiki/index.md`** — Master catalog of all wiki pages, organized by type. Read this first when answering queries. Update on every ingest.
- **`wiki/log.md`** — Append-only chronological record of operations. Format: `## [YYYY-MM-DD] action | description`

## Operations

### Ingest (adding a new source)
1. Read the source article in `raw/`
2. Discuss key takeaways with the user
3. Create or update relevant wiki pages (entity, concept, event)
4. **Crucially**: look for connections to existing wiki content — contradictions, reinforcements, evolving narratives
5. Update `wiki/index.md`
6. Append to `wiki/log.md`

A single source typically touches 5-15 wiki pages. Prioritize cross-references and relationship mapping — that's the core value.

### Query (answering questions)
1. Read `wiki/index.md` to find relevant pages
2. Read those pages and synthesize an answer
3. If the answer is substantial, offer to file it as a new wiki page

### Lint (wiki health check)
Look for: contradictions between pages, stale claims superseded by newer sources, orphan pages, missing cross-references, concepts mentioned but lacking their own page, gaps worth investigating.

## Source Context: The Economist

All raw sources are articles from **The Economist**. Keep this in mind when analyzing:

- **Editorial stance**: The Economist is liberal (in the classical sense) — pro-free-trade, pro-market, pro-democracy, internationalist. Its analysis is rigorous but carries this perspective. When synthesizing into the wiki, note where the framing reflects this editorial position vs. where it's reporting facts.
- **"Leaders" section**: These are editorial opinion pieces representing The Economist's institutional view. Treat them as informed analysis with a clear point of view, not neutral reporting.
- **Section structure**: The Economist organizes by region and topic (`leaders/`, `finance-and-economics/`, `science-and-technology/`, `culture/`, `middle-east-and-asia/`, etc.). The `raw/` subdirectories follow this structure.
- **Cross-article coherence**: Articles in the same weekly issue often share a theme (e.g., multiple Iran war articles in one issue). Look for how The Economist builds a multi-angle narrative across sections — this is where the richest cross-connections emerge.
- **Data quality**: The Economist cites named sources, institutions (OECD, IMO, Kpler, etc.), and specific figures. These are generally reliable and should be preserved in wiki pages with attribution.

## Key Analytical Priorities

This wiki exists to understand **how the world works and where it's heading**. When ingesting or synthesizing:
- Track **causal chains** between events (e.g., war -> strait closure -> oil price -> inflation)
- Note **competing narratives** and which evidence supports each
- Flag **uncertainties** and **pivot points** where outcomes could diverge
- Identify **patterns** that rhyme across regions or time periods
- Maintain a sense of **timeline** — what happened when, what's unresolved

## Language: Bilingual Wiki (English + Korean)

All wiki pages (except `index.md` and `log.md`) **must be bilingual**. This applies to every operation — ingest, query-filing, lint fixes, and any new page creation.

### Structure

```markdown
---
(YAML frontmatter — English only, appears once)
---

# English Title

English content...

## See Also
- [[links]] (English only, appears once)

---

# 한국어 제목

한국어 내용... (동일한 구조와 세부 수준)
```

### Rules
- **English first**, then a horizontal rule (`---`), then **Korean**.
- Frontmatter and `## See Also` appear **only in the English section**.
- The Korean section is a **full translation with the same structure and detail level** — not a summary or abridgement.
- Preserve all `[[wikilinks]]` in both sections. Use Korean display text where helpful (e.g., `[[iran|이란]]`, `[[strait-of-hormuz|호르무즈 해협]]`).
- Tables, bullet lists, bold/italic emphasis, and heading hierarchy must mirror the English.
- `index.md` and `log.md` remain **English-only** for conciseness.
- Discussion with the user in Korean or English, following the user's lead.
