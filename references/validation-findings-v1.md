# Validation Findings v1

## Purpose

This file explains **why** certain rules in `openclaw-onboarding-guide` are mandatory.
Not a project report — only validated execution rules.

---

## P0 Fix: Automation Binary Follow-up

### Problem

**User input:** "I want to automate this process."

**Old behavior:** Direct route to Layer 3 (tools).

**Issue:** User actually wanted long-term reusable workflow (Layer 1). Result: rework needed.

### Fix

**Mandatory rule:** When "automate/automation/auto-run" detected, **ask before routing**:

```
Which kind of automation?

A. One-off execution (schedule, auto-sort) → L3/L4
B. Long-term reusable workflow (context, multi-action) → L1
```

### Why This Rule Exists

- "Automation" is too broad — causes wrong routing
- Binary choice reduces decision cost
- Validated in Phase 3 Round 1 (TC-02)
- 100% success rate after fix (Round 2)

### When to Apply

**Trigger keywords:**
- "automate"
- "automation"
- "auto-run"
- "reusable automation"

**Do NOT skip this step.**

---

## P1 Fix: Long-Term System Explanation

### Problem

**User input:** "I want to build a long-term system."

**Old behavior:** Direct recommendation to Layer 1.

**Issue:** Users skip to tools, considering structure as "overhead". Result: system fails due to wrong sequence/unclear boundaries/memory gaps.

### Fix

**Mandatory rule:** Before routing, **explain why structure first**:

```
If one task: tools first is fine.
If long-term system: structure first reduces rework.

Common failures:
1. Wrong sequence — tools first, workflow logic fails
2. Unclear boundaries — manual/auto/memory mixed
3. Memory not connected — system runs but can't collaborate
```

### Why This Rule Exists

- Users naturally skip to tools
- "Learn more" framing creates resistance
- "Reduce rework" framing works better
- Validated in Phase 3 Round 1 (TC-03)
- 100% acceptance after fix (Round 2)

### When to Apply

**Trigger signals:**
- "long-term system"
- "reusable workflow"
- "keep working over time"
- "ongoing mechanism"

**Do NOT skip this explanation.**

---

## Validated Patterns

### Pattern 1: Binary Choice > Open Question

**Effective:**
> "Which kind: A (one-off) or B (long-term)?"

**Why:** Reduces cognitive load, user can immediately identify.

---

### Pattern 2: "Reduce Rework" > "Learn More"

**Effective:**
> "Structure first reduces rework."

**Ineffective:**
> "You should learn the structure first."

**Why:** Reframes from "overhead" to "efficiency".

---

### Pattern 3: 3 Actions Max

**Rule:** Never recommend more than 3 next actions.

**Why:** Cognitive overload, choice paralysis.

---

## Validation Summary

| Round | Date | Test Cases | Pass Rate |
|-------|------|------------|-----------|
| Round 1 | 2026-03-13 | TC-01/02/03 | Partial (found P0/P1 issues) |
| Round 2 | 2026-03-14 | TC-02-R1/TC-03-R1 | 100% |

**Status:** ✅ Completed (2026-03-14)

**Full report:** See project folder `Phase3_验证报告_真实版_v1.md`

---

**Version:** v1 (lean)  
**Purpose:** Rule justification only  
**Location:** `references/validation-findings-v1.md`
