# CFA Level I Preparation System — Master Blueprint

## Architecture Version: 2.0 (Enhanced)
## Exam Cycle: 2024–2025
## Last Updated: August 2026

---

# 1. SYSTEM OVERVIEW

This document defines the complete architecture of the CFA Level I Preparation Ecosystem. Version 2.0 incorporates five key enhancement principles that transform a static question bank into a living preparation system.

## 1.1 The Five Enhancement Principles

### Principle 1: Error Bank > Question Bank
Every mistake becomes a future question. The system maintains a personal database of "questions designed specifically to catch the mistakes I make." A three-layer architecture: Raw Error → Error Pattern Cluster → Generated Trap Question. See [Error Bank System](../dashboard/error-bank-system.md).

### Principle 2: Pattern Recognition > Question Memorization
Don't just record questions; record HOW questions are constructed. This is what helps when CFA changes the numbers, wording, or context. Recognition templates, question construction recipes, and the "same pattern, different skin" framework. See [Question Construction Recipes](../pattern-library/question-construction-recipes.md).

### Principle 3: Mastery Requires Multi-Condition Verification
"I got 8/10" isn't enough. Mastery requires: (a) correct under time pressure, (b) correct after two-week retention gap, (c) correct in mixed-subject context, (d) correct when the pattern is disguised. The system never trusts one correct answer.

### Principle 4: Evidence-Based Confidence via Dashboard
Instead of "I feel prepared," the system shows: Curriculum: 100%, High-priority concepts: 96%, Formula mastery: 93%, Weak topics: 3, Mock average: 78%, Readiness: Strong. Confidence comes from evidence, not feelings.

### Principle 5: Anti-Overfitting to Previous Questions
CFA isn't an exam where memorizing previous questions works. The real advantage is learning recurring concepts + recurring reasoning patterns + traps + difficulty + application. Official CFA Institute material is the backbone; external material fills gaps.

### Our Target
**90%+ preparation coverage, not 90% question prediction.** This is a much more powerful target — it tells you exactly what you haven't mastered yet instead of relying on confidence or guesswork.

---

# 2. EXAM STRUCTURE CONFIRMED

## 2.1 Current Exam Format
- **Total Questions:** 180 multiple-choice (A, B, C)
- **Session 1:** 135 min (90 questions)
  - Ethics (Group I)
  - Investment Tools: Quantitative Methods, Economics, Financial Statement Analysis (Group II)
- **Session 2:** 135 min (90 questions)
  - Corporate Issuers, Portfolio Management (Group III)
  - Equity, Fixed Income, Derivatives, Alternative Investments (Group IV)
- **Time per Question:** ~90 seconds average

## 2.2 Topic Weights (2024–2025)

| # | Subject | Weight Range | Est. Questions | Priority Tier |
|---|---------|-------------|----------------|---------------|
| 1 | Ethical & Professional Standards | 15%–20% | 27–36 | TIER 1 |
| 2 | Financial Statement Analysis | 11%–14% | 20–25 | TIER 1 |
| 3 | Equity Investments | 11%–14% | 20–25 | TIER 1 |
| 4 | Fixed Income | 11%–14% | 20–25 | TIER 1 |
| 5 | Portfolio Management | 8%–12% | 14–22 | TIER 2 |
| 6 | Alternative Investments | 7%–10% | 13–18 | TIER 2 |
| 7 | Quantitative Methods | 6%–9% | 11–16 | TIER 2 |
| 8 | Economics | 6%–9% | 11–16 | TIER 2 |
| 9 | Corporate Issuers | 6%–9% | 11–16 | TIER 2 |
| 10 | Derivatives | 5%–8% | 9–14 | TIER 3 |

---

# 3. CURRICULUM HIERARCHY DESIGN

## 3.1 Hierarchy Structure

```
Subject → Topic → Subtopic → Learning Outcome → Concept → Skill → Formula/Method → Question Pattern
```

