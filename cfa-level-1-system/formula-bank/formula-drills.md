# CFA Level I — Formula Drill Practice System

> **How to Use:** Cover the right column. Recall the formula from memory. Check your answer. If wrong, mark it and drill it again in 24 hours.

---

## HOW TO RUN FORMULA DRILLS

**Speed Target:** Every Tier 1 formula must be written from memory in under 15 seconds.

**Drill Protocol:**
1. Cover the formula column with paper/hand
2. Read the concept name
3. Write the formula on scratch paper from memory
4. Uncover and check — exact match required
5. Mark: ✅ Instant recall | 🟡 Recalled with effort | ❌ Failed

**Mastery Threshold:** 3 consecutive ✅ days → formula is mastered.

---

## QUANTITATIVE METHODS — FORMULA DRILLS

### TVM (Time Value of Money) — Must be calculator-perfect

| # | Concept | Formula / Rule | Tier |
|---|---------|---------------|------|
| QNT-F001 | Future Value (lump sum) | FV = PV × (1+r)^n | 🔴 T1 |
| QNT-F002 | Present Value (lump sum) | PV = FV / (1+r)^n | 🔴 T1 |
| QNT-F003 | FV of Ordinary Annuity | FV = PMT × [(1+r)^n − 1] / r | 🔴 T1 |
| QNT-F004 | PV of Ordinary Annuity | PV = PMT × [1 − 1/(1+r)^n] / r | 🔴 T1 |
| QNT-F005 | FV of Annuity Due | FVA × (1+r) | 🟡 T2 |
| QNT-F006 | PV of Perpetuity | PV = PMT / r | 🔴 T1 |
| QNT-F007 | Effective Annual Rate | EAR = (1 + stated/m)^m − 1 | 🔴 T1 |
| QNT-F008 | Continuous Compounding EAR | EAR = e^r − 1 | 🟡 T2 |

**DRILL: TVM Quick-Fire**

Q1: You invest $10,000 at 8% for 5 years, compounded annually. FV = ?
> Answer: FV = 10,000 × (1.08)^5 = **$14,693**

Q2: What is the PV of $50,000 to be received in 10 years at 6%?
> Answer: PV = 50,000 / (1.06)^10 = **$27,920**

Q3: Monthly payment of $500 for 3 years at 12% annual (1%/month). PV = ?
> Answer: N=36, I/Y=1%, PMT=500, FV=0 → PV = **$15,053**

Q4: An investment earns 12% stated rate, compounded monthly. What is EAR?
> Answer: EAR = (1 + 0.12/12)^12 − 1 = **(1.01)^12 − 1 = 12.68%**

---

### STATISTICS — Formula Drills

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| QNT-F009 | Arithmetic Mean | X̄ = ΣX / n | 🔴 T1 |
| QNT-F010 | Geometric Mean Return | G = [(1+R₁)(1+R₂)...(1+Rn)]^(1/n) − 1 | 🔴 T1 |
| QNT-F011 | Harmonic Mean | HM = n / Σ(1/Xi) | 🟡 T2 |
| QNT-F012 | Population Variance | σ² = Σ(Xi−μ)² / N | 🟡 T2 |
| QNT-F013 | Sample Variance | s² = Σ(Xi−X̄)² / (n−1) | 🔴 T1 |
| QNT-F014 | Coefficient of Variation | CV = σ / X̄ | 🟡 T2 |
| QNT-F015 | Sharpe Ratio (stats context) | SR = (R_p − R_f) / σ_p | 🔴 T1 |
| QNT-F016 | Covariance | Cov(A,B) = ρ_AB × σ_A × σ_B | 🔴 T1 |
| QNT-F017 | Correlation Coefficient | ρ = Cov(A,B) / (σ_A × σ_B) | 🔴 T1 |
| QNT-F018 | Portfolio Variance (2-asset) | σ²p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(1,2) | 🔴 T1 |

**DRILL: Statistics Quick-Fire**

Q5: Annual returns: Year1=10%, Year2=−5%, Year3=20%. What is the geometric mean?
> Answer: GM = [(1.10)(0.95)(1.20)]^(1/3) − 1 = (1.254)^(1/3) − 1 = **7.83%**

