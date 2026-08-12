# CFA Level I — Fixed Income Question Bank

---

### Q-FIX-0001 | Difficulty: 2 | Time: 90s | Pattern: Direct Calculation | Trap: Bond Pricing

**Question:**
A 5-year bond with a face value of $1,000 pays an annual coupon of 6%. The yield to maturity is 8%. The bond price is closest to:
A) $920.15
B) $960.07
C) $1,000.00


**Correct Answer:** A

**Explanation:** Since coupon (6%) < YTM (8%), this is a DISCOUNT bond (price < par). Price = PV of coupons + PV of face value.

N=5, I/Y=8, PMT=60, FV=1000 → CPT PV = $920.15.

Or: P = 60/1.08 + 60/1.08² + 60/1.08³ + 60/1.08⁴ + 1060/1.08⁵ = 55.56 + 51.44 + 47.63 + 44.10 + 721.42 = $920.15.

**Wrong Answer Analysis:**
- B: Calculation error
- C: Only if YTM = coupon rate (par bond)

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


**Correct Answer:** B

**Explanation:** A callable bond gives the ISSUER the right to redeem early. Since this benefits the issuer, the investor demands compensation → LOWER price and HIGHER yield. V_callable = V_straight - V_call option. The call option reduces the bond's value to the investor.

**Wrong Answer Analysis:**
- A: Describes a PUTABLE bond (investor option → higher price, lower yield)
- C: Callable bonds have lower effective duration, but price is also affected

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


**Correct Answer:** C

**Explanation:** Semi-annual coupon = $1,000 × 6% / 2 = $30. Accrued interest = $30 × (60/180) = $10. Full price = Flat price + Accrued interest = $980 + $10 = $990.

**Wrong Answer Analysis:**
- A: Subtracted accrued interest instead of adding
- B: Ignored accrued interest

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


**Correct Answer:** A

**Explanation:** Modified Duration = Macaulay Duration / (1 + r) = 7.2 / (1.06) = 6.79. For semi-annual bonds, use r per period: ModDur = MacDur / (1 + r_per_period).

Modified duration measures the percentage price change for a 1% (100 bps) change in yield. %ΔP ≈ -ModDur × Δy.

**Wrong Answer Analysis:**
- B: Reported Macaulay duration without conversion
- C: Multiplied instead of divided: 7.2 × 1.06

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


**Correct Answer:** A

**Explanation:** Macaulay duration of a zero-coupon bond equals its maturity (10 years here). For coupon bonds, duration is LESS than maturity because interim coupon payments reduce the weighted-average time to receipt. The lower the coupon, the closer duration is to maturity, but it's always less than maturity for coupon bonds. A 10-year zero has duration = 10 years, the highest of these options.

**Wrong Answer Analysis:**
- B: Higher coupon → lower duration (more weight on earlier payments)
- C: Lower coupon than B, so higher duration than B, but still < 10

**LO Reference:** FIX-06-01-LO01
**Common Trap:** Forgetting that zero-coupon bond duration equals maturity

---

### Q-FIX-0006 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Price Change with Convexity

**Question:**
A bond has modified duration of 6.5 and convexity of 45. If the YTM decreases by 150 basis points, the estimated percentage price change is closest to:
A) +9.75%
B) +10.26%
C) +10.76%


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


**Correct Answer:** B

**Explanation:** Current Yield = Annual Coupon / Bond Price = $50 / $900 = 5.56%. For a discount bond (price < par), current yield is between the coupon rate (5%) and YTM (higher). Current yield only considers coupon income, not capital gains/losses.

**Wrong Answer Analysis:**
- A: This is the coupon rate (50/1000)
- C: Wrong calculation

**LO Reference:** FIX-03-01-LO04
**Formula:** Current Yield = Annual Coupon / Bond Price
**Common Trap:** Using face value instead of market price in denominator

---

### Q-FIX-0008 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Implied Forward Rate

**Question:**
The 2-year spot rate is 3% and the 3-year spot rate is 4%. The 1-year forward rate two years from now (2y1y) is closest to:
A) 5.00%
B) 6.03%
C) 6.00%


**Correct Answer:** B

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


**Correct Answer:** B

**Explanation:** For a callable bond, the Z-spread includes compensation for the embedded call option. OAS = Z-spread - Option value (in spread terms). Therefore, OAS is LOWER than Z-spread for callable bonds. For putable bonds, OAS is HIGHER than Z-spread (investor has the option, so the adjustment is favorable).

**Wrong Answer Analysis:**
- A: Describes PUTABLE bonds, not callable
- C: Only true for option-free bonds (no embedded options)

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


**Correct Answer:** B

**Explanation:** Credit risk = Default probability (likelihood of default) × Loss severity (1 - Recovery rate). The expected loss = Probability of Default × Loss Given Default. Investors demand compensation for both the chance of default and the expected loss if default occurs.

**Wrong Answer Analysis:**
- A: These are separate risk categories, not credit risk components
- C: These are interest rate risks, not credit risks

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


**Correct Answer:** B

**Explanation:** According to the liquidity preference theory, investors demand a premium for the higher interest rate risk of longer-term bonds. Even if future short rates are expected to be UNCHANGED, the liquidity premium makes the yield curve upward sloping. Pure expectations theory (no premium) would predict a flat curve with unchanged rates.

**Wrong Answer Analysis:**
- A: Pure expectations theory prediction (no liquidity premium)
- C: Requires expected rate DROPS to overcome the liquidity premium

**LO Reference:** FIX-05-01-LO03
**Common Trap:** Confusing pure expectations theory with liquidity preference theory

---

### Q-FIX-0012 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Money Market Yields

**Question:**
A 180-day T-bill with a face value of $10,000 is priced at $9,800. The discount rate is closest to:
A) 2.00%
B) 4.00%
C) 4.08%


**Correct Answer:** B

**Explanation:** Discount Rate = (FV - P)/FV × (360/n) = ($10,000 - $9,800)/$10,000 × (360/180) = $200/$10,000 × 2 = 0.02 × 2 = 4.00%.

Note: Money market instruments use 360-day year. The discount rate uses FACE VALUE as denominator.

The add-on rate (AOR) would use purchase price: ($200/$9,800) × (360/180) = 4.08%.
The bond equivalent yield (BEY) uses 365-day year: ($200/$9,800) × (365/180) = 4.14%.