## 3.2 Learning Outcome ID Format

```
SUB-TOP-SUBT-LO##

Where:
  SUB  = 3-letter subject code
  TOP  = 2-digit topic number
  SUBT = 2-digit subtopic number
  LO## = Learning Outcome number

Example: FSA-03-02-LO04
```

## 3.3 Subject Codes

| Code | Subject |
|------|---------|
| ETH | Ethical & Professional Standards |
| QNT | Quantitative Methods |
| ECO | Economics |
| FSA | Financial Statement Analysis |
| COR | Corporate Issuers |
| EQU | Equity Investments |
| FIX | Fixed Income |
| DER | Derivatives |
| ALT | Alternative Investments |
| PRT | Portfolio Management |

---

# 4. CURRICULUM COVERAGE MATRIX COLUMNS

Each entry in the coverage matrix will track:

| Column | Description | Data Type |
|--------|-------------|-----------|
| Subject | Subject name | String |
| Topic | Topic name | String |
| Subtopic | Subtopic name | String |
| Learning Outcome ID | Unique LOS identifier | String |
| LOS Description | Official LOS text or summary | String |
| Concept | Specific concept being tested | String |
| Importance | Tier 1-5 priority | Integer |
| Formula Required | Formula name(s) | String/Array |
| Conceptual Knowledge | Required conceptual understanding | String |
| Calculation Skill | Required calculation ability | String |
| Interpretation Skill | Required interpretation ability | String |
| Question Patterns | Applicable pattern types | Array |
| Official Practice Available | Yes/No/Unknown | Boolean |
| Original Practice Required | Yes/No | Boolean |
| My Accuracy | % correct | Float |
| My Attempts | Count | Integer |
| My Confidence | 1-5 scale | Integer |
| Status | See statuses below | Enum |

## 4.1 Status Values

| Status | Meaning | Trigger |
|--------|---------|---------|
| Not Started | Not yet attempted | Default |
| Learning | Currently studying | First engagement |
| Practicing | Active question practice | After first attempt |
| Weak | Accuracy < 60% | Performance threshold |
| Strong | Accuracy 60-79% | Performance threshold |
| Mastered | Accuracy 80%+ consistently | Multiple correct attempts |
| Retest Required | Previously weak, needs recheck | Spaced repetition trigger |

---

# 5. QUESTION BANK TAXONOMY

## 5.1 Question Metadata Structure

Every question will carry the following metadata:

| Field | Description | Values/Format |
|-------|-------------|---------------|
| Question ID | Unique identifier | Q-{SUB}-{SEQ:04d} |
| Subject | Subject area | 10 subject enum |
| Topic | Specific topic | String |
| Subtopic | Specific subtopic | String |
| Learning Outcome | LOS reference | LOS ID |
| Concept | Concept tested | String |
| Difficulty | Difficulty level | 1-5 |
| Question Type | Type classification | See types |
| Cognitive Skill | Bloom's taxonomy level | Recall/Understand/Apply/Analyze |
| Calc/Concept/Interpret | Primary skill category | Enum |
| Formula Required | Formula name | String |
| Time Target | Expected solving time (sec) | Integer |
| Source | Where question came from | String |
| Source Type | Type of source | Official/Prep Provider/Original/Candidate |
| Original vs Official | Classification | Enum |
| Pattern Tag | Question pattern type | String |
| Trap Tag | Common trap tested | String |
| Related Concepts | Linked concepts | Array |
| Explanation | Full explanation | Text |
| Correct Answer | A/B/C/D | Enum |
| Wrong-Answer Rationale | Why each wrong option is wrong | Text |
| Common Misconception | Misconception tested | Text |
| Revision Interval | Spaced repetition interval (days) | Integer |
| My Attempts | Attempt count | Integer |
| My Accuracy | % correct on this question | Float |
| My Average Time | Average time spent | Float |
| Last Attempted | Date | Date |
| Confidence | Self-rated 1-5 | Integer |
| Mastery Score | Calculated 0-100 | Float |

