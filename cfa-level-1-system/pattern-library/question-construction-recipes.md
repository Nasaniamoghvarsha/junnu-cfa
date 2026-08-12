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

### 2.4 TEMPLATE: "Which Standard Is Violated?"

**Recognition Signature:**
- Setup describes a professional situation
- Pivot: "Has [person] most likely violated..." or "Which Standard..."
- Options are Standard references (I(A), II(B), etc.) or Yes/No with reasoning
- Key trap: multiple Standards COULD apply but ONE is clearly primary

### 2.5 TEMPLATE: Adjustment/Reconciliation

**Recognition Signature:**
- Setup gives reported/starting value
- Provides an adjustment factor
- Pivot: "After adjusting for X, Y would be..."
- Tests whether you know WHAT to adjust and in WHICH DIRECTION

---

## 3. SUBJECT-SPECIFIC RECIPES 

Here are the specific ways CFA constructs questions by subject.

### 3.1 ETHICS (2 Recipes)

**RECIPE 1: The "Dual Role" Conflict**
- **SETUP**: An analyst has personal investments/roles that conflict with their employer/clients. They disclose it to *someone* but not *everyone*, or they trade based on a specific timeline.
- **PIVOT**: "Has the analyst violated the Standards regarding..."
- **OPTIONS**:
  - *Option A (Trap)*: No, because they disclosed to employer. (Trap: Client disclosure missing).
  - *Option B (Trap)*: Yes, violated Independence & Objectivity. (Trap: It's actually a Priority of Transactions issue).
  - *Option C (Correct)*: Yes, violated Priority of Transactions.

**RECIPE 2: The Mosaic Theory Boundary**
- **SETUP**: Analyst collects public data (earnings, economic reports) and non-material non-public data (observing a parking lot, chatting with a supplier). They combine it to issue a "Strong Buy".
- **PIVOT**: "The analyst's action is most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: A violation of Material Nonpublic Information because they used non-public data. (Trap: Ignores that it was *non-material*).
  - *Option B (Trap)*: A violation of Diligence and Reasonable Basis. (Trap: Misdiagnosing the core issue).
  - *Option C (Correct)*: Not a violation, because it relies on the Mosaic Theory.

**WORKED EXAMPLE (Ethics):**
*Setup*: Sarah, a portfolio manager, overhears a CEO at a coffee shop say their upcoming earnings will miss expectations. She confirms with public sector data that the industry is struggling. She shorts the stock. 
*Pivot*: Did Sarah violate Standard II(A) Material Nonpublic Information?
*Answer*: Yes. The coffee shop tip is material (earnings miss) and nonpublic. The public sector data doesn't cleanse the insider info. The trap option would say "No, under Mosaic Theory" because she used public data too.

### 3.2 QUANTITATIVE METHODS (3 Recipes)

**RECIPE 1: The Time Value of Money Disconnect**
- **SETUP**: You need to value a series of cash flows, but the payment frequency doesn't match the compounding frequency, or the start date is deferred (e.g., first payment in Year 4).
- **PIVOT**: "The present value of the investment is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Calculates PV using $n$ periods without deferring back to Year 0.
  - *Option B (Trap)*: Uses annual rate instead of periodic rate.
  - *Option C (Correct)*: Uses correct rate and discounts back to Year 0.

**RECIPE 2: Hypothesis Testing Interpretation**
- **SETUP**: Gives a test statistic, a critical value, and a p-value.
- **PIVOT**: "The analyst should most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: Reject null because test stat > p-value. (Trap: Mixing metrics).
  - *Option B (Trap)*: Fail to reject null because test stat < critical value, proving the null is true. (Trap: You can never *prove* the null, only fail to reject).
  - *Option C (Correct)*: Reject null because test stat > critical value.

**RECIPE 3: Probability Tree Calculation**
- **SETUP**: Provides a base probability (e.g., economy booms 60%) and conditional probabilities (e.g., stock rises 80% if boom, 30% if bust).
- **PIVOT**: "The unconditional probability of the stock rising is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Uses only the 80% (ignoring the economic weighting).
  - *Option B (Trap)*: Multiplies 0.60 * 0.80 and stops. (Trap: Forgot the other branch).
  - *Option C (Correct)*: (0.60 * 0.80) + (0.40 * 0.30) = 0.60.

**WORKED EXAMPLE (Quant):**
*Setup*: A project pays $10,000 annually for 5 years, starting at the end of Year 3. Discount rate is 8%.
*Pivot*: PV today is closest to?
*Options & Catch*: 
- Calculate $PMT=10k, I/Y=8, N=5 \rightarrow PV_2 = 39,927$. (Trap: Option A is $39,927. Forgot to discount to Year 0). 
- Discount $39,927$ back 3 years instead of 2. (Trap: Option B is $31,695$).
- *Correct*: Discount back 2 years: $39,927 / 1.08^2 = 34,231$.

### 3.3 ECONOMICS (2 Recipes)

**RECIPE 1: Market Structure Identification**
- **SETUP**: Describes a firm's pricing power, barriers to entry, and product differentiation.
- **PIVOT**: "The market structure is best described as:"
- **OPTIONS**:
  - *Option A (Trap)*: Perfect competition. (Trap: Setup mentions some differentiation).
  - *Option B (Trap)*: Monopoly. (Trap: Setup mentions low barriers).
  - *Option C (Correct)*: Monopolistic competition.

**RECIPE 2: Macroeconomic Policy Effect**
- **SETUP**: Central bank buys bonds in the open market.
- **PIVOT**: "The most likely impact on interest rates and domestic currency is:"
- **OPTIONS**:
  - *Option A (Trap)*: Rates ↑, Currency appreciates. (Trap: Reverse effect).
  - *Option B (Trap)*: Rates ↓, Currency appreciates. (Trap: Half right, but lower rates depreciate currency).
  - *Option C (Correct)*: Rates ↓, Currency depreciates.

**WORKED EXAMPLE (Econ):**
*Setup*: An economy is in a recession. The government increases spending (expansionary fiscal) and the central bank sells securities (contractionary monetary).
*Pivot*: The impact on interest rates will most likely be:
*Options & Catch*:
- A) Decrease. (Trap: Assumes expansionary fiscal lowers rates).
- B) Ambiguous. (Trap: Thinks they offset).
- C) *Correct*: Increase. Both actions drive interest rates up (government borrowing increases demand for funds; central bank selling reduces money supply).

