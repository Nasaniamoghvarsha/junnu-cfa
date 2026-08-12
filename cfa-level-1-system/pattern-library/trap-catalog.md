# CFA Level I — Comprehensive Trap Catalog and Exam Drills

## Purpose: Catalog the most common traps, errors, and misconceptions tested across CFA Level I.

---

## EXAM-DAY TRAP CHECKLIST

*Run through this mental checklist before finalizing any complex answer on exam day:*

- [ ] **Did I read "Most Likely" or "Least Likely"?** (Underline or highlight these words mentally).
- [ ] **Are my units consistent?** (Annual vs Semi-Annual rates, percentages vs decimals, months vs years).
- [ ] **Is my calculator in the right mode?** (BGN for annuities due, END for ordinary annuities. Clear the memory!).
- [ ] **Did I check the directional sign?** (e.g., Price and Yield move oppositely, ModDur has a negative sign).
- [ ] **Is the exchange rate base currency clear?** (Remember: A/B means B per 1 A. Base is always the first currency).
- [ ] **Am I confusing a nominal rate with a real rate?** (Fisher effect, inflation adjustments).
- [ ] **Did I account for all terminal cash flows?** (Salvage value, return of net working capital at end of project).
- [ ] **Am I using Market Value weights?** (WACC always uses market value, not book value).
- [ ] **Have I verified the tax shield?** (Cost of debt needs (1-t), cost of equity does not).
- [ ] **Is this a trick about strictness?** (Ethics: Always apply the strictest rule between local law and CFA standards).

---

## HIGH-FREQUENCY TRAP MATRIX

| Subject | Most Tested Trap Concept | Frequency | Impact on Score |
|---|---|---|---|
| **Quant** | Annuity Due vs Ordinary (Calculator BGN/END) | High | Medium |
| **Economics** | Real vs Nominal Exchange Rates & Base Currency | High | High |
| **FSA** | LIFO to FIFO adjustments & COGS/Inventory impacts | Very High | High |
| **Corporate** | WACC Book vs Market Weights & Flotation Costs | High | Medium |
| **Equity** | Discounting FCFE with WACC (Mismatch) | High | High |
| **Fixed Income** | Price-Yield convexity and duration signs | Very High | High |
| **Derivatives** | Put-Call Parity rearranging & signs | High | Medium |
| **Alts** | Fee structure (Management vs Incentive deduction order) | Medium | High |
| **Portfolio** | Sharpe vs Treynor usage (Total vs Systematic Risk) | High | Medium |
| **Ethics** | Strict vs Local Laws & Independence/Objectivity | Very High | High |

---

## TRAP RECOGNITION SPEED DRILLS

*Test your reflexes. Can you spot the trap in under 10 seconds?*

1. **Scenario:** "An analyst calculates a bond's modified duration as 5. If yields increase by 1%, the price changes by 5%."
   **Trap:** Missing the negative sign. Price *decreases* by 5%. Yields and prices move inversely.

2. **Scenario:** "A firm has an increasing inventory balance while prices are falling. Under LIFO, their COGS is higher than under FIFO."
   **Trap:** LIFO means last in first out. If prices are falling, the last items purchased are cheaper. Therefore, LIFO COGS is *lower*, not higher.

3. **Scenario:** "To calculate the 5-year annualized historical return of a portfolio, the analyst uses the arithmetic mean."
   **Trap:** For compounding historical multi-period wealth, the *geometric mean* is required. Arithmetic overstates the true compounded return.

4. **Scenario:** "Company A increases its debt leverage, so its ROE increases. This means the company is performing better fundamentally."
   **Trap:** DuPont analysis shows that leverage artificially boosts ROE without necessarily improving operating efficiency (margin) or asset utilization.

5. **Scenario:** "An investor buys an American call on a non-dividend paying stock and plans to exercise early if it goes deep ITM."
   **Trap:** Never exercise an American call on a non-dividend stock early; you destroy the time value of the option. Sell the option instead.

