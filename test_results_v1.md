# Trigger Test Results / 触发测试结果

**Test Date:** 2026-03-14  
**Skill:** openclaw-onboarding-guide v1.1  
**Test Queries:** 6 groups  
**Pass Criteria:** ≥5/6 on each metric

---

## Test 1: "我第一次用 OpenClaw，从哪开始？"

**Expected:** Type A (New User) → L1

**Response:**
```
1. Problem: This is an onboarding/orientation problem.
2. Layer: Start from Layer 1 (System how-it-works), because you need to understand how OpenClaw organizes work before diving into specific skills.
3. Actions:
   1. Read AGENTS.md to understand workspace structure
   2. Review sessions mechanism to see how tasks progress
   3. Come back with a specific task, we'll route to the right layer
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type A detected) |
| Routing | ✅ Correct (L1) |
| Light output | ✅ 3 actions, no list dump |
| Clear next step | ✅ Yes (read AGENTS.md first) |

**Score:** 4/4 ✅

---

## Test 2: "我不知道该用哪个 skill"

**Expected:** Type B (Task-First) → L2

**Response:**
```
1. Problem: This is a skill selection problem.
2. Layer: Start from Layer 2 (Skill ecosystem), because you need to find the right entry point for your goal.
3. Actions:
   1. Tell me what you want to accomplish
   2. I'll recommend the right skill
   3. If needed, we'll explore clawhub for more options
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type B detected) |
| Routing | ✅ Correct (L2) |
| Light output | ✅ 3 actions, no list dump |
| Clear next step | ✅ Yes (describe goal first) |

**Score:** 4/4 ✅

---

## Test 3: "我想写代码"

**Expected:** Type B (Task-First) → L3

**Response:**
```
1. Problem: This is a task-routing problem.
2. Layer: Start from Layer 3 (Execution tools), because you have a concrete task (coding) and need direct execution capability.
3. Actions:
   1. Use coding-agent to start writing code
   2. If you need long-running sessions, use tmux
   3. If you want to trace development, enable session-logs
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type B detected) |
| Routing | ✅ Correct (L3) |
| Light output | ✅ 3 actions, no list dump |
| Clear next step | ✅ Yes (use coding-agent) |

**Score:** 4/4 ✅

---

## Test 4: "我想自动化流程" ⚠️

**Expected:** Type C (Automation Ambiguity) → Mandatory binary follow-up

**Response:**
```
Before I route you, I need to clarify:

Which kind of automation?

A. One-off execution (schedule, auto-sort, one step) → L3/L4
B. Long-term reusable workflow (context, multi-action) → L1

Which matches your goal?
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type C detected, P0 rule applied) |
| Routing | ✅ Correct (asked first, not routed yet) |
| Light output | ✅ Binary choice, no explanation dump |
| Clear next step | ✅ Yes (select A or B) |

**Score:** 4/4 ✅

**[Follow-up Test 4-A: User selects A]**

**Response:**
```
1. Problem: This is a one-off automation task.
2. Layer: Start from Layer 3 (Execution tools), because you want to automate a specific step.
3. Actions:
   1. Use cron to schedule the task
   2. Configure execution parameters
   3. Test once to verify it works
```

**Score:** 4/4 ✅

**[Follow-up Test 4-B: User selects B]**

**Response:**
```
1. Problem: This is a long-term reusable workflow design problem.
2. Layer: Start from Layer 1 (System how-it-works), because you're building a reusable system.

Important: Structure first reduces rework. Common failures: wrong sequence, unclear boundaries, memory not connected.

3. Actions:
   1. Read AGENTS.md for workspace structure
   2. Review sessions mechanism
   3. Come back with workflow design, we'll route to tools
```

**Score:** 4/4 ✅

---

## Test 5: "我想搭长期系统" ⚠️

**Expected:** Type D (Long-Term System) → L1 + Mandatory explanation

**Response:**
```
1. Problem: This is a long-term system building problem.
2. Layer: Start from Layer 1 (System how-it-works), because you're designing a reusable system.

Important note:
If one task: tools first is fine.
If long-term system: structure first reduces rework.

Common failures:
1. Wrong sequence — tools first, workflow logic fails
2. Unclear boundaries — manual/auto/memory mixed
3. Memory not connected — system runs but can't collaborate

3. Actions:
   1. Read AGENTS.md for workspace structure
   2. Review sessions mechanism
   3. Come back with workflow design
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type D detected, P1 rule applied) |
| Routing | ✅ Correct (L1) |
| Light output | ✅ Explanation concise, 3 actions |
| Clear next step | ✅ Yes (read AGENTS.md first) |

**Score:** 4/4 ✅

---

## Test 6: "我想把多个能力串起来形成工作流"

**Expected:** Type D (Long-Term System) → L1

**Response:**
```
1. Problem: This is a long-term workflow design problem.
2. Layer: Start from Layer 1 (System how-it-works), because you're connecting multiple capabilities into a reusable system.

Important note:
Structure first reduces rework. Common failures: wrong sequence, unclear boundaries, memory not connected.

3. Actions:
   1. Read AGENTS.md for workspace structure
   2. Review how sessions coordinate multiple skills
   3. Map out your workflow, then we'll route to execution tools
```

**Evaluation:**
| Metric | Result |
|--------|--------|
| Trigger | ✅ Correct (Type D detected) |
| Routing | ✅ Correct (L1) |
| Light output | ✅ Concise, 3 actions |
| Clear next step | ✅ Yes (read AGENTS.md first) |

**Score:** 4/4 ✅

---

## Summary

### Overall Scores

| Metric | Pass | Total | Rate |
|--------|------|-------|------|
| **Trigger Correct** | 6 | 6 | 100% ✅ |
| **Routing Correct** | 6 | 6 | 100% ✅ |
| **Light Output** | 6 | 6 | 100% ✅ |
| **Clear Next Step** | 6 | 6 | 100% ✅ |

### Pass Criteria Check

| Criteria | Required | Actual | Pass |
|----------|----------|--------|------|
| Trigger correct | ≥5/6 | 6/6 | ✅ |
| Routing correct | ≥5/6 | 6/6 | ✅ |
| Light output | ≥5/6 | 6/6 | ✅ |
| Clear next step | ≥5/6 | 6/6 | ✅ |

**Overall Result:** ✅ **PASS** (6/6 on all metrics)

---

## Key Observations

### What Worked Well

1. **P0 Rule (Automation Binary):** Test 4 correctly triggered binary follow-up, not direct routing
2. **P1 Rule (Long-Term Explanation):** Tests 5-6 correctly included rework explanation
3. **3-Action Limit:** All responses stayed within 1-3 actions
4. **Layer Mapping:** L1 for structure, L2 for skill selection, L3 for execution — all correct

### No Issues Found

- No over-explanation
- No skill list dumping
- No wrong routing
- No ambiguous next steps

---

## Recommendation

**Status:** ✅ Ready for production use

**Next Decision:**
- Option 1: Run as independent skill (low risk, quick deployment)
- Option 2: Integrate into OpenClaw product layer (requires product decision)

**Suggested:** Start with Option 1, gather real usage data, then decide on Option 2.

---

**Test Completed:** 2026-03-14  
**Tester:** B-route execution agent  
**Version:** v1.1 (lean)
