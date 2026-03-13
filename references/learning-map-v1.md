# Learning Map v1

## Purpose

Define the 5-layer capability map for `openclaw-onboarding-guide`.
Goal: Help users quickly identify (1) which layer they're in, (2) why start here, (3) where to go next.

---

## 5-Layer Structure

### Layer 1: System How-It-Works

**Use when:** User needs to understand structure or build long-term reusable system.

**Signals:**
- "I'm new, where to start?"
- "How is OpenClaw organized?"
- "I want to build a long-term workflow"
- "How do memory/routing/workflow fit together?"

**Focus:** Structure, sequence, boundaries, memory-workflow relationship.

**Key docs:** AGENTS.md, sessions mechanism, memory rules.

---

### Layer 2: Skill Ecosystem

**Use when:** User knows goal but not which skill/entry point.

**Signals:**
- "Which skill should I use?"
- "I know what I want, but don't know the entry"
- "So many capabilities, which path first?"

**Focus:** Skill selection, entry judgment, task-to-layer mapping.

**Key docs:** skills-mechanism, clawhub, wrapper/bridge.

---

### Layer 3: Execution Tools

**Use when:** User has concrete task, needs direct execution.

**Signals:**
- "I want to write code"
- "I want to control browser"
- "I want to schedule a reminder"
- "I want to run a script/command"

**Focus:** Direct execution, tool invocation, task implementation.

**Key skills:** coding-agent, tmux, cron, himalaya, session-logs.

---

### Layer 4: Business / Applied Capabilities

**Use when:** User solving real work scenario (docs/content/files/business).

**Signals:**
- "I want to process a PDF"
- "I want to summarize a document"
- "I want to automate a reporting flow"
- "I want to use OpenClaw for business tasks"

**Focus:** Real work scenarios, document/content/business processing.

**Key skills:** summarize, xlsx, pdf, docx.

---

### Layer 5: Edge / Optional

**Use only when:** Niche, experimental, or clearly not main path.

**Principle:** Do not actively route here unless clearly specialized.

**Examples:** browser_visible, dingtalk_channel, news.

---

## Entry Order

**Default:** L1 → L2 → L3 → L4

**Not mandatory:** This is navigation order, not linear learning path.
Layer skipping depends on user problem type.

---

## When Layer Skipping Is Allowed

### Can Skip to L3/L4

**When:**
- Very clear task
- One-time action only
- Don't care about long-term structure
- Already know the goal, no modeling needed

**Examples:**
- "I want to write code"
- "I want to process a document"
- "I want a scheduled reminder"

---

## When Layer Skipping Is NOT Recommended

### Long-Term System Scenarios

**When:** Building long-term system, reusable workflow, stable collaboration.

**Why not skip:** Not to "learn more", but to reduce rework.

**Common failures:**
1. **Wrong sequence** — tools first, then workflow logic fails
2. **Unclear boundaries** — manual/auto/memory mixed
3. **Memory not connected** — system runs but can't collaborate long-term

---

## Recommended Explanation

> "If one task: tools first is fine.
> If long-term system: structure first reduces rework.
> Because long-term system failures are usually: wrong sequence, unclear boundaries, memory not connected."

---

## Usage Principles

- Do NOT explain all layers at once
- Only explain 1-2 layers most relevant to current user
- Not a systematic lecture
- Goal: help choose entry, not trap in concepts

---

## Success Criteria

User can state 2 of 3:
1. What kind of problem they have
2. Which layer to start from
3. What exactly to do next

---

**Version:** v1 (lean)  
**Validated:** Phase 3 (2026-03-14)  
**Location:** `references/learning-map-v1.md`