6. **Scenario:** "The local law allows receiving gifts up to $500. CFA Standards say gifts must not compromise objectivity. The analyst accepts a $400 gift without disclosing."
   **Trap:** Strictest law applies. CFA Standards require disclosure to the employer of any gifts that might reasonably be seen to influence judgment.

7. **Scenario:** "The central bank buys bonds in the open market to stimulate the economy. This is fiscal policy."
   **Trap:** Central bank actions (open market operations, policy rates) are *monetary* policy. Fiscal policy is government taxation and spending.

8. **Scenario:** "A project's NPV is positive, but its IRR is less than the WACC."
   **Trap:** Mathematically impossible for a standard conventional project. If NPV > 0, then IRR must be > WACC.

9. **Scenario:** "The EUR/USD rate goes from 1.10 to 1.15. The USD has appreciated."
   **Trap:** EUR/USD means USD per 1 EUR. It now takes 1.15 USD (more than before) to buy 1 EUR. The USD has *depreciated*.

10. **Scenario:** "A hedge fund charges 2/20 with a hard hurdle rate of 5%. It returns 10%. The incentive fee is calculated on the full 10%."
    **Trap:** A *hard* hurdle means the incentive fee is only on the excess return (10% - 5% = 5%). A soft hurdle would apply to the full 10%.

---

## UNIVERSAL TRAPS (Cross-Subject)

### TRAP-001: Directional Confusion
**Description:** Getting the sign/relationship direction wrong.
**Examples:** 
- Bond price moves opposite to yield
- Call option value increases with volatility, put also increases
- Higher elasticity means MORE responsive, not less
**Protection:** Draw relationship arrows before answering.

### TRAP-002: Unit Mismatch
**Description:** Using wrong time units or currency.
**Examples:**
- Annual vs. semi-annual rates
- Percentage vs. decimal form
- Foreign currency quoting conventions
**Protection:** Always convert to consistent units.

### TRAP-003: CFA Notation Convention
**Description:** CFA uses specific notation that differs from market convention.
**Biggest trap:** FX quotes: EUR/USD means USD per EUR (EUR is base).
**Protection:** Know CFA conventions cold before exam day.

### TRAP-004: "Least Likely" Blindness
**Description:** Answering as if the question asks "most likely."
**Examples:** Choosing a correct statement when asked for incorrect one.
**Protection:** Circle "least" or "not" in the question stem.

### TRAP-005: Plausible Distractors
**Description:** All options seem reasonable but only one is exactly right.
**Examples:** Close numbers, similar but distinct concepts.
**Protection:** Look for the EXACT distinction being tested.

### TRAP-006: Information Overload
**Description:** Extraneous data in question stem.
**Examples:** Extra financial ratios, irrelevant scenario details.
**Protection:** Identify which numbers you actually need before looking at the data block.

### TRAP-007: Assumption Blindness
**Description:** Forgetting key assumptions.
**Examples:** CAPM assumes perfect markets; MM propositions assume no taxes (in base case).
**Protection:** Mentally list assumptions before answering theory questions.

### TRAP-008: Semi-Annual vs Annual Compounding
**Description:** Failing to adjust N and I/Y on the calculator for semi-annual payments.
**Examples:** Using N=10 and I/Y=8 for a 10-year semi-annual bond instead of N=20 and I/Y=4.
**Protection:** The moment you see "semi-annual," multiply N by 2 and divide I/Y by 2.

### TRAP-009: Time Zero vs Time One
**Description:** Misidentifying when the first cash flow occurs in NPV/IRR calculations.
**Examples:** Putting next year's cash flow into CF0 instead of CF1.
**Protection:** Draw a timeline. CF0 is always "today/now."

---

## QUANTITATIVE METHODS TRAPS

### QNT-TRAP-001: Mean Confusion
**Trap:** Confusing arithmetic mean with geometric mean.
**When tested:** Multi-period return questions.
**Protection:** "Geometric for compounding over time. Arithmetic for expected next-period return."

