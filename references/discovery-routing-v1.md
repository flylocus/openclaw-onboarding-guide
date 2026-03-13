# Discovery Routing v1

## Purpose

Define task routing logic for `openclaw-onboarding-guide`.
Map natural language to: (1) problem type, (2) capability layer, (3) next action.

---

## General Principles

1. Identify problem type first
2. Map to layer second
3. Recommend 1-3 actions last
4. Do NOT list many skills
5. Do NOT exceed 3 entry points

---

## 4 Problem Types

### Type A: New User / Orientation

**Signals:**
- "I'm new to OpenClaw"
- "Where do I start?"
- "What can OpenClaw do?"
- "Skills or docs first?"

**Route:** L1 (primary), L2 (secondary)

**Focus:** Build structure understanding, then give first action.

---

### Type B: Task-First Routing

**Signals:**
- "Which skill should I use?"
- "I know what to do, but don't know entry"
- "How to handle this requirement?"

**Route:** L2 (primary), L3/L4 (if task very clear)

**Focus:** Problem type, recommended layer, ≤3 entries.

---

### Type C: Automation Ambiguity ⚠️

**Signals:**
- "I want to automate"
- "Auto-run this"
- "Reusable automation"

**Mandatory:** Do NOT route. Ask first:

```
Which kind?
1. One-off execution → L3/L4
2. Long-term reusable workflow → L1
```

**After user selects:**
- If 1: Route to L3/L4 (specific task automation)
- If 2: Route to L1 (system structure)

---

### Type D: Long-Term System Building ⚠️

**Signals:**
- "Build a long-term system"
- "Continuous running mechanism"
- "Connect multiple capabilities"

**Route:** L1

**Mandatory explanation:**
```
If one task: tools first is fine.
If long-term: structure first reduces rework.

Failures: wrong sequence, unclear boundaries, memory not connected.
```

---

## Priority Judgment Order

1. **New user or has task?**
   - New → Type A
   - Has task → Continue

2. **One-off or long-term?**
   - One-off → L3/L4
   - Long-term → L1

3. **Don't know skill or structure?**
   - Don't know skill → L2
   - Don't know structure → L1

---

## Typical Routing Examples

| User Input | Type | Layer | Actions |
|------------|------|-------|---------|
| "I want to write code" | B | L3 | coding-agent → tmux (if long) → session-logs |
| "Process long text/docs" | B | L4 | summarize/pdf/docx → workflow if repeated |
| "Automate this" | C | Ask first | Binary question before routing |
| "Build long-term system" | D | L1 | Structure → ecosystem → tools |

---

## Output Template

```
1. Problem: [type in one sentence]
2. Layer: [name + reason in one sentence]
3. Actions:
   1. [Action 1]
   2. [Action 2]
   3. [Action 3, optional]
```

---

## Quantity Limits

- Max 3 actions
- Max 3 entry points
- Do NOT spread full skill list
- If uncertain: narrow scope, don't add options

---

## Failure Signals

- User still doesn't know where to start
- User must guess among many entries
- User pushed to execution but needs structure first
- User wanted one task but got over-explained

---

## Success Signals

User can state 2 of 3:
1. What type of problem they have
2. Which layer to enter first
3. What to do next

---

**Version:** v1 (lean)  
**Validated:** Phase 3 (2026-03-14)  
**Location:** `references/discovery-routing-v1.md`
