# CFA Level I — Fixed Income Question Bank

---

### Q-FIX-0001 | Difficulty: 2 | Time: 90s | Pattern: Direct Calculation | Trap: Bond Pricing

**Question:**
A 5-year bond with a face value of $1,000 pays an annual coupon of 6%. The yield to maturity is 8%. The bond price is closest to:

A) $920.15
B) $960.07
C) $1,000.00
D) $1,080.30

**Correct Answer:** A

**Explanation:** Since coupon (6%) < YTM (8%), this is a DISCOUNT bond (price < par). Price = PV of coupons + PV of face value.

N=5, I/Y=8, PMT=60, FV=1000 → CPT PV = $920.15.

Or: P = 60/1.08 + 60/1.08² + 60/1.08³ + 60/1.08⁴ + 1060/1.08⁵ = 55.56 + 51.44 + 47.63 + 44.10 + 721.42 = $920.15.

**Wrong Answer Analysis:**
- B: Calculation error
- C: Only if YTM = coupon rate (par bond)
- D: Price > par would require YTM < coupon rate

**LO Reference:** FIX-03-01-LO01
**Formula:** P = Σ C/(1+r)^t + FV/(1+r)^n
**Common Trap:** Forgetting that discount bonds trade below par

---

### Q-FIX-0002 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Callable vs. Putable

**Question:**
Compared to an otherwise identical option-free bond, a callable bond will most likely have:

A) Higher price and lower yield
B) Lower price and higher yield
C) Same price but lower duration
D) Higher price but higher yield

**Correct Answer:** B

**Explanation:** A callable bond gives the ISSUER the right to redeem early. Since this benefits the issuer, the investor demands compensation → LOWER price and HIGHER yield. V_callable = V_straight - V_call option. The call option reduces the bond's value to the investor.

**Wrong Answer Analysis:**
- A: Describes a PUTABLE bond (investor option → higher price, lower yield)
- C: Callable bonds have lower effective duration, but price is also affected
- D: Price and yield move in opposite directions

**LO Reference:** FIX-01-01-LO04
**Formula:** V_callable = V_straight - V_call
**Common Trap:** Confusing callable (issuer option, bad for investor) with putable (investor option, good)

---

### Q-FIX-0003 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Accrued Interest

**Question:**
A bond with a 6% annual coupon (paid semi-annually) is quoted at a flat price of $980. It has been 60 days since the last coupon payment, and the coupon period is 180 days. The full (dirty) price is closest to:

A) $970.00
B) $980.00
C) $990.00
D) $1,000.00

**Correct Answer:** C

**Explanation:** Semi-annual coupon = $1,000 × 6% / 2 = $30. Accrued interest = $30 × (60/180) = $10. Full price = Flat price + Accrued interest = $980 + $10 = $990.

**Wrong Answer Analysis:**
- A: Subtracted accrued interest instead of adding
- B: Ignored accrued interest
- D: Arithmetic error

**LO Reference:** FIX-03-01-LO03
**Formula:** Full Price = Flat Price + Accrued Interest
**Common Trap:** Forgetting to add accrued interest to quoted price

---

### Q-FIX-0004 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Modified Duration

**Question:**
A bond has a Macaulay duration of 7.2 years and a YTM of 6% (annual-pay). The modified duration is closest to:

A) 6.79
B) 7.20
C) 7.63
D) 7.92

**Correct Answer:** A

**Explanation:** Modified Duration = Macaulay Duration / (1 + r) = 7.2 / (1.06) = 6.79. For semi-annual bonds, use r per period: ModDur = MacDur / (1 + r_per_period).

Modified duration measures the percentage price change for a 1% (100 bps) change in yield. %ΔP ≈ -ModDur × Δy.

**Wrong Answer Analysis:**
- B: Reported Macaulay duration without conversion
- C: Multiplied instead of divided: 7.2 × 1.06
- D: Wrong calculation

