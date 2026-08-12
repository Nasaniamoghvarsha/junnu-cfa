# CFA Level I — Complete Formula Bank

## Usage: This is your master formula reference. Covers every formula required at Level I.

---

# FORMULA INDEX BY SUBJECT

| Subject | Formula Count |
|---------|--------------|
| Quantitative Methods | 25 |
| Economics | 12 |
| Financial Statement Analysis | 20 |
| Corporate Issuers | 14 |
| Equity Investments | 16 |
| Fixed Income | 22 |
| Derivatives | 12 |
| Alternative Investments | 8 |
| Portfolio Management | 15 |

---

# QUANTITATIVE METHODS FORMULAS

## QNT-F001: Holding Period Return (HPR)

**Formula:** HPR = (P₁ - P₀ + D) / P₀

**Variables:**
- P₁ = Ending price
- P₀ = Beginning price
- D = Dividends/income received

**When to Use:** Calculating return on any single-period investment
**When NOT to Use:** Multi-period returns (use geometric mean instead)
**Common Mistakes:** Forgetting to include dividends/income
**Calculator Steps:** Simple arithmetic

---

## QNT-F002: Arithmetic Mean Return

**Formula:** R̄ = (Σ Rᵢ) / n

**Variables:**
- Rᵢ = Individual period returns
- n = Number of periods

**When to Use:** Estimating expected future return from historical data
**When NOT to Use:** Measuring actual multi-period growth (use geometric mean)
**Common Mistakes:** Using when compounding matters

---

## QNT-F003: Geometric Mean Return

**Formula:** R_G = [(1+R₁)(1+R₂)...(1+Rₙ)]^(1/n) - 1

**Variables:**
- Rᵢ = Period returns
- n = Number of periods

**When to Use:** Measuring actual compound growth rate over multiple periods
**When NOT to Use:** Estimating single-period expected return
**Common Mistakes:** Confusing with arithmetic mean; using wrong formula for average

---

## QNT-F004: Harmonic Mean

**Formula:** R_H = n / Σ(1/Rᵢ)

**When to Use:** Averaging ratios (e.g., P/E ratios), cost averaging
**Relationship:** R_H ≤ R_G ≤ R̄ (always)
**Common Mistakes:** Using arithmetic mean for ratio averaging

---

## QNT-F005: Future Value (Single Cash Flow)

**Formula:** FV = PV × (1 + r)^n

**Variables:**
- PV = Present value
- r = Interest rate per period
- n = Number of periods

**Calculator:** N, I/Y, PV, → CPT FV

---

## QNT-F006: Present Value (Single Cash Flow)

**Formula:** PV = FV / (1 + r)^n

**Calculator:** N, I/Y, FV, → CPT PV

---

## QNT-F007: Future Value of Annuity

**Formula:** FV_annuity = PMT × [(1+r)^n - 1] / r

**When to Use:** Ordinary annuity (payments at end of period)
**Annuity Due:** Multiply result by (1+r)

---

## QNT-F008: Present Value of Annuity

**Formula:** PV_annuity = PMT × [1 - 1/(1+r)^n] / r

---

## QNT-F009: Present Value of Perpetuity

**Formula:** PV = PMT / r

**When to Use:** No-growth perpetuity
**When NOT to Use:** When growth is expected

---

## QNT-F010: Present Value of Growing Perpetuity (Gordon Growth)

**Formula:** PV = PMT₁ / (r - g)

**Variables:**
- PMT₁ = Next period payment
- r = Required rate of return
- g = Growth rate (constant, r > g)

---

## QNT-F011: Effective Annual Rate (EAR)

**Formula:** EAR = (1 + r/m)^m - 1

**Variables:**
- r = Stated annual rate
- m = Compounding periods per year

**Continuous Compounding:** EAR = e^r - 1

---

## QNT-F012: Population Variance

**Formula:** σ² = Σ(Xᵢ - μ)² / N

**Variables:**
- Xᵢ = Individual observations
- μ = Population mean
- N = Population size

---

## QNT-F013: Sample Variance

**Formula:** s² = Σ(Xᵢ - X̄)² / (n - 1)

**Why n-1:** Degrees of freedom correction for unbiased estimator

---

## QNT-F014: Standard Deviation

**Formula:** σ = √(σ²)

---

## QNT-F015: Covariance