### QNT-TRAP-002: Population vs. Sample
**Trap:** Using n instead of n-1 for sample variance.
**Protection:** "n-1 for samples."

### QNT-TRAP-003: Type I vs. Type II Error
**Trap:** Reversing the definitions.
- Type I = Rejecting true H₀ (false positive)
- Type II = Not rejecting false H₀ (false negative)
**Protection:** Memory aid — "Type I is jumping to conclusions; Type II is missing the signal."

### QNT-TRAP-004: Correlation ≠ Causation
**Trap:** Inferring causation from correlation.
**Protection:** Always ask "could there be a third variable?"

### QNT-TRAP-005: EAR Confusion
**Trap:** Using stated rate when EAR is needed (or vice versa).
**Protection:** Check compounding frequency first.

### QNT-TRAP-006: Annuity Due vs. Ordinary Annuity
**Trap:** Wrong BGN/END mode on calculator.
**Protection:** "Does payment happen at beginning or end of period?"

### QNT-TRAP-007: R² Interpretation
**Trap:** Thinking high R² means the model is good/correct.
**Truth:** R² only measures fit, not correctness or causality.
**Protection:** "R² tells you fit, not truth."

### QNT-TRAP-008: Harmonic Mean
**Trap:** Forgetting when to use it vs arithmetic mean.
**When tested:** Cost averaging (e.g., buying a fixed dollar amount of shares each month).
**Protection:** "Harmonic mean is for cost averaging."

### QNT-TRAP-009: Normal vs Student's t-Distribution
**Trap:** Using the normal (Z) distribution when variance is unknown and the sample size is small.
**Protection:** "Small sample (<30) + unknown variance = use t-distribution."

---

## ECONOMICS TRAPS

### ECO-TRAP-001: Elasticity Direction
**Trap:** Confusing elastic vs. inelastic and the effect on total revenue.
- Elastic: Price up → Revenue down
- Inelastic: Price up → Revenue up
**Protection:** Draw the demand curve.

### ECO-TRAP-002: Shutdown vs. Exit
**Trap:** Confusing short-run shutdown (P < AVC) with long-run exit (P < ATC).
**Protection:** "Short run = variable costs matter; Long run = all costs matter."

### ECO-TRAP-003: Fiscal vs. Monetary Policy
**Trap:** Attributing the wrong tool to the wrong authority.
**Protection:** "Fiscal = government (tax/spend); Monetary = central bank."

### ECO-TRAP-004: Fisher Effect Sign
**Trap:** R_nom = R_real + π^e — simple but easy to rearrange wrong.
**Protection:** "Nominal = Real + Expected Inflation."

### ECO-TRAP-005: Comparative Advantage
**Trap:** Confusing absolute advantage (who produces more) with comparative advantage (lower opportunity cost).
**Protection:** ALWAYS compute opportunity cost for both parties.

### ECO-TRAP-006: CFA FX Notation
**Trap:** A/B means B units per 1 A. Opposite of natural reading for many.
**Protection:** "First currency is the base — you buy/sell the base."

### ECO-TRAP-007: Veblen vs Giffen Goods
**Trap:** Confusing why they both have upward sloping demand curves.
**Protection:** "Veblen = high status/luxury; Giffen = inferior good + lack of substitutes + income effect overwhelms substitution effect."

### ECO-TRAP-008: Current Account vs Capital/Financial Account
**Trap:** Misclassifying trade flows vs investment flows.
**Protection:** "Current Account = trade & income; Capital/Financial Account = assets & investments."

---

## FINANCIAL STATEMENT ANALYSIS TRAPS

### FSA-TRAP-001: LIFO vs. FIFO in Rising Prices
**Trap:** Confusing which gives higher/lower COGS and inventory.
- Rising prices: LIFO → higher COGS, lower inventory, lower NI
**Protection:** Draw price direction first.

### FSA-TRAP-002: Capitalize vs. Expense
**Trap:** Forgetting that capitalizing boosts current income but creates future depreciation.
**Protection:** "Capitalize = spread the pain; Expense = all pain now."