**LO Reference:** FIX-06-01-LO02
**Formula:** ModDur = MacDur / (1 + r)
**Common Trap:** Confusing Macaulay duration with modified duration

---

### Q-FIX-0005 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Duration Properties

**Question:**
Which of the following bonds will have the highest Macaulay duration, all else equal?

A) A 10-year zero-coupon bond
B) A 10-year bond with a 10% coupon
C) A 10-year bond with a 5% coupon
D) A 5-year zero-coupon bond

**Correct Answer:** A

**Explanation:** Macaulay duration of a zero-coupon bond equals its maturity (10 years here). For coupon bonds, duration is LESS than maturity because interim coupon payments reduce the weighted-average time to receipt. The lower the coupon, the closer duration is to maturity, but it's always less than maturity for coupon bonds. A 10-year zero has duration = 10 years, the highest of these options.

**Wrong Answer Analysis:**
- B: Higher coupon → lower duration (more weight on earlier payments)
- C: Lower coupon than B, so higher duration than B, but still < 10
- D: 5-year zero → duration = 5 years

**LO Reference:** FIX-06-01-LO01
**Common Trap:** Forgetting that zero-coupon bond duration equals maturity

---

### Q-FIX-0006 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Price Change with Convexity

**Question:**
A bond has modified duration of 6.5 and convexity of 45. If the YTM decreases by 150 basis points, the estimated percentage price change is closest to:

A) +9.75%
B) +10.26%
C) +10.76%
D) +11.25%

**Correct Answer:** B

**Explanation:** %ΔP ≈ -ModDur × Δy + ½ × Conv × (Δy)²

= -(6.5) × (-0.015) + ½ × 45 × (-0.015)²
= 0.0975 + 0.5 × 45 × 0.000225
= 0.0975 + 0.0050625
= 0.10256

%ΔP ≈ 10.26%

Without convexity: 6.5 × 0.015 = 9.75% (understates). Convexity adds about 51 bps.

**Wrong Answer Analysis:**
- A: Duration-only estimate (ignores convexity): 9.75%
- C: Overstatement or arithmetic error
- D: Wrong sign or calculation

**LO Reference:** FIX-06-01-LO06
**Formula:** %ΔP ≈ -ModDur × Δy + ½Conv × (Δy)²
**Common Trap:** Forgetting the convexity adjustment in large yield changes

---

### Q-FIX-0007 | Difficulty: 2 | Time: 60s | Pattern: Direct Calculation | Trap: Current Yield

**Question:**
A bond with a face value of $1,000, a coupon rate of 5%, and a current market price of $900 has a current yield closest to:

A) 5.00%
B) 5.56%
C) 5.88%
D) 6.25%

**Correct Answer:** B

**Explanation:** Current Yield = Annual Coupon / Bond Price = $50 / $900 = 5.56%. For a discount bond (price < par), current yield is between the coupon rate (5%) and YTM (higher). Current yield only considers coupon income, not capital gains/losses.

**Wrong Answer Analysis:**
- A: This is the coupon rate (50/1000)
- C: Wrong calculation
- D: Wrong calculation

**LO Reference:** FIX-03-01-LO04
**Formula:** Current Yield = Annual Coupon / Bond Price
**Common Trap:** Using face value instead of market price in denominator

---

### Q-FIX-0008 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Implied Forward Rate

**Question:**
The 2-year spot rate is 3% and the 3-year spot rate is 4%. The 1-year forward rate two years from now (2y1y) is closest to:

A) 5.00%
B) 5.03%
C) 6.00%
D) 6.03%

**Correct Answer:** D

**Explanation:** (1+z₃)³ = (1+z₂)² × (1+₂f₁)
(1.04)³ = (1.03)² × (1+₂f₁)
1.124864 = 1.0609 × (1+₂f₁)
₁+₂f₁ = 1.124864 / 1.0609 = 1.06028
₂f₁ = 6.03%

