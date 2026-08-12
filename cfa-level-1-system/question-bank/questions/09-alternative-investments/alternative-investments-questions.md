# CFA Level I — Alternative Investments Question Bank

---

### Q-ALT-0001 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Alternative Investment Features

**Question:**
Which of the following is most likely a common characteristic of alternative investments compared to traditional investments?

A) Higher liquidity
B) Greater regulatory oversight
C) Lower management fees
D) Less transparency and lower liquidity

**Correct Answer:** D

**Explanation:** Alternative investments typically feature less transparency (limited reporting requirements), lower liquidity (lock-up periods, limited redemption windows), higher fees (management + incentive), and narrower manager specialization. These are key distinguishing features from traditional public market investments.

**Wrong Answer Analysis:**
- A: Alternative investments typically have LOWER liquidity
- B: Alternatives typically have LESS regulatory oversight
- C: Alternatives have HIGHER fees (management fee + incentive fee)

**LO Reference:** ALT-01-01-LO01
**Common Trap:** Confusing alternative investment characteristics with traditional investment features

---

### Q-ALT-0002 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Hedge Fund Fees

**Question:**
A hedge fund has a 2% management fee (on beginning AUM) and a 20% incentive fee with a soft hurdle rate of 5%. Beginning AUM is $100 million, and the fund earns 15% before fees. Total fees are closest to:

A) $4.0 million
B) $4.6 million
C) $5.0 million
D) $5.6 million

**Correct Answer:** C

**Explanation:** Management fee = 2% × $100M = $2M. Return before fees = $100M × 15% = $15M. With soft hurdle: Fund cleared the 5% hurdle ($5M), so incentive fee applies to ALL profits. Incentive fee = 20% × ($15M - $2M) = 20% × $13M = $2.6M. Wait, with soft hurdle, if hurdle is met, incentive applies to entire profits.

Actually, I need to clarify: With SOFT hurdle, if the return exceeds the hurdle, the incentive fee is calculated on the ENTIRE return (not just the excess above the hurdle). 

Gross return = $100M × 15% = $15M
Hurdle = $100M × 5% = $5M (met)
Management fee = $2M
Incentive fee = 20% × ($15M - $2M) = 20% × $13M = $2.6M
Total fees = $2M + $2.6M = $4.6M

That's answer B. But let me reconsider...

With a soft hurdle and the hurdle is met, incentive is on all profits. Some versions calculate: Incentive = 20% × (Gross return - Management fee) = 20% × ($15M - $2M) = $2.6M. Total = $4.6M.

With a HARD hurdle: Incentive only on profits above hurdle = 20% × ($15M - $5M) = 20% × $10M = $2M. Total = $4M.

But the question says SOFT hurdle. With soft hurdle, the incentive is on ALL profits once the hurdle is exceeded (not just excess). So incentive = 20% × ($15M - $2M) = $2.6M. Total = $4.6M.

Answer is B.

**Correct Answer:** B

**Explanation:** Management fee = 2% × $100M = $2M. Gross return = 15% > 5% hurdle (met, soft hurdle). Incentive fee = 20% × ($15M - $2M) = $2.6M. Total fees = $4.6M. With a soft hurdle, the incentive fee applies to ALL profits once the hurdle is exceeded.

**Wrong Answer Analysis:**
- A: Used hard hurdle: 20% × ($15M - $5M - $2M) or similar
- C: Forgot management fee deduction before incentive: 20% × $15M = $3M + $2M = $5M
- D: Overstated fees

**LO Reference:** ALT-02-01-LO01
**Common Trap:** Confusing soft hurdle (incentive on all profits) with hard hurdle (incentive only on excess)

---

### Q-ALT-0003 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: High-Water Mark

**Question:**
A hedge fund has a high-water mark provision. Last year, the fund's AUM fell from $100 million to $85 million. This year, it rises to $105 million. With a 20% incentive fee, the incentive fee earned this year is closest to:

A) $1 million
B) $2 million
C) $3 million
D) $4 million

**Correct Answer:** A

