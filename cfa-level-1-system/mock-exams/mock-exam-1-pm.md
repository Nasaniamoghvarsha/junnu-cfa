# CFA Level I — Official Mock Exam 1 (Session 2: Afternoon Paper)

**Format:** 90 Questions | 135 Minutes | Official 3-Option Exam Mechanics  
**Topic Coverage:** Equity Investments, Fixed Income, Derivatives, Alternative Investments, Portfolio Management  

---

## Section F: Equity Investments

### Q-MOCK1-PM-010 | Difficulty: 3 | Time: 90s | Pattern: Calculation | Trap: DDM Growth Rate

**Question:**
An analyst calculates that a stock will pay an annual dividend of $2.50 next year ($D_1$). The required rate of return on equity is 10.0%, and dividends are expected to grow at a constant rate of 4.0% indefinitely. According to the Gordon Growth Model, what is the intrinsic value of the stock?

A) $41.67
B) $62.50
C) $65.00

**Correct Answer:** B

**Explanation:** Gordon Growth Model: $V_0 = D_1 / (r - g)$.
Given $D_1 = \$2.50$, $r = 10.0\% = 0.10$, and $g = 4.0\% = 0.04$.
$V_0 = 2.50 / (0.10 - 0.04) = 2.50 / 0.06 = \$62.50$.

**Wrong Answer Analysis:**
- A: Incorrect — erroneously adds $g$ to $r$ in denominator ($2.50 / (0.10 + 0.04) = \$17.86$) or uses $D_0$ incorrectly.
- C: Incorrect — compounds $D_1$ again by $(1 + g)$ in numerator ($2.50 \times 1.04 / 0.06 = \$65.00$), which is done only when given current dividend $D_0$.

**LO Reference:** EQ-03-01-LO02 (Gordon Growth Dividend Discount Model)

---

### Q-MOCK1-PM-011 | Difficulty: 2 | Time: 60s | Pattern: Conceptual | Trap: Market Efficiency Forms

**Question:**
If security prices fully reflect all past market trading data and all publicly available information, but do NOT reflect nonpublic insider information, the market is best described as being in which form of market efficiency?

A) Weak-form efficient
B) Semi-strong form efficient
C) Strong-form efficient

**Correct Answer:** B

**Explanation:** Semi-strong form market efficiency asserts that security prices rapidly adjust to all publicly available information (financial statements, market data, news announcements). Insider nonpublic information can still earn abnormal returns in semi-strong form efficient markets.

**Wrong Answer Analysis:**
- A: Incorrect — weak-form efficiency asserts prices reflect only historical market trading data (prices and volume).
- C: Incorrect — strong-form efficiency asserts prices reflect ALL public AND private insider information.

**LO Reference:** EQ-02-01-LO01 (Efficient Market Hypothesis Forms)

---

## Section G: Fixed Income

### Q-MOCK1-PM-012 | Difficulty: 3 | Time: 90s | Pattern: Calculation | Trap: Full vs Flat Bond Price

**Question:**
A 5-year coupon bond has a annual coupon rate of 6.0% (payable annually) and a yield-to-maturity of 5.0%. Exactly 180 days have passed since the last coupon payment (assuming a 360-day year). If the flat price of the bond is $1,043.29, what is the full (dirty) price of the bond?

A) $1,043.29
B) $1,073.29
C) $1,103.29

**Correct Answer:** B

**Explanation:** $\text{Full Price} = \text{Flat Price} + \text{Accrued Interest}$.
$\text{Accrued Interest} = \text{Coupon Payment} \times (\text{Days Elapsed} / \text{Days in Period})$.
Annual Coupon $= 6.0\% \times \$1,000 = \$60.00$.
$\text{Accrued Interest} = \$60.00 \times (180 / 360) = \$30.00$.
$\text{Full Price} = \$1,043.29 + \$30.00 = \$1,073.29$.

**Wrong Answer Analysis:**
- A: Incorrect — gives the flat (clean) price without adding accrued interest.
- C: Incorrect — adds the full annual coupon of $60.00 instead of pro-rating for 180 days.

**LO Reference:** FI-02-01-LO03 (Bond Pricing Full vs Flat Price and Accrued Interest)