### 3.4 FINANCIAL STATEMENT ANALYSIS (3 Recipes)

**RECIPE 1: The LIFO/FIFO Adjustment**
- **SETUP**: Gives LIFO inventory, LIFO reserve, and tax rate.
- **PIVOT**: "If the firm had used FIFO, retained earnings would be higher by:"
- **OPTIONS**:
  - *Option A (Trap)*: The full LIFO reserve. (Trap: Forgot taxes).
  - *Option B (Trap)*: LIFO reserve * Tax Rate. (Trap: This is the tax hit, not the RE increase).
  - *Option C (Correct)*: LIFO reserve * (1 - Tax Rate).

**RECIPE 2: Cash Flow Categorization (US GAAP vs IFRS)**
- **SETUP**: Firm pays interest, receives dividends, and pays taxes.
- **PIVOT**: "Under IFRS, cash flow from operations (CFO) is most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: Treats all as CFO. (Trap: This is US GAAP).
  - *Option B (Trap)*: Puts taxes in financing. (Trap: Taxes are always operating unless specifically tied to an investing/financing transaction).
  - *Option C (Correct)*: Recognizes IFRS flexibility (e.g., interest paid can be CFO or CFF).

**RECIPE 3: Capitalizing vs. Expensing**
- **SETUP**: A firm capitalizes an expenditure instead of expensing it.
- **PIVOT**: "In the first year, the impact on CFO and net income is most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: CFO lower, NI lower. (Trap: Direction error).
  - *Option B (Trap)*: CFO unchanged, NI higher. (Trap: Missed CFO impact).
  - *Option C (Correct)*: CFO higher (outflow moves to CFI), NI higher (only depreciation hits year 1).