**Wrong Answer Analysis:**
- A: Forgot to annualize: 200/10000 = 2%
- C: This is the add-on rate (AOR)

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


**Correct Answer:** B

**Explanation:** Affirmative covenants require the issuer TO DO certain things (e.g., maintain insurance, pay taxes, submit financial statements, maintain minimum ratios). Negative covenants RESTRICT the issuer from doing certain things (e.g., issuing more debt, selling assets, paying excessive dividends).

**Wrong Answer Analysis:**
- A: NEGATIVE covenant (restriction on debt issuance)
- C: NEGATIVE covenant (restriction on asset sales)

**LO Reference:** FIX-01-01-LO02
**Common Trap:** Confusing affirmative covenants (things to DO) with negative covenants (things NOT to do)

---

### Q-FIX-0014 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Duration Gap

**Question:**
A bond portfolio has a market value of $10 million, modified duration of 6.0, and convexity of 25. If the portfolio manager wants to reduce the portfolio's modified duration to 4.0 using a bond futures contract with modified duration of 8.0 and contract value of $100,000, how many futures contracts should be sold? (Assume the CTD bond has a conversion factor of 1.0.)
A) 25
B) 50
C) 125


**Correct Answer:** A

**Explanation:** Number of contracts = (Target Dur - Current Dur) × Portfolio Value / (Futures Dur × Contract Value) = (4.0 - 6.0) × $10,000,000 / (8.0 × $100,000) = (-2.0 × $10,000,000) / ($800,000) = -$20,000,000 / $800,000 = -25 contracts.

Negative means SELL 25 contracts. Selling futures reduces the portfolio's duration exposure.

**Wrong Answer Analysis:**
- B: Used wrong calculation, maybe forgot duration ratio
- C: Wrong denominator

**LO Reference:** FIX-06-01-LO03
**Common Trap:** Forgetting the sign (negative = sell); wrong contract value in denominator

---

### Q-FIX-0015 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: MBS Prepayment Risk

**Question:**
When interest rates decline, mortgage-backed security (MBS) investors face:
A) Extension risk because homeowners refinance less
B) Contraction risk because homeowners refinance more
C) No prepayment risk because MBS are government guaranteed


**Correct Answer:** B

**Explanation:** When rates DECLINE, homeowners refinance to lock in lower rates → prepayments INCREASE → MBS investors receive principal back EARLIER than expected → must reinvest at lower rates. This is CONTRACTION risk (the MBS "contracts" or shortens). Extension risk occurs when rates RISE and prepayments slow.

**Wrong Answer Analysis:**
- A: Extension risk occurs when rates RISE, not fall
- C: MBS have prepayment risk regardless of guarantees

**LO Reference:** FIX-08-01-LO02
**Common Trap:** Confusing contraction risk (falling rates → faster prepayments) with extension risk (rising rates → slower prepayments)

---

### Q-FIX-0016 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Clean vs Dirty Bond Price

**Question:**
A semi-annual coupon bond with a par value of $1,000 and a 6% annual coupon is priced at a flat (clean) price of $980.00. The last coupon was paid 90 days ago, and the current coupon period has 180 days. The full (dirty) price of the bond is closest to:
A) $985.00
B) $995.00
C) $1,010.00


**Correct Answer:** B

**Explanation:** Calculation of Accrued Interest (AI) and Full (Dirty) Price:
$$\text{Semi-annual Coupon Payment} = \frac{\$1,000 \times 6\%}{2} = \$30.00$$
$$\text{Accrued Interest} = \$30.00 \times \left(\frac{90}{180}\right) = \$15.00$$
$$\text{Full (Dirty) Price} = \text{Clean Price} + \text{Accrued Interest} = \$980.00 + \$15.00 = \$995.00$$

**TI BA II Plus Keystrokes:**
- Accrued Interest = $30 \times (90 / 180) = 15$
- Full Price = $980 + 15 = 995$

**Wrong Answer Analysis:**
- A: Incorrect — calculated accrued interest on annual basis without dividing coupon by 2 ($30 \times 90/360 = 7.50$).
- C: Incorrect — added full annual coupon ($30$) instead of accrued fraction.

**LO Reference:** FIX-02-01-LO01 (Bond Accrued Interest & Full Price)
**Related Concepts:** Clean price, dirty price, accrued interest, coupon period fraction
**Common Misconception:** Forgetting to divide annual coupon by 2 for semi-annual bond pricing.

---

### Q-FIX-0017 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Bond Equivalent Yield Conversion

**Question:**
A 90-day T-bill with a face value of $1,000 is selling for $985. Which of the following statements regarding its Bank Discount Yield (BDY) and Bond Equivalent Yield (BEY) is most accurate?
A) BEY is higher than BDY because BEY uses a 365-day year and purchase price as denominator
B) BDY is higher than BEY because BDY uses a 360-day year
C) BEY and BDY are equal for all short-term money market instruments


**Correct Answer:** A

**Explanation:**
$$\text{BDY} = \left(\frac{1,000 - 985}{1,000}\right) \times \left(\frac{360}{90}\right) = 1.50\% \times 4 = 6.00\%$$
$$\text{BEY} = \left(\frac{1,000 - 985}{985}\right) \times \left(\frac{365}{90}\right) = 1.523\% \times 4.0556 = 6.18\%$$
BEY is ALWAYS higher than BDY because: (1) BEY uses purchase price ($985$) in the denominator rather than face value ($1,000$), making the return fraction larger, and (2) BEY annualizes using $365$ days instead of $360$ days.

**TI BA II Plus Keystrokes:**
- BDY: $(15 / 1000) \times (360 / 90) = 0.06 \to 6.00\%$
- BEY: $(15 / 985) \times (365 / 90) = 0.06176 \to 6.18\%$

**Wrong Answer Analysis:**
- B: Incorrect — BDY uses 360 days, but face value denominator depresses BDY below BEY.
- C: Incorrect — BDY and BEY are calculated differently and produce different numbers.

**LO Reference:** FIX-03-01-LO02 (Money Market Yield Measures)
**Related Concepts:** Bank discount yield, bond equivalent yield, money market yield
**Common Misconception:** Thinking 360-day factor makes BDY higher than 365-day BEY.

---

### Q-FIX-0018 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Forward Rate Implication

