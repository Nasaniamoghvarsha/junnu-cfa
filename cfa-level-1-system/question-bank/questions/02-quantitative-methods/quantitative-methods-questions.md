# CFA Level I — Quantitative Methods Question Bank

---

### Q-QNT-0001 | Difficulty: 2 | Time: 90s | Pattern: Direct Calculation | Trap: Annuity Due vs. Ordinary

**Question:**
An investor plans to deposit $5,000 at the end of each year for 20 years into an account earning 7% annually. The future value of these deposits is closest to:

A) $194,960
B) $204,975
C) $214,300
D) $229,300

**Correct Answer:** B

**Explanation:** This is an ordinary annuity FV problem (payments at end of year). FV = PMT × [(1+r)^n - 1] / r = 5,000 × [(1.07)^20 - 1] / 0.07 = 5,000 × 40.99549 = $204,977.45 ≈ $204,975. If this were an annuity due, you'd multiply by (1.07), but the "end of each year" signals ordinary annuity.

**Wrong Answer Analysis:**
- A: Result if using wrong interest rate or n
- C: Close but calculated incorrectly
- D: This is the annuity DUE value (× 1.07): $219,325

**LO Reference:** QNT-02-01-LO02
**Formula:** FVA = PMT × [(1+r)^n - 1] / r
**Common Trap:** Forgetting to check if annuity is ordinary or due

---

### Q-QNT-0002 | Difficulty: 3 | Time: 90s | Pattern: Missing-Variable Problem | Trap: EAR Confusion

**Question:**
An investment of $10,000 grows to $17,958.56 over 6 years. If interest is compounded quarterly, the stated annual interest rate is closest to:

A) 8.50%
B) 9.00%
C) 9.74%
D) 10.00%

**Correct Answer:** D

**Explanation:** First find quarterly rate: FV = PV(1+r)^n → 17,958.56 = 10,000(1+r)^24 → (1+r)^24 = 1.795856 → 1+r = 1.795856^(1/24) = 1.02472. Quarterly rate = 2.472%. Stated annual = 2.472% × 4 = 9.89%. Hmm, let me recalculate: 1.795856^(1/24). Using log: ln(1.795856)/24 = 0.0247. e^0.0247 = 1.025. Stated annual = 10.0%.

Actually: (1 + r/4)^24 = 17,958.56/10,000 = 1.795856. r/4 = (1.795856)^(1/24) - 1 = 0.024999 ≈ 0.025. r = 10.0%.

**Wrong Answer Analysis:**
- A: Incorrect calculation of the periodic rate
- B: Close but wrong compounding treatment
- C: EAR approximation as stated rate

**LO Reference:** QNT-02-01-LO01, QNT-02-01-LO01
**Formula:** FV = PV × (1 + r/m)^(m×n)
**Common Trap:** Confusing stated annual rate with EAR

---

### Q-QNT-0003 | Difficulty: 2 | Time: 60s | Pattern: Direct Calculation | Trap: Mean Confusion

**Question:**
An investment has the following annual returns: Year 1: 10%, Year 2: -5%, Year 3: 20%, Year 4: 15%. The geometric mean return is closest to:

A) 8.75%
B) 9.45%
C) 10.00%
D) 10.50%

**Correct Answer:** B

**Explanation:** Geometric mean = [(1.10)(0.95)(1.20)(1.15)]^(1/4) - 1 = [1.4421]^(0.25) - 1 = 1.0957 - 1 = 9.57%. The closest answer is 9.45%. The arithmetic mean would be (10 + (-5) + 20 + 15)/4 = 10%, but geometric is always ≤ arithmetic mean and is the correct measure for multi-period compounding.

**Wrong Answer Analysis:**
- A: Arithmetic mean approximation
- C: This is the arithmetic mean (incorrect for multi-period)
- D: Too high

**LO Reference:** QNT-01-01-LO02
**Formula:** R_G = [(1+R₁)(1+R₂)...(1+Rₙ)]^(1/n) - 1
**Common Trap:** Using arithmetic mean for multi-period returns

---

### Q-QNT-0004 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Correlation Interpretation

**Question:**
Stock A has a standard deviation of returns of 20%. Stock B has a standard deviation of 30%. The covariance between their returns is 0.036. The correlation coefficient is closest to:

A) 0.40
B) 0.50
C) 0.60
D) 0.70

**Correct Answer:** C

**Explanation:** ρ = Cov(A,B) / (σ_A × σ_B) = 0.036 / (0.20 × 0.30) = 0.036 / 0.06 = 0.60. Note: covariance uses decimal form of returns, and the result is the correlation coefficient (unitless, range -1 to +1).

**Wrong Answer Analysis:**
- A: Used percentages instead of decimals
- B: Arithmetic error
- D: Arithmetic error

**LO Reference:** QNT-03-01-LO05
**Formula:** ρ = Cov(X,Y) / (σ_X × σ_Y)
**Common Trap:** Forgetting to convert percentages to decimals

---

### Q-QNT-0005 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Type I vs. Type II

**Question:**
In hypothesis testing, which of the following is most accurate regarding a Type II error?

A) It is the probability of rejecting a true null hypothesis
B) It is the probability of failing to reject a false null hypothesis
C) It decreases as the significance level increases
D) It is controlled by setting the significance level of the test

**Correct Answer:** B

**Explanation:** A Type II error is failing to reject the null hypothesis when it is actually false. This is also known as β, and the power of the test is 1 - β. Type I error (α, the significance level) is rejecting a true null hypothesis. Type II error is NOT directly controlled by the significance level — it's affected by sample size, effect size, and α.

**Wrong Answer Analysis:**
- A: This describes Type I error (α), not Type II (β)
- C: Incorrect — as α increases, β generally DECREASES, not increases
- D: This describes Type I error control, not Type II

**LO Reference:** QNT-08-01-LO02
**Common Trap:** Reversing Type I (reject true H₀) and Type II (fail to reject false H₀)

---

### Q-QNT-0006 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Portfolio Variance Components

**Question:**
A portfolio consists of 60% Stock X and 40% Stock Y. Stock X has an expected return of 12% with standard deviation 25%. Stock Y has an expected return of 8% with standard deviation 15%. If the correlation between X and Y is 0.3, the portfolio standard deviation is closest to:

A) 16.2%
B) 17.8%
C) 19.5%
D) 21.0%

**Correct Answer:** B

**Explanation:** σ²_p = w_X²σ_X² + w_Y²σ_Y² + 2w_X w_Y ρ σ_X σ_Y
= (0.6²)(0.25²) + (0.4²)(0.15²) + 2(0.6)(0.4)(0.3)(0.25)(0.15)
= 0.36 × 0.0625 + 0.16 × 0.0225 + 2 × 0.6 × 0.4 × 0.3 × 0.0375
= 0.0225 + 0.0036 + 0.0054
= 0.0315

σ_p = √0.0315 = 0.1775 = 17.75% ≈ 17.8%

Note that 17.8% is LESS than the weighted average of 21% (0.6×25 + 0.4×15), showing the diversification benefit.

**Wrong Answer Analysis:**
- A: Missed the covariance term
- C: Close to weighted average (21%) — ignoring diversification
- D: Used correlation = 1

**LO Reference:** QNT-05-01-LO02
**Formula:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂
**Common Trap:** Forgetting the covariance/correlation term

---

### Q-QNT-0007 | Difficulty: 2 | Time: 60s | Pattern: Direct Calculation | Trap: Standard Error Formula

**Question:**
A sample of 100 observations from a population with unknown variance has a sample mean of 50 and sample standard deviation of 10. The standard error of the sample mean is:

A) 0.10
B) 1.00
C) 10.00
D) 100.00

**Correct Answer:** B

**Explanation:** Standard error = s / √n = 10 / √100 = 10 / 10 = 1.00. Since population variance is unknown, we use the sample standard deviation in the formula.

**Wrong Answer Analysis:**
- A: Used n instead of √n: 10/100 = 0.10
- C: Reported standard deviation instead of standard error
- D: Completely wrong calculation

**LO Reference:** QNT-07-01-LO02
**Formula:** SE = s / √n
**Common Trap:** Using n instead of √n in the denominator

---

### Q-QNT-0008 | Difficulty: 2 | Time: 90s | Pattern: Direct Calculation | Trap: Bayes' Theorem Application

**Question:**
A disease affects 1% of the population. A test for the disease is 95% accurate (both sensitivity and specificity). If a person tests positive, what is the approximate probability they actually have the disease?

