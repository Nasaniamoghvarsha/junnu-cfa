# CFA Level I — Question Pattern Library

> **Purpose:** Catalog all recurring question structures across CFA Level I topics. Learn the *template*, not the *question* — so you can solve ANY question built from it.

---

## THE 20 CFA QUESTION PATTERNS

---

### PATTERN 1: FORMULA IDENTIFICATION
**Examiner Intent:** Can you identify WHICH formula applies to this specific context?  
**Typical Wording:** "Which of the following would be most appropriate to use when..."  
**5-Second Recognition:** Multiple formulas offered as options — context tells you which applies  
**Speed Target:** 45 seconds (recognition, no calculation needed)

**Worked Example:**
> An analyst wants to measure the riskiness of a portfolio that consists of only 2 assets where the assets may be correlated. Which measure would be most appropriate?
> A) Standard deviation of each asset added together
> B) Portfolio variance using the 2-asset formula with covariance
> C) Beta of the portfolio

**Answer: B** — correlation/covariance drives portfolio risk; simple addition ignores diversification.

**Wrong option traps:** A forgets correlation; C is for systematic risk only, not total portfolio risk.

---

### PATTERN 2: DIRECT CALCULATION
**Examiner Intent:** Execute a formula correctly given all inputs.  
**Typical Wording:** "...is closest to:"  
**5-Second Recognition:** All numbers given, question is numerical, options are numerical  
**Speed Target:** 75 seconds (setup + calculator + verify)

**Worked Example:**
> An investor deposits $1,000/month into an account earning 6% annually (0.5%/month) for 10 years (120 months). The future value is closest to:
> A) $120,000  B) $163,879  C) $179,084

**Answer: B** — FV Ordinary Annuity: N=120, I/Y=0.5%, PMT=1000, PV=0 → FV=$163,879

**Wrong option traps:** A is the naive sum (no compounding); C uses annual rate without converting to monthly.

---

### PATTERN 3: MISSING-VARIABLE PROBLEM
**Examiner Intent:** Rearrange a formula to solve for an unknown.  
**Typical Wording:** "Given X and Y, the Z is closest to:"  
**5-Second Recognition:** Some variables given, asked for a different one — requires algebra or calculator's compute function  
**Speed Target:** 90 seconds

**Worked Example:**
> An investment of $5,000 grows to $8,811.71 over 8 years with annual compounding. The annual interest rate is closest to:
> A) 6.5%  B) 7.3%  C) 8.0%

**Answer: C** — Solve: (8811.71/5000)^(1/8) − 1 = (1.7623)^(0.125) − 1 = 0.08 = **8.0%**

**Calculator approach:** N=8, PV=−5000, FV=8811.71, PMT=0 → CPT I/Y = 8.0%

---

### PATTERN 4: CONCEPT COMPARISON
**Examiner Intent:** Know the relationship between two similar but distinct concepts.  
**Typical Wording:** "Compared to X, Y is most likely..."  
**5-Second Recognition:** Two concepts being compared; no numbers needed  
**Speed Target:** 45 seconds

**Worked Example:**
> Compared to Macaulay duration, modified duration is best described as:
> A) A measure of time-weighted cash flows
> B) A measure of interest rate sensitivity
> C) Always longer in duration

**Answer: B** — Macaulay = time-weighted average; Modified = price sensitivity. ModDur = MacDur/(1+y)

**Memory aid:** Mac = Time; Mod = Sensitivity. Mod is always slightly LESS than Mac.

---

### PATTERN 5: SCENARIO INTERPRETATION
**Examiner Intent:** Apply a concept to a described real-world situation.  
**Typical Wording:** "Given the following scenario..." then asks for a conclusion  
**5-Second Recognition:** Long vignette; question asks "what should happen" or "what is the violation"  
**Speed Target:** 90 seconds (read carefully, identify the key fact)

**Worked Example:**
> A portfolio manager at XYZ Capital reads an analyst's independent research note that a pharmaceutical company's drug trial is likely to fail. The manager sells the stock before the results are announced. Has the manager violated any CFA Standard?
> A) Yes, violation of Standard II(A) Material Nonpublic Information
> B) No, because the analyst's research is based on publicly available information
> C) No, because the manager did not communicate with company insiders