**Question:**
Given the 1-year spot rate $S_1 = 4.0\%$ and the 2-year spot rate $S_2 = 5.0\%$, the 1-year forward rate starting 1 year from today, $f(1,1)$, is closest to:
A) 4.50%
B) 6.01%
C) 7.00%


**Correct Answer:** B

**Explanation:** Using the no-arbitrage forward rate formula:
$$(1 + S_2)^2 = (1 + S_1)^1 \times (1 + f(1,1))^1$$
$$(1.05)^2 = (1.04)^1 \times (1 + f(1,1))$$
$$1.1025 = 1.04 \times (1 + f(1,1))$$
$$1 + f(1,1) = \frac{1.1025}{1.04} = 1.060096 \implies f(1,1) = 6.01\%$$

**TI BA II Plus Keystrokes:**
$1.05^2 / 1.04 - 1 = 0.060096 \to 6.01\%$

**Wrong Answer Analysis:**
- A: Incorrect — simple arithmetic average ($\frac{4+5}{2} = 4.5\%$).
- C: Incorrect — simple subtraction ($2 \times 5\% - 4\% = 6.0\%$ linear approximation without compounding precision).

**LO Reference:** FIX-04-01-LO01 (Spot & Forward Rate Relationships)
**Related Concepts:** Forward rate, spot curve, bootstrapping, no-arbitrage
**Common Misconception:** Using simple linear subtraction instead of geometric compounding factors.

---

### Q-FIX-0019 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Price Change Duration Approximation

**Question:**
A portfolio of fixed income securities has a Modified Duration of 7.5 years and a Money Duration of $15,000,000. If market yield increases by 40 basis points (0.40%), the estimated percentage price change of the portfolio is closest to:
A) -3.00%
B) -6.00%
C) -30.00%


**Correct Answer:** A

**Explanation:** Estimated percentage price change using Modified Duration:
$$\%\Delta P \approx -\text{Modified Duration} \times \Delta y$$
$$\%\Delta P \approx -7.5 \times (+0.0040) = -0.0300 = -3.00\%$$

Money Duration represents the dollar value change per unit yield change ($\Delta P_{\text{dollar}} = -\text{Money Duration} \times \Delta y = -15,000,000 \times 0.0040 = -\$60,000$).

**TI BA II Plus Keystrokes:**
$-7.5 \times 0.0040 = -0.03 \to -3.00\%$

**Wrong Answer Analysis:**
- B: Incorrect — multiplied duration by 0.80% instead of 0.40%.
- C: Incorrect — miscalculated decimal places ($7.5 \times 0.40 = 3.0$ without converting basis points).

**LO Reference:** FIX-05-01-LO01 (Modified Duration & Interest Rate Sensitivity)
**Related Concepts:** Modified duration, Money duration, basis points, yield sensitivity
**Common Misconception:** Confusing basis point inputs ($40\text{ bps} = 0.0040$).

---

### Q-FIX-0020 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Duration + Convexity Adjustment

**Question:**
A 10-year bond has a Modified Duration of 8.0 years and a Convexity of 80.0. If yields decrease by 100 basis points (-1.00%), the total estimated percentage change in bond price (including convexity adjustment) is closest to:
A) +7.60%
B) +8.40%
C) +8.80%


**Correct Answer:** B

**Explanation:** Total estimated price change combining duration and convexity:
$$\%\Delta P \approx \left(-\text{ModDur} \times \Delta y\right) + \left[\frac{1}{2} \times \text{Convexity} \times (\Delta y)^2\right]$$
$$\text{Duration Effect} = -8.0 \times (-0.0100) = +0.0800 = +8.00\%$$
$$\text{Convexity Effect} = \frac{1}{2} \times 80.0 \times (-0.0100)^2 = 40.0 \times 0.0001 = +0.0040 = +0.40\%$$
$$\%\Delta P \approx +8.00\% + 0.40\% = +8.40\%$$

Convexity ALWAYS acts as a positive adjustment to price for option-free bonds regardless of whether yields rise or fall.

**TI BA II Plus Keystrokes:**
- Duration effect: $-8 \times -0.01 = 0.08$
- Convexity effect: $0.5 \times 80 \times (-0.01)^2 = 0.004$
- Total: $0.08 + 0.004 = 0.084 \to +8.40\%$

**Wrong Answer Analysis:**
- A: Incorrect — subtracted convexity adjustment instead of adding it ($8.00\% - 0.40\% = 7.60\%$).
- C: Incorrect — doubled convexity term ($8.00\% + 0.80\% = 8.80\%$).

**LO Reference:** FIX-05-01-LO02 (Convexity Adjustment)
**Related Concepts:** Duration-convexity approximation, second-order Taylor series, price-yield curve
**Common Misconception:** Subtraction of convexity term when yields decrease (convexity is always added for option-free bonds).

---

### Q-FIX-0021 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Negative Convexity in Callable Bonds

**Question:**
A callable bond exhibits "negative convexity" when market yields drop significantly below the bond's coupon rate. This negative convexity occurs because:
A) The issuer is likely to call the bond, capping price appreciation near the call price
B) Duration increases rapidly as interest rates drop
C) Coupon payments decrease automatically when interest rates fall


**Correct Answer:** A

**Explanation:** When interest rates fall significantly below the coupon rate, the probability of the issuer calling the bond approaches 100%. The bond price is effectively capped near the call price. As a result, price appreciation slows down relative to an option-free bond, causing the price-yield curve to flatten and display NEGATIVE convexity.

**Wrong Answer Analysis:**
- B: Incorrect — duration of a callable bond DECREASES (shortens to the call date) as yields drop.
- C: Incorrect — fixed coupon payments do not change; the call option limits capital appreciation.

**LO Reference:** FIX-06-01-LO01 (Callable Bonds & Negative Convexity)
**Related Concepts:** Callable bonds, call option, negative convexity, price cap
**Common Misconception:** Believing option-free bonds can have negative convexity.

---

### Q-FIX-0022 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Effective vs Modified Duration

**Question:**
Why MUST Effective Duration be used instead of Modified Duration when analyzing bonds with embedded options (such as callable or putable bonds)?
A) Modified Duration assumes future cash flows do not change when interest rates change
B) Effective Duration ignores convexity adjustments
C) Modified Duration can only be calculated for zero-coupon bonds


**Correct Answer:** A

