# CFA Level I — Question Construction Recipe Book

## Purpose: Don't just record questions. Record HOW questions are constructed. This lets you recognize the pattern even when CFA changes the numbers, wording, or context.

---

## WHY PATTERNS MATTER MORE THAN QUESTIONS

CFA examiners don't write random questions. They follow construction templates. If you learn the template, you can solve ANY question built from it — regardless of the numbers, the company name, or the specific wording.

**This is the difference between:**
- "I've seen this exact question before" (fragile, memorization)
- "I recognize this construction pattern" (robust, understanding)

---

## 1. QUESTION CONSTRUCTION ANATOMY

Every CFA question has the same skeleton:

```
[SETUP] → Context, scenario, data
[PIVOT] → "Based on this..." or "Which of the following..."
[QUESTION] → What they're actually asking
[OPTIONS] → 1 correct + 3 distractors (each with a specific trap purpose)
```

### 1.1 The Setup — What They Give You

| Setup Type | Example | Purpose |
|------------|---------|---------|
| Pure numbers | "A bond has a 6% coupon..." | Tests direct calculation |
| Scenario | "An analyst is evaluating..." | Tests application |
| Comparative | "Compared to Company X, Company Y..." | Tests directional understanding |
| Adjustment | "After adjusting for the LIFO reserve..." | Tests multi-step reasoning |
| Definitions | "The term 'normal backwardation' refers to..." | Tests recall |
| Table/Data | A mini income statement | Tests data extraction + calculation |

### 1.2 The Pivot — How They Transition

| Pivot Phrase | What It Signals |
|-------------|-----------------|
| "...is closest to:" | Calculation required (they expect rounding) |
| "...is most likely:" | Conceptual judgment (multiple may be plausible) |
| "...is least likely:" | Reverse reasoning (find the FALSE one) |
| "...will most likely:" | Directional prediction |
| "...is best described as:" | Definition/classification |
| "...would be:" | Hypothetical/adjustment scenario |

### 1.3 The Options — How Distractors Are Built

Every wrong option serves a PURPOSE:

| Distractor Type | How It's Built | Example (for FV of $1,000, 7%, 10yr) |
|-----------------|----------------|--------------------------------------|
| **Forgot-step trap** | Omitted one step | Used PMT without compounding |
| **Wrong-formula trap** | Used similar but wrong formula | Used PV formula instead of FV |
| **Direction trap** | Correct magnitude, wrong sign | -$19,672 instead of +$19,672 |
| **Common-error trap** | Result of the most common student error | Used n=10 instead of n=20 for semi-annual |
| **Plausible-adjacent trap** | Close to correct but from different method | Used simple interest approximation |
| **Unit-confusion trap** | Correct answer in wrong units | $196.72 instead of $19,672 |

---

## 2. RECOGNITION TEMPLATES — BY PATTERN

### 2.1 TEMPLATE: Direct Calculation

**Recognition Signature:**
- Setup provides all needed inputs
- No irrelevant numbers (or exactly 1-2 distractors)
- Pivot is "...is closest to:"
- Options are numerical, clustered within 10-20% of each other

**When you see this, immediately:**
1. Identify the formula needed
2. Extract only the relevant inputs (ignore distractors)
3. Check units (annual/semi-annual, percentage/decimal)
4. Execute on calculator
5. Compare to options — if exact match, confident; if "closest to," check rounding

**Same pattern, different disguise:**
```
VERSION A (Standard): "Calculate the FV of $5,000 invested at 8% for 15 years."
VERSION B (Reverse): "What rate turns $5,000 into $15,892 in 15 years?"
VERSION C (Per-period): "$500 deposited monthly at 6% APR for 20 years. FV?"
VERSION D (Growth): "Dividends growing at 5%. What will the dividend be in Year 8?"
```

ALL four are the same template: identify formula, extract inputs, compute. Only the framing changes.

### 2.2 TEMPLATE: Directional Relationship