**Formula:** Cov(X,Y) = Σ[(Xᵢ - X̄)(Yᵢ - Ȳ)] / (n - 1)

---

## QNT-F016: Correlation Coefficient

**Formula:** ρ(X,Y) = Cov(X,Y) / (σ_X × σ_Y)

**Range:** -1 ≤ ρ ≤ +1
**Interpretation:** ρ = +1 perfect positive, ρ = -1 perfect negative, ρ = 0 no linear relationship

---

## QNT-F017: Bayes' Formula

**Formula:** P(A|B) = P(B|A) × P(A) / P(B)

**When to Use:** Updating probability given new information

---

## QNT-F018: Expected Value

**Formula:** E(X) = Σ Xᵢ × P(Xᵢ)

---

## QNT-F019: Portfolio Expected Return

**Formula:** E(R_p) = Σ wᵢ × E(Rᵢ)

**Variables:**
- wᵢ = Weight of asset i
- E(Rᵢ) = Expected return of asset i
- Σ wᵢ = 1

---

## QNT-F020: Portfolio Variance (Two Assets)

**Formula:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(R₁,R₂)
**Alternative:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂

---

## QNT-F021: Roy's Safety-First Ratio

**Formula:** SFR = (E(R_p) - R_L) / σ_p

**Variables:**
- E(R_p) = Portfolio expected return
- R_L = Threshold/minimum acceptable return
- σ_p = Portfolio standard deviation

**Interpretation:** Higher is better; measures how many standard deviations the expected return is above the threshold

---

## QNT-F022: Standard Error of the Mean

**Formula:** SE = σ / √n (known σ) or SE = s / √n (unknown σ)

---

## QNT-F023: Z-Statistic

**Formula:** Z = (X̄ - μ₀) / (σ/√n)

---

## QNT-F024: t-Statistic

**Formula:** t = (X̄ - μ₀) / (s/√n), df = n - 1

---

## QNT-F025: Simple Linear Regression

**Formula:** Yᵢ = b₀ + b₁Xᵢ + εᵢ

**Slope:** b₁ = Cov(X,Y) / Var(X)
**Intercept:** b₀ = Ȳ - b₁X̄
**R²:** SSR/SST = 1 - SSE/SST

---

# ECONOMICS FORMULAS

## ECO-F001: Own-Price Elasticity of Demand

**Formula:** E = (%ΔQ) / (%ΔP) = (ΔQ/ΔP) × (P/Q)

**Interpretation:** |E| > 1 elastic, |E| < 1 inelastic, |E| = 1 unit elastic

---

## ECO-F002: Income Elasticity of Demand

**Formula:** E_I = (%ΔQ) / (%ΔI)

**Interpretation:** E_I > 0 normal good, E_I < 0 inferior good

---

## ECO-F003: Cross-Price Elasticity of Demand

**Formula:** E_XY = (%ΔQ_X) / (%ΔP_Y)

**Interpretation:** E_XY > 0 substitutes, E_XY < 0 complements

---

## ECO-F004: GDP (Expenditure Approach)

**Formula:** GDP = C + I + G + (X - M)

**Variables:**
- C = Consumption
- I = Investment
- G = Government spending
- X = Exports
- M = Imports

---

## ECO-F005: GDP Deflator

**Formula:** GDP Deflator = (Nominal GDP / Real GDP) × 100

---

## ECO-F006: Quantity Theory of Money

**Formula:** MV = PY

**Variables:**
- M = Money supply
- V = Velocity of money
- P = Price level
- Y = Real output

---

## ECO-F007: Fisher Effect

**Formula:** R_nom = R_real + π^e

**Variables:**
- R_nom = Nominal interest rate
- R_real = Real interest rate
- π^e = Expected inflation rate

---

## ECO-F008: Fiscal Multiplier

**Formula:** Multiplier = 1 / [1 - MPC(1 - t)]

**Variables:**
- MPC = Marginal propensity to consume
- t = Tax rate

---

## ECO-F009: Real Exchange Rate

**Formula:** Real ER = Nominal ER × (CPI_foreign / CPI_domestic)

---

## ECO-F010: Forward Exchange Rate (Covered Interest Rate Parity)

**Formula:** F = S × (1 + r_d) / (1 + r_f)

**Variables:**
- F = Forward rate
- S = Spot rate
- r_d = Domestic interest rate
- r_f = Foreign interest rate