**Explanation:** Modified Duration assumes that future cash flows remain fixed regardless of yield movements ($\frac{dCF}{dy} = 0$). For bonds with embedded options (callable/putable), cash flows ARE yield-dependent (e.g., call is exercised when yields fall). Effective Duration explicitly measures price sensitivity to yield changes by re-evaluating option-adjusted cash flows.

**Wrong Answer Analysis:**
- B: Incorrect — Effective Duration accommodates convexity shifts in option-embedded bonds.
- C: Incorrect — Modified Duration is valid for any option-free coupon bond, not just zero-coupon bonds.

**LO Reference:** FIX-05-01-LO03 (Effective Duration for Embedded Options)
**Related Concepts:** Effective duration, embedded options, yield-dependent cash flows
**Common Misconception:** Using Modified Duration for option-embedded bonds.

---

### Q-FIX-0023 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Credit Spread Components

**Question:**
The yield spread on a corporate bond over a risk-free benchmark government bond reflects compensation for:
A) Credit risk and liquidity risk only
B) Credit risk, liquidity risk, and tax treatment differences
C) Default risk only


**Correct Answer:** B

**Explanation:** A corporate bond yield spread over a benchmark government bond incorporates multiple risk premiums: (1) Default Risk & Credit Migration Risk (Credit Risk), (2) Liquidity Risk (corporate bonds trade less liquidly than treasuries), and (3) Tax Status Differences (e.g., municipal bonds vs corporate bonds).

**Wrong Answer Analysis:**
- A: Incorrect — omits tax treatment differences.
- C: Incorrect — default risk is only one component of the total credit spread.

**LO Reference:** FIX-07-01-LO01 (Credit Spread Components)
**Related Concepts:** Credit spread, liquidity premium, default risk, tax status
**Common Misconception:** Equating the entire yield spread solely to expected default loss.

---

### Q-FIX-0024 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: 4 Cs of Credit Analysis

**Question:**
In traditional credit analysis, evaluating a corporate borrower's leverage, interest coverage ratios, and cash flow predictability falls under which of the "4 Cs of Credit"?
A) Character
B) Capacity
C) Collateral


**Correct Answer:** B

**Explanation:** The "4 Cs of Credit" are Capacity, Capital, Collateral, and Character. Evaluating financial metrics such as debt leverage, interest coverage ratios, operating margins, and cash flow generating ability falls under **Capacity** (the borrower's ability to service its debt obligations).

**Wrong Answer Analysis:**
- A: Character refers to management integrity, governance, and operating track record.
- C: Collateral refers to quality and value of assets backing the debt.

**LO Reference:** FIX-07-01-LO02 (4 Cs of Credit Analysis)
**Related Concepts:** Credit analysis, Capacity, leverage ratios, debt service
**Common Misconception:** Confusing Capacity (financial coverage/cash flow) with Capital or Collateral.

---

### Q-FIX-0025 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Expected Loss Calculation

**Question:**
A portfolio manager holds a 5-year corporate bond with a par value of $1,000. Credit rating models estimate a 5-year cumulative Probability of Default (PD) of 4.0% and a Loss Given Default (LGD) of 60% (Recovery Rate = 40%). The expected loss from default over 5 years is:
A) $24.00
B) $40.00
C) $60.00


**Correct Answer:** A

**Explanation:** Calculation of Expected Loss (EL):
$$\text{Expected Loss} = \text{Par Value} \times \text{Probability of Default (PD)} \times \text{Loss Given Default (LGD)}$$
$$\text{LGD} = 100\% - \text{Recovery Rate} = 100\% - 40\% = 60\% = 0.60$$
$$\text{Expected Loss} = \$1,000 \times 0.04 \times 0.60 = \$24.00$$

**TI BA II Plus Keystrokes:**
$1,000 \times 0.04 \times 0.60 = 24.00$

**Wrong Answer Analysis:**
- B: Incorrect — multiplied par value by PD only ($1,000 \times 0.04 = \$40$).
- C: Incorrect — multiplied par value by LGD only ($1,000 \times 0.60 = \$600 \to \$60$).

**LO Reference:** FIX-07-01-LO03 (Expected Loss & Credit Risk Metrics)
**Related Concepts:** Expected loss, Probability of Default, Loss Given Default, Recovery Rate
**Common Misconception:** Forgetting to multiply by Loss Given Default (LGD) in Expected Loss.

*End of Expanded Fixed Income Question Bank (Q-FIX-0001 through Q-FIX-0025)*

---

### Q-FIX-0026 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
Affirmative bond covenants typically require the bond issuer to:?
A) Maintain adequate collateral insurance and pay taxes on time
B) Maintain adequate collateral insurance and comply with all financial regulations.
C) Ensure minimum EBITDA margins of at least 25% and maintain a debt-to-equity ratio of no more than 3.5.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-10 (Bond Indenture Covenants). Maintain adequate collateral insurance and pay taxes on time.

**Wrong Answer Analysis:**
- B: This distractor is wrong because it only requires the issuer to comply with financial regulations, which may not be sufficient to protect investors' interests. A covenant requiring adequate collateral insurance provides a stronger financial safety net.
- C: This distractor is wrong because the EBITDA margin and debt-to-equity ratio requirements are overly restrictive and may not accurately reflect the issuer's actual financial performance.

**LO Reference:** LO-FIX-10 (Bond Indenture Covenants)
**Related Concepts:** Bond Indenture Covenants, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0027 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
Bond price-yield curves exhibit positive convexity, meaning bond price increases when yields fall are:?
A) Larger than bond price decreases when yields rise by an equal amount
B) Convexity occurs when the percentage change in price is greater than the percentage change in yield for a given yield movement.
C) The effect of convexity can be observed as an increase in bond price when yields decrease, and an increase in duration when yields rise.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-11 (Bond Pricing Convexity). Larger than bond price decreases when yields rise by an equal amount.

**Wrong Answer Analysis:**
- B: This distractor is wrong because convexity does not imply that price moves by more than yield; it implies that the percentage change in price is greater than the percentage change in yield for a given yield movement. The actual effect of convexity depends on the specific bond characteristics and yield changes.
- C: This distractor is wrong because it incorrectly describes how duration changes with yields; while longer durations are indeed observed when yields rise, this does not directly address the concept of price-yield convexity.