**Answer: B** — Mosaic theory: combining non-material nonpublic + public info is permitted.

**Trap:** The "non-material" qualifier matters. Drug trial *likely* to fail ≠ definitive inside information.

---

### PATTERN 6: FINANCIAL STATEMENT ADJUSTMENT
**Examiner Intent:** Can you adjust reported figures to reflect economic reality?  
**Typical Wording:** "After adjusting for..., the [ratio/figure] would be..."  
**5-Second Recognition:** Question involves LIFO→FIFO, operating/finance lease, capitalization vs. expensing  
**Speed Target:** 90 seconds

**Worked Example:**
> A company reports under LIFO with inventory of $400K and a LIFO reserve of $75K. If converted to FIFO, the current ratio would most likely:
> A) Decrease  B) Remain unchanged  C) Increase

**Answer: C** — FIFO inventory = LIFO + Reserve = $475K → Current assets increase → Current ratio increases

**Trap:** Students forget the LIFO reserve is added, not subtracted. In rising prices, LIFO always understates inventory vs. FIFO.

---

### PATTERN 7: VALUATION
**Examiner Intent:** Calculate intrinsic value from model inputs.  
**Typical Wording:** "The intrinsic value per share is closest to:"  
**5-Second Recognition:** Dividend or cash flow given + growth rate + discount rate → GGM or DDM or DCF  
**Speed Target:** 75 seconds

**Worked Example:**
> A firm just paid a dividend of $2.00 (D₀). Dividends are expected to grow at 5% indefinitely. The required return on equity is 9%. The intrinsic value is closest to:
> A) $47.50  B) $52.50  C) $40.00

**Answer: B** — D₁ = 2.00 × 1.05 = $2.10. V₀ = 2.10/(0.09−0.05) = 2.10/0.04 = **$52.50**

**Trap A:** Uses D₀ instead of D₁ → gets $2.00/0.04 = $50.00 (close but wrong)  
**Trap C:** Wrong denominator (uses 0.09 instead of 0.04)

---

### PATTERN 8: YIELD CALCULATION
**Examiner Intent:** Compute or compare yield measures for fixed income.  
**Typical Wording:** "The [yield measure] is closest to:"  
**5-Second Recognition:** Bond/money market security given; asked for current yield, YTM, BEY, or similar  
**Speed Target:** 75 seconds

**Worked Example:**
> A 4% coupon bond (semi-annual) matures in 5 years and is priced at $950. The yield to maturity is closest to:
> A) 4.00%  B) 5.07%  C) 5.30%

**Answer: B** — N=10, PV=−950, FV=1000, PMT=20 → CPT I/Y = 2.53% × 2 = **5.07%** (BEY)

**Trap C:** Uses PMT=40 (annual) instead of 20 (semi-annual); Trap A: confuses coupon rate with YTM.

---

### PATTERN 9: RISK INTERPRETATION
**Examiner Intent:** Identify, measure, and compare risk types.  
**Typical Wording:** "Which has the highest/lowest [risk measure]?"  
**5-Second Recognition:** Multiple securities being compared by risk; or asked which risk measure to use  
**Speed Target:** 60 seconds

**Worked Example:**
> Two funds: Fund A has Sharpe=0.80, Treynor=12; Fund B has Sharpe=0.60, Treynor=15. For an investor evaluating funds as the ONLY investment, which metric is appropriate and which fund is better?
> A) Sharpe; Fund A  B) Treynor; Fund B  C) Sharpe; Fund B

**Answer: A** — As the only investment, TOTAL risk matters → Sharpe. Fund A Sharpe=0.80 > 0.60.

**Trap B:** Treynor is for a component of a diversified portfolio, not the only investment.

---

### PATTERN 10: ETHICS SCENARIO
**Examiner Intent:** Apply one or more specific CFA Standards to a professional situation.  
**Typical Wording:** "Does [person] most likely violate Standard..." or "What should [person] do?"  
**5-Second Recognition:** A person's action is described; asked whether it violates a standard  
**Speed Target:** 90 seconds (read carefully — focus on the specific standard mentioned)

**Worked Example:**
> An analyst receives a $500 gift from a company whose stock she covers. Local law in her country allows this. Her firm's policy prohibits gifts over $100 without written disclosure. She accepts the gift and discloses it in writing to her manager. Has she violated any Standard?
> A) Yes, Standard I(B) — accepting compromises independence
> B) Yes, Standard IV(A) — the firm policy was violated by accepting the gift
> C) No, she disclosed in writing which satisfies both standards