**WORKED EXAMPLE (FSA):**
*Setup*: A firm using LIFO reports Inventory of $500, LIFO Reserve of $50. Tax rate is 20%.
*Pivot*: What is the adjusted FIFO equity?
*Catch*: 
- Add $50 to Equity. (Trap: Forgot tax).
- *Correct*: Add $50 * (1 - 0.20) = $40 to Equity. 

### 3.5 CORPORATE ISSUERS (2 Recipes)

**RECIPE 1: WACC with Flawed Data**
- **SETUP**: Gives target capital structure, current capital structure, cost of equity, and YTM of debt.
- **PIVOT**: "The WACC is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Uses current structure instead of target weights.
  - *Option B (Trap)*: Uses coupon rate instead of YTM for cost of debt.
  - *Option C (Correct)*: Uses target weights, YTM, and applies (1-T) to debt.

**RECIPE 2: NPV / IRR Conflict**
- **SETUP**: Two mutually exclusive projects. Project A has higher NPV but lower IRR than Project B.
- **PIVOT**: "The firm should most likely choose:"
- **OPTIONS**:
  - *Option A (Trap)*: Project B because IRR is higher. (Trap: Ignores mutually exclusive rule).
  - *Option B (Trap)*: Both projects. (Trap: Misses 'mutually exclusive').
  - *Option C (Correct)*: Project A because NPV always rules for mutually exclusive projects.

**WORKED EXAMPLE (Corp Issuers):**
*Setup*: Target Debt/Equity = 1. (Meaning weights are 50/50). Cost of equity = 12%. Cost of debt (pre-tax YTM) = 6%. Tax = 25%.
*Pivot*: WACC is closest to?
*Catch*: Option A uses 1 instead of 0.5 for weights. Option B forgets the tax shield on debt (0.5 * 12% + 0.5 * 6% = 9%). *Correct* Option C uses tax shield: 0.5(12%) + 0.5(6% * 0.75) = 8.25%.

### 3.6 EQUITY INVESTMENTS (2 Recipes)

**RECIPE 1: Gordon Growth Model (DDM) Disguise**
- **SETUP**: Gives EPS, payout ratio, required return (r), and ROE.
- **PIVOT**: "The intrinsic value of the stock is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Uses $E_1$ instead of $D_1$.
  - *Option B (Trap)*: Calculates $g = ROE \times \text{Retention}$, but uses $D_0$ in the numerator without multiplying by $(1+g)$.
  - *Option C (Correct)*: Calculates $g$, finds $D_1 = D_0(1+g)$, applies $V = D_1 / (r - g)$.

**RECIPE 2: Index Weighting Impact**
- **SETUP**: A price-weighted index and a market-cap-weighted index. A high-price, low-market-cap stock splits 2-for-1.
- **PIVOT**: "The impact on the indices is most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: Both change. (Trap: Stock splits don't change market cap).
  - *Option B (Trap)*: Market-cap index drops. (Trap: Confuses price weighting with cap weighting).
  - *Option C (Correct)*: Price-weighted divisor adjusts, cap-weighted is unaffected.

**WORKED EXAMPLE (Equity):**
*Setup*: Current dividend $D_0 = \$2.00$. ROE = 15%, payout ratio = 40%. Required return = 10%.
*Pivot*: Value is closest to?
*Catch*: 
- Calc $g = 15\% \times (1-0.4) = 9\%$. 
- Trap 1: $2.00 / (0.10 - 0.09) = 200$. (Used $D_0$).
- *Correct*: $D_1 = 2.00(1.09) = 2.18$. Value = $2.18 / 0.01 = 218$.

### 3.7 FIXED INCOME (3 Recipes)