## 5.2 Question Types

### A. Conceptual
- Definition questions
- Principle identification
- Relationship questions
- Interpretation questions
- Comparison questions

### B. Calculation
- Direct calculation (single formula)
- Multi-step calculation
- Formula selection
- Reverse calculation (given result, find input)
- Data interpretation from tables/charts

### C. Application
- Scenario-based application
- Real-world case adaptation

### D. Analytical
- Result interpretation
- "What does this mean" questions

### E. Trap Questions
- Common mistake testing
- Unit confusion
- Sign reversal
- Convention errors (e.g., CFA FX notation)

### F. Integrated Questions
- Two+ related concepts combined
- Cross-topic integration

### G. Time-Pressure Questions
- Fast recognition and execution
- Sub-60 second target

### H. High-Difficulty Questions
- Distinguish strong preparation from memorization

## 5.3 Difficulty Levels

| Level | Name | Description | Expected Accuracy (Benchmark) |
|-------|------|-------------|------|
| 1 | Foundation | Basic recall, definition | >90% |
| 2 | Basic CFA Level I | Simple application | >80% |
| 3 | Standard CFA Level I | Typical exam question | >70% |
| 4 | Difficult | Multi-step, nuanced | >60% |
| 5 | Very Difficult | Expert-level, subtle traps | >50% |

## 5.4 Solving Time Classification

| Category | Time | Use |
|----------|------|-----|
| Rapid | <60 seconds | Simple recall, definitions |
| Standard | 60–90 seconds | Typical exam pace |
| Extended | 90–120 seconds | Multi-step calculations |
| Long | 120–180 seconds | Complex integrated problems |
| Extended Long | 180+ seconds | Mock exam only, not typical |

---

# 6. QUESTION PATTERN LIBRARY DESIGN

## 6.1 Pattern Categories

1. **Formula Identification** — "Which formula would you use?"
2. **Calculation from Given Data** — Direct computation
3. **Missing-Variable Problem** — Solve for unknown input
4. **Concept Comparison** — Compare/contrast two ideas
5. **Scenario Interpretation** — Apply concept to situation
6. **Financial Statement Adjustment** — Adjust reported figures
7. **Valuation** — Calculate asset/firm value
8. **Yield Calculation** — Various yield measures
9. **Risk Interpretation** — Identify/measure/compare risk
10. **Ethics Scenario** — Standards application
11. **"Most Likely" Question** — CFA's favorite phrasing
12. **"Least Likely" Question** — Reverse reasoning
13. **Impact of Changing One Variable** — Sensitivity analysis
14. **Multi-Step Calculation** — Sequential computation
15. **Concept + Calculation Combination** — Hybrid

## 6.2 Pattern Library Entry Format

```yaml
Pattern-{ID}:
  name: Pattern name
  examiner_intent: What the examiner is testing
  typical_wording: Common question phrasing
  required_knowledge: Knowledge prerequisites
  typical_trap: Common mistake
  difficulty: 1-5
  expected_time: seconds
  frequency: High/Medium/Low (based on official material analysis)
  example_questions: [Question IDs]
```

---

# 7. FORMULA BANK DESIGN

## 7.1 Formula Entry Structure

| Field | Description |
|-------|-------------|
| Formula ID | Unique identifier |
| Formula | Mathematical expression |
| Variable Definitions | Meaning of each variable |
| When to Use | Application contexts |
| When NOT to Use | Common misapplications |
| Units | Units of inputs/outputs |
| Rearranged Versions | Alternative forms |
| Common Mistakes | Error catalog |
| Related Formulas | Formula relationships |
| Examples | Worked examples |
| Mental Shortcut | Quick method where applicable |
| Calculator Steps | BA II Plus / HP 12C steps |
| Subject | Subject area |
| Importance | 1-5 priority |

---