**Answer: C** — Strictest standard applies (firm policy at $100) but she disclosed in writing. Written disclosure satisfies Standard I(B). No violation if disclosed.

**Trap A:** Gifts don't automatically compromise independence; disclosure is the key. **Trap B:** She DID comply with firm policy (disclosure was required, not refusal).

---

### PATTERN 11: "MOST LIKELY" QUESTION
**Examiner Intent:** Test precise, nuanced knowledge — multiple answers may be plausible.  
**Typical Wording:** "...is MOST LIKELY..."  
**5-Second Recognition:** The qualifier "most likely" means the correct answer is "most" correct, not "always" correct  
**Speed Target:** 60 seconds

**Key Rule:** Eliminate clearly wrong answers first. Between two plausible answers, ask: which is ALWAYS true vs. usually true?

**Worked Example:**
> A Treasury bond has a longer maturity than a corporate bond with the same coupon rate. The Treasury bond most likely has:
> A) Lower yield due to lower default risk
> B) Higher interest rate risk
> C) Both A and B

**Answer: C** — Both statements are true. But if only one answer is provided, B is the "most likely" unique feature since A is obvious from risk structure.

---

### PATTERN 12: "LEAST LIKELY" QUESTION
**Examiner Intent:** Find the FALSE statement among plausible-sounding options.  
**Typical Wording:** "...is LEAST LIKELY to..."  
**5-Second Recognition:** Reverse framing — you must find what is WRONG  
**Speed Target:** 60 seconds

**Critical Habit:** Circle or underline "least" before reading options. Change your mental filter from "true?" to "false?".

**Worked Example:**
> Which of the following is LEAST LIKELY a characteristic of a perfectly competitive market?
> A) Many buyers and sellers  B) Differentiated products  C) Free entry and exit

**Answer: B** — Differentiated products are a characteristic of monopolistic competition, NOT perfect competition (which requires homogeneous products).

---

### PATTERN 13: IMPACT OF CHANGING ONE VARIABLE
**Examiner Intent:** Directional sensitivity — what happens when an input changes?  
**Typical Wording:** "If X increases, [result] will most likely..."  
**5-Second Recognition:** One variable changes; asked for direction of impact on another  
**Speed Target:** 60 seconds

**Worked Example:**
> All else equal, if the yield to maturity of a bond increases, the bond's modified duration will most likely:
> A) Increase  B) Decrease  C) Remain unchanged

**Answer: B** — Higher yield → higher discount rate → less time-weighted PV contribution from distant cash flows → shorter effective duration. (Exception: zero-coupon bonds, where duration = maturity regardless.)

---

### PATTERN 14: MULTI-STEP CALCULATION
**Examiner Intent:** Chain 2–4 calculations; getting any step wrong cascades to wrong answer.  
**Typical Wording:** Implicit — setup requires intermediate calculations  
**5-Second Recognition:** Multiple data points that must be processed sequentially  
**Speed Target:** 120 seconds

**Worked Example:**
> A stock has a beta of 1.2, the risk-free rate is 3%, the market risk premium is 6%. If the stock's current price is $50 and it paid a $1.50 dividend last year (D₀), growing at 4%, is the stock overvalued or undervalued?
> A) Overvalued — market price exceeds intrinsic value
> B) Undervalued — intrinsic value exceeds market price
> C) Fairly valued

**Step 1 — Required return (CAPM):** r = 3 + 1.2×6 = 10.2%  
**Step 2 — D₁:** 1.50 × 1.04 = $1.56  
**Step 3 — Intrinsic value (GGM):** V₀ = 1.56/(0.102−0.04) = 1.56/0.062 = $25.16  
**Step 4 — Compare:** $50 market > $25.16 intrinsic → **Overvalued → Answer A**

---

### PATTERN 15: CONCEPT + CALCULATION COMBINATION
**Examiner Intent:** Must get both the calculation AND its interpretation correct.  
**5-Second Recognition:** Asks "calculate X AND interpret" or offers calculated values with interpretations as options  
**Speed Target:** 90 seconds