**LO Reference:** LO-FIX-11 (Bond Pricing Convexity)
**Related Concepts:** Bond Pricing Convexity, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0028 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
Modified duration measures the percentage price change of a bond per 100 bps change in:?
A) Yield to maturity (YTM)
B) Holding period yield (HPY) is the average return of a portfolio or individual security over a specific time horizon.
C) Weighted average cost of capital (WACC) is the weighted average of all costs associated with owning a firm's debt and equity.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-12 (Macaulay vs Modified Duration). Yield to maturity (YTM).

**Wrong Answer Analysis:**
- Distractors reflect realistic misconceptions.

**LO Reference:** LO-FIX-12 (Macaulay vs Modified Duration)
**Related Concepts:** Macaulay vs Modified Duration, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0029 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
For a callable bond trading near its call price, effective duration is:?
A) Lower than that of an equivalent option-free bond due to price capping
B) Effective duration for a callable bond trading near its call price is greater than that of an equivalent option-free bond due to the cost of buying options.
C) The effective duration of a callable bond traded near its call price is typically equal to that of an option-free bond, since the bond's value is close enough to par that the call feature has limited impact on the overall duration.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-13 (Effective Duration Callable Bonds). Lower than that of an equivalent option-free bond due to price capping.

**Wrong Answer Analysis:**
- B: Incorrect because the cost of buying options actually decreases the effective duration. The option premium reduces the bond's value at the call date, leading to a shorter effective duration.
- C: Incorrect because when a bond is traded near its call price, the cost of the call feature can increase the effective duration by reducing the bond's value over time.

**LO Reference:** LO-FIX-13 (Effective Duration Callable Bonds)
**Related Concepts:** Effective Duration Callable Bonds, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0030 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
Credit spread risk refers to the risk of bond price decline resulting from:?
A) An increase in the market credit spread required over the benchmark risk-free rate
B) Credit spread risk refers to the risk of bond price decline resulting from an increase in the credit rating of a borrower.
C) Credit spread risk refers to the risk of bond price decline resulting from changes in interest rates.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-14 (Credit Risk Default vs Spread Risk). An increase in the market credit spread required over the benchmark risk-free rate.

**Wrong Answer Analysis:**
- B: Incorrect because an increase in the credit rating would likely decrease, not increase, the market credit spread required over the benchmark risk-free rate. The correct answer is that an increase in the market credit spread required over the benchmark risk-free rate leads to higher yields for similar-risk bonds, causing their prices to decline.
- C: Incorrect because changes in interest rates affect all bond prices equally, not just those with wider spreads. Credit spread risk is a specific type of risk associated with bonds having wider credit spreads than the benchmark risk-free rate.

**LO Reference:** LO-FIX-14 (Credit Risk Default vs Spread Risk)
**Related Concepts:** Credit Risk Default vs Spread Risk, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0031 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
In a securitized asset-backed structure, credit tranching protects senior bondholders by:?
A) Absorbing first losses in junior (subordinated/equity) tranches
B) Absorbing first losses in senior (senior/equity) tranches
C) Providing liquidity to investors via a special purpose entity


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-15 (Securitization ABS Credit Tranching). Absorbing first losses in junior (subordinated/equity) tranches.

**Wrong Answer Analysis:**
- B: This distractor is wrong because credit tranching does not absorb first losses from senior tranches, which would be less desirable for senior bondholders. Senior tranches generally have higher priority in the event of defaults or delinquencies.
- C: This distractor is wrong because while a special purpose entity may provide liquidity to investors, this is not the primary purpose of credit tranching, which is to protect senior bondholders from first losses.

**LO Reference:** LO-FIX-15 (Securitization ABS Credit Tranching)
**Related Concepts:** Securitization ABS Credit Tranching, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
---

### Q-FIX-0032 | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
CMBS structures protect investors against prepayment risk primarily through:?
A) Loan-level call protection mechanisms such as defeasance or prepayment penalties
B) CMBS structures protect investors against prepayment risk primarily through portfolio-level credit enhancement and amortization periods for all loan pools in the securitization.
C) CMBS structures protect investors against prepayment risk primarily through individual loan guarantees with the servicer assuming the credit risk of each loan.


**Correct Answer:** A

**Explanation:** Correct application for LO-FIX-16 (Commercial Mortgage Backed Securities (CMBS)). Loan-level call protection mechanisms such as defeasance or prepayment penalties.

**Wrong Answer Analysis:**
- B: This answer is wrong because while CMBS structures may include some degree of portfolio-level credit enhancement, it does not provide protection for investors. The primary mechanism to mitigate prepayment risk in CMBS is loan-level call protection mechanisms such as defeasance or prepayment penalties. Amortization periods do not directly protect against prepayment risk, and are primarily used to reduce the risk of early repayment through the extension of the loan term.
- C: This answer is wrong because individual loan guarantees with the servicer assuming the credit risk of each loan does not provide protection for investors from prepayment risk. The primary mechanism to mitigate this risk in CMBS is also loan-level call protection mechanisms such as defeasance or prepayment penalties.

**LO Reference:** LO-FIX-16 (Commercial Mortgage Backed Securities (CMBS))
**Related Concepts:** Commercial Mortgage Backed Securities (CMBS), CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.

---

### Q-FIX-0033 | Difficulty: 3 | Time: 90s | Pattern: Reverse Calculation / Decision Scenario | Trap: Core Concept Calibration

**Question:**
A 10-year zero-coupon bond with a YTM of 5% has a Macaulay duration equal to:?
A) 10.0 years (Macaulay duration of a zero-coupon bond equals its maturity)
B) The Macaulay duration of a zero-coupon bond equals its maturity, but this assumes all the money flows are at maturity, however in reality cash inflows can occur before maturity. So, we need to calculate the weighted average time of money flow, and it comes out to be 8.5 years
C) The Macaulay duration of a zero-coupon bond equals its maturity only when there is only one cash inflow at maturity, but in this case we have 10-year cash inflows every year, which makes the weighted average time equal to its maturity, 10 years.


**Correct Answer:** A

**Explanation:** Level 3 depth application for LO-FIX-02 (Zero-Coupon Bond Price Sensitivity). 10.0 years (Macaulay duration of a zero-coupon bond equals its maturity).

**Wrong Answer Analysis:**
- B: The explanation for B is wrong because Macaulay duration of a zero-coupon bond does not take into account multiple cash flows across different periods. It only equals maturity when there is one single cash inflow at maturity, and that's not the case here.
- C: The explanation for C is incorrect because even though it correctly identifies the maturity as 10 years, it incorrectly states why it is so. Macaulay duration of a zero-coupon bond actually equals its maturity due to having only one time of money flow at maturity, not because of multiple cash inflows across different periods.