# 8. ETHICS SPECIAL SYSTEM DESIGN

## 8.1 Ethics Structure

- Standard-by-standard question bank
- Each Standard (I-VII) with all sub-sections (A-D)
- Scenario library (50+ scenarios)
- Common ethical traps catalog
- "Most appropriate action" question set
- "Violation / No violation" question set
- GIPS-related question set
- Professional conduct scenario set

## 8.2 Ethics Tracking (Separate from Main Dashboard)

| Metric | Target |
|--------|--------|
| Scenario accuracy | >80% |
| Standard identification accuracy | >85% |
| Trap recognition rate | >75% |
| GIPS accuracy | >80% |

---

# 9. COVERAGE DASHBOARD DESIGN

## 9.1 Dashboard Sections

### Overall Dashboard
- Curriculum coverage %
- Question coverage %
- Pattern coverage %
- Formula coverage %
- Mock completion %
- Average accuracy
- Readiness score (0-100)

### By Subject
- Coverage %
- Accuracy %
- Weakness index
- Priority score
- Mastery status

### By Topic
- Questions attempted
- Accuracy
- Average time
- Difficulty performance
- Last revision date
- Mastery status

### Error Dashboard
- Top 10 recurring mistakes
- Top 10 weak concepts
- Top 10 slow concepts
- Top 10 high-priority concepts requiring revision

---

# 10. READINESS SCORING SYSTEM DESIGN

## 10.1 Readiness Dimensions

| # | Dimension | Weight | Measurement |
|---|-----------|--------|-------------|
| 1 | Curriculum Coverage | 15% | % of LOs covered |
| 2 | Question Coverage | 15% | % of concept patterns practiced |
| 3 | Accuracy | 20% | Weighted average accuracy |
| 4 | Difficulty Resilience | 10% | Accuracy on Difficulty 4-5 questions |
| 5 | Time Management | 10% | % questions completed within target time |
| 6 | Retention | 10% | Accuracy on retested concepts after 2+ weeks |
| 7 | Weakness Control | 10% | % of previously weak areas now resolved |
| 8 | Mock Performance | 5% | Average mock exam score |
| 9 | Ethics Readiness | 3% | Ethics scenario accuracy |
| 10 | Formula Mastery | 2% | Formula recall and application accuracy |

## 10.2 Readiness Levels

| Score Range | Level | Meaning |
|-------------|-------|---------|
| 90+ | Very Strong | High confidence of exam readiness |
| 80-89 | Strong | Well-prepared, minor gaps remain |
| 70-79 | Good | Solid foundation, targeted work needed |
| 60-69 | Developing | Significant gaps to address |
| <60 | Low | Major preparation required |

## 10.3 90% Preparation Standard

The system will report "Preparation Coverage: ~90%+" ONLY when:

- [ ] 100% Learning Outcome coverage achieved
- [ ] 90%+ important concept coverage achieved
- [ ] 90%+ question-pattern coverage achieved
- [ ] Strong performance on all high-priority topics
- [ ] No major unresolved weak topic (accuracy <50%)
- [ ] Formula mastery achieved (≥85% on formula tests)
- [ ] Ethics mastery achieved (≥80% on scenarios)
- [ ] Multiple full mocks completed (≥3)
- [ ] Consistent mock performance (score range <10% variation)
- [ ] Mistake log reviewed and resolved
- [ ] Previously weak concepts successfully retested
- [ ] Time management within acceptable range
- [ ] Adequate retention after spaced revision

---

# 11. MOCK EXAM SYSTEM DESIGN

## 11.1 Mock Exam Composition

| Source | Quantity | Purpose |
|--------|----------|---------|
| Original CFA-style questions | 5 full mocks | Primary practice |
| Pattern-targeted mocks | 3 mocks | Weakness-focused |
| Speed mocks | 2 mocks | Time management |
| Final preparation mock | 1 mock | Exam simulation |