A) 16%
B) 50%
C) 84%
D) 95%

**Correct Answer:** A

**Explanation:** Using Bayes' theorem:
- P(Disease) = 0.01, P(No Disease) = 0.99
- P(Test+ | Disease) = 0.95, P(Test+ | No Disease) = 0.05 (false positive)
- P(Disease | Test+) = [P(Test+|Disease) × P(Disease)] / P(Test+)
- P(Test+) = (0.95 × 0.01) + (0.05 × 0.99) = 0.0095 + 0.0495 = 0.059
- P(Disease | Test+) = 0.0095 / 0.059 = 0.161 ≈ 16%

Despite the test being 95% accurate, the low base rate means a positive result is only 16% likely to be true. This is a classic "base rate neglect" problem.

**Wrong Answer Analysis:**
- B: Approximate 50/50 guess
- C: Inverted Bayes
- D: Confused test accuracy with P(Disease|Test+)

**LO Reference:** QNT-04-01-LO02
**Formula:** P(A|B) = P(B|A) × P(A) / P(B)
**Common Trap:** Neglecting base rates in probability updating

---

### Q-QNT-0009 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Test Statistic Selection

**Question:**
A researcher wants to test whether the mean return of a stock is different from zero. She has 25 monthly returns with a sample mean of 0.8% and sample standard deviation of 2.5%. The appropriate test statistic is:

A) Z-statistic = 1.60
B) t-statistic with 24 degrees of freedom = 1.60
C) t-statistic with 25 degrees of freedom = 1.60
D) Chi-square statistic

**Correct Answer:** B

**Explanation:** Since population variance is unknown and sample size is small (n < 30), use a t-test with df = n - 1 = 24. t = (0.008 - 0) / (0.025/√25) = 0.008 / 0.005 = 1.60. A Z-test would be appropriate only if we knew the population standard deviation.

**Wrong Answer Analysis:**
- A: Wrong test — Z is for known population variance or large samples
- C: Wrong degrees of freedom — df = n - 1 = 24, not 25
- D: Chi-square is for variance tests, not mean tests

**LO Reference:** QNT-08-01-LO03
**Formula:** t = (X̄ - μ₀) / (s/√n)
**Common Trap:** Using Z-test when population variance is unknown

---

### Q-QNT-0010 | Difficulty: 3 | Time: 90s | Pattern: Concept + Calculation | Trap: R² Interpretation

**Question:**
A simple linear regression yields R² = 0.64. The correlation coefficient between X and Y is closest to:

A) 0.36
B) 0.64
C) 0.80
D) Cannot be determined from R² alone

**Correct Answer:** C

**Explanation:** In simple linear regression, the correlation coefficient (r) equals ±√R². Here, √0.64 = 0.80. The sign of the correlation matches the sign of the slope coefficient b₁. So the correlation is either +0.80 or -0.80 depending on the direction of the relationship, but the magnitude is 0.80.

**Wrong Answer Analysis:**
- A: Subtracted 0.64 from 1 (this is the unexplained portion)
- B: Confused R² with correlation
- D: In simple regression, the magnitude CAN be determined (sign requires slope)

**LO Reference:** QNT-10-01-LO03
**Formula:** r = ±√R² (simple regression only)
**Common Trap:** Confusing R² with correlation coefficient

---

### Q-QNT-0011 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Skewness and Central Tendency

**Question:**
For a positively skewed distribution, which of the following relationships is most likely correct?

A) Mean < Median < Mode
B) Mean = Median = Mode
C) Mean > Median > Mode
D) Mode > Mean > Median

**Correct Answer:** C

**Explanation:** In a positively (right) skewed distribution, the tail extends to the right, pulling the mean upward. The order is: Mean > Median > Mode. In negatively skewed: Mean < Median < Mode. In a normal distribution: Mean = Median = Mode.

**Wrong Answer Analysis:**
- A: This describes NEGATIVELY skewed distribution
- B: This describes a normal (symmetric) distribution
- D: Confused ordering

**LO Reference:** QNT-03-01-LO04
**Common Trap:** Reversing the ordering for positive vs. negative skew

---

### Q-QNT-0012 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Portfolio Math