**LO Reference:** LO-FIX-02 (Zero-Coupon Bond Price Sensitivity)
**Related Concepts:** Zero-Coupon Bond Price Sensitivity, CFA curriculum core concept
**Common Misconception:** Confusing baseline formulas with reverse calculations or application scenarios.
---

### Q-FIX-0034 | Difficulty: 3 | Time: 90s | Pattern: Reverse Calculation / Decision Scenario | Trap: Core Concept Calibration

**Question:**
A steepening of the yield curve occurs when long-term bond yields increase by:?
A) A greater amount than short-term bond yields
B) A flattening of the yield curve occurs when long-term bond yields decrease by more than short-term bond yields.
C) A steepening of the yield curve occurs when long-term bond yields increase, but only if they are less than the rate of inflation plus 1%.


**Correct Answer:** A

**Explanation:** Level 3 depth application for LO-FIX-05 (Yield Curve Shifts Parallel vs Non-Parallel). A greater amount than short-term bond yields.

**Wrong Answer Analysis:**
- B: A flattening of the yield curve is the opposite of a steepening, and B incorrectly describes the direction of the relationship. 
- C: While the relationship between interest rates and inflation is complex, this statement incorrectly implies that long-term yields must be less than the rate of inflation plus 1% to cause a steepening, which is not necessarily true.

**LO Reference:** LO-FIX-05 (Yield Curve Shifts Parallel vs Non-Parallel)
**Related Concepts:** Yield Curve Shifts Parallel vs Non-Parallel, CFA curriculum core concept
**Common Misconception:** Confusing baseline formulas with reverse calculations or application scenarios.
---

### Q-FIX-0035 | Difficulty: 3 | Time: 90s | Pattern: Reverse Calculation / Decision Scenario | Trap: Core Concept Calibration

**Question:**
Extension risk in Mortgage-Backed Securities (MBS) occurs when interest rates rise, causing:?
A) Prepayments to slow down, extending the average life of the MBS portfolio
B) Prepayments to accelerate, reducing the average life of the MBS portfolio.
C) Extension risk is actually caused by an increase in servicing costs due to longer loan terms and higher interest rates.


**Correct Answer:** A

**Explanation:** Level 3 depth application for LO-FIX-07 (Mortgage Prepayment Risk Extension Risk). Prepayments to slow down, extending the average life of the MBS portfolio.

**Wrong Answer Analysis:**
- B: This distractor incorrectly suggests that prepayment acceleration would extend the life of the MBS portfolio, which is opposite of what is intended. The correct answer (A) states that prepayments slow down, extending the life of the portfolio.
- C: While higher servicing costs can be a risk associated with longer loan terms and interest rate increases, this is not the primary cause of extension risk in MBS. The correct explanation is that rising interest rates lead to prepayment slowdowns, increasing the average life of the portfolio.

**LO Reference:** LO-FIX-07 (Mortgage Prepayment Risk Extension Risk)
**Related Concepts:** Mortgage Prepayment Risk Extension Risk, CFA curriculum core concept
**Common Misconception:** Confusing baseline formulas with reverse calculations or application scenarios.

---

### Q-FIX-0036 | Difficulty: 4 | Time: 120s | Pattern: Reverse Calculation / Multi-Step Application | Trap: Formula Misapplication

**Question:**
A 5-year coupon bond has an effective duration of 4.2 and effective convexity of 22.0. If yields decline by 100 bps (-1.0%), the estimated percentage price change is:?
A) +4.31% (% Change = -Duration * dY + 0.5 * Convexity * (dY)^2 = -4.2 * (-0.01) + 0.5 * 22 * (0.01)^2 = 0.042 + 0.0011 = 4.31%)
B) The decrease in yield caused a reduction in bond price that was not fully captured by the duration adjustment, leading to an underestimation of the percentage price change.
C) The convexity term was incorrectly squared, resulting in an incorrect addition of 0.5*22*(0.01)^2 = 0.0022 and a total estimated price change of -4.2*(-0.01) + 0.0022 = 0.0422, rather than the correct 0.0421.


**Correct Answer:** A

**Explanation:** High-value marginal EEC addition for LO-FIX-03 (Bond Effective Duration & Yield Curve Sensitivity). +4.31% (% Change = -Duration * dY + 0.5 * Convexity * (dY)^2 = -4.2 * (-0.01) + 0.5 * 22 * (0.01)^2 = 0.042 + 0.0011 = 4.31%).

**Wrong Answer Analysis:**
- B: The decrease in yield caused a reduction in bond price that was not fully captured by the duration adjustment, leading to an underestimation of the percentage price change.
- C: The convexity term was incorrectly squared, resulting in an incorrect addition of 0.5*22*(0.01)^2 = 0.0022 and a total estimated price change of -4.2*(-0.01) + 0.0022 = 0.0422, rather than the correct 0.0421.

**LO Reference:** LO-FIX-03 (Bond Effective Duration & Yield Curve Sensitivity)
**Related Concepts:** Bond Effective Duration & Yield Curve Sensitivity, CFA curriculum core concept
**Common Misconception:** Confusing baseline formulas with multi-step calculations or scenario logic.
---

### Q-FIX-0037 | Difficulty: 4 | Time: 120s | Pattern: Reverse Calculation / Multi-Step Application | Trap: Formula Misapplication

**Question:**
In a sequential-pay CMO structure, principal prepayments are directed first to:?
A) Tranche A (the shortest-maturity tranche) until fully retired before paying Tranche
B) Pay off the EEC with the highest monthly payment first, regardless of tranche maturity.
C) Pay off Tranche A and EEC simultaneously until both are fully retired before paying Tranche B.


**Correct Answer:** A

**Explanation:** High-value marginal EEC addition for LO-FIX-06 (Collateralized Mortgage Obligations (CMO) Sequential Pay). Tranche A (the shortest-maturity tranche) until fully retired before paying Tranche B.

**Wrong Answer Analysis:**
- B: This distractor is wrong because in a sequential-pay CMO structure, principal prepayments should prioritize the shortest-maturity tranche (Tranche A) to minimize future cash shortfalls. Paying off the EEC with the highest monthly payment first would not achieve this goal and could result in higher costs for investors.
- C: This distractor is wrong because paying off Tranche A and EEC simultaneously may not be the most efficient approach, as it could delay prepayment of the shorter-maturity tranche (Tranche B). In a sequential-pay structure, principal prepayments should prioritize the shortest-maturity tranche until fully retired before moving on to the next one.