### FSA-TRAP-003: Cash Flow Sign Convention
**Trap:** Wrong signs for operating cash flow adjustments.
**Protection:** "Asset increase = cash outflow; Liability increase = cash inflow."

### FSA-TRAP-004: Diluted EPS — Anti-dilutive
**Trap:** Including anti-dilutive securities in diluted EPS calculation.
**Protection:** "If conversion INCREASES EPS, it's anti-dilutive — exclude it."

### FSA-TRAP-005: DuPont Decomposition
**Trap:** Forgetting the multiplication chain or adding the terms instead.
**Protection:** "ROE = Profitability (Margin) × Efficiency (Turnover) × Leverage (Multiplier)."

### FSA-TRAP-006: DTA vs. DTL
**Trap:** Getting the sign wrong on deferred tax.
- DTA: Future deductible (prepaid tax)
- DTL: Future taxable (tax delayed)
**Protection:** "Asset = benefit coming; Liability = bill coming."

### FSA-TRAP-007: Capitalizing Interest
**Trap:** Not adjusting cash flows when interest is capitalized (CFI vs CFO).
**Protection:** "Capitalized interest flows to CFI, expensed interest flows to CFO."

### FSA-TRAP-008: Operating vs Finance Leases (Lessee)
**Trap:** Missing the impact on CFO vs CFF (US GAAP differences).
**Protection:** "Finance lease principal repayment goes to CFF; operating lease total payment is CFO (US GAAP)."

---

## CORPORATE ISSUERS TRAPS

### COR-TRAP-001: Sunk Cost Fallacy
**Trap:** Including sunk costs in NPV analysis.
**Protection:** "Sunk costs are gone — ignore them."

### COR-TRAP-002: NPV vs. IRR Conflict
**Trap:** Choosing IRR over NPV for mutually exclusive projects.
**Protection:** "NPV always wins for mutually exclusive projects."

### COR-TRAP-003: WACC — Market vs. Book Weights
**Trap:** Using book values instead of market values for weights.
**Protection:** "WACC always uses MARKET values."

### COR-TRAP-004: MM Proposition Direction
**Trap:** Forgetting that debt adds value WITH taxes (tax shield) but NOT without.
**Protection:** "Taxes make debt valuable."

### COR-TRAP-005: Flotation Costs
**Trap:** Adjusting the WACC instead of the initial cash flow.
**Protection:** "Flotation costs = upfront fee. Subtract them directly from the initial project cash flow (CF0)."

### COR-TRAP-006: Dividend Irrelevance
**Trap:** Assuming MM dividend irrelevance applies in the real world with taxes and friction.
**Protection:** "MM says dividends don't matter ONLY in a theoretical perfect market without taxes."

---

## EQUITY INVESTMENTS TRAPS

### EQU-TRAP-001: Gordon Growth — r must exceed g
**Trap:** Forgetting that r > g is required; negative denominator = nonsense.
**Protection:** "r > g or the model breaks."

### EQU-TRAP-002: Trailing vs. Forward P/E
**Trap:** Mixing up which earnings to use.
- Trailing: E₀ (past 12 months)
- Forward: E₁ (next 12 months)
**Protection:** "Trailing looks back; Forward looks ahead."

### EQU-TRAP-003: Market Efficiency — Who Can Beat the Market?
**Trap:** Confusing which form prevents which strategy.
- Weak: Technical analysis fails
- Semi-strong: Fundamental analysis fails
- Strong: Even insider info can't help
**Protection:** "Weak = past prices; Semi-strong = public info; Strong = all info."

### EQU-TRAP-004: Index Divisor Adjustments
**Trap:** Forgetting that stock splits require divisor adjustment in price-weighted indices.
**Protection:** "Divisor changes when constituent prices change for non-market reasons (splits)."