Q6: σ_A=20%, σ_B=30%, ρ_AB=0.40. What is Cov(A,B)?
> Answer: Cov = 0.40 × 0.20 × 0.30 = **0.024 (or 2.4%)**

Q7: Portfolio: 60% in A (σ=25%), 40% in B (σ=15%), Cov(A,B)=0.020. Portfolio σ = ?
> Answer: σ²p = (0.6)²(0.0625) + (0.4)²(0.0225) + 2(0.6)(0.4)(0.020)
> = 0.0225 + 0.0036 + 0.0096 = 0.0357 → σp = **18.9%**

---

### HYPOTHESIS TESTING — Formula Drills

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| QNT-F019 | z-statistic | z = (X̄ − μ₀) / (σ/√n) | 🔴 T1 |
| QNT-F020 | t-statistic | t = (X̄ − μ₀) / (s/√n) | 🔴 T1 |
| QNT-F021 | Standard Error of Mean | SE = σ/√n (or s/√n) | 🔴 T1 |
| QNT-F022 | Confidence Interval | X̄ ± z_(α/2) × (σ/√n) | 🔴 T1 |
| QNT-F023 | Chi-square test statistic | χ² = (n−1)s²/σ₀² | 🟡 T2 |
| QNT-F024 | F-statistic (variance test) | F = s₁²/s₂² (larger/smaller) | 🟡 T2 |
| QNT-F025 | Bayes' Formula | P(A|B) = P(B|A)×P(A) / P(B) | 🔴 T1 |

**DRILL: Hypothesis Testing Quick-Fire**

Q8: n=25, X̄=0.8%, s=2.5%. Test H₀: μ=0. What is the test statistic?
> Answer: t = (0.8 − 0) / (2.5/√25) = 0.8/0.5 = **t = 1.60**, df = 24

Q9: 95% CI for population mean. n=100, X̄=50, s=10.
> Answer: 50 ± 1.96 × (10/√100) = 50 ± 1.96 = **(48.04, 51.96)**

Q10: P(Disease)=1%, Test accuracy=95% both ways. P(Disease|Positive test) = ?
> Answer (Bayes): P(+|D)×P(D) / P(+) = (0.95×0.01) / (0.95×0.01 + 0.05×0.99)
> = 0.0095 / (0.0095 + 0.0495) = 0.0095/0.059 = **≈16%**

---

## ECONOMICS — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| ECO-F001 | Price Elasticity of Demand | PED = %ΔQ / %ΔP | 🔴 T1 |
| ECO-F002 | Cross-Price Elasticity | CPE = %ΔQa / %ΔPb | 🟡 T2 |
| ECO-F003 | Income Elasticity | IE = %ΔQ / %ΔIncome | 🟡 T2 |
| ECO-F004 | Nominal GDP | NGDP = P × Q (current prices) | 🔴 T1 |
| ECO-F005 | Real GDP | RGDP = P₀ × Q (base prices) | 🔴 T1 |
| ECO-F006 | GDP Expenditure | GDP = C + I + G + (X−M) | 🔴 T1 |
| ECO-F007 | Fisher Effect | R_nominal = R_real + π^e | 🔴 T1 |
| ECO-F008 | Multiplier | k = 1/(1−MPC) | 🟡 T2 |
| ECO-F009 | Money Multiplier | MM = 1/reserve requirement | 🟡 T2 |

**DRILL: Economics Quick-Fire**

Q11: Price rises from $10 to $12 (+20%). Quantity falls from 100 to 80 (−20%). PED = ?
> Answer: PED = −20%/+20% = **−1.0 (unit elastic)**
> Revenue impact: unchanged (elastic would decrease, inelastic would increase)

Q12: R_real = 3%, Inflation expectation = 2.5%. What is R_nominal?
> Answer: R_nominal = 3% + 2.5% = **5.5%**

---