**Wrong Answer Analysis:**
- A: 3×4 - 2×3 = 12-6 = 6% (simplistic and slightly wrong)
- B: Minor calculation error
- C: 4% + (4% - 3%) = 5% (linear extrapolation)

**LO Reference:** FIX-05-01-LO02
**Formula:** (1+z_B)^B = (1+z_A)^A × (1+IFR)^(B-A)
**Common Trap:** Using simple linear approximation instead of compounding

---

### Q-FIX-0009 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Yield Spreads

**Question:**
For a callable corporate bond, the option-adjusted spread (OAS) compared to its Z-spread is most likely:

A) Higher
B) Lower
C) Equal
D) Cannot be determined

**Correct Answer:** B

**Explanation:** For a callable bond, the Z-spread includes compensation for the embedded call option. OAS = Z-spread - Option value (in spread terms). Therefore, OAS is LOWER than Z-spread for callable bonds. For putable bonds, OAS is HIGHER than Z-spread (investor has the option, so the adjustment is favorable).

**Wrong Answer Analysis:**
- A: Describes PUTABLE bonds, not callable
- C: Only true for option-free bonds (no embedded options)
- D: Can be determined — callable bonds always have OAS < Z-spread

**LO Reference:** FIX-04-01-LO03
**Formula:** OAS = Z-spread - Option Cost
**Common Trap:** Reversing OAS vs. Z-spread for callable vs. putable bonds

---

### Q-FIX-0010 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Credit Risk Components

**Question:**
Credit risk consists of which two components?

A) Market risk and liquidity risk
B) Default probability and loss severity
C) Interest rate risk and reinvestment risk
D) Systematic risk and unsystematic risk

**Correct Answer:** B

**Explanation:** Credit risk = Default probability (likelihood of default) × Loss severity (1 - Recovery rate). The expected loss = Probability of Default × Loss Given Default. Investors demand compensation for both the chance of default and the expected loss if default occurs.

**Wrong Answer Analysis:**
- A: These are separate risk categories, not credit risk components
- C: These are interest rate risks, not credit risks
- D: These are equity risk classifications

**LO Reference:** FIX-07-01-LO01
**Formula:** Expected Loss = PD × LGD
**Common Trap:** Forgetting that credit risk has two dimensions (probability and severity)

---

### Q-FIX-0011 | Difficulty: 3 | Time: 90s | Pattern: Scenario Interpretation | Trap: Theories of Term Structure

**Question:**
If investors believe that short-term rates will remain unchanged but demand a premium for holding longer-term bonds, the yield curve will most likely be:

A) Flat
B) Upward sloping
C) Downward sloping
D) Humped

**Correct Answer:** B

**Explanation:** According to the liquidity preference theory, investors demand a premium for the higher interest rate risk of longer-term bonds. Even if future short rates are expected to be UNCHANGED, the liquidity premium makes the yield curve upward sloping. Pure expectations theory (no premium) would predict a flat curve with unchanged rates.

**Wrong Answer Analysis:**
- A: Pure expectations theory prediction (no liquidity premium)
- C: Requires expected rate DROPS to overcome the liquidity premium
- D: Requires specific expected rate patterns

**LO Reference:** FIX-05-01-LO03
**Common Trap:** Confusing pure expectations theory with liquidity preference theory

---

### Q-FIX-0012 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Money Market Yields

**Question:**
A 180-day T-bill with a face value of $10,000 is priced at $9,800. The discount rate is closest to:

A) 2.00%
B) 4.00%
C) 4.08%
D) 4.17%

**Correct Answer:** B

**Explanation:** Discount Rate = (FV - P)/FV × (360/n) = ($10,000 - $9,800)/$10,000 × (360/180) = $200/$10,000 × 2 = 0.02 × 2 = 4.00%.

Note: Money market instruments use 360-day year. The discount rate uses FACE VALUE as denominator.