### EQU-TRAP-005: FCFF vs FCFE Discount Rates
**Trap:** Using WACC to discount Free Cash Flow to Equity (FCFE).
**Protection:** "FCFF uses WACC (firm-wide), FCFE uses Cost of Equity (equity holders only)."

### EQU-TRAP-006: Industry Life Cycle Stages
**Trap:** Confusing the Growth and Shakeout stages.
**Protection:** "Shakeout = slowing growth, falling margins, increasing competition."

---

## FIXED INCOME TRAPS

### FIX-TRAP-001: Duration Sign
**Trap:** Forgetting the negative sign: %ΔP = -ModDur × Δy.
**Protection:** "Price and yield move in opposite directions."

### FIX-TRAP-002: Macaulay vs. Modified Duration
**Trap:** Using the wrong one.
**Protection:** "MacDur is in years; ModDur is price sensitivity. ModDur = MacDur/(1+r)."

### FIX-TRAP-003: Convexity Always Helps
**Trap:** Forgetting convexity adjustment is always POSITIVE for option-free bonds, whether yields rise or fall.
**Protection:** "Convexity is the bondholder's friend."

### FIX-TRAP-004: Clean vs. Dirty Price
**Trap:** Using clean price (quoted) when full price (transaction) is needed.
**Protection:** "Full (Dirty) price = Clean price + Accrued Interest."

### FIX-TRAP-005: OAS vs. Z-Spread
**Trap:** For callable bonds, OAS < Z-spread. For putable, OAS > Z-spread.
**Protection:** "Option cost = Z-spread - OAS. Callable = issuer option = cost > 0."

### FIX-TRAP-006: Spot vs Forward Rates
**Trap:** Simply multiplying or averaging spot rates instead of geometric linking.
**Protection:** "(1+S2)^2 = (1+S1) × (1+1y1y)."

### FIX-TRAP-007: Matrix Pricing
**Trap:** Simply averaging yields without adjusting for maturity differences linearly.
**Protection:** "Linear interpolation requires exact maturity weighting. Don't just divide by 2."

---

## DERIVATIVES TRAPS

### DER-TRAP-001: Put-Call Parity Rearrangement
**Trap:** Wrong rearrangement leading to wrong missing component.
**Protection:** "Fiduciary Call (c + PV(X)) = Protective Put (p + S)."

### DER-TRAP-002: Option Value Bounds
**Trap:** Forgetting that an American call on a non-dividend stock should NOT be exercised early.
**Protection:** "Early exercise destroys time value."

### DER-TRAP-003: Forward Pricing with Income
**Trap:** Forgetting to subtract PV of income/benefits from spot price.
**Protection:** "Benefits to holding the underlying asset reduce the forward price."

### DER-TRAP-004: Swaps as Portfolios
**Trap:** Not recognizing a swap as a series of forward contracts.
**Protection:** "A swap is just a portfolio of forwards with a constant rate."

### DER-TRAP-005: Moneyness vs Profitability
**Trap:** Thinking an in-the-money option is necessarily profitable (ignoring the premium paid).
**Protection:** "In the money means intrinsic value > 0, but it doesn't mean you made your initial premium back."

---

## ALTERNATIVE INVESTMENTS TRAPS

### ALT-TRAP-001: Fee Calculation Order
**Trap:** Wrong order of fee deductions (management fee first, then incentive).
**Protection:** "Management fee comes off the top, incentive fee is calculated on what's left (usually)."

### ALT-TRAP-002: High-Water Mark
**Trap:** Forgetting that high-water mark prevents double-counting of recovery.
**Protection:** "Can't earn incentive fees twice on the same gains."

### ALT-TRAP-003: Contango vs. Backwardation
**Trap:** Reversing which gives positive vs. negative roll yield.
- Long position: Backwardation → positive roll yield
**Protection:** "Backwardation = futures below spot = roll up = positive for longs."

### ALT-TRAP-004: Soft vs Hard Hurdle Rates
**Trap:** Calculating incentive fees on the entire return (when hard) or only the excess (when soft).
**Protection:** "Soft = applies to all of it once met, Hard = applies only to the excess."