---

## ECO-F011: Forward Premium/Discount

**Formula:** Forward premium = (F - S) / S × (360/n)

**Interpretation:** Positive = forward premium, Negative = forward discount

---

## ECO-F012: Breakeven Point

**Formula:** TR = TC or P = ATC

**Shutdown Point:** P < AVC

---

# FINANCIAL STATEMENT ANALYSIS FORMULAS

## FSA-F001: Basic EPS

**Formula:** Basic EPS = (Net Income - Preferred Dividends) / Weighted Average Common Shares

---

## FSA-F002: Diluted EPS

**Formula:** Diluted EPS = (NI - Pref Div + Convert Adjustments) / (WACS + Dilutive Securities)

---

## FSA-F003: Current Ratio

**Formula:** Current Ratio = Current Assets / Current Liabilities

---

## FSA-F004: Quick Ratio (Acid Test)

**Formula:** Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities

---

## FSA-F005: Cash Ratio

**Formula:** Cash Ratio = (Cash + Marketable Securities) / Current Liabilities

---

## FSA-F006: Debt-to-Equity Ratio

**Formula:** D/E = Total Debt / Total Equity

---

## FSA-F007: Gross Profit Margin

**Formula:** Gross Margin = (Revenue - COGS) / Revenue = Gross Profit / Revenue

---

## FSA-F008: Operating Profit Margin

**Formula:** Operating Margin = Operating Income / Revenue

---

## FSA-F009: Net Profit Margin

**Formula:** Net Margin = Net Income / Revenue

---

## FSA-F010: Return on Assets (ROA)

**Formula:** ROA = Net Income / Average Total Assets

---

## FSA-F011: Return on Equity (ROE)

**Formula:** ROE = Net Income / Average Total Equity

---

## FSA-F012: DuPont Decomposition (3-Factor)

**Formula:** ROE = (NI/Revenue) × (Revenue/Assets) × (Assets/Equity)
**= Net Margin × Asset Turnover × Financial Leverage**

---

## FSA-F013: Inventory Turnover

**Formula:** Inventory Turnover = COGS / Average Inventory

**Days of Inventory:** 365 / Inventory Turnover

---

## FSA-F014: Receivables Turnover

**Formula:** Receivables Turnover = Revenue / Average Receivables

**DSO:** 365 / Receivables Turnover

---

## FSA-F015: Free Cash Flow to Firm (FCFF)

**Formula:** FCFF = CFO + Interest(1-t) - FCInv

**Alternative:** FCFF = EBIT(1-t) + Dep - FCInv - ΔWC

---

## FSA-F016: Free Cash Flow to Equity (FCFE)

**Formula:** FCFE = CFO - FCInv + Net Borrowing

---

## FSA-F017: Straight-Line Depreciation

**Formula:** Depreciation = (Cost - Residual Value) / Useful Life

---

## FSA-F018: Double-Declining Balance Depreciation

**Formula:** Depreciation = (2 / Useful Life) × Book Value at Beginning of Year

---

## FSA-F019: Effective Tax Rate

**Formula:** Effective Tax Rate = Income Tax Expense / Pre-Tax Income

---

## FSA-F020: Interest Coverage Ratio

**Formula:** Interest Coverage = EBIT / Interest Expense

---

# CORPORATE ISSUERS FORMULAS

## COR-F001: Net Present Value (NPV)

**Formula:** NPV = Σ CFₜ/(1+r)^t - Initial Investment

**Decision:** Accept if NPV > 0

---

## COR-F002: Internal Rate of Return (IRR)

**Formula:** Solve for r where NPV = 0

**Decision:** Accept if IRR > Required Return

---

## COR-F003: Weighted Average Cost of Capital (WACC)

**Formula:** WACC = w_d × r_d(1-t) + w_p × r_p + w_e × r_e

---

## COR-F004: Cost of Equity (CAPM)

**Formula:** r_e = R_f + β(R_m - R_f)

---

## COR-F005: Cost of Preferred Stock

**Formula:** r_p = D_p / P_p

---

## COR-F006: After-Tax Cost of Debt

**Formula:** r_d(1 - t)

---

## COR-F007: Degree of Operating Leverage (DOL)

**Formula:** DOL = %Δ Operating Income / %Δ Sales
**Alternative:** DOL = Contribution Margin / Operating Income

---