**Explanation:** The high-water mark was $100M. This year's value ($105M) exceeded the HWM, so incentive is due only on profits ABOVE the previous HWM: 20% × ($105M - $100M) = 20% × $5M = $1M. Without the HWM, the fee would have been 20% × ($105M - $85M) = $4M — but the HWM prevents double-counting of recovery.

**Wrong Answer Analysis:**
- B: Used wrong basis
- C: Used wrong basis
- D: Ignored high-water mark: 20% × ($105M - $85M) = $4M

**LO Reference:** ALT-02-01-LO01
**Common Trap:** Forgetting that high-water mark prevents incentive fees on recovery of losses

---

### Q-ALT-0004 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Contango vs. Backwardation

**Question:**
When the futures price of a commodity is below the expected future spot price, the market is in:

A) Contango
B) Normal backwardation
C) Full carry
D) A carrying charge market

**Correct Answer:** B

**Explanation:** Normal backwardation: Futures price < Expected future spot price. This occurs when hedgers are net short (producers hedging) and speculators demand a risk premium to go long → futures prices are bid below expected spot. Contango (sometimes called "normal contango" or simply "contango"): Futures > Spot, often due to storage costs.

Note: Contango ≠ "futures > spot" (though that's one definition). The Keynes theory definition: normal backwardation = futures < expected future spot.

**Wrong Answer Analysis:**
- A: Contango means futures > spot (or futures > expected spot, depending on context)
- C: Full carry = futures = spot + full cost of carry
- D: Carrying charge market is another term for contango

**LO Reference:** ALT-05-01-LO01
**Common Trap:** Confusing contango/backwardation based on spot vs. futures vs. expected spot

---

### Q-ALT-0005 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Commodity Returns

**Question:**
A commodity investor goes long a futures contract. The spot return is 3%, the roll yield is -2%, and the collateral yield is 1%. The total return is closest to:

A) 0%
B) 1%
C) 2%
D) 4%

**Correct Answer:** C

**Explanation:** Total return = Spot return + Roll yield + Collateral yield = 3% + (-2%) + 1% = 2%. Roll yield is negative because the market is in contango (futures > spot, rolling up costs money). Collateral yield comes from interest earned on the cash used as collateral.

**Wrong Answer Analysis:**
- A: 3% - 2% - 1% = 0% (used negative collateral yield)
- B: Forgot collateral yield: 3% - 2% = 1%
- D: 3% + 2% + (-1%)? Wrong signs

**LO Reference:** ALT-05-01-LO02
**Formula:** Total Return = Spot Return + Roll Yield + Collateral Yield
**Common Trap:** Getting the sign of roll yield wrong

---

### Q-ALT-0006 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: PE Fund Structures

**Question:**
In a typical private equity fund structure, the general partner (GP) most likely:

A) Provides the majority of the fund's capital
B) Has limited liability for the fund's obligations
C) Manages the fund's investments and earns carried interest
D) Is a passive investor with no management role

**Correct Answer:** C

**Explanation:** The GP manages the fund, makes investment decisions, and earns carried interest (typically 20% of profits). Limited partners (LPs) provide the majority of capital and have limited liability. The GP typically has UNLIMITED liability for fund obligations.

**Wrong Answer Analysis:**
- A: LPs provide the majority of capital, not the GP
- B: GPs typically have UNLIMITED liability; LPs have limited liability
- D: LPs are passive investors; GPs actively manage

**LO Reference:** ALT-01-01-LO03
**Common Trap:** Confusing GP (manager, carried interest, unlimited liability) with LP (investor, limited liability, passive)

---

### Q-ALT-0007 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: VC Stages

**Question:**
A venture capital investment made in a company that has a proven business model, generating revenue but not yet profitable, and needs capital to scale operations is most likely classified as:

A) Seed stage
B) Early stage
C) Later stage (expansion)
D) Mezzanine stage

**Correct Answer:** C

**Explanation:** Later-stage/expansion VC targets companies with established products, growing revenue, and a path to profitability. The company needs capital to SCALE. Seed stage = idea/concept. Early stage = product development, initial commercialization. Mezzanine = pre-IPO bridge financing.

**Wrong Answer Analysis:**
- A: Seed stage = pre-revenue, concept development
- B: Early stage = product development, initial market entry
- D: Mezzanine = pre-IPO, near-exit financing