## FINANCIAL STATEMENT ANALYSIS — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| FSA-F001 | Gross Profit Margin | GPM = Gross Profit / Revenue | 🔴 T1 |
| FSA-F002 | Net Profit Margin | NPM = Net Income / Revenue | 🔴 T1 |
| FSA-F003 | Return on Assets | ROA = Net Income / Avg Total Assets | 🔴 T1 |
| FSA-F004 | Return on Equity | ROE = Net Income / Avg Stockholders' Equity | 🔴 T1 |
| FSA-F005 | DuPont 3-Factor | ROE = (NI/S) × (S/A) × (A/E) | 🔴 T1 |
| FSA-F006 | DuPont 5-Factor | ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Leverage | 🟡 T2 |
| FSA-F007 | Current Ratio | CA / CL | 🔴 T1 |
| FSA-F008 | Quick Ratio | (Cash + ST Securities + Receivables) / CL | 🔴 T1 |
| FSA-F009 | Cash Ratio | (Cash + ST Securities) / CL | 🟡 T2 |
| FSA-F010 | Inventory Turnover | COGS / Average Inventory | 🔴 T1 |
| FSA-F011 | Days of Inventory | 365 / Inventory Turnover | 🔴 T1 |
| FSA-F012 | Receivables Turnover | Revenue / Average Receivables | 🔴 T1 |
| FSA-F013 | Days Sales Outstanding | 365 / Receivables Turnover | 🔴 T1 |
| FSA-F014 | Payables Turnover | COGS / Average Payables | 🟡 T2 |
| FSA-F015 | Days Payable | 365 / Payables Turnover | 🟡 T2 |
| FSA-F016 | Cash Conversion Cycle | DOI + DSO − DPO | 🔴 T1 |
| FSA-F017 | Debt-to-Equity | Total Debt / Total Equity | 🔴 T1 |
| FSA-F018 | Debt-to-Assets | Total Debt / Total Assets | 🟡 T2 |
| FSA-F019 | Interest Coverage (TIE) | EBIT / Interest Expense | 🔴 T1 |
| FSA-F020 | EPS (Basic) | (Net Income − Preferred Dividends) / Weighted Avg Shares | 🔴 T1 |

**DRILL: FSA Quick-Fire**

Q13: COGS=$600K, Avg Inventory=$100K. Days of Inventory = ?
> Answer: Inventory Turnover = 600/100 = 6×. DOI = 365/6 = **60.8 days**

Q14: ROE=18%, Net Margin=6%, Asset Turnover=1.5×. What is the equity multiplier?
> Answer: ROE = NM × AT × EM → 0.18 = 0.06 × 1.5 × EM → EM = **2.0×**

Q15 (LIFO→FIFO): LIFO Inventory = $400K, LIFO Reserve = $80K, Tax Rate = 30%.
If converting to FIFO: Adjusted Inventory = ? Adjusted Net Income Impact = ?
> Inventory: $400K + $80K = **$480K**
> Net Income adjustment: LIFO Reserve × (1−tax) = $80K × 0.70 = **+$56K** (higher under FIFO)

---

## CORPORATE ISSUERS — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| COR-F001 | Net Present Value | NPV = Σ[CF_t/(1+r)^t] − I₀ | 🔴 T1 |
| COR-F002 | IRR Definition | NPV = 0 at r=IRR | 🔴 T1 |
| COR-F003 | WACC | w_d×k_d×(1−t) + w_p×k_p + w_e×k_e | 🔴 T1 |
| COR-F004 | CAPM (Cost of Equity) | k_e = R_f + β(R_m − R_f) | 🔴 T1 |
| COR-F005 | Cost of Debt (after-tax) | k_d × (1 − tax rate) | 🔴 T1 |
| COR-F006 | Degree of Operating Leverage | DOL = %ΔOperating Income / %ΔSales | 🟡 T2 |
| COR-F007 | DOL (formula version) | DOL = (Sales − Variable Costs) / EBIT | 🟡 T2 |
| COR-F008 | Degree of Financial Leverage | DFL = %ΔEarnings / %ΔOperating Income | 🟡 T2 |
| COR-F009 | DTL | DTL = DOL × DFL | 🟡 T2 |

**DRILL: Corporate Issuers Quick-Fire**