**LO Reference:** LO-FIX-06 (Collateralized Mortgage Obligations (CMO) Sequential Pay)
**Related Concepts:** Collateralized Mortgage Obligations (CMO) Sequential Pay, CFA curriculum core concept
**Common Misconception:** Confusing baseline formulas with multi-step calculations or scenario logic.

---

### Q-FIX-0038 | Difficulty: 4 | Time: 120s | Pattern: Decision Scenario / Formula Integration | Trap: Core Concept Calibration

**Question:**
For a bond with an embedded call option, the Option-Adjusted Spread (OAS) relative to its Z-spread is:?
A) Lower than the Z-spread, because OAS removes the cost of the call option
B) OAS does not remove the cost of the call option, it simply reduces the return to compensate for the reduced risk associated with the embedded call option.
C) A bond with an embedded call option would typically have a lower OAS than its Z-spread because the Z-spread assumes no embedded options, whereas OAS accounts for the increased cost of carrying the option


**Correct Answer:** A

**Explanation:** Batch 4 targeted EEC closure addition for LO-FIX-08 (Yield Spread Measures OAS vs Z-Spread). Lower than the Z-spread, because OAS removes the cost of the call option.

**Wrong Answer Analysis:**
- B: Explanation why B is wrong
- C: Explanation why C is wrong

**LO Reference:** LO-FIX-08 (Yield Spread Measures OAS vs Z-Spread)
**Related Concepts:** Yield Spread Measures OAS vs Z-Spread, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
---

### Q-FIX-0039 | Difficulty: 4 | Time: 120s | Pattern: Decision Scenario / Formula Integration | Trap: Core Concept Calibration

**Question:**
A credit rating transition matrix displays:?
A) The probability that a bond of a given rating will be upgraded, downgraded, or default over a specified timeframe
B) The credit rating transition matrix displays the likelihood of a bond being retained at its current rating.
C) The credit rating transition matrix displays the average yield to maturity for bonds across all rating levels.


**Correct Answer:** A

**Explanation:** Batch 4 targeted EEC closure addition for LO-FIX-09 (Credit Risk Rating Agencies & Transition Matrix). The probability that a bond of a given rating will be upgraded, downgraded, or default over a specified timeframe.

**Wrong Answer Analysis:**
- B: Incorrect because it refers to the retention probability, not the upgrading/downgrading or defaulting probabilities. The transition matrix shows the probabilities of changes in rating (upgrades, downgrades, defaults) over time. 
- C: Incorrect because it refers to yield to maturity, which is a different concept altogether. Yield to maturity is a characteristic of individual bonds, whereas the credit rating transition matrix provides information on rating changes over time.

**LO Reference:** LO-FIX-09 (Credit Risk Rating Agencies & Transition Matrix)
**Related Concepts:** Credit Risk Rating Agencies & Transition Matrix, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
---

### Q-FIX-0040 | Difficulty: 4 | Time: 120s | Pattern: Decision Scenario / Formula Integration | Trap: Core Concept Calibration

**Question:**
Auto loan ABS prepayments are typically measured using the:?
A) Absolute Prepayment Speed (ABS) metric
B) Monthly Prepayment Rate (MPR) metric, which accounts for prepayment timing and frequency.
C) Total Losses to Outstanding Principal (TLOP) ratio, which considers the cumulative losses from defaults over time.


**Correct Answer:** A

**Explanation:** Batch 4 targeted EEC closure addition for LO-FIX-10 (Asset-Backed Securities (ABS) Auto Loan Prepayments). Absolute Prepayment Speed (ABS) metric.

**Wrong Answer Analysis:**
- B is wrong because MPR measures average monthly payments received, rather than the overall speed of prepayments. Prepayment speed requires a measure that captures both the timing and frequency of payments.
- C is wrong because TLOP focuses on losses from defaults, whereas auto loan ABS prepayments typically refer to voluntary payments made by borrowers towards their outstanding principal balances.

**LO Reference:** LO-FIX-10 (Asset-Backed Securities (ABS) Auto Loan Prepayments)
**Related Concepts:** Asset-Backed Securities (ABS) Auto Loan Prepayments, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.

---

### Q-FIX-0041 | Difficulty: 4 | Time: 120s | Pattern: Surgical Concept Closure / Decision Scenario | Trap: Core Concept Calibration

**Question:**
Single Monthly Mortality (SMM) measures the percentage of remaining mortgage principal prepaid in:?
A) A single month relative to expected scheduled principal payments
B) SMM measures the percentage of remaining mortgage principal prepaid in relation to outstanding principal balance at the time of prepayment.
C) SMM measures the percentage of remaining mortgage principal prepaid based on historical average monthly payment growth rates.


**Correct Answer:** A

**Explanation:** Batch 5 surgical closure addition targeting 95% concept milestone for LO-FIX-17 (Structured Finance Mortgage Prepayment Rate Measures SMM). A single month relative to expected scheduled principal payments.

**Wrong Answer Analysis:**
- B: This distractor is wrong because SMM is based on scheduled payments, not outstanding balances. The correct answer focuses on a single month relative to expected scheduled principal payments.
- C: This distractor is wrong because it incorrectly implies that the percentage of prepaid principal is calculated based on historical average monthly payment growth rates, whereas SMM measures prepayment as a proportion of scheduled payments.

**LO Reference:** LO-FIX-17 (Structured Finance Mortgage Prepayment Rate Measures SMM)
**Related Concepts:** Structured Finance Mortgage Prepayment Rate Measures SMM, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
---

### Q-FIX-0042 | Difficulty: 4 | Time: 120s | Pattern: Surgical Concept Closure / Decision Scenario | Trap: Core Concept Calibration

**Question:**
Sovereign CDS credit events typically include bankruptcy, failure to pay, and:?
A) Restructuring or debt repudiation/moratorium by the issuing sovereign government
B) Insolvency or dissolution of the governing body responsible for the sovereign's debt obligations
C) Default on a key monetary policy decision, such as inflation targeting agreement


**Correct Answer:** A