**LO Reference:** ALT-03-01-LO02
**Common Trap:** Confusing expansion/later-stage VC with mezzanine (pre-IPO) financing

---

### Q-ALT-0008 | Difficulty: 2 | Time: 60s | Pattern: Direct Calculation | Trap: MOIC

**Question:**
A private equity fund invests $50 million in a company. After 5 years, it sells the company for $110 million and had received $15 million in dividends during the holding period. The MOIC is closest to:

A) 2.20×
B) 2.50×
C) 2.80×
D) 3.10×

**Correct Answer:** B

**Explanation:** MOIC = (Realized Value + Unrealized Value) / Total Invested Capital = ($110M + $15M) / $50M = $125M / $50M = 2.50×. MOIC measures total return multiple independent of time. This investment returned 2.5 times the invested capital.

**Wrong Answer Analysis:**
- A: Only included sale value: $110M / $50M = 2.20× (forgot dividends)
- C: Calculation error
- D: Calculation error

**LO Reference:** ALT-02-01-LO02
**Formula:** MOIC = (Realized + Unrealized) / Invested Capital
**Common Trap:** Forgetting dividend distributions in MOIC calculation

---

### Q-ALT-0009 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: REIT Characteristics

**Question:**
Which of the following is most likely a characteristic of Real Estate Investment Trusts (REITs)?

A) They pay no dividends to shareholders
B) They are required to distribute most of their taxable income as dividends
C) They are taxed at the corporate level like regular corporations
D) They can only invest in residential properties

**Correct Answer:** B

**Explanation:** REITs must distribute at least 90% of taxable income to shareholders as dividends to maintain their tax-advantaged status. In exchange, REITs generally pay no corporate tax on distributed income (taxed at investor level). They invest across residential, commercial, industrial, and other property types.

**Wrong Answer Analysis:**
- A: REITs are REQUIRED to distribute most income as dividends
- C: REITs generally avoid corporate tax by distributing income
- D: REITs invest across all property types, not just residential

**LO Reference:** ALT-04-01-LO01
**Common Trap:** Confusing REIT tax treatment with regular corporate taxation

---

### Q-ALT-0010 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Hedge Fund Strategies

**Question:**
A hedge fund strategy that seeks to profit from pricing discrepancies between related securities (e.g., convertible bonds and the underlying stock) while maintaining low net market exposure is most likely:

A) Global macro
B) Event-driven
C) Relative value
D) Long/short equity

**Correct Answer:** C

**Explanation:** Relative value strategies seek to exploit pricing inefficiencies between related securities while minimizing directional market exposure. Convertible arbitrage (buying convertibles, shorting stock) is a classic example. Event-driven focuses on corporate events (M&A), global macro on economic trends, and long/short takes directional bets.

**Wrong Answer Analysis:**
- A: Global macro = bets on broad economic/market trends
- B: Event-driven = corporate events (mergers, restructurings, bankruptcies)
- D: Long/short equity = directional equity exposure, typically net long

**LO Reference:** ALT-06-01-LO01
**Common Trap:** Confusing relative value (market-neutral pricing discrepancies) with event-driven (corporate events)

---

### Q-ALT-0011 | Difficulty: 2 | Time: 60s | Pattern: "Most Likely" Question | Trap: Infrastructure

**Question:**
Which of the following is most likely an example of a "brownfield" infrastructure investment?

A) Building a new toll road from scratch
B) Expanding an existing airport terminal
C) Developing green energy on undeveloped land
D) Constructing a new water treatment facility

**Correct Answer:** B

**Explanation:** Brownfield investments involve existing/operational infrastructure being expanded, upgraded, or refurbished. Greenfield involves building NEW infrastructure from scratch. Expanding an existing airport is brownfield; building a new airport, road, or facility from scratch is greenfield.

**Wrong Answer Analysis:**
- A: New construction from scratch = greenfield
- C: New development on undeveloped land = greenfield
- D: New construction = greenfield

**LO Reference:** ALT-04-01-LO03
**Common Trap:** Confusing greenfield (new) with brownfield (existing/expansion)

---

### Q-ALT-0012 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: LBO Characteristics

**Question:**
A leveraged buyout (LBO) is most likely characterized by:

A) Low use of debt financing
B) The target company's assets serving as collateral for acquisition debt
C) Reliance on the target's growth prospects rather than cash flows
D) Minority ownership by the private equity firm

**Correct Answer:** B

**Explanation:** In an LBO, the target company's assets AND cash flows are used as collateral for the acquisition debt. The key LBO characteristics: high leverage (60-90% debt), target's assets/cash flows backing the debt, majority/control ownership by the PE firm, and reliance on stable cash flows for debt service.

**Wrong Answer Analysis:**
- A: LBOs use HIGH debt (60-90% of purchase price)
- C: LBOs rely on STABLE CASH FLOWS (to service debt), not growth prospects
- D: PE firms typically take MAJORITY/CONTROL positions in LBOs

**LO Reference:** ALT-03-01-LO01
**Common Trap:** Understanding that LBOs rely on cash flows (not just asset values) for debt service

---

### Q-ALT-0013 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Real Estate Valuation

**Question:**
Which of the following real estate valuation methods is most likely to suffer from "appraisal smoothing"?

A) Comparable sales approach
B) Income approach (DCF)
C) Appraisal-based indices
D) REIT share prices

**Correct Answer:** C

**Explanation:** Appraisal-based indices rely on periodic property appraisals, which tend to be infrequent and based partly on past comparable transactions. This creates "appraisal smoothing" — reported values lag actual market movements, underestimating volatility and correlations. Transaction-based and REIT indices don't have this issue.

**Wrong Answer Analysis:**
- A: Comparable sales use recent transactions (less smoothing)
- B: DCF is forward-looking and not subject to appraisal smoothing
- D: REIT prices trade daily in the market (no smoothing)

**LO Reference:** ALT-04-01-LO02
**Common Trap:** Confusing which valuation methods suffer from smoothing bias

---

### Q-ALT-0014 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Private Debt

**Question:**
Which of the following is most likely a characteristic of mezzanine debt?

A) It is the most senior form of debt in the capital structure
B) It typically has equity-like features such as warrants
C) It is secured by specific company assets
D) It has lower yields than senior secured debt

**Correct Answer:** B

**Explanation:** Mezzanine debt is subordinated (junior to senior secured debt) and often includes equity kickers (warrants, conversion rights) to compensate for higher risk. It has higher yields than senior debt and is typically unsecured. Its hybrid nature (debt + equity features) is its defining characteristic.

**Wrong Answer Analysis:**
- A: Mezzanine is subordinated/JUNIOR, not senior
- C: Mezzanine is typically UNSECURED
- D: Mezzanine has HIGHER yields (more risk) than senior secured

**LO Reference:** ALT-03-01-LO04
**Common Trap:** Confusing mezzanine (junior, equity-like) with senior secured debt

---

### Q-ALT-0015 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Fee with Hurdle and Catch-Up

**Question:**
A PE fund has a 2% management fee, 20% incentive fee, an 8% hard hurdle rate, and a 100% catch-up provision. Beginning AUM is $50M, and gross return is 25%. The GP's incentive fee is closest to:

A) $1.70M
B) $2.30M
C) $2.50M
D) $3.40M

**Correct Answer:** B

**Explanation:** Management fee = 2% × $50M = $1M. Gross return = $50M × 25% = $12.5M. Net of mgmt fee = $11.5M. Hurdle = 8% × $50M = $4M.

With catch-up: First, LP gets hurdle = $4M. Then GP catches up: GP gets 20% of profits, LP gets remaining 80%. Since GP has been paid $0 so far, catch-up = (20%/80%) × $4M = $1M.

Split remaining profits: $11.5M - $4M - $1M = $6.5M. GP gets 20% × $6.5M = $1.3M. Total GP incentive = $1M + $1.3M = $2.3M.

**Wrong Answer Analysis:**
- A: Forgot catch-up or wrong calculation
- C: Simple 20% × $11.5M = $2.3M (coincidentally same without considering catch-up split)
- D: 20% × ($12.5M + $4M) or similar error

**LO Reference:** ALT-01-01-LO03
**Common Trap:** Mishandling catch-up provision calculations

---

*End of Alternative Investments Question Bank*