Q16: Project CF: Year0=−$100K, Year1=$40K, Year2=$50K, Year3=$40K. r=10%. NPV = ?
> NPV = −100 + 40/1.1 + 50/1.21 + 40/1.331
> = −100 + 36.36 + 41.32 + 30.05 = **+$7.73K → Accept**

Q17: Debt=40% (cost=6%, tax=30%), Equity=60% (R_f=3%, β=1.2, Rm=9%). WACC = ?
> k_e = 3 + 1.2(9−3) = 3+7.2 = 10.2%
> WACC = 0.40×6%×0.70 + 0.60×10.2% = 1.68% + 6.12% = **7.80%**

---

## EQUITY INVESTMENTS — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| EQU-F001 | Gordon Growth Model (GGM) | V₀ = D₁ / (r − g) | 🔴 T1 |
| EQU-F002 | GGM — D₁ from D₀ | D₁ = D₀ × (1+g) | 🔴 T1 |
| EQU-F003 | Leading P/E | P₀/E₁ | 🔴 T1 |
| EQU-F004 | Trailing P/E | P₀/E₀ | 🔴 T1 |
| EQU-F005 | P/B Ratio | Market Price / Book Value per Share | 🔴 T1 |
| EQU-F006 | Price/Sales | Market Price / Revenue per Share | 🟡 T2 |
| EQU-F007 | Enterprise Value | EV = Market Cap + Debt − Cash | 🟡 T2 |
| EQU-F008 | EV/EBITDA | EV / EBITDA | 🟡 T2 |
| EQU-F009 | Required Return (DDM) | r = D₁/P₀ + g | 🔴 T1 |

**DRILL: Equity Quick-Fire**

Q18: D₁=$2.50, r=10%, g=4%. Intrinsic value = ?
> V₀ = 2.50 / (0.10 − 0.04) = 2.50/0.06 = **$41.67**

Q19: Stock at $40, D₀=$1.80, g=5%. Required return = ?
> D₁ = 1.80 × 1.05 = $1.89
> r = 1.89/40 + 0.05 = 4.73% + 5% = **9.73%**

---

## FIXED INCOME — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| FI-F001 | Bond Price | P = Σ[C/(1+y)^t] + FV/(1+y)^n | 🔴 T1 |
| FI-F002 | Current Yield | Annual Coupon / Price | 🔴 T1 |
| FI-F003 | Modified Duration | ModDur = MacDur / (1 + y/m) | 🔴 T1 |
| FI-F004 | Price Change (Duration) | %ΔP ≈ −ModDur × Δy | 🔴 T1 |
| FI-F005 | Price Change (+ Convexity) | %ΔP ≈ −ModDur × Δy + ½ × Convexity × (Δy)² | 🔴 T1 |
| FI-F006 | Full Price | Clean Price + Accrued Interest | 🔴 T1 |
| FI-F007 | Accrued Interest | (Days since coupon / Days in period) × Coupon | 🟡 T2 |
| FI-F008 | OAS | Z-spread − Option Value | 🔴 T1 |
| FI-F009 | Duration of Bond Portfolio | Weighted avg of individual durations | 🔴 T1 |
| FI-F010 | BPV (Basis Point Value) | BPV = ModDur × V × 0.0001 | 🟡 T2 |

**DRILL: Fixed Income Quick-Fire**

Q20: Bond: ModDur=6.5, Convexity=52. Yield rises 50bp (0.50%). %ΔP = ?
> %ΔP ≈ −6.5 × 0.005 + ½ × 52 × (0.005)²
> = −0.0325 + ½ × 52 × 0.000025
> = −0.0325 + 0.00065 = **−3.185% (price falls)**

Q21: 5% coupon bond, semi-annual, 10 years, yield=6%. Price = ?
> N=20, I/Y=3%, PMT=25, FV=1000 → P = **$925.61**

---