**Recognition Signature:**
- Setup compares two scenarios or asks "if X changes..."
- Uses words like "compared to," "all else equal," "ceteris paribus"
- Options are directional (higher/lower, increase/decrease)
- Often has "most likely" pivot

**When you see this, immediately:**
1. Draw the relationship arrow (X↑ → Y↓? X↑ → Y↑?)
2. State the direction out loud before looking at options
3. Eliminate options with wrong direction first
4. Then pick the remaining option

**Same pattern, different contexts:**
```
BONDS: "If YTM increases, bond price..." → DECREASES (inverse)
OPTIONS: "If volatility increases, call price..." → INCREASES (positive vega)
FX: "If domestic rates rise, domestic currency..." → APPRECIATES
ECONOMICS: "If MPC increases, fiscal multiplier..." → INCREASES
EQUITY: "If required return increases, justified P/E..." → DECREASES
```

The TEMPLATE is identical: identify the relationship arrow. Only the specific variables change.

### 2.3 TEMPLATE: Missing Variable (Formula Rearrangement)

**Recognition Signature:**
- Setup gives result + most inputs, withholds ONE variable
- "Given X and Y, the Z is..."
- Often feels "backwards" — you're solving for something normally given
- Options are clustered around the answer

**When you see this, immediately:**
1. Write the full formula
2. Rearrange to isolate the unknown
3. Plug in known values
4. Solve

**Same pattern, different disguises:**
```
TVM: "Given FV, PMT, r → find n"
BONDS: "Given price, coupon, par → find YTM"
DDM: "Given price, D₁, r → find implied g"
FX: "Given forward, spot, r_d → find r_f"
```

### 2.4 TEMPLATE: "Which Standard Is Violated?"

**Recognition Signature:**
- Setup describes a professional situation
- Pivot: "Has [person] most likely violated..." or "Which Standard..."
- Options are Standard references (I(A), II(B), etc.) or Yes/No with reasoning
- Key trap: multiple Standards COULD apply but ONE is clearly primary

**When you see this, immediately:**
1. Identify the CORE action (trading, recommending, disclosing, etc.)
2. Map action to Standard category (e.g., trading → II, recommending → V)
3. Check for the strictest/most specific Standard
4. Verify: would a reasonable person see this as a violation?

### 2.5 TEMPLATE: Adjustment/Reconciliation

**Recognition Signature:**
- Setup gives reported/starting value
- Provides an adjustment factor
- Pivot: "After adjusting for X, Y would be..."
- Tests whether you know WHAT to adjust and in WHICH DIRECTION

**When you see this, immediately:**
1. Identify: what is the reported value? What is the TRUE value?
2. Determine: does the adjustment INCREASE or DECREASE the reported figure?
3. Apply the adjustment
4. Recalculate any downstream effects

**Same pattern, different contexts:**
```
INVENTORY: LIFO → FIFO adjustment
DEPRECIATION: Reported → Economic depreciation adjustment
TAXES: Book → Tax basis adjustment
OFF-BALANCE-SHEET: Reported → Capitalized operating lease adjustment
```

---

## 3. THE "SAME PATTERN, DIFFERENT SKIN" FRAMEWORK

### 3.1 What Changes vs. What Stays the Same

When CFA disguises a pattern, here's what they can change:

| Element | Can Change? | Example |
|---------|-------------|---------|
| Numbers | ✅ Always | $50 becomes $75, 5% becomes 8% |
| Company/Industry | ✅ Always | Tech firm becomes manufacturing |
| Time periods | ✅ Often | Annual → semi-annual, 5yr → 3yr |
| Direction | ✅ Often | Rising prices → falling prices |
| Currency/Units | ✅ Sometimes | Dollars → Euros, % → bps |
| **Concept tested** | ❌ Never | The underlying concept is the constant |
| **Formula required** | ❌ Rarely | Might rearrange but same formula |
| **Trap mechanism** | ❌ Rarely | Same trap, different wrapping |
| **Reasoning path** | ❌ Never | The logic you follow is identical |

### 3.2 Pattern Recognition Drill

When you encounter a new question, train yourself to ask:

```
1. "Have I seen this STRUCTURE before?" (not this exact question)
2. "What PATTERN does this match?"
3. "What's the UNDERLYING CONCEPT being tested?"
4. "What TRAP is built into the distractor options?"
5. "What would this question look like with different numbers?"
6. "What would this question look like in reverse?"
```

### 3.3 Recognition Practice Protocol

For every 10 questions you answer:
1. **Answer the question** (normal)
2. **Name the pattern** ("This is a Missing Variable template")
3. **Identify the trap** ("The $35.71 distractor is D₀ instead of D₁")
4. **Rewrite mentally** ("If D₀ were $3 instead of $2.50, the answer would be...")
5. **Reverse it** ("If they gave me the price and asked for the growth rate...")

This 5-step cycle builds pattern recognition, not question memorization.

---

## 4. TEMPLATE-BASED QUESTION GENERATION

### 4.1 Generation Rules by Template

When creating new questions from a template:

```
TEMPLATE: Direct Calculation
  Vary: [numbers, compounding frequency, time period]
  Keep: [concept, formula, difficulty]
  Add trap: [unit confusion, wrong compounding, D₀ vs D₁]

TEMPLATE: Directional Relationship
  Vary: [scenario, variable names, context]
  Keep: [relationship direction, concept]
  Add trap: [reverse the obvious relationship, test a corner case]

TEMPLATE: Missing Variable
  Vary: [which variable is missing, numbers]
  Keep: [formula, concept]
  Add trap: [give seemingly sufficient but wrong formula]

TEMPLATE: Ethics Scenario
  Vary: [characters, industry, specific action]
  Keep: [Standard being tested, violation status]
  Add trap: [add a secondary Standard that could plausibly apply]
```

### 4.2 Template Library — Quick Reference

| Template ID | Name | Subjects | Key Marker |
|-------------|------|----------|------------|
| T-DC | Direct Calculation | All | "...is closest to:" with numbers |
| T-DR | Directional Relationship | All | "compared to," "if X changes" |
| T-MV | Missing Variable | Quant, FI, EQ, DER | "Given X and Y, find Z" |
| T-ADJ | Adjustment | FSA, COR | "After adjusting for..." |
| T-VAL | Valuation | EQ, FI | "The intrinsic value is..." |
| T-ETH | Ethics | ETH | "Has [person] violated..." |
| T-ML | Most Likely | All | "...is most likely..." |
| T-LL | Least Likely | All | "...is least likely..." |
| T-SEL | Formula Selection | Quant, DER | "Which formula/test..." |
| T-INT | Interpretation | All | "This result indicates..." |
| T-CMP | Comparison | All | "Compared to X, Y..." |
| T-SCN | Scenario Application | All | Narrative + question |

---

## 5. ANTI-MEMORIZATION SAFEGUARDS

### 5.1 Questions to Never Trust

If you find yourself thinking any of these, you're memorizing, not learning:

| Thought | Why It's Dangerous | What To Do Instead |
|---------|-------------------|-------------------|
| "I've seen this exact question" | CFA changes numbers | Find the pattern, not the question |
| "The answer was B last time" | Answers change with numbers | Learn the reasoning, not the letter |
| "This is the same as Kaplan Q47" | Different source, different framing | Map it to a CFA LOS, not a source |
| "I remember the answer is $37.14" | Numbers will be different | Remember D₁/(r-g), not the output |
| "This topic always has 2 calculation Qs" | Topic weights shift | Prepare for any number of questions |

### 5.2 The "Prove You Understand" Test

For any concept you think you've mastered, answer these:

1. **What happens if the numbers double?** Can you recalculate?
2. **What happens in reverse?** Can you solve for the input instead of output?
3. **What's the most common wrong answer?** Can you identify the trap?
4. **When does this formula NOT apply?** Can you identify boundaries?
5. **How would you explain this to someone who keeps getting it wrong?** Can you teach it?

If you can't answer all 5, you don't understand the concept — you've only memorized a specific question.

---

*End of Question Construction Recipe Book*