The add-on rate (AOR) would use purchase price: ($200/$9,800) × (360/180) = 4.08%.
The bond equivalent yield (BEY) uses 365-day year: ($200/$9,800) × (365/180) = 4.14%.

**Wrong Answer Analysis:**
- A: Forgot to annualize: 200/10000 = 2%
- C: This is the add-on rate (AOR)
- D: This is close to the bond equivalent yield

**LO Reference:** FIX-03-01-LO06
**Formula:** DR = (FV - P)/FV × (360/n)
**Common Trap:** Confusing discount rate, add-on rate, and bond equivalent yield

---

### Q-FIX-0013 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Bond Indenture

**Question:**
Which of the following is most likely an affirmative covenant in a bond indenture?

A) A restriction on the issuance of additional debt
B) A requirement to maintain a minimum interest coverage ratio
C) A restriction on the sale of assets
D) A limitation on dividend payments

**Correct Answer:** B

**Explanation:** Affirmative covenants require the issuer TO DO certain things (e.g., maintain insurance, pay taxes, submit financial statements, maintain minimum ratios). Negative covenants RESTRICT the issuer from doing certain things (e.g., issuing more debt, selling assets, paying excessive dividends).

**Wrong Answer Analysis:**
- A: NEGATIVE covenant (restriction on debt issuance)
- C: NEGATIVE covenant (restriction on asset sales)
- D: NEGATIVE covenant (restriction on dividends)

**LO Reference:** FIX-01-01-LO02
**Common Trap:** Confusing affirmative covenants (things to DO) with negative covenants (things NOT to do)

---

### Q-FIX-0014 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Duration Gap

**Question:**
A bond portfolio has a market value of $10 million, modified duration of 6.0, and convexity of 25. If the portfolio manager wants to reduce the portfolio's modified duration to 4.0 using a bond futures contract with modified duration of 8.0 and contract value of $100,000, how many futures contracts should be sold? (Assume the CTD bond has a conversion factor of 1.0.)

A) 25
B) 50
C) 125
D) 250

**Correct Answer:** A

**Explanation:** Number of contracts = (Target Dur - Current Dur) × Portfolio Value / (Futures Dur × Contract Value) = (4.0 - 6.0) × $10,000,000 / (8.0 × $100,000) = (-2.0 × $10,000,000) / ($800,000) = -$20,000,000 / $800,000 = -25 contracts.

Negative means SELL 25 contracts. Selling futures reduces the portfolio's duration exposure.

**Wrong Answer Analysis:**
- B: Used wrong calculation, maybe forgot duration ratio
- C: Wrong denominator
- D: Used absolute values and wrong math

**LO Reference:** FIX-06-01-LO03
**Common Trap:** Forgetting the sign (negative = sell); wrong contract value in denominator

---

### Q-FIX-0015 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: MBS Prepayment Risk

**Question:**
When interest rates decline, mortgage-backed security (MBS) investors face:

A) Extension risk because homeowners refinance less
B) Contraction risk because homeowners refinance more
C) No prepayment risk because MBS are government guaranteed
D) Default risk because lower rates hurt mortgage affordability

**Correct Answer:** B

**Explanation:** When rates DECLINE, homeowners refinance to lock in lower rates → prepayments INCREASE → MBS investors receive principal back EARLIER than expected → must reinvest at lower rates. This is CONTRACTION risk (the MBS "contracts" or shortens). Extension risk occurs when rates RISE and prepayments slow.

**Wrong Answer Analysis:**
- A: Extension risk occurs when rates RISE, not fall
- C: MBS have prepayment risk regardless of guarantees
- D: Lower rates typically IMPROVE affordability

**LO Reference:** FIX-08-01-LO02
**Common Trap:** Confusing contraction risk (falling rates → faster prepayments) with extension risk (rising rates → slower prepayments)

---

*End of Fixed Income Question Bank*