**Worked Example:**
> A simple regression of monthly stock returns on market returns yields b₀=0.5%, b₁=1.3, R²=0.72. Which of the following best describes the regression output?
> A) The stock has alpha of 0.5% and explains 72% of the variation in market returns
> B) The stock's returns vary 1.3 times with the market, with 72% of the stock's variation explained by market returns
> C) The stock has a correlation with the market of 72%

**Answer: B** — b₁=beta (sensitivity), R²=proportion of stock's variance explained by market. Correlation = √0.72 = 0.85, not 0.72.

---

### PATTERN 16: BOND PRICE-YIELD RELATIONSHIP
**Examiner Intent:** Apply the fundamental inverse relationship between bond prices and yields.  
**Typical Wording:** "If interest rates rise by 50 basis points, the bond price will..."  
**5-Second Recognition:** Given duration/convexity + yield change → calculate price impact  
**Speed Target:** 90 seconds

**Worked Example:**
> A bond has Modified Duration = 7.2 and Convexity = 85. Yields fall by 100 bps (1%). The approximate percentage price change is:
> A) +7.20%  B) +7.625%  C) +8.20%

**Answer: B** — %ΔP ≈ −(7.2)(−0.01) + ½(85)(0.01)² = +0.072 + 0.00425 = **+7.625%**

**Trap A:** Ignores convexity adjustment. Note: convexity ALWAYS adds to price for option-free bonds.

---

### PATTERN 17: STATISTICAL HYPOTHESIS TESTING
**Examiner Intent:** Choose the right test, interpret the result correctly.  
**Typical Wording:** "The appropriate test statistic is..." or "At the 5% significance level..."  
**5-Second Recognition:** H₀ and H₁ given; sample statistics provided  
**Speed Target:** 90 seconds

**Decision Framework:**
```
σ² known + large n  → z-test
σ² unknown           → t-test (df = n−1)
Test variance         → χ² test (1 sample)
Compare variances     → F-test (2 samples)
```

**Worked Example:**
> A portfolio manager tests whether active return differs from zero. She has 36 months of data with mean active return 0.4%/month and standard deviation 1.8%/month. The test statistic and conclusion at 5% significance (critical t ≈ ±2.03, df=35) are:
> A) t=1.33; fail to reject H₀
> B) t=2.07; reject H₀ — return is significantly different from zero  
> C) z=2.07; reject H₀

**Answer: A** — t = 0.4/(1.8/√36) = 0.4/0.3 = 1.33 < 2.03 → **Fail to reject H₀**

**Trap B:** Miscalculates SE; **Trap C:** n=36 but σ² unknown → use t, not z.

---

### PATTERN 18: ETHICS CONFLICT-OF-INTEREST SCENARIO
**Examiner Intent:** Identify conflicts of interest and the required disclosure/action.  
**5-Second Recognition:** Multiple relationships or payments described; asked about disclosure requirements  
**Speed Target:** 90 seconds

**Worked Example:**
> A sell-side analyst receives $5,000/quarter from a company for providing investor relations consulting. She issues a BUY recommendation on the company's stock. Which action is MOST appropriate?
> A) Refuse the consulting payment to maintain independence
> B) Disclose the payment arrangement to clients and employer in the research report
> C) Issue the BUY only if her analysis independently supports it, with no disclosure needed if her view is genuine

**Answer: B** — Standard VI(A): Disclose conflicts. The analyst need not refuse the fee, but MUST disclose. Genuine belief doesn't eliminate the disclosure obligation.

---

### PATTERN 19: ALTERNATIVE INVESTMENT FEE CALCULATION
**Examiner Intent:** Calculate net returns after management fees and incentive fees.  
**Typical Wording:** "The investor's net return after all fees is closest to:"  
**5-Second Recognition:** "2-and-20" fee structure, high-water mark, hurdle rate  
**Speed Target:** 90 seconds

**Worked Example:**
> A hedge fund uses a 2% management fee (on beginning NAV) and 20% incentive fee (above 8% hurdle). Beginning NAV = $100M. Gross return = 18%. What is the net return to investors?
> A) 13.4%  B) 13.8%  C) 14.2%