## COR-F008: Degree of Financial Leverage (DFL)

**Formula:** DFL = %Δ Net Income / %Δ Operating Income
**Alternative:** DFL = EBIT / (EBIT - Interest)

---

## COR-F009: Degree of Total Leverage (DTL)

**Formula:** DTL = DOL × DFL = %Δ Net Income / %Δ Sales

---

## COR-F010: Cash Conversion Cycle

**Formula:** CCC = DOH + DSO - DPO

---

## COR-F011: Cost of Trade Credit (EAR)

**Formula:** EAR = [1 + d/(1-d)]^(365/(Payment Period - Discount Period)) - 1

---

## COR-F012: Modigliani-Miller Proposition I (With Taxes)

**Formula:** V_L = V_U + tD

---

## COR-F013: Modigliani-Miller Proposition II (With Taxes)

**Formula:** r_e = r₀ + (r₀ - r_d)(1-t)(D/E)

---

## COR-F014: Return on Invested Capital (ROIC)

**Formula:** ROIC = NOPAT / Invested Capital

---

# EQUITY INVESTMENTS FORMULAS

## EQU-F001: Gordon Growth Model (Constant Growth DDM)

**Formula:** V₀ = D₁ / (r - g) = D₀(1+g) / (r - g)

---

## EQU-F002: Sustainable Growth Rate

**Formula:** g = ROE × Retention Ratio = ROE × (1 - Payout Ratio)

---

## EQU-F003: Trailing P/E Ratio

**Formula:** P₀/E₀ or P/E = (D₁/E₁) / (r - g) = Payout Ratio / (r - g)

---

## EQU-F004: Forward P/E Ratio

**Formula:** P₀/E₁ = (D₁/E₁) / (r - g)

---

## EQU-F005: Price-to-Book Ratio (P/B)

**Formula:** P/B = Market Price per Share / Book Value per Share

---

## EQU-F006: Enterprise Value

**Formula:** EV = Market Cap + Market Value of Preferred + Market Value of Debt - Cash and Equivalents

---

## EQU-F007: EV/EBITDA

**Formula:** EV/EBITDA = Enterprise Value / EBITDA

---

## EQU-F008: Preferred Stock Valuation

**Formula:** V₀ = D / r

---

## EQU-F009: Two-Stage DDM

**Formula:** V₀ = Σ Dₜ/(1+r)^t (high growth stage) + V_n/(1+r)^n (terminal value)

---

## EQU-F010: Margin Call Price

**Formula:** P_call = P₀ × (1 - Initial Margin) / (1 - Maintenance Margin)

---

## EQU-F011: Price-Weighted Index

**Formula:** Index Value = Σ Pᵢ / Divisor

---

## EQU-F012: Market Cap-Weighted Index

**Formula:** Index Value = Σ(Pᵢ × Qᵢ) / Divisor

---

## EQU-F013: Total Return (Index)

**Formula:** Total Return = (P₁ - P₀ + Dividends) / P₀

---

## EQU-F014: ROE

**Formula:** ROE = Net Income / Shareholders' Equity

---

## EQU-F015: Price-to-Sales (P/S)

**Formula:** P/S = Market Price per Share / Sales per Share

---

## EQU-F016: Price-to-Cash Flow (P/CF)

**Formula:** P/CF = Market Price per Share / Cash Flow per Share

---

# FIXED INCOME FORMULAS

## FIX-F001: Bond Price

**Formula:** P = Σ C/(1+r)^t + FV/(1+r)^n

**Or using spot rates:** P = Σ C/(1+z_t)^t + FV/(1+z_n)^n

---

## FIX-F002: Current Yield

**Formula:** Current Yield = Annual Coupon / Bond Price

---

## FIX-F003: Accrued Interest

**Formula:** AI = Coupon × (Days since last coupon / Days in coupon period)

---

## FIX-F004: Full (Dirty) Price

**Formula:** Full Price = Flat Price + Accrued Interest

---

## FIX-F005: Macaulay Duration

**Formula:** MacDur = Σ[t × PV(CFₜ)] / Σ PV(CFₜ)

---

## FIX-F006: Modified Duration

**Formula:** ModDur = MacDur / (1 + r)

**Where r = YTM per coupon period**

---

## FIX-F007: Effective Duration

**Formula:** EffDur = (P_down - P_up) / (2 × P₀ × Δy)