**Explanation:** Batch 5 surgical closure addition targeting 95% concept milestone for LO-FIX-18 (Credit Default Swaps Sovereign CDS Default Triggers). Restructuring or debt repudiation/moratorium by the issuing sovereign government.

**Wrong Answer Analysis:**
- B: Incorrect because restructuring or debt repudiation/moratorium by the issuing sovereign government is a more direct credit event. Insolvency or dissolution of the governing body may be a proximate cause but not a typical CDS credit event. In contrast to other types of events, such as bankruptcy, insolvency or dissolution does not necessarily result in an immediate loss of access to new financing, and therefore, may not directly trigger a default on CDS contracts.
- C: Incorrect because this is more related to policy mistakes rather than sovereign credit events. CDS typically focus on the probability of actual debt defaults (such as restructuring or repudiation) rather than hypothetical policy decisions.

**LO Reference:** LO-FIX-18 (Credit Default Swaps Sovereign CDS Default Triggers)
**Related Concepts:** Credit Default Swaps Sovereign CDS Default Triggers, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.

---

### Q-FIX-0043 | Difficulty: 4 | Time: 120s | Pattern: Cost-Efficient Depth Optimization / Reverse Math | Trap: Core Concept Calibration

**Question:**
A 90-day bank bill with par value $1,000,000 trades at a discount rate of 4.0%. Its purchase price is:?
A) $990,000 (Price = Par * [1 - (Days/360) * Discount Rate] = $1,000,000 * [1 - (90/360)*0.04] = $990,000)
B) Discount rate calculation error, Days/360 should be 0.25 not 0.04 for a 90-day trade, and the actual discount price is $995,000.
C) Incorrect application of formula, instead of multiplying Discount Rate by (Days/360), it should be Dividend Rate by (Days/360) or simply as a percentage of Par Value, resulting in a purchase price of $999,600.


**Correct Answer:** A

**Explanation:** Batch 6 cost-efficient ORANGE depth addition for LO-FIX-04 (Bond Money Market Discount Rate vs Add-On Rate). $990,000 (Price = Par * [1 - (Days/360) * Discount Rate] = $1,000,000 * [1 - (90/360)*0.04] = $990,000).

**Wrong Answer Analysis:**
- Distractors reflect realistic misconceptions.

**LO Reference:** LO-FIX-04 (Bond Money Market Discount Rate vs Add-On Rate)
**Related Concepts:** Bond Money Market Discount Rate vs Add-On Rate, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.

---

### Q-FIX-0044 | Difficulty: 4 | Time: 120s | Pattern: Micro-Batch High-Yield Rescue / Reverse Math | Trap: Core Concept Calibration

**Question:**
For a bond with positive convexity, when market yields change by +/- 200 bps, the duration-predicted price change:?
A) Underestimates price increases when yields fall, and overestimates price declines when yields rise
B) Price movements are equally predictable, regardless of the direction of yield changes.
C) Duration is unaffected by yield changes, so no price change occurs.


**Correct Answer:** A

**Explanation:** Batch 7 micro-batch high-yield rescue addition for LO-FIX-05 (Bond Price Yield Curve Convexity Effect). Underestimates price increases when yields fall, and overestimates price declines when yields rise.

**Wrong Answer Analysis:**
- B: Incorrect because a positive convexity bond's duration changes in response to yield movements, affecting its price. When yields fall, a longer-duration bond tends to increase in value (overestimating price increases), while when yields rise, a shorter-duration bond tends to increase in value (underestimating price declines).
- C: Incorrect because the bond's duration is inversely related to yield changes, not unaffected.

**LO Reference:** LO-FIX-05 (Bond Price Yield Curve Convexity Effect)
**Related Concepts:** Bond Price Yield Curve Convexity Effect, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
---

### Q-FIX-0045 | Difficulty: 4 | Time: 120s | Pattern: Micro-Batch High-Yield Rescue / Reverse Math | Trap: Core Concept Calibration

**Question:**
To immunize a single-liability fixed income portfolio against interest rate risk, the portfolio manager must ensure:?
A) Portfolio Macaulay duration equals the liability investment horizon, and PV of assets equals PV of liabilities
B) Macaulay duration should match the liability yield curve, not investment horizon.
C) The portfolio manager must ensure PV of assets equals the weighted average of liabilities' cash flows.


**Correct Answer:** A

**Explanation:** Batch 7 micro-batch high-yield rescue addition for LO-FIX-11 (Bond Portfolio Duration Immunization). Portfolio Macaulay duration equals the liability investment horizon, and PV of assets equals PV of liabilities.

**Wrong Answer Analysis:**
- B: Incorrect because Macaulay duration should be matched to the relevant yield curve (e.g. liability or risk-free), not necessarily the investment horizon. This approach does not account for potential changes in the yield curve over time.
- C: Incorrect because it confuses the concept of PV of assets with the weighted average of liabilities' cash flows, which is actually the correct approach to ensure a portfolio can meet its future cash obligations.

**LO Reference:** LO-FIX-11 (Bond Portfolio Duration Immunization)
**Related Concepts:** Bond Portfolio Duration Immunization, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
---

### Q-FIX-0046 | Difficulty: 4 | Time: 120s | Pattern: Micro-Batch High-Yield Rescue / Reverse Math | Trap: Core Concept Calibration

**Question:**
The upfront premium paid on a Credit Default Swap (CDS) equals:?
A) (CDS Credit Spread - CDS Fixed Coupon) * CDS Duration
B) CDS Upfront Premium equals the CDS Credit Spread times CDS Credit Rating
C) CDS Upfront Premium equals (CDS Credit Spread - CDS Fixed Coupon) times par value of bond


**Correct Answer:** A

**Explanation:** Batch 7 micro-batch high-yield rescue addition for LO-FIX-12 (Credit Default Swaps Upfront Premium Calculation). (CDS Credit Spread - CDS Fixed Coupon) * CDS Duration.

**Wrong Answer Analysis:**
- B: Explanation why B is wrong
- C: Explanation why C is wrong
- B: Incorrect because it assumes the upfront premium is directly proportional to the credit rating, rather than the credit spread.
- C: Incorrect because it incorrectly includes the fixed coupon payment and par value of a bond in calculating the upfront premium. The correct calculation involves only the credit spread.

**LO Reference:** LO-FIX-12 (Credit Default Swaps Upfront Premium Calculation)
**Related Concepts:** Credit Default Swaps Upfront Premium Calculation, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced decision scenarios.
