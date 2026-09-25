---
name: context-engineering
description: Expert system for persistent context engineering, token optimization, and harness-driven agent memory.
---

# Master Context Engineering & Agent Harness Architecture

## 1. High-Level Concepts & Mental Models

### The Three-Pillar Production Architecture
1. **The Interface (FastAPI):**
   - The Gateway and Front Desk that accepts incoming client requests, validates data schemas, and returns clean HTTP responses.
   - Handles connection routing, status codes, and web protocols without embedding heavy agent logic directly inside routes.
2. **The Brain (Context Engineering):**
   - The structured intelligence, rules, prompt constraints, and persistent memory stored on disk.
   - Pre-defines exact behavior, eliminates hallucinations, prevents trial-and-error loops, and slashes token consumption by 70% to 90%.
3. **The Muscle (Agent Harness):**
   - The runtime execution engine and scaffolding that gives the agent physical operational abilities.
   - Manages concurrent threads, sub-second network sockets, anti-bot evasion, and OS terminal commands.

---

## 2. Core Context Engineering Directives

1. **Working Memory on Disk (Persistent Context):**
   - Never rely on volatile conversation history for mission-critical logic or system rules.
   - Always persist learned directives, bugfixes, and configurations to `AGENTS.md` (workspace root) and `SKILL.md` (skills registry).
   - Guarantees 100% survival across conversation compactors and context window limits.

2. **Strict Data Authenticity (Zero-Hallucination Law):**
   - Never generate synthetic or predicted contact URLs or emails (e.g. guessing LinkedIn slugs or mail addresses).
   - All extracted leads and records must originate from genuine DOM structures and verified search engine edge caches.

3. **Sub-2-Second Concurrency Standard (`bp.concurrency`):**
   - Always dispatch multi-channel search queries and X-Ray tasks concurrently using multi-threaded workers and TLS-spoofed sockets.
   - Never execute independent scraping queries sequentially. Reduces total execution time from 20s+ to ~1.18 seconds.

4. **Cross-Platform Output Safety (Windows CP1252):**
   - Never stream unhandled Unicode emojis directly to standard output on Windows environments.
   - Always use clean ASCII status indicators (`[OK]`, `[SUCCESS]`, `[BENCHMARK]`) to guarantee zero `charmap` codec exceptions.

5. **Progressive Disclosure & Token Pruning:**
   - Keep high-level descriptions concise in agent manifests.
   - Deep architectural sub-systems load selectively on-demand only when relevant tasks trigger them.

---

## 3. The Enterprise Interaction Lifecycle (FastAPI + Context Engineering + Harness)

1. **Client Intake Stage:**
   - Client sends an API request (e.g. `POST /api/v1/hunt-leads` with target parameters).
   - FastAPI validates the parameters and immediately passes the workload to the Agent Harness.

2. **Context Synthesis Stage:**
   - The Context Engine intercepts the request, enriches it with pre-validated domain rules, strips unnecessary tokens, and constructs deterministic search queries without hallucinating.

3. **Harness Execution Stage:**
   - The Harness coordinates multi-threaded workers in parallel, bypassing anti-bot shields and network bottlenecks in under 2 seconds.

4. **Response Delivery Stage:**
   - Raw data is validated, structured, and returned through FastAPI to the client as clean, high-density JSON.
