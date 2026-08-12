# CFA Level I — Personal Error Bank System

## Purpose: Every mistake becomes a future question. Build a personal database of "questions designed specifically to catch the mistakes I make."

---

## WHY THE ERROR BANK IS MORE IMPORTANT THAN THE QUESTION BANK

A standard question bank tests what CFA tests. An error bank tests what YOU get wrong.

The difference is enormous:
- Question bank = "Can you solve this CFA-style question?"
- Error bank = "Can you avoid the specific mistake you made last week?"

After 500+ practice questions, 80% of your remaining errors will come from the same 5-10 recurring mistake patterns. The error bank catches those patterns before the exam does.

---

## 1. ERROR BANK ARCHITECTURE

### 1.1 The Three-Layer Structure

```
Layer 1: Raw Error → Individual mistake, classified and timestamped
Layer 2: Error Pattern → Clustered mistakes sharing the same ROOT CAUSE
Layer 3: Generated Trap → Custom question designed to re-trigger the pattern
```

### 1.2 Error Bank Entry (Layer 1)

Every mistake gets a record:

```yaml
error_id: ERR-{DATE}-{SEQ}
question_id: Q-FSA-0005
date: 2026-08-15
subject: Financial Statement Analysis
topic: Inventory
concept: LIFO Reserve
error_type: TF  # Trap Failure
error_subtype: DIRECTION  # Got the direction wrong
description: |
  Subtracted LIFO reserve instead of adding it. In rising prices,
  FIFO inventory = LIFO inventory + LIFO reserve. I went the
  wrong way.
root_cause: |
  Memorized "adjust inventory for LIFO" but didn't internalize
  the DIRECTION. Rising prices → LIFO understates inventory →
  must ADD reserve to get FIFO.
confidence_before: 4  # I thought I knew this
confidence_after: 2   # Realized I didn't
time_spent: 110s  # Exceeded 90s target
guessed: false
changed_answer: false

# These fields populate the generated trap question
trap_question_trigger: LI_FI_DI_REC  # LIFO→FIFO inventory direction reconciliation
trap_question_seed: |
  Period of {RISING|FALLING} prices, company uses {LIFO|FIFO},
  inventory is $X, reserve is $Y. What is {FIFO|LIFO} inventory?
trap_question_params:
  price_direction: rising
  reporting_method: LIFO
  inventory_value: [400000, 600000]  # random range
  reserve_value: [100000, 250000]
  target_method: FIFO
  correct_operation: ADD
  trap_operation: SUBTRACT
```

### 1.3 Error Pattern Cluster (Layer 2)

When 3+ errors share the same root cause, they become a pattern:

```yaml
pattern_id: PAT-001
pattern_name: "Directional Confusion in Accounting Adjustments"
total_errors: 4
error_ids: [ERR-0815-001, ERR-0820-003, ERR-0825-001, ERR-0830-002]
root_cause: |
  I consistently know WHAT adjustment to make but get the
  DIRECTION wrong (add vs. subtract). This affects LIFO reserve,
  deferred tax, depreciation adjustments, and bond
  premium/discount amortization.
affected_concepts:
  - LIFO to FIFO conversion
  - DTA vs DTL creation
  - Capitalize vs expense effect
  - Bond discount amortization
mastery_status: ACTIVE  # Still occurring
retest_count: 2         # Retested twice, still making errors
priority: CRITICAL      # Affects multiple high-weight topics
```

### 1.4 Generated Trap Question (Layer 3)

The system creates a question designed to re-trigger YOUR specific mistake:

```yaml
trap_question_id: TRAP-FSA-DIR-001
parent_errors: [ERR-0815-001, ERR-0820-003]
generation_date: 2026-08-20
concept: LIFO Reserve Adjustment
question: |
  Original CFA-style practice question (Error-Bank Generated)

  During a period of FALLING prices, a company using FIFO reports
  inventory of $520,000. The company discloses that if it had used
  LIFO, inventory would have been $580,000. The LIFO reserve is
  closest to:
A) -$60,000
B) $60,000
C) $580,000

  D) $520,000

correct_answer: A
explanation: |
  In FALLING prices, FIFO reports LOWER inventory than LIFO
  (opposite of rising prices!). LIFO reserve = LIFO inventory -
  FIFO inventory = $580,000 - $520,000 = $60,000. But the
  reserve is NEGATIVE here because LIFO > FIFO in falling prices?
  
  Actually: LIFO Reserve = FIFO Inventory - LIFO Inventory.
  In rising prices: FIFO > LIFO → positive reserve.
  In falling prices: FIFO < LIFO → negative reserve.
  
  So: $520,000 - $580,000 = -$60,000.

trap_targeted: |
  This question targets two specific error patterns:
  1. Your tendency to assume "rising prices" as default
  2. Your tendency to subtract when you should add (or vice versa)
  
  It deliberately uses FALLING prices — the opposite of the
  question you originally got wrong — AND asks for the reserve
  (the intermediate calculation you mishandled).

mistake_you_made_previously: |
  On Q-FSA-0005, you subtracted the LIFO reserve instead of
  adding it. That question used RISING prices. This question
  uses FALLING prices to verify you understand the PRINCIPLE
  (direction depends on price trend) not just the specific case.

retest_interval: 3 days  # First retest
```

---

## 2. ERROR PATTERN CLUSTERING RULES

The system automatically clusters errors when:

| Rule | Condition | Action |
|------|-----------|--------|
| Same Error Type + Same Subject | 2+ errors | Link as potential pattern |
| Same Root Cause | 2+ errors | Create pattern cluster |
| Same Concept + Different Question | 3+ errors | Flag concept as HIGH RISK |
| Same Error Type + Different Subjects | 3+ errors | Flag as CROSS-SUBJECT weakness |
| Trap Failure + Same Trap Tag | 2+ errors | Generate trap-specific drill |
| Directional Error (add vs. subtract) | 2+ errors | Create "direction reversal" drill |
| Changed Answer + Any Pattern | 3+ errors | Flag confidence/trust issue |

---

## 3. MISTAKE-TO-QUESTION GENERATION RULES

### 3.1 Generation Triggers

A new question is generated when:
- **Immediate:** First error on a Tier 1 concept → 1 clone question (different numbers)
- **Pattern:** Third error sharing the same root cause → 3 trap questions (varied context)
- **Retest Failure:** Failing a retest → 2 questions (one clone, one reversed)
- **Cross-Subject:** Same error type across different subjects → 2 integrated questions

### 3.2 Question Variation Methods

When generating a new question from an error:

| Method | What Changes | What Stays Same | When to Use |
|--------|-------------|-----------------|-------------|
| **Clone** | Numbers only | Concept, structure, difficulty | First retest |
| **Reversal** | Direction (add→subtract, call→put) | Concept | Second retest |
| **Context Shift** | Scenario, industry, wording | Underlying concept | Third retest |
| **Difficulty Bump** | Add a step, combine concepts | Core concept | Fourth retest |
| **Time Pressure** | Same question, shorter time | Everything | Mastery gate |
| **Mixed Subject** | Add related concept from another subject | Core concept | Final verification |

### 3.3 Example: Full Error-to-Mastery Progression

```
ERROR: Q-FSA-0005 — LIFO Reserve direction (subtracted instead of added)

WEEK 1 — Clone (different numbers)
  → Q: "Rising prices, LIFO inv = $600K, reserve = $200K. FIFO inv?"
  → Tests: Same concept, new numbers. Can you replicate the fix?

WEEK 2 — Reversal (falling prices)
  → Q: "FALLING prices, FIFO inv = $400K, LIFO inv = $350K. Reserve?"
  → Tests: Do you understand direction depends on price trend?

WEEK 3 — Context Shift (different framing)
  → Q: "Company switches from LIFO to FIFO for reporting. COGS adjustment?"
  → Tests: Do you recognize the concept when framed differently?

WEEK 4 — Difficulty Bump (multi-step)
  → Q: "Adjust LIFO financials to FIFO, recalculate ROE and inventory turnover"
  → Tests: Can you apply the concept in a multi-step problem?

WEEK 6 — Time Pressure (90 seconds)
  → Q: Same as Week 4 but timed
  → Tests: Can you execute under exam conditions?

WEEK 8 — Mixed Subject (cross-topic)
  → Q: "LIFO-to-FIFO adjustment + effects on FCFF calculation"
  → Tests: Can you integrate the concept with related material?
```