**Step 1 — Gross gain:** $100M × 18% = $18M. New NAV = $118M  
**Step 2 — Management fee:** $100M × 2% = $2M. NAV = $116M  
**Step 3 — Hurdle:** $100M × 8% = $8M. Return above hurdle = $10M  
**Step 4 — Incentive fee:** $10M × 20% = $2M. NAV = $114M  
**Step 5 — Net return:** ($114M − $100M)/$100M = **14.0%**

Closest to: **C (14.2%)** — minor rounding differences in order of operations.

---

### PATTERN 20: PORTFOLIO RISK-RETURN DOMINANCE
**Examiner Intent:** Identify which portfolio is superior under mean-variance framework.  
**Typical Wording:** "Which portfolio is MOST efficient?" or "Portfolio X dominates Portfolio Y if..."  
**5-Second Recognition:** Multiple portfolios shown with return and risk; asked to identify dominant one  
**Speed Target:** 60 seconds

**Dominance Rule:**
```
Portfolio A dominates B if:
  E(R_A) ≥ E(R_B) AND σ_A < σ_B  (same/better return, less risk)
  OR
  E(R_A) > E(R_B) AND σ_A ≤ σ_B  (higher return, same/less risk)
```

**Worked Example:**
> Three portfolios: X(10%, 15%), Y(10%, 18%), Z(12%, 15%). Which statement is most accurate?
> A) X dominates Y; Z dominates X  
> B) Z dominates both X and Y  
> C) None dominate; all are on the efficient frontier

**Answer: A** — X vs Y: Same return, X has lower risk → X dominates Y. Z vs X: Same risk, Z has higher return → Z dominates X. Y is dominated → NOT on efficient frontier.

---

## PATTERN-BY-SUBJECT MAPPING

### Which patterns dominate by subject:

| Subject | Top Patterns |
|---------|-------------|
| **Ethics** | 10 (Ethics Scenario), 5 (Scenario Interpretation), 11 (Most Likely), 18 (Conflict of Interest) |
| **Quant Methods** | 2 (Direct Calc), 3 (Missing Variable), 4 (Concept Comparison), 14 (Multi-Step), 17 (Hypothesis Testing) |
| **Economics** | 4 (Concept Comparison), 13 (Variable Change), 5 (Scenario Interpretation), 2 (Direct Calc) |
| **FSA** | 2 (Direct Calc), 6 (Statement Adjustment), 4 (Concept Comparison), 14 (Multi-Step) |
| **Corporate Issuers** | 2 (Direct Calc), 3 (Missing Variable), 1 (Formula ID), 13 (Variable Change) |
| **Equity** | 7 (Valuation/GGM), 2 (Direct Calc), 4 (Concept Comparison), 14 (Multi-Step DDM) |
| **Fixed Income** | 2 (Direct Calc), 8 (Yield Calc), 16 (Price-Yield), 4 (Concept Comparison) |
| **Derivatives** | 2 (Direct Calc), 1 (Formula ID), 3 (Missing Variable), 4 (Concept Comparison) |
| **Alt Investments** | 19 (Fee Calc), 5 (Scenario Interpretation), 4 (Concept Comparison) |
| **Portfolio Mgmt** | 9 (Risk Interpretation), 2 (Direct Calc), 20 (Dominance), 15 (Concept+Calc) |

---

## 5-SECOND PATTERN RECOGNITION CHEATSHEET

| If you see... | It's Pattern... | First move... |
|---------------|----------------|---------------|
| All numbers given + "closest to" | 2 Direct Calc | ID formula → plug in |
| Some numbers + solve for X | 3 Missing Variable | Rearrange or use calculator |
| Two concepts being compared | 4 Concept Comparison | What makes them different? |
| "If X increases, Y will..." | 13 Variable Change | Draw the relationship arrow |
| "Least likely" or "not" | 12 Least Likely | Flip your filter to "find false" |
| Person does something, violation? | 10 Ethics Scenario | Which standard? Strictest law? |
| DDM inputs: D, r, g | 7 Valuation | GGM: D₁/(r-g) |
| Duration + yield change | 16 Bond Price-Yield | %ΔP ≈ -MD×Δy + ½Conv×(Δy)² |
| Fee structure + gross return | 19 Alt Fee Calc | Work through steps sequentially |
| Portfolio comparison table | 20 Dominance | Higher return OR lower risk |

---

*This pattern library is your exam intelligence system — learn the template, beat any question.*