---

### Q-MOCK1-PM-013 | Difficulty: 4 | Time: 120s | Pattern: Conceptual | Trap: Duration and Convexity Effect

**Question:**
For a option-free bond, when interest rates decrease by 100 basis points, the actual price increase calculated using modified duration alone will be:

A) Equal to the actual price increase
B) Less than the actual price increase
C) Greater than the actual price increase

**Correct Answer:** B

**Explanation:** Modified duration provides a linear approximation of the price-yield relationship. Because of positive convexity, the true price-yield curve lies above the duration tangent line. For interest rate decreases, convexity causes the actual price increase to be LARGER than predicted by duration alone. Therefore, duration alone UNDERESTIMATES the price increase (it is less than the actual price increase).

**Wrong Answer Analysis:**
- A: Incorrect — linear duration ignores convexity curvature.
- C: Incorrect — duration alone overestimates price drops for yield increases, but underestimates price gains for yield drops.

**LO Reference:** FI-03-02-LO01 (Modified Duration and Convexity Adjustment)

---

## Section H: Derivatives

### Q-MOCK1-PM-014 | Difficulty: 3 | Time: 90s | Pattern: Conceptual | Trap: Option Moneyness & Greeks

**Question:**
An investor buys a European call option on a stock with an exercise price of $50. At expiration, the underlying stock price is $58. If the option premium paid was $3.00, what is the net payoff (profit) to the option buyer at expiration?

A) $5.00
B) $8.00
C) $11.00

**Correct Answer:** A

**Explanation:** Gross Payoff $= \max(0, S_T - X) = \max(0, 58 - 50) = \$8.00$.
Net Profit $= \text{Gross Payoff} - \text{Option Premium Paid} = \$8.00 - \$3.00 = \$5.00$.

**Wrong Answer Analysis:**
- B: Incorrect — gives gross payoff ($8.00) without deducting the $3.00 premium paid.
- C: Incorrect — erroneously adds option premium to gross payoff.

**LO Reference:** DER-01-01-LO02 (Call Option Payoff and Profit Calculation)

---

## Section I: Alternative Investments

### Q-MOCK1-PM-015 | Difficulty: 3 | Time: 90s | Pattern: Conceptual | Trap: Private Equity Fee Structures

**Question:**
A private equity fund charges a 2% management fee and a 20% performance fee (carried interest) with a 8% hurdle rate. If the fund earns a gross return of 6% in a given year, how much performance fee will the general partner (GP) collect?

A) 0%
B) 1.2%
C) 2.0%

**Correct Answer:** A

**Explanation:** A hurdle rate is the minimum return the fund must achieve before the GP is eligible to receive performance fees (carried interest). Because the gross return of 6% is below the 8% hurdle rate, the GP receives $0.00$ performance fee.

**Wrong Answer Analysis:**
- B: Incorrect — calculates $20\% \times 6\% = 1.2\%$, ignoring the hurdle rate condition.
- C: Incorrect — confuses management fee with performance fee.

**LO Reference:** ALT-01-01-LO03 (Private Equity Fee Calculation and Hurdle Rates)

---

## Section J: Portfolio Management

### Q-MOCK1-PM-016 | Difficulty: 3 | Time: 90s | Pattern: Calculation | Trap: Sharpe vs Treynor Ratio

**Question:**
A portfolio has an expected return of 14.0%, a beta of 1.2, and a total standard deviation of 18.0%. If the risk-free rate of return is 4.0%, what is the Sharpe Ratio of the portfolio?

A) 0.56
B) 0.78
C) 8.33

**Correct Answer:** A

**Explanation:** Sharpe Ratio $= (R_p - R_f) / \sigma_p = (14.0\% - 4.0\%) / 18.0\% = 10.0\% / 18.0\% = 0.5555 \dots \approx 0.56$.

**Wrong Answer Analysis:**
- B: Incorrect — calculates Treynor Ratio using Beta instead of standard deviation ($10.0\% / 1.2 = 8.33$).
- C: Incorrect — calculates Treynor Ratio without converting percent ($10.0 / 1.2 = 8.33$).

**LO Reference:** PM-02-01-LO01 (Sharpe Ratio and Performance Risk Metrics)