### ALT-TRAP-005: PE Valuation Multiples
**Trap:** Using Equity Value instead of Enterprise Value (EV) with EBITDA multiples.
**Protection:** "EV goes with EBITDA (firm-wide), Equity goes with Net Income (shareholders only)."

---

## PORTFOLIO MANAGEMENT TRAPS

### PRT-TRAP-001: Sharpe vs. Treynor
**Trap:** Using Sharpe for well-diversified portfolios (use Treynor) or Treynor for total portfolio evaluation.
- Sharpe = Total risk (σ)
- Treynor = Systematic risk (β)
**Protection:** "Sharpe for total portfolio; Treynor for one piece of a diversified portfolio."

### PRT-TRAP-002: CML vs. SML
**Trap:** Using CML (total risk) to evaluate individual securities.
**Protection:** "CML is for efficient portfolios only; SML is for individual securities."

### PRT-TRAP-003: Cognitive vs. Emotional Bias
**Trap:** Misclassifying biases. Cognitive errors can be corrected with education; emotional biases are harder.
**Protection:** "Cognitive = thinking error; Emotional = feeling error."

### PRT-TRAP-004: Beta Calculation
**Trap:** Using correlation when you need beta (or vice versa).
**Protection:** "β = ρ × (σ_i/σ_m); ρ scales but β accounts for relative volatility too."

### PRT-TRAP-005: Risk Aversion vs Risk Tolerance
**Trap:** Using them interchangeably.
**Protection:** "Risk aversion is a penalty factor in the utility formula; tolerance is capacity + willingness."

### PRT-TRAP-006: Strategic vs Tactical Asset Allocation
**Trap:** Confusing long-term target weights with short-term deviations.
**Protection:** "Strategic = Long-term Policy; Tactical = Active short-term deviations based on views."

---

## ETHICS TRAPS

### ETH-TRAP-001: Strictest Law Apply
**Trap:** Choosing the CFA standard when local law is stricter.
**Truth:** Always apply the STRICTEST standard.
**Protection:** "Stricter of: local law OR CFA standards."

### ETH-TRAP-002: Mosaic Theory vs. MNPI
**Trap:** Confusing mosaic theory (using public + non-material nonpublic information) with trading on MNPI.
**Protection:** "Mosaic = public pieces assembled legally; MNPI = private material piece used illegally."

### ETH-TRAP-003: Fair Dealing — Not Equal Treatment
**Trap:** Thinking fair dealing means equal treatment.
**Truth:** Fair dealing means all clients must have access to recommendations simultaneously, but allocations can vary by suitability.
**Protection:** "Fair ≠ equal."

### ETH-TRAP-004: GIPS — Who Can Claim Compliance?
**Trap:** Thinking software vendors or consultants can claim GIPS compliance.
**Truth:** Only firms that actually manage assets.
**Protection:** "Must manage money to claim GIPS."

### ETH-TRAP-005: Referral Fees
**Trap:** Thinking referral fees are prohibited.
**Truth:** They must be DISCLOSED to clients and employers.
**Protection:** "Disclosure, not prohibition."

### ETH-TRAP-006: Independence and Objectivity — Gifts
**Trap:** Thinking ALL gifts violate independence.
**Truth:** Token gifts that do not influence judgment are acceptable.
**Protection:** "Would a reasonable person think this gift could influence?"

### ETH-TRAP-007: Guaranteed Returns
**Trap:** Allowing guarantees on asset-backed securities but failing to explain the underlying risk.
**Truth:** Can only guarantee if a sovereign or equivalent backs it, even then, explain clearly.
**Protection:** "Never guarantee market returns."

### ETH-TRAP-008: Supervisor Responsibilities
**Trap:** Assuming delegation of duties removes supervisory responsibility.
**Truth:** You cannot delegate away your responsibility.
**Protection:** "Delegation does not mean abdication."

---

*End of Comprehensive Trap Catalog*