## 11.2 Mock Exam Characteristics

Each mock should approximate:
- **Topic distribution:** Match official weights
- **Difficulty mix:** ~20% Easy, ~50% Medium, ~25% Hard, ~5% Very Hard
- **Question style:** Mix of conceptual, calculation, application
- **Time pressure:** 90 seconds per question average

## 11.3 Mock Exam Analysis Template

After each mock, generate:
- Overall score (%)
- Subject-level scores
- Topic-level scores
- Accuracy by difficulty level
- Time per question (average and distribution)
- Easy-question accuracy
- Medium-question accuracy
- Difficult-question accuracy
- Guess accuracy (self-reported)
- Careless-error rate
- Calculation-error rate
- Concept-error rate
- Strong areas identified
- Weak areas identified
- Hidden weaknesses (correct but slow/uncertain)
- High-risk topics
- Low-return topics
- Time-management problems
- Revision priorities (ranked)

---

# 12. SPACED RETEST SYSTEM DESIGN

## 12.1 Retest Progression

| Attempt | Status | Action | Interval |
|---------|--------|--------|----------|
| 1st attempt | Wrong | Add to retest queue | Retest after 1 day |
| 2nd attempt | Wrong again | Flag as weak, deeper review | Retest after 3 days |
| 2nd attempt | Correct | Promote | Retest after 7 days |
| 3rd attempt | Correct | Promote | Retest after 14 days |
| 4th attempt | Correct | Move to maintenance | Retest after 30 days |
| Maintenance | Correct | Maintain | Retest after 60 days |

## 12.2 Mastery Requirements

A concept is mastered ONLY when:
- Answered correctly on ≥3 separate occasions
- At least one correct answer was under timed conditions
- At least one correct answer was in a mixed-subject context
- Most recent attempt was correct
- Confidence rating ≥4

---

# 13. CALCULATION SKILL TRACKING DESIGN

| Skill | Measurement | Target |
|-------|-------------|--------|
| Formula Recognition | % correct formula selection | >90% |
| Calculator Execution | % correct numerical answer | >85% |
| Multi-Step Calculation | % correct on 3+ step problems | >75% |
| Interpretation | % correct interpretation of results | >85% |
| Speed | % completed within time target | >80% |

---

# 14. ACTIVE RECALL SYSTEM DESIGN

Beyond MCQs, the system will include:
- Formula recall (write the formula from memory)
- Definition recall (define key terms)
- Explain-in-your-own-words prompts
- True/False reasoning with justification
- Mini case interpretations
- "What happens if..." questions
- Error identification (find the mistake)
- Calculation without formula prompt

---

# 15. FINAL 30-DAY PROTOCOL DESIGN

### Week 4 (Days 30-23)
- Review high-weight topics (Ethics, FSA, Equity, FI)
- Complete 1 full mock
- Targeted practice on weak areas from mock

### Week 3 (Days 22-16)
- Formula recall drills daily
- Ethics scenario practice daily
- Complete 1 full mock
- Mixed-subject practice sets

### Week 2 (Days 15-8)
- Complete 2 full mocks
- Intensive weakness remediation
- Speed drills
- Error log review

### Week 1 (Days 7-1) — FINAL WEEK
- High-value formulas review
- High-risk concepts review
- Ethics final review
- Error log final pass
- Rapid recall drills
- Exam strategy review
- Time management calibration
- Confidence building
- NO new difficult material (unless major gap)

---

# 16. FILE STRUCTURE