---

## FIX-F008: Approximate Convexity

**Formula:** Conv = (P_down + P_up - 2P₀) / (P₀ × (Δy)²)

---

## FIX-F009: Price Change (Duration + Convexity)

**Formula:** %ΔP ≈ -ModDur × Δy + ½ × Conv × (Δy)²

---

## FIX-F010: Money Duration

**Formula:** MoneyDur = ModDur × Price (per 100 par value)

---

## FIX-F011: PVBP (Price Value of a Basis Point)

**Formula:** PVBP = (P_down - P_up) / 2

---

## FIX-F012: Implied Forward Rate

**Formula:** (1+z_A)^A × (1+IFR)^{B-A} = (1+z_B)^B

**IFR = [(1+z_B)^B / (1+z_A)^A]^{1/(B-A)} - 1**

---

## FIX-F013: G-Spread

**Formula:** G-Spread = Bond YTM - Benchmark Government Bond YTM

---

## FIX-F014: Z-Spread

**Formula:** P = Σ C/(1+z_t + Z)^t + FV/(1+z_n + Z)^n
*(Solve for Z that makes equation equal market price)*

---

## FIX-F015: Option-Adjusted Spread (OAS)

**Formula:** OAS = Z-Spread - Option Value

---

## FIX-F016: Discount Rate (Money Market)

**Formula:** DR = (FV - P)/FV × (360/n)

---

## FIX-F017: Add-On Rate (Money Market)

**Formula:** AOR = (FV - P)/P × (360/n)

---

## FIX-F018: Bond Equivalent Yield (BEY)

**Formula:** BEY = [(FV - P)/P] × (365/n)

---

## FIX-F019: Single Monthly Mortality (SMM)

**Formula:** SMM = 1 - (1 - CPR)^(1/12)

---

## FIX-F020: Conditional Prepayment Rate (CPR)

**Formula:** CPR = 1 - (1 - SMM)^12

---

## FIX-F021: Yield to Call (YTC)

**Formula:** Same as bond pricing formula, but using call price as FV and time to call as n

---

## FIX-F022: Yield to Worst (YTW)

**Formula:** Lowest of YTM, YTC (all call dates), YTP (all put dates)

---

# DERIVATIVES FORMULAS

## DER-F001: Forward Price (No Cash Flows)

**Formula:** F₀(T) = S₀ × (1 + r)^T

**Continuous:** F₀(T) = S₀ × e^(rT)

---

## DER-F002: Forward Price (With Known Income)

**Formula:** F₀(T) = [S₀ - PV(I)] × (1 + r)^T

---

## DER-F003: Forward Price (With Known Yield)

**Formula:** F₀(T) = S₀ × (1 + r - q)^T

---

## DER-F004: Forward Value (During Life)

**Formula:** V_t = (F_t - F₀) / (1 + r)^(T-t)

---

## DER-F005: Currency Forward Price

**Formula:** F = S × [(1 + r_d) / (1 + r_f)]^T

---

## DER-F006: Put-Call Parity (European)

**Formula:** c₀ + X/(1+r)^T = p₀ + S₀

**Interpretation:** Fiduciary call = Protective put

---

## DER-F007: Put-Call-Forward Parity

**Formula:** c₀ + X/(1+r)^T = p₀ + F₀(T)/(1+r)^T

---

## DER-F008: Binomial Model — Up/Down Factors

**Formula:** u = S_up/S₀, d = S_down/S₀

---

## DER-F009: Risk-Neutral Probability

**Formula:** π = (1 + r - d) / (u - d)

---

## DER-F010: Option Value (One-Period Binomial)

**Formula:** c₀ = [π × c_up + (1-π) × c_down] / (1+r)

---

## DER-F011: Hedge Ratio

**Formula:** h = (c_up - c_down) / (S_up - S_down)

---

## DER-F012: Swap Fixed Rate

**Formula:** r_fix = (1 - PV factor_n) / Σ PV factors

---

# ALTERNATIVE INVESTMENTS FORMULAS

## ALT-F001: Management Fee

**Formula:** Management Fee = Fee Rate × AUM (beginning or ending)

---

## ALT-F002: Incentive Fee (Basic)

**Formula:** Incentive Fee = Fee Rate × (Ending Value - Beginning Value - Management Fees)

---

## ALT-F003: Incentive Fee with Hurdle Rate