---

## 4. PERSONAL TRAP QUESTION GENERATOR

### 4.1 The Generator Prompt Template

When you ask the system to generate questions from your error bank:

```
"Using my error bank, generate 5 questions designed to catch
my 3 most frequent mistake patterns. Use the following
generation rules:
- 2 clone questions (different numbers, same structure)
- 1 reversal question (opposite direction/scenario)
- 1 context-shift question (same concept, different framing)
- 1 difficulty-bump question (add a step or combine concepts)
Prioritize patterns tagged CRITICAL."
```

### 4.2 Error Bank Commands

| Command | What It Does |
|---------|-------------|
| `LOG ERROR [question_id]` | Record a new mistake with full classification |
| `SHOW ERRORS` | Display recent errors (last 10) |
| `SHOW PATTERNS` | Display active error pattern clusters |
| `GENERATE TRAPS [pattern_id]` | Create new questions targeting a specific pattern |
| `GENERATE TRAPS ALL` | Create questions for all active patterns |
| `RETEST ERRORS [date_range]` | Retest all errors from a period |
| `ERROR SUMMARY` | Show error distribution by type, subject, and pattern |
| `ERROR TREND` | Show error frequency over time |

---

## 5. ERROR BANK DASHBOARD

### 5.1 Top 10 Recurring Mistakes

| # | Pattern | Errors | Last Occurred | Status | Trend |
|---|---------|--------|---------------|--------|-------|
| 1 | Directional Confusion (FSA Adjustments) | 4 | 3 days ago | ACTIVE | → |
| 2 | Weight Confusion (Averages) | 3 | 5 days ago | ACTIVE | ↑ |
| 3 | CFA FX Notation | 3 | 1 week ago | RESOLVING | ↓ |
| 4 | D₁ vs D₀ (Gordon Growth) | 2 | 2 weeks ago | RESOLVED | ↓ |
| 5 | Type I vs Type II Error | 2 | 2 weeks ago | RESOLVED | ↓ |
| ... | ... | ... | ... | ... | ... |

### 5.2 Error Distribution by Type

| Error Type | Count | % | Trend |
|------------|-------|-----|-------|
| Trap Failure (TF) | 12 | 30% | ↑ |
| Calculation Error (CE) | 8 | 20% | → |
| Conceptual Misunderstanding (CM) | 7 | 18% | ↓ |
| Reading Error (RE) | 5 | 13% | ↑ |
| Knowledge Gap (KG) | 4 | 10% | ↓ |
| Time Pressure (TP) | 3 | 8% | → |
| Careless (CA) | 1 | 3% | ↓ |

### 5.3 Error Hotspots by Subject

| Subject | Errors | % of Total | Highest Error Type |
|---------|--------|------------|-------------------|
| FSA | 12 | 30% | Trap Failure |
| Fixed Income | 8 | 20% | Calculation Error |
| Ethics | 6 | 15% | Misinterpretation |
| Quant | 5 | 13% | Conceptual |
| Economics | 4 | 10% | Trap Failure |
| Equity | 3 | 8% | Calculation Error |
| Corp Issuers | 2 | 5% | Knowledge Gap |

---

## 6. ERROR BANK MAINTENANCE

### 6.1 Weekly Error Review Protocol

Every week, review your error bank:

1. **Sort by recency** — Are new errors clustering?
2. **Sort by frequency** — What keeps coming back?
3. **Check resolved patterns** — Are they still resolved?
4. **Generate traps** — For any pattern with 3+ errors
5. **Retest oldest errors** — Verify retention after 4+ weeks

### 6.2 Error Resolution Criteria

An error pattern is marked RESOLVED when:
- [ ] Retested 3 times (spaced: 1 day, 7 days, 14 days)
- [ ] All 3 retests answered correctly
- [ ] At least 1 retest was under time pressure
- [ ] At least 1 retest used varied context (not a clone)
- [ ] No recurrence for 30+ days

If any condition fails → pattern returns to ACTIVE.

### 6.3 The "Never Trust One Correct Answer" Rule

An error is never resolved by getting it right ONCE. The system requires:
- **Right once** = luck or fresh memory
- **Right twice** = possible understanding
- **Right three times, spaced, under varied conditions** = probable mastery

---

*End of Error Bank System*
