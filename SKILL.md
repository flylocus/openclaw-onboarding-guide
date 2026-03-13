---
name: openclaw-onboarding-guide
description: Guide users into the right OpenClaw entry point using a validated learning-map structure. Use when user is new, asks where to start, doesn't know which skill to use, or wants to automate but is unsure about one-off vs reusable workflow.
validation: "Phase 3 validated (2026-03-14)"
key_rules: "Automation binary follow-up (P0), Long-term system explanation (P1)"
---

# OpenClaw Onboarding Guide

## Core Responsibility

Help users:
1. Identify what kind of problem they have
2. Map to the right capability layer (1-5)
3. Recommend 1-3 next actions only

**Do NOT** dump long skill lists. **Do NOT** exceed 3 recommendations.

---

## Capability Layers (Quick Reference)

| Layer | Name | Use When |
|-------|------|----------|
| **L1** | System How-It-Works | User needs to understand structure / build long-term workflow |
| **L2** | Skill Ecosystem | User knows goal but not which skill/entry |
| **L3** | Execution Tools | User has concrete task, needs direct execution |
| **L4** | Business Capabilities | User solving real work scenario (docs/content/files) |
| **L5** | Edge/Optional | Niche/experimental needs only |

**Details:** See `references/learning-map-v1.md`

---

## Mandatory Rules ⚠️

### Rule 1: Automation Ambiguity (P0 Fix)

If user says "automate", "automation", "auto-run", **do NOT route immediately**.

**Ask first:**

```
Which kind of automation?

A. One-off execution (schedule, auto-sort, one step) → L3/L4
B. Long-term reusable workflow (context, multi-action) → L1
```

**Why:** "Automation" is too broad. Validated in Phase 3 Round 1.

---

### Rule 2: Long-Term System Explanation (P1 Fix)

If user wants long-term system/reusable workflow, **explain before routing**:

```
If one task: tools first is fine.
If long-term system: structure first reduces rework.

Common failures:
1. Wrong sequence — tools first, then workflow logic fails
2. Unclear boundaries — manual/auto/memory mixed
3. Memory not connected — system runs but can't collaborate
```

**Why:** Users skip to tools. Explanation reduces skip-step. Validated Phase 3 Round 1.

---

## Response Format

### 1. Problem Type (one sentence)
"This is a [task-routing / onboarding / workflow-design] problem."

### 2. First Layer (one sentence)
"Start from Layer X, because [reason]."

### 3. Next Actions (1-3 only)
1. [Action 1]
2. [Action 2]
3. [Action 3, optional]

---

## Trigger Conditions

**Use this skill when:**
- User is new to OpenClaw
- User asks "where to start"
- User doesn't know which skill to use
- User mentions "automate" (apply Rule 1)
- User wants long-term system (apply Rule 2)

**Do NOT use when:**
- User already knows exact skill needed
- User is advanced, beyond onboarding
- Single tool call needed without guidance

---

## Example (Minimal)

**User:** "I want to automate this process."

**Response:**
```
Before routing, I need to clarify:

Which kind of automation?

A. One-off execution (schedule, auto-sort) → L3/L4
B. Long-term reusable workflow → L1

Which matches your goal?
```

**[User selects A]**

```
1. Problem: One-off automation task
2. Layer: L3 (Execution tools) — specific step automation
3. Actions:
   1. Use cron to schedule
   2. Configure parameters
   3. Test once
```

**More examples:** See `references/discovery-routing-v1.md`

---

## Reference Files

| File | Purpose |
|------|---------|
| `references/learning-map-v1.md` | 5-layer structure, entry order, skip rules |
| `references/discovery-routing-v1.md` | 4 problem types, routing templates, examples |
| `references/validation-findings-v1.md` | P0/P1 fixes, validated patterns |

**Read references when:**
- User needs layer details → learning-map
- User needs routing examples → discovery-routing
- You need to understand why rules exist → validation-findings

---

## Success Criteria

✅ User knows: (1) problem type, (2) first layer, (3) next action  
❌ Fail if: too many choices, no clear step, list instead of route

---

**Version:** v1.1 (lean / 收敛版)  
**Validated:** Phase 3 two-round (2026-03-14)  
**Location:** `~/.openclaw/skills/openclaw-onboarding-guide/SKILL.md`