**Question:**
An investor has a portfolio with expected return 9% and standard deviation 14%. The risk-free rate is 2%. Using Roy's Safety-First criterion with a threshold return of 3%, the Safety-First ratio is closest to:

A) 0.21
B) 0.43
C) 0.50
D) 0.64

**Correct Answer:** B

**Explanation:** SFR = (E(R_p) - R_L) / σ_p = (9% - 3%) / 14% = 6% / 14% = 0.4286 ≈ 0.43. This means the expected return is 0.43 standard deviations above the threshold. A higher SFR is better — it indicates lower shortfall risk.

**Wrong Answer Analysis:**
- A: Used risk-free rate as numerator: (9-2)/14 = 0.50, but that's Sharpe ratio
- C: This is the Sharpe ratio: (9-2)/14 = 0.50
- D: Different threshold calculation

**LO Reference:** QNT-05-01-LO03
**Formula:** SFR = (E(R_p) - R_L) / σ_p
**Common Trap:** Confusing Safety-First ratio with Sharpe ratio

---

### Q-QNT-0013 | Difficulty: 2 | Time: 60s | Pattern: Concept Comparison | Trap: Normal vs. Lognormal

**Question:**
Which of the following is most accurate about the lognormal distribution?

A) It is symmetric like the normal distribution
B) It is bounded below by zero and positively skewed
C) Asset returns, not prices, are best modeled by lognormal
D) It has a mean equal to its median

**Correct Answer:** B

**Explanation:** The lognormal distribution is positively skewed (right-skewed) and bounded below by zero. This makes it useful for modeling asset PRICES (which cannot be negative). Asset RETURNS are typically modeled with the normal distribution. The lognormal has mean > median.

**Wrong Answer Analysis:**
- A: Lognormal is positively skewed, not symmetric
- C: Returns are modeled as normal; PRICES are modeled as lognormal
- D: In lognormal, mean > median (not equal)

**LO Reference:** QNT-06-01-LO01
**Common Trap:** Confusing what is modeled by normal (returns) vs. lognormal (prices)

---

### Q-QNT-0014 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Regression Inference

**Question:**
A regression of stock returns on market returns produces: b₀ = 0.02, b₁ = 1.2, SE(b₁) = 0.3, n = 36. To test whether the stock has a beta significantly different from 1 (market beta), the test statistic and conclusion at 5% significance (critical t ≈ 2.03 for 34 df) are:

A) t = 0.67; fail to reject H₀: β = 1
B) t = 0.67; reject H₀: β = 1, stock beta differs from market
C) t = 4.00; reject H₀: β = 1, stock beta differs from market
D) t = 4.00; fail to reject H₀: β = 1

**Correct Answer:** A

**Explanation:** t = (b₁ - 1) / SE(b₁) = (1.2 - 1) / 0.3 = 0.2 / 0.3 = 0.667. Since |0.667| < 2.03, we fail to reject H₀ that β = 1. The stock's beta is not statistically different from the market beta at the 5% level.

Note: df = n - 2 = 34 for simple regression (2 parameters estimated).

**Wrong Answer Analysis:**
- B: Same t-stat but wrong conclusion
- C: Used (b₁ - 0)/SE: 1.2/0.3 = 4.0 — testing wrong hypothesis
- D: Same wrong t-stat, wrong conclusion

**LO Reference:** QNT-10-01-LO04
**Formula:** t = (b₁ - β₀) / SE(b₁)
**Common Trap:** Testing against 0 when hypothesis is about a specific value

---

### Q-QNT-0015 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Sampling Bias Types

**Question:**
A mutual fund database includes only funds that are currently active, excluding those that have been liquidated or merged. An analysis of this database is most likely to suffer from:

A) Data snooping bias
B) Survivorship bias
C) Look-ahead bias
D) Time-period bias

**Correct Answer:** B

**Explanation:** Survivorship bias occurs when only surviving/active entities are included in the analysis, excluding those that failed. In mutual fund databases, including only surviving funds overstates average historical returns because poorly performing funds that were liquidated are excluded.

**Wrong Answer Analysis:**
- A: Data snooping = finding patterns by over-searching the same data
- C: Look-ahead = using information not available at the time
- D: Time-period = results specific to a particular time period

**LO Reference:** QNT-07-01-LO03
**Common Trap:** Confusing the four sampling biases

---

*End of Quantitative Methods Question Bank*