**Formula:** Incentive Fee = Fee Rate × max(0, Profit above hurdle)

---

## ALT-F004: Incentive Fee with High-Water Mark

**Formula:** Only earned on profits above previous highest AUM

---

## ALT-F005: MOIC (Multiple on Invested Capital)

**Formula:** MOIC = (Realized Value + Unrealized Value) / Total Invested Capital

---

## ALT-F006: Commodity Total Return

**Formula:** Total Return = Spot Return + Roll Yield + Collateral Yield

---

## ALT-F007: Roll Yield

**Formula:** Roll Yield = (F_near - F_far) / F_near (for long position)

**Positive in backwardation, negative in contango**

---

## ALT-F008: Net-of-Fee Return

**Formula:** Net Return = Gross Return - Management Fee - Incentive Fee

---

# PORTFOLIO MANAGEMENT FORMULAS

## PRT-F001: Portfolio Expected Return

**Formula:** E(R_p) = Σ wᵢ × E(Rᵢ)

---

## PRT-F002: Portfolio Variance (Two Assets)

**Formula:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(R₁,R₂)

---

## PRT-F003: Capital Allocation Line (CAL)

**Formula:** E(R_p) = R_f + [(E(R_i) - R_f) / σ_i] × σ_p

**Slope = Sharpe Ratio of risky asset**

---

## PRT-F004: Capital Market Line (CML)

**Formula:** E(R_p) = R_f + [(E(R_m) - R_f) / σ_m] × σ_p

---

## PRT-F005: CAPM / Security Market Line (SML)

**Formula:** E(R_i) = R_f + β_i × [E(R_m) - R_f]

---

## PRT-F006: Beta

**Formula:** β_i = Cov(R_i, R_m) / Var(R_m) = ρ(i,m) × σ_i / σ_m

---

## PRT-F007: Sharpe Ratio

**Formula:** Sharpe = (R_p - R_f) / σ_p

**Measures:** Excess return per unit of total risk

---

## PRT-F008: Treynor Ratio

**Formula:** Treynor = (R_p - R_f) / β_p

**Measures:** Excess return per unit of systematic risk

---

## PRT-F009: Jensen's Alpha

**Formula:** α_p = R_p - [R_f + β_p(R_m - R_f)]

**Interpretation:** α > 0 outperformance, α < 0 underperformance

---

## PRT-F010: M² (M-Squared)

**Formula:** M² = (R_p - R_f) × (σ_m/σ_p) - (R_m - R_f)

---

## PRT-F011: Information Ratio

**Formula:** IR = (R_p - R_b) / Tracking Error

---

## PRT-F012: Covariance from Correlation

**Formula:** Cov(R_i, R_j) = ρ(i,j) × σ_i × σ_j

---

## PRT-F013: Portfolio Beta

**Formula:** β_p = Σ wᵢ × βᵢ

---

## PRT-F014: Required Return (CAPM)

**Formula:** r_required = R_f + β × (Market Risk Premium)

---

## PRT-F015: Utility Function

**Formula:** U = E(R) - ½ × A × σ²

**Variables:**
- U = Utility
- A = Risk aversion coefficient (A > 0 risk-averse)

---

# HIGHEST-PRIORITY FORMULAS (Tier 1 Memorization)

These are the formulas you should be able to recall instantly:

1. FV/PV — TVM (QNT-F005, QNT-F006)
2. EAR — Effective Annual Rate (QNT-F011)
3. Correlation — ρ = Cov/(σ_X × σ_Y) (QNT-F016)
4. Portfolio Variance (QNT-F020)
5. GDP = C + I + G + (X-M) (ECO-F004)
6. Fisher Effect (ECO-F007)
7. NPV (COR-F001)
8. WACC (COR-F003)
9. CAPM (PRT-F005)
10. Gordon Growth Model (EQU-F001)
11. Bond Pricing (FIX-F001)
12. Modified Duration (FIX-F006)
13. Price Change: Duration + Convexity (FIX-F009)
14. Put-Call Parity (DER-F006)
15. Sharpe Ratio (PRT-F007)
16. ROE DuPont (FSA-F012)
17. FCFF (FSA-F015)
18. Forward Price (DER-F001)
19. Currency Forward (DER-F005)
20. Safety-First Ratio (QNT-F021)

---

*End of Formula Bank*