```
cfa-level-1-system/
├── architecture/
│   └── master-blueprint.md          ← THIS FILE
├── curriculum/
│   ├── coverage-matrix.md           ← Complete curriculum matrix
│   └── learning-outcomes/           ← Per-subject LOS breakdowns
│       ├── 01-ethics.md
│       ├── 02-quantitative-methods.md
│       ├── 03-economics.md
│       ├── 04-financial-statement-analysis.md
│       ├── 05-corporate-issuers.md
│       ├── 06-equity-investments.md
│       ├── 07-fixed-income.md
│       ├── 08-derivatives.md
│       ├── 09-alternative-investments.md
│       └── 10-portfolio-management.md
├── question-bank/
│   ├── metadata-structure.md        ← Question taxonomy reference
│   └── questions/                   ← All questions by subject
│       ├── 01-ethics/
│       │   ├── standard-i.md
│       │   ├── standard-ii.md
│       │   ├── standard-iii.md
│       │   ├── standard-iv.md
│       │   ├── standard-v.md
│       │   ├── standard-vi.md
│       │   ├── standard-vii.md
│       │   └── gips.md
│       ├── 02-quantitative-methods/
│       ├── 03-economics/
│       ├── 04-financial-statement-analysis/
│       ├── 05-corporate-issuers/
│       ├── 06-equity-investments/
│       ├── 07-fixed-income/
│       ├── 08-derivatives/
│       ├── 09-alternative-investments/
│       └── 10-portfolio-management/
├── formula-bank/
│   ├── all-formulas.md              ← Complete formula reference
│   └── formula-drills.md            ← Active recall drills
├── pattern-library/
│   ├── pattern-catalog.md           ← All question patterns
│   └── trap-catalog.md              ← Common trap catalog
├── mock-exams/
│   ├── mock-1.md
│   ├── mock-2.md
│   ├── mock-3.md
│   ├── mock-4.md
│   └── mock-5.md
├── dashboard/
│   └── tracking-system.md           ← Performance tracking templates
├── protocols/
│   ├── 30-day-plan.md
│   └── 7-day-plan.md
└── README.md                        ← System overview and navigation
```

---

# 17. BUILD ORDER (Recommended Sequence)

### PHASE A — Foundation (This Phase)
1. ✅ Master Blueprint (this document)
2. Curriculum coverage matrix (all LOs mapped)
3. Question metadata structure
4. Formula bank (all formulas collected)
5. Pattern library (all patterns cataloged)

### PHASE B — Core Question Bank
6. Ethics questions (highest weight, special treatment)
7. FSA questions (high weight, calculation-heavy)
8. Fixed Income questions (high weight)
9. Equity questions (high weight)
10. Portfolio Management questions
11. Quantitative Methods questions
12. Economics questions
13. Corporate Issuers questions
14. Alternative Investments questions
15. Derivatives questions

### PHASE C — Systems
16. Mock exam construction
17. Dashboard and tracking system
18. Readiness scoring implementation
19. Final protocols (30-day, 7-day)

### PHASE D — Quality Control
20. Duplication check
21. Answer verification
22. Difficulty calibration
23. Time-target validation

---

# 18. SUCCESS CRITERIA

The system is complete when:

- [x] ✅ Architecture documented
- [ ] Every current Learning Outcome has been mapped
- [ ] Every important concept has ≥5 practice questions
- [ ] Important question patterns are represented
- [ ] Formula bank covers all required formulas
- [ ] Ethics scenario bank has ≥50 scenarios
- [ ] ≥5 full mock exams constructed
- [ ] Readiness scoring system operational
- [ ] 30-day and 7-day protocols documented
- [ ] All questions have verified answers and explanations

---

# 19. DISCLAIMERS

> **Preparation Priority Model:** The priority scores and pattern analyses in this system constitute a preparation-priority model, not a prediction of actual exam questions. No claim is made that specific questions or topics will appear on any given CFA exam.

> **Source Attribution:** Questions marked as "Original CFA-style practice question" are original creations designed to test the same concepts as the official CFA Institute curriculum. They are not actual CFA Institute questions and should not be treated as such.

> **Official Material:** Where official CFA Institute practice questions or mock exams are incorporated, they are used in accordance with fair use principles for educational purposes. Large-scale reproduction of copyrighted CFA Institute material is not performed.

---

*End of Master Blueprint*