**RECIPE 1: The Matrix Pricing / Interpolation**
- **SETUP**: Given yields for 2-year and 5-year bonds. You need to price a 3-year illiquid bond.
- **PIVOT**: "The estimated yield for the 3-year bond is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Simple average of the two yields. (Trap: Ignores the time weighting).
  - *Option B (Trap)*: Incorrect interpolation math.
  - *Option C (Correct)*: Linear interpolation based on distance in years.

**RECIPE 2: Price / Yield / Maturity Relationship**
- **SETUP**: A premium bond and a discount bond with the same maturity and YTM.
- **PIVOT**: "As they approach maturity, assuming constant YTM, the prices will most likely:"
- **OPTIONS**:
  - *Option A (Trap)*: Both increase. (Trap: Misses premium pull-to-par).
  - *Option B (Trap)*: Premium increases, discount decreases. (Trap: Reversed).
  - *Option C (Correct)*: Premium decreases, discount increases (pull-to-par effect).

**RECIPE 3: Duration / Convexity Price Change**
- **SETUP**: Bond has duration of 5, convexity of 40. Yield increases by 100 bps.
- **PIVOT**: "The percentage change in price is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: -5.0%. (Trap: Ignored convexity).
  - *Option B (Trap)*: -4.6%. (Trap: Forgot the 0.5 in convexity formula, or didn't square the yield change).
  - *Option C (Correct)*: Calculates $-D(\Delta y) + 0.5 \times C \times (\Delta y)^2$.

**WORKED EXAMPLE (Fixed Income):**
*Setup*: ModDur = 6.0, Convexity = 50. Yield drops by 200 bps (0.02).
*Pivot*: Price change is closest to?
*Catch*: 
- Duration only: $-6 \times (-0.02) = +12.0\%$. (Trap).
- *Correct*: $+12.0\% + 0.5 \times 50 \times (-0.02)^2 = 12.0\% + 1.0\% = +13.0\%$.

### 3.8 DERIVATIVES (2 Recipes)

**RECIPE 1: Forward Pricing (No Arbitrage)**
- **SETUP**: Spot price, risk-free rate, and storage costs/convenience yield.
- **PIVOT**: "The no-arbitrage forward price is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Subtracts storage costs. (Trap: Storage costs *increase* forward price).
  - *Option B (Trap)*: Adds convenience yield. (Trap: Convenience yield *decreases* forward price).
  - *Option C (Correct)*: Spot + FV(Storage) - FV(Convenience).

**RECIPE 2: Option Value Boundaries**
- **SETUP**: American vs European calls/puts.
- **PIVOT**: "Which of the following is most accurate regarding the option premium?"
- **OPTIONS**:
  - *Option A (Trap)*: American call is always > European call. (Trap: Only true if dividend-paying).
  - *Option B (Trap)*: European put > American put. (Trap: American is always $\geq$).
  - *Option C (Correct)*: Identifies the correct boundary conditions.

**WORKED EXAMPLE (Derivatives):**
*Setup*: Spot = $1,000. Risk-free rate = 5%. PV of dividends = $20. 1-year forward contract.
*Pivot*: Forward price is closest to?
*Catch*: Option A ignores dividends ($1000 \times 1.05 = 1050$). Option B adds dividends. *Correct* Option C subtracts PV of dividends before compounding: $(1000 - 20) \times 1.05 = 1029$.

### 3.9 ALTERNATIVE INVESTMENTS (1 Recipe)

**RECIPE 1: Fee Structure Cascade**
- **SETUP**: Hedge fund has 2/20 fee structure, hard hurdle rate of 5%, high-water mark. Start value $100M, End value $110M.
- **PIVOT**: "The total fees earned by the manager are closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Calculates 20% on the whole $10M gain. (Trap: Ignored hurdle rate).
  - *Option B (Trap)*: Calculates incentive fee before deducting management fee (if independent).
  - *Option C (Correct)*: Management fee = $2.2M (based on end value or start depending on setup). Hurdle = $5M. Incentive = 20% of ($110M - $100M - $5M) = $1M. Total = $3.2M.

**WORKED EXAMPLE (Alts):**
*Setup*: $100M fund, 2% management fee (on year-end value), 20% incentive fee with a hard hurdle of 4%. Year-end value is $110M. Fees are calculated independently.
*Pivot*: Total fees?
*Catch*: 
- Mgmt Fee = $110M \times 2\% = \$2.2M$.
- Return = $10M$. Hurdle = $100M \times 4\% = \$4M$.
- Profit above hurdle = $10M - 4M = \$6M$.
- Incentive = $6M \times 20\% = \$1.2M$.
- Total = $3.4M$. 
- Trap: Deducting mgmt fee before calculating incentive fee (would only do this if net of fee is specified).

### 3.10 PORTFOLIO MANAGEMENT (2 Recipes)

**RECIPE 1: CAPM vs. SML vs. CML**
- **SETUP**: A portfolio has a standard deviation of 15% and beta of 1.2. Market return is 10%, RF is 3%.
- **PIVOT**: "The required return based on the CAPM is:"
- **OPTIONS**:
  - *Option A (Trap)*: Uses standard deviation instead of beta. (Trap: Confuses CML with SML).
  - *Option B (Trap)*: Multiplies beta by market return ($1.2 \times 10\% = 12\%$). (Trap: Forgot to subtract RF to get premium).
  - *Option C (Correct)*: $3\% + 1.2(10\% - 3\%) = 11.4\%$.

**RECIPE 2: Portfolio Variance Expansion**
- **SETUP**: Two stocks, weights 60/40, standard deviations 20% and 30%, correlation 0.5.
- **PIVOT**: "The portfolio standard deviation is closest to:"
- **OPTIONS**:
  - *Option A (Trap)*: Simple weighted average ($0.6 \times 20\% + 0.4 \times 30\% = 24\%$). (Trap: Ignored diversification benefit).
  - *Option B (Trap)*: Forgets the '2' in the $2w_1w_2\sigma_1\sigma_2\rho$ term.
  - *Option C (Correct)*: Properly calculates variance, then remembers to square root it for standard deviation.

**WORKED EXAMPLE (Portfolio Mgmt):**
*Setup*: $W_A = 0.5, W_B = 0.5. \sigma_A = 10\%, \sigma_B = 20\%. \rho = 0.$
*Pivot*: Portfolio standard deviation?
*Catch*: 
- Trap 1: Weighted average = 15%.
- *Correct*: Variance = $0.5^2(0.10)^2 + 0.5^2(0.20)^2 + 0 = 0.0025 + 0.01 = 0.0125$. 
- Standard deviation = $\sqrt{0.0125} = 11.18\%$.

---

## 6. ANTI-MEMORIZATION SAFEGUARDS

### 6.1 Questions to Never Trust

If you find yourself thinking any of these, you're memorizing, not learning:

| Thought | Why It's Dangerous | What To Do Instead |
|---------|-------------------|-------------------|
| "I've seen this exact question" | CFA changes numbers | Find the pattern, not the question |
| "The answer was B last time" | Answers change with numbers | Learn the reasoning, not the letter |
| "This is the same as Kaplan Q47" | Different source, different framing | Map it to a CFA LOS, not a source |
| "I remember the answer is $37.14" | Numbers will be different | Remember D₁/(r-g), not the output |
| "This topic always has 2 calculation Qs" | Topic weights shift | Prepare for any number of questions |

### 6.2 The "Prove You Understand" Test

For any concept you think you've mastered, answer these:

1. **What happens if the numbers double?** Can you recalculate?
2. **What happens in reverse?** Can you solve for the input instead of output?
3. **What's the most common wrong answer?** Can you identify the trap?
4. **When does this formula NOT apply?** Can you identify boundaries?
5. **How would you explain this to someone who keeps getting it wrong?** Can you teach it?

If you can't answer all 5, you don't understand the concept — you've only memorized a specific question.

---

*End of Question Construction Recipe Book*