## DERIVATIVES — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| DER-F001 | Forward Price (no income) | F₀ = S₀ × (1+r)^T | 🔴 T1 |
| DER-F002 | Forward Price (with income) | F₀ = (S₀ − PV(Income)) × (1+r)^T | 🔴 T1 |
| DER-F003 | Forward Price (continuous) | F₀ = S₀ × e^(r−q)T | 🟡 T2 |
| DER-F004 | Put-Call Parity | c + PV(X) = p + S₀ | 🔴 T1 |
| DER-F005 | Intrinsic Value (Call) | max(S − X, 0) | 🔴 T1 |
| DER-F006 | Intrinsic Value (Put) | max(X − S, 0) | 🔴 T1 |
| DER-F007 | Lower Bound (European Call) | c ≥ max(S − PV(X), 0) | 🟡 T2 |
| DER-F008 | Lower Bound (European Put) | p ≥ max(PV(X) − S, 0) | 🟡 T2 |

**DRILL: Derivatives Quick-Fire**

Q22: S₀=$100, r=5%, T=1 year. Forward price = ?
> F₀ = 100 × (1.05)^1 = **$105**

Q23: S=$50, X=$48, r=4%, T=0.5 years. Call=? Put=? (Put-Call Parity)
> PV(X) = 48/(1.04)^0.5 = 48/1.0198 = $47.07
> If call=c=$4: p = c + PV(X) − S = 4 + 47.07 − 50 = **p = $1.07**

---

## PORTFOLIO MANAGEMENT — FORMULA DRILLS

| # | Concept | Formula | Tier |
|---|---------|---------|------|
| PM-F001 | Portfolio Return | R_p = Σ(w_i × R_i) | 🔴 T1 |
| PM-F002 | Sharpe Ratio | (R_p − R_f) / σ_p | 🔴 T1 |
| PM-F003 | Treynor Ratio | (R_p − R_f) / β_p | 🔴 T1 |
| PM-F004 | Jensen's Alpha | α = R_p − [R_f + β_p(R_m − R_f)] | 🔴 T1 |
| PM-F005 | Information Ratio | (R_p − R_B) / σ_active | 🟡 T2 |
| PM-F006 | Beta | β = Cov(R_i, R_m) / Var(R_m) = ρ × (σ_i/σ_m) | 🔴 T1 |
| PM-F007 | CAPM (Expected Return) | E(R_i) = R_f + β_i(E(R_m) − R_f) | 🔴 T1 |
| PM-F008 | M² (Modigliani) | M² = Sharpe × σ_m + R_f | 🟡 T2 |
| PM-F009 | Roy's Safety-First | SF Ratio = (E(R_p) − R_T) / σ_p | 🟡 T2 |

**DRILL: Portfolio Management Quick-Fire**

Q24: R_p=12%, R_f=3%, σ_p=15%, β=0.9. Sharpe and Treynor = ?
> Sharpe = (12−3)/15 = **0.60**
> Treynor = (12−3)/0.9 = **10.0**

Q25: R_p=14%, R_f=3%, β=1.1, R_m=11%. Jensen's Alpha = ?
> Expected = 3 + 1.1(11−3) = 3 + 8.8 = 11.8%
> α = 14 − 11.8 = **+2.2% (outperformance)**

---

## MASTER DRILL SCORECARD

Track your performance across all formula drills:

| Subject | # Formulas | First Drill Score | 7-Day Retest | 14-Day Retest | Status |
|---------|-----------|-------------------|--------------|---------------|--------|
| Quantitative Methods | 25 | ___/25 | ___/25 | ___/25 | ⬜ |
| Economics | 9 | ___/9 | ___/9 | ___/9 | ⬜ |
| FSA | 20 | ___/20 | ___/20 | ___/20 | ⬜ |
| Corporate Issuers | 9 | ___/9 | ___/9 | ___/9 | ⬜ |
| Equity | 9 | ___/9 | ___/9 | ___/9 | ⬜ |
| Fixed Income | 10 | ___/10 | ___/10 | ___/10 | ⬜ |
| Derivatives | 8 | ___/8 | ___/8 | ___/8 | ⬜ |
| Portfolio Management | 9 | ___/9 | ___/9 | ___/9 | ⬜ |
| **TOTAL** | **99** | **___/99** | **___/99** | **___/99** | ⬜ |

**Target: 95%+ on 14-day retest before exam day.**

---

*Complement this with the main [Formula Bank](all-formulas.md) for full derivations and context.*
