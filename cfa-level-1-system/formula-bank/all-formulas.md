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

* **Variables:** 
  - R_H: harmonic mean
  - n: number of values in the dataset
  - Rᵢ: individual rates or returns for each value in the dataset

* **When to Use:** 
  - Calculate the harmonic mean when you need to find an average that is skewed by extreme values, such as very high or low values.

* **When NOT to Use:** 
  - When you are calculating a simple average (arithmetic mean) where the order of values doesn't matter.
  - When you are dealing with a small number of data points, as the harmonic mean can be sensitive to outliers.

* **Common Mistakes:**
  - Forgetting that n is in the denominator, leading to incorrect calculations.
  - Not recognizing when the formula is not applicable due to skewness or outliers.

* **Calculator Steps:** 
  N/A

---

## QNT-F005: Future Value (Single Cash Flow)

**Formula:** FV = PV × (1 + r)^n

* Variables:
  * FV (Future Value)
  * PV (Present Value)
  * r (Interest Rate)
  * n (Number of Periods)

* When to Use: 
  Apply this formula when you need to calculate the future value of a single cash flow, such as calculating the amount an investor will receive in the future based on an initial investment or a series of payments.

* When NOT to Use:
  Do not use this formula for investments that produce multiple cash flows over time. This formula only applies to a single cash flow and assumes simple interest accrual.

* Common Mistakes: 
  Common errors candidates make include using incorrect values for the variables, misinterpreting the exponentiation of (1 + r), or failing to consider compounding periods.

* Calculator Steps:
  N/A

---

## QNT-F006: Present Value (Single Cash Flow)

**Formula:** PV = FV / (1 + r)^n

* **Variables:** 
  - n (number of periods): The number of time periods over which the cash flow will be invested
  - FV (Future Value): The value that an investment is expected to have in the future
  - r (interest rate): The interest rate associated with the investment period
  - PV (Present Value): The current value of a future amount, calculated by the formula

* **When to Use:**
  Use this formula when calculating the present value of a single cash flow at the end of an investment period. This can be useful for evaluating investments that have a specific future cash inflow.

* **When NOT to Use:**
  Do not use this formula if you need to calculate the future value of a series of cash flows, or if you are calculating compound interest over multiple periods.

* **Common Mistakes:**
  Candidates often forget to specify the number of periods (n) in the investment period, which can lead to incorrect calculations. They may also mistakenly use the formula for time values of money (e.g. PV = FV / (1 - r)^-n).

* **Calculator Steps:** 
  N/A

---

## QNT-F007: Future Value of Annuity

**Formula:** FV_annuity = PMT × [(1+r)^n - 1] / r

**Variables:**
- **PMT (Periodic Payment)**: The regular payment made into an annuity.
- **r (Interest Rate)**: The interest rate per period. This can be annual or periodic, depending on how often payments are made.
- **n (Number of Periods)**: The total number of periods the money is invested for.

**When to Use:**
Use this formula when calculating the future value of an annuity, which consists of a series of regular payments made at equal intervals over a fixed period. This can be used in situations where investors receive a steady income stream from a pension or other sources.

**When NOT to Use:**
Do not use this formula when you are calculating the present value of an annuity (i.e., determining how much money you will have now if you invest a certain amount in the future). The FV_annuity and PV_annuity formulas are mutually exclusive, and using them together can lead to incorrect results.

**Common Mistakes:**
- Candidates often forget to convert the interest rate from an annual rate to a periodic rate when using this formula.
- Some candidates may incorrectly calculate the number of periods (n) or assume that payments are made at the end of each period, rather than at the beginning.
- Others might neglect to account for any fees associated with investing in the annuity.

---

## QNT-F008: Present Value of Annuity

**Formula:** PV_annuity = PMT × [1 - 1/(1+r)^n] / r

* Variables:
  * n: Number of payments in the annuity
  * PMT: Annual payment amount
  * PV_annuity: Present value of the annuity
  * r: Interest rate (as a decimal)
  * t: Time period (in years)

* When to Use:
  * Use when calculating the present value of an annuity, which is a series of equal payments made at regular intervals.

* When NOT to Use:
  * Do not use this formula for loans with non-uniform interest rates or principal payments.
  * Also do not use it if there are other periodic payments (e.g. interest only payments).

* Common Mistakes:
  * Incorrectly assuming that the interest rate is annual, rather than nominal.
  * Not accounting for compounding when calculating the present value of an annuity.

* Calculator Steps:
  N/A

---

## QNT-F009: Present Value of Perpetuity

**Formula:** PV = PMT / r

* **Variables:** 
  - PV: Present Value of the perpetuity
  - PMT: Periodic payment (per period)
  - r: Interest rate per period 

* **When to Use:** 
  - To calculate the present value of a perpetual series of payments made at regular intervals.

* **When NOT to Use:** 
  - When the interest rate is zero or negative, as this would result in an undefined present value.
  - When the payment amount (PMT) is not constant across all periods, but rather varies with time.

* **Common Mistakes:** 
  - Forgetting to consider the effect of compounding when calculating interest rates.
  - Incorrectly assuming that the interest rate remains constant over time.

---

## QNT-F010: Present Value of Growing Perpetuity (Gordon Growth)

**Formula:** PV = PMT₁ / (r - g)

* **Variables:** 
  * `PMT`: The periodic interest payment on a bond
  * `r`: The annual coupon rate of the bond (after tax)
  * `g`: The growth rate of the periodic payments (the increase in interest rates per year)

* **When to Use:** 
  When calculating the present value of an annuity due with a growing perpetuity, or when determining the yield to maturity for a bond with a coupon that grows over time.

* **When NOT to Use:** 
  The formula is not suitable for projects or investments without periodic payments. It also doesn't account for other costs associated with borrowing, such as fees and interest on undrawn loans.

* **Common Mistakes:** 
  Assuming the growth rate equals the yield to maturity: r ≠ g. Forgetting that the formula calculates the present value of the future cash flows not the yield to maturity. Incorrectly using the formula without considering taxes or other factors that may affect the interest rate.

* **Calculator Steps:** 
  N/A

---

## QNT-F011: Effective Annual Rate (EAR)

**Formula:** EAR = (1 + r/m)^m - 1

* Variables:
  * r: nominal interest rate (annual percentage rate)
  * m: compounding frequency per year
* When to Use:
  * Calculate the effective annual rate when a nominal interest rate is given for a specific period of time and you need to convert it to an effective annual rate.
* When NOT to Use:
  * Do not use this formula if you are given the periodic interest rate (r) or the total amount compounded after a certain period, as these values can be used directly in other formulas to calculate the effective annual rate.
* Common Mistakes:
  * Not converting the compounding frequency from months or quarters to years
  * Using the wrong units for the nominal interest rate (e.g., using an annual percentage rate instead of a decimal value)
* Calculator Steps:
  * N/A

---

## QNT-F012: Population Variance

**Formula:** σ² = Σ(Xᵢ - μ)² / N

* Variables:
  - X: individual observations in a dataset
  - μ: population mean
  - σ: population standard deviation (not directly used in this formula, but related)
  - N: total number of observations in the sample or population

* When to Use:
  - This formula is used when calculating the variance of a population from a sample. It's essential for understanding and modeling variability.

* When NOT to Use:
  - Do not use this formula when you're working with samples where the population mean (μ) is unknown, as it requires knowledge of μ to calculate σ².

* Common Mistakes:
  - Misinterpreting the role of N in the formula; sometimes candidates forget that it represents either the sample size or the total number of observations, which can lead to incorrect conclusions about the nature of the data.
  - Incorrectly calculating Σ(Xᵢ - μ)²; candidates may mistakenly round values during calculation, lose track of the squared terms, or fail to properly handle zero deviations.

* Calculator Steps:
  - N/A

---

## QNT-F013: Sample Variance

**Formula:** s² = Σ(Xᵢ - X̄)² / (n - 1)

**Variables:**
- Xᵢ: Each individual data point
- X̄: The sample mean
- n: The number of observations in the sample
- s²: The population variance (sample variance)
- Σ: The summation symbol, indicating that we are summing over all terms

**When to Use:**
- When calculating the sample variance for a dataset where you know the individual data points and want to estimate the population variance.
- When working with datasets where n ≥ 2.

**When NOT to Use:**
- When estimating the population variance from a sample, use the formula σ² = Σ(Xᵢ - μ)² / (n), but since we are given the sample mean X̄, we can use this formula.
 
**Common Mistakes:**
- Forgetting to divide by n - 1 when calculating the sample variance, leading to an overestimation of the population variance.

**Calculator Steps:**
N/A

---

## QNT-F014: Standard Deviation

**Formula:** σ = √(σ²)

* **Variables:** 
  - σ (standard deviation) is already defined in the formula.

* **When to Use:** 
  - Use this formula when you need to calculate the standard deviation of a population or sample.

* **When NOT to Use:** 
  - Do not use this formula for calculating sample standard deviations, as it does not take into account the number of observations (n) in the dataset.

* **Common Mistakes:** 
  - Overlooking that σ² is equal to σ in this formula, which would result in an undefined value if taken literally.
  - Not recognizing the relationship between the formula and the original definition of standard deviation, where σ = √(Σ(xi - μ)² / n), and incorrectly applying it as a simplified version.

* **Calculator Steps:** 
  - N/A

---

## QNT-F015: Covariance

**Formula:** Cov(X,Y) = Σ[(Xᵢ - X̄)(Yᵢ - Ȳ)] / (n - 1)

* Variables:
  - X: The value of one variable
  - Y: The value of another variable
  - X̄: The mean (average) of variable X
  - Ȳ: The mean (average) of variable Y
  - n: The number of data points (observations)

* When to Use:
  - To calculate the covariance between two variables, which is a measure of how much they move together.
  - In portfolio analysis and risk management to understand the relationship between asset returns.

* When NOT to Use:
  - If you're trying to determine if there's a linear relationship between variables (use correlation instead).
  - For calculating the variance or standard deviation of individual variables.

* Common Mistakes:
  - Not considering the degrees of freedom (n-1) in the denominator.
  - Incorrectly applying the formula for zero covariance (i.e., when one variable is constant and the other varies).

* Calculator Steps:
  - N/A

---

## QNT-F016: Correlation Coefficient

**Formula:** ρ(X,Y) = Cov(X,Y) / (σ_X × σ_Y)

* **Variables:**
  - Cov(X,Y): The covariance between variables X and Y
  - ρ(X,Y): The correlation coefficient between variables X and Y
  - σ_X: The standard deviation of variable X
  - σ_Y: The standard deviation of variable Y

* **When to Use:**
  - To measure the linear relationship between two continuous variables
  - To determine the strength and direction of a linear relationship between two variables
  - When the data is normally distributed or approximately normal

* **When NOT to Use:**
  - When dealing with non-continuous variables (e.g., categorical, binary)
  - When the data has an uneven distribution (e.g., skewed, outliers)
  - When calculating correlation in a non-standardized dataset

* **Common Mistakes:**
  - Forgetting to check for normality assumptions
  - Not accounting for multicollinearity between variables
  - Using the wrong formula or units

* **Calculator Steps:**
  - Use the Cov(X,Y) function to calculate the covariance
  - Use the σ_X and σ_Y functions to calculate the standard deviations, then multiply them together
  - Divide the result of the covariance calculation by the product of the two standard deviations

---

## QNT-F017: Bayes' Formula

**Formula:** P(A|B) = P(B|A) × P(A) / P(B)

* Variables:
  - P(A|B): Conditional probability of event A given event B
  - P(B|A): Conditional probability of event B given event A
  - P(A): Probability of event A
  - P(B): Probability of event B

* When to Use:
  - Apply Bayes' Formula when you want to calculate the conditional probability of an event, given that another event has occurred.

* When NOT to Use:
  - Do not apply Bayes' Formula if you are unsure about the values or assumptions required for each probability. The formula can be complex and sensitive to incorrect input.

* Common Mistakes:
  - Misinterpreting the formula as a simple multiplication of probabilities, rather than a conditional probability relationship.
  - Assuming that P(B) is equal to 1 (or the normalizing factor), when in fact it may not always be the case.

* Calculator Steps:
  - N/A

---

## QNT-F018: Expected Value

**Formula:** E(X) = Σ Xᵢ × P(Xᵢ)

* **Variables:** 
  - X: represents individual values in a probability distribution
  - P(X): represents the probability of each value occurring
  - Σ (Greek letter sigma): represents the summation operation
  - E(X): represents the expected value

* **When to Use:** 
  - When calculating the average value that can be expected from a random variable
  - When determining the expected return on investment or profit in financial contexts
  - When analyzing probabilities and outcomes in various fields, including finance, engineering, and statistics

* **When NOT to Use:** 
  - When dealing with discrete random variables only; for continuous distributions, use integration instead.
  - In situations where the probability distribution is not known or defined.

* **Common Mistakes:** 
  - Forgetting to account for all possible values in the sum (leading to incorrect expected value calculations)
  - Misinterpreting Σ as a multiplier rather than an operator
  - Incorrectly applying the formula to skewed distributions; use logarithms if necessary

* **Calculator Steps:**
  - N/A

---

## QNT-F019: Portfolio Expected Return

**Formula:** E(R_p) = Σ wᵢ × E(Rᵢ)

* Variables:
  - $w_i$ is the weight of asset i in the portfolio
  - $E(R_i)$ is the expected return of asset i
  - $R_p$ is the expected return of the portfolio

* When to Use:
  - Calculate the expected return of a portfolio when you know the individual expected returns and weights of each asset.

* When NOT to Use:
  - Do not use this formula if you do not know the individual expected returns or weights of each asset in the portfolio.
  - Do not use this formula for portfolios with multiple layers (e.g., a portfolio of stocks and bonds), as it only accounts for two-level portfolios.

* Common Mistakes:
  - Failing to calculate the correct weights, leading to incorrect results
  - Ignoring the fact that individual expected returns may be different from expected returns calculated using historical data
  - Not considering the implications of tax efficiency or transaction costs on portfolio expected return

* Calculator Steps:
  - N/A

---

## QNT-F020: Portfolio Variance (Two Assets)

**Formula:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(R₁,R₂)

* **Variables:** 
    - σ_p²: Portfolio variance (two assets)
    - w₁ and w₂: Weight of each asset in the portfolio
    - σ₁² and σ₂²: Variance of individual assets 1 and 2 respectively
    - Cov(R₁,R₂): Covariance between returns of assets 1 and 2

* **When to Use:** 
    When calculating the total variance of a two-asset portfolio, where you know the weights of each asset and the variances of the individual assets.

* **When NOT to Use:** 
    When the covariance between the two assets is not known or cannot be estimated.

* **Common Mistakes:** 
    - Not accounting for covariance: candidates may incorrectly assume that covariance can always be ignored or assumed as zero.
    - Incorrectly applying correlation coefficient: candidates should understand that the formula requires a specific type of covariance, which might differ from the correlation coefficient used in other contexts.

* **Calculator Steps:**
    N/A

---

## QNT-F021: Roy's Safety-First Ratio

**Formula:** SFR = (E(R_p) - R_L) / σ_p

* Variables:
  - E(R_p): Expected return of the portfolio
  - R_L: Risk-free rate
  - σ_p: Standard deviation of the portfolio returns

* When to Use:
  - Use the Roy's Safety-First Ratio when you need to evaluate the trade-off between expected return and risk for a given investment portfolio.

* When NOT to Use:
  - Do not use this formula when calculating the required return or when assessing an individual security's beta, as it is designed specifically for portfolio evaluation.

* Common Mistakes:
  - Failing to substitute actual values into the formula
  - Incorrectly assuming that σ_p represents the standard deviation of the risk-free rate

* Calculator Steps:
  - N/A

---

## QNT-F022: Standard Error of the Mean

**Formula:** SE = σ / √n (known σ) or SE = s / √n (unknown σ)

* **Variables:**
  - σ: population standard deviation (known)
  - n: sample size
  - s: sample standard deviation (unknown)

* **When to Use:**
  - When you know the population standard deviation and need to calculate the standard error of the mean.

* **When NOT to Use:**
  - When you don't know the population standard deviation (you should use the formula with 's' instead).

* **Common Mistakes:**
  - Forgetting to square the sample size 'n' in the denominator.
  - Using σ instead of s when the population standard deviation is unknown.

* **Calculator Steps:**
  - Press: √
  - Enter: σ/s (for unknown σ) or n (for known σ)
  - =

---

## QNT-F023: Z-Statistic

**Formula:** Z = (X̄ - μ₀) / (σ/√n)

* **Variables:** 
  - $Z$: The z-statistic value
  - $X̄$: The sample mean
  - $\mu₀$: The population mean (often assumed to be equal to the known population standard deviation)
  - $\sigma$: The population standard deviation
  - $n$: The sample size

* **When to Use:** 
  - To calculate the z-statistic for a normally distributed dataset when the population parameters are unknown, and the sample is representative of the population.

* **When NOT to Use:** 
  - When the data does not meet the assumptions of normality or equal variances.
  - When the population standard deviation $\sigma$ is known, use the t-statistic instead (Z-test for means).
  
* **Common Mistakes:**
  - Assuming that the population mean can be replaced by the sample mean without justification ($\mu_0$ should only be used when there's strong evidence it's correct)
  - Forgetting to square root $n$, which affects $\sigma$
  - Misusing the Z-statistic for non-normal data

* **Calculator Steps:** 
  - N/A

---

## QNT-F024: t-Statistic

**Formula:** t = (X̄ - μ₀) / (s/√n), df = n - 1

* Variables:
  * X̄: The sample mean
  * μ₀: The population mean
  * s: The sample standard deviation
  * n: The sample size

* When to Use:
  * Calculate the t-statistic when comparing a sample mean to a known population mean, and the sample size is small (usually n < 30).

* When NOT to Use:
  * Do not use this formula when calculating confidence intervals or standard errors, as it only provides a test statistic.

* Common Mistakes:
  * Assuming that the sample standard deviation (s) is equal to the population standard deviation (σ), which is rarely the case.
  * Failing to check for normality of the data distribution and appropriate transformation if necessary.

* Calculator Steps:
  N/A

---

## QNT-F025: Simple Linear Regression

**Formula:** Yᵢ = b₀ + b₁Xᵢ + εᵢ

* **Variables:** 
  - $Y_{{i}}$: The dependent variable (the variable being predicted)
  - $b_0$ and $b_1$: The intercept and slope of the regression line
  - $X_i$: The independent variable(s) used in the regression
  - $\varepsilon_{i}$: The error term or residual (the difference between the observed and predicted values)

* **When to Use:** 
  When analyzing the relationship between two variables, where you want to model the dependent variable as a linear function of one or more independent variables.

* **When NOT to Use:** 
  When the relationship between the variables is non-linear or when there are multiple independent variables with complex interactions. Also, not suitable for time-series data or data that has seasonality.

* **Common Mistakes:** 
  - Incorrect estimation of the slope ($b_1$) due to lack of data or incorrect assumption about the relationship between $X_i$ and $Y_{i}$
  - Failure to account for outliers in the dataset, which can significantly impact the accuracy of the regression line
  - Not considering autocorrelation or heteroscedasticity in the data, which can lead to biased estimates of the parameters

* **Calculator Steps:** 
  N/A

---

# ECONOMICS FORMULAS

## ECO-F001: Own-Price Elasticity of Demand

**Formula:** E = (%ΔQ) / (%ΔP) = (ΔQ/ΔP) × (P/Q)

* Variables:
  - Q: Quantity demanded
  - P: Price of the good
  - ΔQ: Change in quantity demanded
  - ΔP: Change in price

* When to Use:
  - To measure how responsive consumers are to a change in price when holding quantity constant.

* When NOT to Use:
  - When changes in quantity and price occur simultaneously (ΔQ = ΔP), because it would result in division by zero.
  - In situations where the relationship between quantity demanded and price is not linear, i.e., hyperbolic demand curves.

* Common Mistakes:
  - Assuming that percentage changes in Q and P can be used directly in the formula when they are actually ratios (ΔQ/ΔP), rather than actual percentages.
  - Not considering the effect of holding constant one variable while analyzing how responsive consumers are to a change in price with respect to the other variable.

* Calculator Steps:
  - Use a calculator for the division and multiplication operations: ΔQ / ΔP and P / Q
  - Multiply the two results from above (ΔQ/ΔP) × (P/Q)

---

## ECO-F002: Income Elasticity of Demand

**Formula:** E_I = (%ΔQ) / (%ΔI)

* Variables:
  * %ΔQ: percentage change in quantity demanded (ΔQ / Q)
  * %ΔI: percentage change in income (ΔI / I)
 
* When to Use:
  * Calculate the income elasticity of demand when you need to determine how much a change in income affects the quantity demanded, and vice versa.
  * Apply this formula when analyzing the responsiveness of demand to changes in income.

* When NOT to Use:
  * Do not use this formula for calculating price elasticity of demand or supply, as it only accounts for changes in income.

* Common Mistakes:
  * Candidates often incorrectly calculate the percentage change in income (ΔI / I), which can lead to incorrect results.
  * Failure to consider the base year values (Q and I) when applying the formula, resulting in inaccurate calculations.

* Calculator Steps:
  N/A

---

## ECO-F003: Cross-Price Elasticity of Demand

**Formula:** E_XY = (%ΔQ_X) / (%ΔP_Y)

* **Variables:** 
  - QX: Quantity demanded of good X
  - PY: Quantity demanded of good Y
  - ΔQX: Percentage change in quantity demanded of good X
  - ΔPY: Percentage change in price of good Y

* **When to Use:** 
  - When analyzing the responsiveness of demand for one good to changes in the price of another good.
  - In situations where two goods are complementary (substitutes), using cross-price elasticity helps determine whether the relationship is positive or negative.

* **When NOT to Use:**
  - When analyzing the responsiveness of demand for a single good, use the percentage change in price (ΔPX) and quantity demanded (ΔQX).
  - In situations with multiple goods that are substitutes, use the total cross-price elasticity of demand (sum of individual cross-elasticities).

* **Common Mistakes:** 
  - Not accounting for the direction of substitution (i.e., assuming all substitutions are equal without considering positive or negative effects)
  - Using a single good's data instead of analyzing its individual and combined effects with other goods.

* **Calculator Steps:**
  - N/A

---

## ECO-F004: GDP (Expenditure Approach)

**Formula:** GDP = C + I + G + (X - M)

**Variables:**
- C: Consumer spending (household consumption expenditure)
- I: Investment (business fixed investment, such as capital expenditures)
- G: Government expenditure
- X: Exports (value of goods and services sold to other countries)
- M: Imports (value of goods and services bought from other countries)

**When to Use:**
- When calculating a country's total Gross Domestic Product (GDP) using the expenditure approach.

**When NOT to Use:**
- When calculating GDP using the income or price approaches.
- When analyzing individual components of consumption, investment, government expenditure, exports, and imports separately.

**Common Mistakes:**
- Forgetting to include taxes and subsidies as part of household consumption expenditure (C) and business fixed investment (I).
- Incorrectly assuming that all exports are subject to tariffs or other trade restrictions.
- Failing to account for net exports (X - M), which may result in an inaccurate GDP calculation.

**Calculator Steps:**
- Use a standard calculator with basic arithmetic capabilities.

---

## ECO-F005: GDP Deflator

**Formula:** GDP Deflator = (Nominal GDP / Real GDP) × 100

* **Variables:** 
    * Nominal GDP
    * Real GDP
    * Percentage (%)

* **When to Use:**
    * To measure the rate of change in the general price level in an economy over time, typically for countries with a high degree of price stability.

* **When NOT to Use:**
    * When calculating the inflation rate or deflator for specific periods other than long-term (e.g. quarterly) data.
    * When nominal and real GDP have a large discrepancy due to seasonal fluctuations in prices.

* **Common Mistakes:** 
    * Incorrectly applying the formula with nominal and real GDP values that have been adjusted for price differences.
    * Not considering the implications of using this formula on specific types of economic data (e.g. short-term data).

* **Calculator Steps:**
    * Use % key to input percentage value
    * Use / key to divide Nominal GDP by Real GDP
    * Use × key to multiply result by 100

---

## ECO-F006: Quantity Theory of Money

**Formula:** MV = PY

* **Variables:**
  - M: The money supply (the total amount of currency and coins in circulation)
  - V: The velocity of money (the number of times a unit of currency is spent per unit of time)
  - P: The price level (the general price level of goods and services in an economy)
  - Y: The real GDP or output of the economy

* **When to Use:**
  - When analyzing the relationship between the money supply, velocity, and price level.
  - In understanding how changes in the money supply can affect inflation.

* **When NOT to Use:**
  - When trying to calculate the actual amount of money in circulation or its impact on real GDP.
  - In forecasting future economic growth or performance based solely on this formula.

* **Common Mistakes:**
  - Assuming that the velocity of money is constant, which it is not.
  - Not accounting for other factors that can affect inflation and the price level.
  - Misinterpreting the relationship between the variables; e.g., assuming MV = PY implies that an increase in M directly causes Y.

* **Calculator Steps:**
  - N/A

---

## ECO-F007: Fisher Effect

**Formula:** R_nom = R_real + π^e

* **Variables:**
  - π (pi): represents the rate of change in interest rates
  - e: a mathematical constant approximately equal to 2.71828
  - R_real: real return on an investment or asset
  - R_nom: nominal return on an investment or asset

* **When to Use:**
  - To calculate the nominal return on an asset when there is a known rate of change in interest rates.

* **When NOT to Use:**
  - When the rate of change in interest rates (π) is not known or constant.
  - When the real return on an investment or asset (R_real) is not available.

* **Common Mistakes:**
  - Assuming π is equal to 1, when in fact it represents a specific rate of change.
  - Failing to account for compounding interest when using this formula.

* **Calculator Steps:**
  - Use the exponentiation key (^) to calculate e^π.
  - Multiply R_real by the result of e^π.

---

## ECO-F008: Fiscal Multiplier

**Formula:** Multiplier = 1 / [1 - MPC(1 - t)]

* Variables:
  * t: The marginal tax rate (a decimal value between 0 and 1)
  * MPC: The marginal propensity to consume (a decimal value between 0 and 1)
  
* When to Use:
  The fiscal multiplier is used when analyzing the impact of government spending on aggregate demand in an economy. It's especially relevant during times of recession or economic downturn, as governments often increase spending to stimulate economic growth.

* When NOT to Use:
  Do not apply the fiscal multiplier in situations where there are large shifts in consumer behavior, such as during major changes in tax policies or significant alterations in government spending priorities.

* Common Mistakes:
  Candidates may incorrectly assume that the marginal propensity to consume remains constant over time. However, MPC can change depending on various economic factors, including interest rates and expectations of future income.

* Calculator Steps:
  N/A

---

## ECO-F009: Real Exchange Rate

**Formula:** Real ER = Nominal ER × (CPI_foreign / CPI_domestic)

* Variables:
  - Nominal ER (Nominal Exchange Rate)
  - CPI_foreign (Consumer Price Index for Foreign Countries)
  - CPI_domestic (Consumer Price Index for Domestic Countries)

* When to Use:
  - To calculate the real exchange rate, which represents the value of a country's currency in terms of the purchasing power of its currency relative to other countries.

* When NOT to Use:
  - In situations where you need to account for changes in foreign interest rates or economic indicators that affect currency fluctuations.
  - When dealing with specific sectors or industries that have unique exchange rate implications.

* Common Mistakes:
  - Failing to adjust the CPI values for inflation and using the raw values, which would lead to inaccurate real exchange rate calculations.
  - Not considering the differences in economic conditions between domestic and foreign countries when calculating the real ER.

* Calculator Steps:
  N/A

---

## ECO-F010: Forward Exchange Rate (Covered Interest Rate Parity)

**Formula:** F = S × (1 + r_d) / (1 + r_f)

* **Variables:**
  - F: forward exchange rate
  - S: spot exchange rate
  - r_d: domestic interest rate
  - r_f: foreign interest rate

* **When to Use:**
  - When you need to calculate the forward exchange rate given the current spot exchange rate, domestic interest rate, and foreign interest rate.

* **When NOT to Use:**
  - When the time period of the investment is not known or when the interest rates are not constant over time.
  - When dealing with floating-rate notes or other types of instruments that have variable interest rates.

* **Common Mistakes:**
  - Forgetting to use the correct order of operations (PEMDAS/BODMAS) and incorrectly calculating the values of r_d and r_f.
  - Misinterpreting the variables as F = S / (1 + r_d), which would give an incorrect result, or misunderstanding that F is equal to the ratio of interest rates.

* **Calculator Steps:**
  - N/A

---

## ECO-F011: Forward Premium/Discount

**Formula:** Forward premium = (F - S) / S × (360/n)

**Variables:**
- F: Face Value of the forward contract
- S: Spot price of the underlying asset at expiration date
- n: Number of days between expiration date and settlement date

**When to Use:**
- When calculating the forward premium or discount for a forward contract.
- In scenarios where an investor needs to determine the implied interest rate on a forward contract.

**When NOT to Use:**
- When calculating the actual interest rates that have been prepaid or paid in a forward contract.
- In situations where the investor is simply trying to estimate the expected returns of a forward contract, as this formula only calculates the premium or discount.

**Common Mistakes:**
- Forgetting to specify the number of days between expiration and settlement dates (n).
- Failing to account for compounding interest when calculating the implied interest rate.
- Incorrectly assuming that the face value of the forward contract is equal to the nominal value of the underlying asset.

**Calculator Steps:**
- Use the [÷] key to divide.
- Use the [\*] key to multiply.
- Use the [360] key for the numerator.
- Use the [/] key to calculate the quotient.
- N/A

---

## ECO-F012: Breakeven Point

**Formula:** TR = TC or P = ATC

* Variables:
  - TR: Total Revenue
  - TC: Total Cost
  - P: Profit
  - ATC: Average Total Cost
  - P/V: Price per Unit
  - C: Number of Units Sold

* When to Use:
  - To determine the breakeven point for a business or company.
  - When calculating profit and total revenue are known.

* When NOT to Use:
  - If not enough information is provided about cost structure, pricing strategy, etc.
  - In cases where multiple inputs change simultaneously; then you would want to use marginal analysis to identify the input(s) that cause a change in overall output while keeping other inputs fixed.

* Common Mistakes:
  - Assuming all costs are equal and similar; not accounting for different types of costs like variable, fixed or sunk.
  - Ignoring the fact that prices may vary based on market conditions.

---

# FINANCIAL STATEMENT ANALYSIS FORMULAS

## FSA-F001: Basic EPS

**Formula:** Basic EPS = (Net Income - Preferred Dividends) / Weighted Average Common Shares

* Variables:
  - Net Income
  - Preferred Dividends
  - Weighted Average Common Shares

* When to Use:
  - To calculate a company's earnings per share (EPS) when the number of common shares outstanding is variable.

* When NOT to Use:
  - When calculating EPS for companies with fixed or constant preferred dividends, as it would not accurately reflect the diluted impact on common EPS.
  - When there are no preferred dividends.

* Common Mistakes:
  - Not accounting for dilution (e.g., convertible bonds, options) when using this formula.
  - Incorrectly assuming that all preferred dividends are paid out in full to shareholders, which may not be the case.

* Calculator Steps:
  N/A

---

## FSA-F002: Diluted EPS

**Formula:** Diluted EPS = (NI - Pref Div + Convert Adjustments) / (WACS + Dilutive Securities)

* **Variables:** 
  - NI: Net Income
  - Pref Div: Preferred Dividend
  - Convert Adjustments: Adjustment for convertible securities (e.g., additional shares issued)
  - WACS: Weighted Average Cost of Shares
  - Dilutive Securities: Additional shares that make the calculation of diluted EPS required

* **When to Use:** 
  - Apply when calculating diluted earnings per share (EPS) for shares with conversion options, such as convertible bonds or stock options.

* **When NOT to Use:** 
  - Do not apply if there are no dilutive securities present or if the adjustment for convertible securities is already included in the net income calculation.

* **Common Mistakes:** 
  - Forgetting to consider all dilutive securities and their conversion rates
  - Incorrectly calculating the weighted average cost of shares (WACS)
  - Failing to properly account for convertible adjustments

* **Calculator Steps:** 
  - Press [ ] to enter net income (NI) value.
  - Press [ ] to enter preferred dividend (Pref Div) value.
  - Press [ ] to enter conversion adjustment value.
  - Press [ ] to enter weighted average cost of shares (WACS) value.
  - Press [ ] to select the dilutive securities input option and enter their values.
  - Press [ ] to calculate diluted EPS.

---

## FSA-F003: Current Ratio

**Formula:** Current Ratio = Current Assets / Current Liabilities

* Variables:
  - Current Assets
  - Current Liabilities

* When to Use:
  - To assess a company's liquidity and its ability to pay short-term debts.

* When NOT to Use:
  - On companies with a high ratio of current liabilities to current assets, as this may indicate a liquidity crisis.
  - For companies in highly seasonal or cyclic industries.

* Common Mistakes:
  - Not considering the net change in working capital.
  - Ignoring off-balance-sheet items.

* Calculator Steps:
  - Use the / key to divide Current Assets by Current Liabilities.

---

## FSA-F004: Quick Ratio (Acid Test)

**Formula:** Quick Ratio = (Cash + Marketable Securities + Receivables) / Current Liabilities

* **Variables:** 
  - Cash
  - Marketable Securities
  - Receivables
  - Current Liabilities

* **When to Use:**
  - When assessing a company's ability to pay its short-term debts and evaluating liquidity.

* **When NOT to Use:**
  - When analyzing a company's long-term solvency or debt management.
  - When the company has significant inventory or other non-current assets that are not easily convertible into cash.

* **Common Mistakes:** 
  - Incorrectly assuming that all receivables can be collected immediately, which may overstate liquidity.
  - Ignoring non-cash current assets and focusing solely on cash and marketable securities.

* **Calculator Steps:**
  - N/A

---

## FSA-F005: Cash Ratio

**Formula:** Cash Ratio = (Cash + Marketable Securities) / Current Liabilities

* Variables:
  - Cash: Current liquid assets available to pay short-term debts
  - Marketable Securities: Investments that can be easily sold in the market
  - Current Liabilities: Debts that are due within one year or less

* When to Use:
  - To evaluate a company's ability to meet its short-term debt obligations
  - To assess an investor's liquidity and potential for paying dividends

* When NOT to Use:
  - In situations where a company has a history of cash flow issues or significant investments in long-term assets
  - For companies with high levels of debt financing, as it may not accurately reflect their overall financial health

* Common Mistakes:
  - Failing to account for non-current assets and liabilities that affect liquidity
  - Not considering the impact of interest income on marketable securities
  - Using outdated or incorrect data

* Calculator Steps:
  N/A

---

## FSA-F006: Debt-to-Equity Ratio

**Formula:** D/E = Total Debt / Total Equity

* Variables:
  - Total Debt (D): The total amount of debt owed by a company at a given time.
  - Total Equity (E): The total amount of equity owned by shareholders and other stakeholders in a company.

* When to Use:
  - To assess a company's level of indebtedness and its ability to generate cash from operations and invest in new opportunities.
  - In financial ratios, such as the Debt-to-Equity Ratio, which can help investors evaluate a company's capital structure and credit risk.

* When NOT to Use:
  - On companies with no debt or equity, as the ratio will be undefined (D/E = ∞).
  - When calculating the debt-to-equity ratio for an individual investor, rather than a company, as it is more relevant to companies.

* Common Mistakes:
  - Failing to include interest on long-term debt in the total debt calculation.
  - Not considering share buybacks when calculating equity.
  - Misinterpreting the ratio as indicative of creditworthiness or financial health without considering other factors such as return on equity.

---

## FSA-F007: Gross Profit Margin

**Formula:** Gross Margin = (Revenue - COGS) / Revenue = Gross Profit / Revenue

* Variables:
  - Revenue: The total amount of money earned by a business from its normal operations.
  - COGS (Cost of Goods Sold): The direct costs associated with producing and delivering a product or service, such as raw materials, labor, and overhead.
  - Gross Margin: The difference between revenue and COGS, expressed as a percentage.

* When to Use:
  - This formula is used to calculate the gross profit margin, which is an important metric for evaluating a company's profitability and pricing strategy.

* When NOT to Use:
  - This formula should not be used when there are no revenues or COGS, as this would result in a division by zero error.

* Common Mistakes:
  - Candidates often incorrectly assume that COGS includes indirect costs, such as rent or salaries of management. COGS only includes direct costs.
  - Another common mistake is to calculate the gross margin as a percentage of expenses (COGS) instead of revenue.

* Calculator Steps:
  - N/A

---

## FSA-F008: Operating Profit Margin

**Formula:** Operating Margin = Operating Income / Revenue

* Variables:
  - Operating Income: The net income earned by a company from its core operations before accounting for non-operating items.
  - Revenue: The total amount of sales generated by a company in a given period.

* When to Use:
  - To evaluate the profitability of a company's operations and compare it to industry averages or competitors.
  - When analyzing a company's financial health and ability to generate returns on investment (ROI).

* When NOT to Use:
  - As a standalone metric for evaluating a company's overall financial performance, as it only considers operating income and does not account for other factors like capital expenditures or cash flow.

* Common Mistakes:
  - Failing to calculate the numerator (Operating Income) correctly.
  - Incorrectly using non-operating items in the Operating Income calculation.
  - Forgetting to consider the denominator (Revenue) when comparing Operating Margin to industry averages or competitors.

* Calculator Steps:
  - Use the ÷ key to divide the numerator by the denominator.
  - N/A

---

## FSA-F009: Net Profit Margin

**Formula:** Net Margin = Net Income / Revenue

* Variables:
  - **Net Income**: The total amount of net income earned by a company from its operations.
  - **Revenue**: The total amount of money earned by a company from its sales and other sources.

* When to Use:
  - Calculate the net profit margin when evaluating a company's financial health, profitability, or comparing it to industry averages.

* When NOT to Use:
  - Do not use this formula to calculate the net profit margin for individual investments or personal finances; instead, refer to the investment's underlying metrics and financial statements.

* Common Mistakes:
  - Candidates often forget to account for taxes and other expenses when calculating net income.
  - Incorrectly dividing by revenue without considering the impact of inflation, currency fluctuations, or industry-specific adjustments.

* Calculator Steps:
  - Enter Net Income
  - Press ÷ (division)
  - Enter Revenue

---

## FSA-F010: Return on Assets (ROA)

**Formula:** ROA = Net Income / Average Total Assets

* Variables:
  - Net Income
  - Average Total Assets

* When to Use:
  - Calculating a company's profitability relative to its asset base.
  - Comparing the performance of companies within the same industry.

* When NOT to Use:
  - For calculating the return on equity (ROE), which requires net income and total shareholder equity as inputs.
  - When comparing companies across different industries or sectors, as ROA is an industry-specific metric.

* Common Mistakes:
  - Not considering non-operating items when calculating net income, leading to inaccurate results.
  - Not using average total assets, as it provides a more stable measure of asset size over time.

* Calculator Steps:
  - N/A

---

## FSA-F011: Return on Equity (ROE)

**Formula:** ROE = Net Income / Average Total Equity

* Variables:
  - Net Income: Refers to a company's net earnings available for common shareholders after deducting all expenses and taxes.
  - Average Total Equity: Represents the average total value of equity over a specific period, usually calculated by taking the average of beginning and ending equity balances.

* When to Use:
  - To calculate the return on equity (ROE) of a company, which is an essential metric for evaluating its financial performance and profitability.

* When NOT to Use:
  - When calculating ROE for a company with no equity or zero net income, as this would result in undefined values.

* Common Mistakes:
  - Calculating average total equity over an incorrect time period.
  - Forgetting to account for taxes, dividends, or other deductions that may impact net income.

* Calculator Steps:
  - Use the division key to calculate ROE: `/`
  - Ensure both Net Income and Average Total Equity are entered correctly.

---

## FSA-F012: DuPont Decomposition (3-Factor)

**Formula:** ROE = (NI/Revenue) × (Revenue/Assets) × (Assets/Equity)

* **Variables:**
  - NI: Net Income
  - Revenue: Total Sales Revenue
  - Assets: Total Assets
  - Equity: Total Shareholder Equity (Shareholders' Equity)
  
* **When to Use:**
  - Calculate the return on equity (ROE) when comparing a company's profitability to its ownership interest.
  - Analyze a company's financial performance relative to its asset base.
  - Evaluate the efficiency of a company's assets in generating profits.

* **When NOT to Use:**
  - Do not use this formula when analyzing a company's debt-to-equity ratio, as it does not account for debt.
  - Avoid using this formula on companies with significant one-time or non-recurring items that distort net income.
  - Do not apply this formula in situations where you need to calculate earnings per share (EPS).

* **Common Mistakes:**
  - Misinterpreting the order of operations in the formula, which can lead to incorrect calculations.
  - Forgetting to adjust for one-time or non-recurring items that affect net income.
  - Failing to consider the significance of revenue and asset growth when analyzing ROE.

* **Calculator Steps:**
  - Use N/A

---

## FSA-F013: Inventory Turnover

**Formula:** Inventory Turnover = COGS / Average Inventory

* Variables:
  - COGS (Cost of Goods Sold)
  - Average Inventory
* When to Use:
  - To measure a company's ability to sell and replace its inventory on an average basis per year
  - In financial statements, such as the balance sheet or income statement
  - For performance evaluation of inventory management
* When NOT to Use:
  - When calculating average inventory for multiple periods (use the formula A = (Beginning + Ending) / 2)
  - If using weighted average inventory method
* Common Mistakes:
  - Not considering the fact that Average Inventory is an estimate, not an exact value
  - Using COGS as a percentage of sales instead of absolute dollar amount
* Calculator Steps:
  - N/A

---

## FSA-F014: Receivables Turnover

**Formula:** Receivables Turnover = Revenue / Average Receivables

* Variables:
  - Revenue: The total sales revenue of a company over a specific period of time.
  - Average Receivables: The average amount of receivables outstanding at a given point in time.

* When to Use:
  - Calculate the receivables turnover ratio when evaluating a company's efficiency in collecting its debts, particularly for businesses with a high volume of sales on credit.

* When NOT to Use:
  - Not suitable for calculating cash flow or liquidity, as it only considers the relationship between revenue and receivables.

* Common Mistakes:
  - Failing to account for the timing differences between revenue recognition and when goods are shipped or delivered.
  - Incorrectly using historical averages of receivables instead of adjusting for current period changes in working capital.

* Calculator Steps:
  N/A

---

## FSA-F015: Free Cash Flow to Firm (FCFF)

**Formula:** FCFF = CFO + Interest(1-t) - FCInv

* Variables:
  * CFO: Capital Expenditures (net of depreciation and capitalization)
  * Interest: Interest expenses
  * t: Tax rate (effective tax rate)

* When to Use:
  * Calculate FCFF when evaluating a company's ability to generate cash for its shareholders, especially during periods of expansion or investment.

* When NOT to Use:
  * Not applicable to companies with no interest expenses, as the formula relies on this component.

* Common Mistakes:
  * Forgetting to account for capitalization, which can significantly impact CFO.
  * Incorrectly applying the tax rate (effective tax rate) in the context of the company's operations.
  * Failing to consider depreciation when calculating CFO.

* Calculator Steps:
  N/A

---

## FSA-F016: Free Cash Flow to Equity (FCFE)

**Formula:** FCFE = CFO - FCInv + Net Borrowing

* Variables:
  - CFO: Cash Flows from Operations
  - FCInv: Capital Expenditures
  - Net Borrowing: After-tax proceeds of debt issuance

* When to Use:
  - To calculate a company's free cash flow available for equity returns, such as dividends or share repurchases.

* When NOT to Use:
  - When estimating cash flows from non-operating activities.
  - When calculating free cash flow available from operating lease payments.
  - For companies that do not issue new debt.

* Common Mistakes:
  - Incorrectly capitalizing or depreciating intangible assets as capital expenditures.
  - Not accounting for taxes on debt issuance in the net borrowing line.
  - Failing to consider other non-operating cash flows, such as interest expenses.

* Calculator Steps:
  N/A

---

## FSA-F017: Straight-Line Depreciation

**Formula:** Depreciation = (Cost - Residual Value) / Useful Life

* **Variables:**
  * Cost: The initial cost of the asset
  * Residual Value: The estimated value of the asset at the end of its useful life
  * Useful Life: The length of time the asset is expected to remain in use before it becomes obsolete or is replaced

* **When to Use:**
  * When calculating depreciation for assets with a fixed residual value and a known useful life, such as equipment, vehicles, or property.

* **When NOT to Use:**
  * When calculating depreciation for intangible assets, such as patents, copyrights, or goodwill.
  * When the asset's useful life is not certain or can be estimated within a reasonable range.

* **Common Mistakes:**
  * Assuming that all assets have a fixed residual value when in fact some may be sold or scrapped at the end of their life.
  * Failing to consider other factors such as inflation, obsolescence, and changes in technology when estimating useful life.
  * Not recalculating depreciation each period if the asset's remaining useful life is less than one year.

* **Calculator Steps:**
  * N/A

---

## FSA-F018: Double-Declining Balance Depreciation

**Formula:** Depreciation = (2 / Useful Life) × Book Value at Beginning of Year

* **Variables:** 
  - Depreciation
  - Useful Life
  - Book Value at Beginning of Year

* **When to Use:**
  - Apply this formula when the company uses the double-declining balance method for depreciation and has a specified useful life for assets.

* **When NOT to Use:**
  - Do not use this formula if the company is using any other depreciation methods, such as straight-line or units-of-production methods, or if the useful life of an asset is not specified.

* **Common Mistakes:**
  - Misinterpretation of the formula as a simple multiplication factor.
  - Failure to consider other factors that may affect depreciation, such as salvage value and interest expenses.

* **Calculator Steps:** 
  N/A

---

## FSA-F019: Effective Tax Rate

**Formula:** Effective Tax Rate = Income Tax Expense / Pre-Tax Income

* Variables:
  - Effective Tax Rate: The tax rate at which a company is taxed on its pre-tax income
  - Income Tax Expense: The total amount of income tax paid by a company
  - Pre-Tax Income: The total amount of income earned by a company before taxes are deducted

* When to Use:
  Apply this formula when calculating the effective tax rate for a company, which is necessary for determining the profitability and cash flow after taxes.

* When NOT to Use:
  Do not apply this formula in situations where you need to calculate the total amount of income tax expense or pre-tax income separately, as that would require additional formulas.

* Common Mistakes:
  - Assuming the effective tax rate can be applied to individual income for personal tax purposes
  - Failing to consider other types of taxes such as capital gains taxes, payroll taxes, and taxes on business expenses
  - Not adjusting the formula for changes in corporate tax laws or rates

* Calculator Steps:
  N/A

---

## FSA-F020: Interest Coverage Ratio

**Formula:** Interest Coverage = EBIT / Interest Expense

* **Variables:** 
  - EBIT (Earnings Before Interest and Taxes)
  - Interest Expense
* **When to Use:**
  - To evaluate a company's ability to meet its interest payments by comparing its earnings capacity to its interest expense
* **When NOT to Use:**
  - When assessing a company's creditworthiness or liquidity, as the ratio does not consider other factors like debt levels and cash flows
* **Common Mistakes:**
  - Failing to account for non-operating items in EBIT calculation
  - Ignoring that Interest Expense can include penalties, fines, and interest on loans taken out for working capital purposes
* **Calculator Steps:** 
  N/A

---

# CORPORATE ISSUERS FORMULAS

## COR-F001: Net Present Value (NPV)

**Formula:** NPV = Σ CFₜ/(1+r)^t - Initial Investment

* **Variables:** 
  * CFₜ: Cash Flow at time t
  * r: Discount rate (interest rate)
  * t: Time period (time in years)

* **When to Use:** 
  * To calculate the present value of future cash flows, including investments and returns on investment.
  * When comparing different investment opportunities with different cash flow schedules.

* **When NOT to Use:** 
  * For projects or investments that do not have a specific cash flow schedule (e.g. perpetual bonds).
  * When calculating the NPV of an existing portfolio without considering future cash flows.

* **Common Mistakes:**
  * Assuming all cash flows occur at the end of each period.
  * Not adjusting for taxes, inflation, or other economic factors that affect cash flows.
  * Failing to consider the initial investment as a negative cash flow.

* **Calculator Steps:** 
  N/A

---

## COR-F002: Internal Rate of Return (IRR)

**Formula:** Solve for r where NPV = 0

* Variables:
  * NPV (Net Present Value): The difference between the present value of cash inflows and outflows over a period
  * r (Interest Rate): The internal rate at which the net present value equals zero
  * CF (Cash Flows): Initial investment or outflow, and future cash inflows and outflows

* When to Use:
  * Determine the profitability of an investment opportunity
  * Compare different investments with varying cash flows
  * Calculate the return on investment for a project or business

* When NOT to Use:
  * For calculating the yield on a fixed-income security, such as bonds
  * To determine the cost of capital for a company's debt financing

* Common Mistakes:
  * Assuming IRR is always positive: IRR can be negative, indicating a cash flow that reduces the investment
  * Failing to consider non-cash flows (e.g. depreciation): Cash flows must include all changes in net assets
  * Rounding errors: Small rounding errors can lead to significant differences in calculated IRR

* Calculator Steps:
  N/A

---

## COR-F003: Weighted Average Cost of Capital (WACC)

**Formula:** WACC = w_d × r_d(1-t) + w_p × r_p + w_e × r_e

* Variables:
  - w_d: weight of debt (as a decimal)
  - r_d(1-t): weighted average cost of debt
  - w_p: weight of preferred stock (as a decimal)
  - r_p: cost of preferred stock
  - w_e: weight of equity (as a decimal)
  - r_e: cost of equity

* When to Use:
  - Calculate the Weighted Average Cost of Capital when you need to estimate the average cost of capital for a company, which is used in various financial decisions such as investment appraisal and funding requirements.

* When NOT to Use:
  - Do not use this formula when there are multiple classes of debt with different interest rates and maturities, or when there are multiple types of equity that have different characteristics, because it assumes simplicity and ignores these complexities.

* Common Mistakes:
  - Misinterpreting the weights as percentages instead of decimals
  - Failing to account for taxes on debt (represented by t)
  - Not correctly calculating the weighted average cost of debt

* Calculator Steps:
  - N/A

---

## COR-F004: Cost of Equity (CAPM)

**Formula:** r_e = R_f + β(R_m - R_f)

* Variables:
  * \(r_e\): cost of equity
  * \(R_f\): risk-free rate
  * \(\beta\): beta (sensitivity to market return)
  * \(R_m\): expected market return

* When to Use:
  Apply the Cost of Equity formula when estimating the cost of equity for a company's capital budgeting decisions, such as evaluating investment projects or determining the minimum required return on investment.

* When NOT to Use:
  Do not use this formula in situations where you are trying to estimate the expected return of a specific asset class (like stocks or bonds), since it is focused on the overall market.

* Common Mistakes:
  - Incorrectly assuming that \(\beta\) can be estimated using the historical volatility and standard deviation of a single stock, when in fact it should use the beta of the relevant industry or market index.
  - Failing to properly account for the risk-free rate (R_f) as a critical component of estimating cost of equity.

---

## COR-F005: Cost of Preferred Stock

**Formula:** r_p = D_p / P_p

* Variables:
  - $r_p$: The cost of preferred stock (or the required return on a preferred stock)
  - $D_p$: The dividend payment per share
  - $P_p$: The price per share

* When to Use:
  Use this formula when you need to calculate the cost of holding a preferred stock, and you know the dividend payment per share.

* When NOT to Use:
  Do not use this formula if you are trying to calculate the expected return on an investment in general (this is specific to preferred stocks).

* Common Mistakes:
  - Assuming that $D_p$ and $P_p$ are always provided - they may be missing or unknown.
  - Forgetting to consider other costs associated with owning a preferred stock, such as call risk.

* Calculator Steps:
  N/A

---

## COR-F006: After-Tax Cost of Debt

**Formula:** r_d(1 - t)

* Variables:
  - r_d: The before-tax cost of debt
  - t: The tax rate (as a decimal)

* When to Use:
  - Calculate the after-tax cost of debt when you want to take into account the tax effects on interest payments.

* When NOT to Use:
  - Do not use this formula if you need to calculate the pre-tax cost of debt or if there are any other tax-related factors at play.

* Common Mistakes:
  - Failing to convert the tax rate from a percentage to a decimal, resulting in an incorrect calculation.
  - Forgetting to include the negative sign when subtracting the tax rate from 1.

* Calculator Steps:
  N/A

---

## COR-F007: Degree of Operating Leverage (DOL)

**Formula:** DOL = %Δ Operating Income / %Δ Sales

**Variables:**
- Δ (delta) represents change in value, typically denoted by the Greek letter delta.
- %Δ (percentage of change) represents percentage change from a base value, usually expressed as a decimal (e.g., 0.05 for 5%).
- Operating Income is the profit earned by a company before interest and taxes.
- Sales are revenues generated by a company.

**When to Use:**
- Apply DOL when analyzing the effect of changes in operating income on sales, particularly useful in understanding the sensitivity of earnings to changes in revenue.
- Useful for evaluating a firm's pricing power or its ability to capture profits from price increases.

**When NOT to Use:**
- Do not apply DOL when changes in other factors like costs, taxes, or interest rates are significant and may overshadow the impact of sales on operating income.

**Common Mistakes:**
- Candidates often fail to consider that DOL is sensitive to the base value used for percentage calculations.
- Misinterpreting Δ Operating Income as equivalent to net income can lead to incorrect conclusions about a firm's ability to capture profits from price increases.

**Calculator Steps:**
N/A

---

## COR-F008: Degree of Financial Leverage (DFL)

**Formula:** DFL = %Δ Net Income / %Δ Operating Income

* Variables:
  - %Δ Net Income: The percentage change in net income from one period to another
  - %Δ Operating Income: The percentage change in operating income from one period to another
  - DFL (Degree of Financial Leverage): The degree of financial leverage, representing the rate at which net income changes when earnings change

* When to Use:
  - To calculate the impact of changes in operating income on net income and, ultimately, shareholder value
  - When analyzing a company's profitability and its sensitivity to changes in its operating performance

* When NOT to Use:
  - In situations where the change in net income is caused by factors other than changes in operating income (e.g., changes in capital structure or accounting policies)
  - When comparing profitability across different companies or industries, as DFL only measures the relationship between operating and net income for a single company

* Common Mistakes:
  - Assuming that DFL represents the rate of return on equity (ROE) or earnings per share (EPS), when in fact it measures the degree to which changes in operating income affect net income
  - Failing to consider other factors that can impact profitability, such as changes in taxes, interest expenses, or capital structure

---

## COR-F009: Degree of Total Leverage (DTL)

**Formula:** DTL = DOL × DFL = %Δ Net Income / %Δ Sales

* Variables:
  - DOL: Degree of Operating Leverage
  - DFL: Degree of Financial Leverage
  - %Δ Net Income: Change in net income from the same period last year
  - %Δ Sales: Change in sales from the same period last year

* When to Use:
  - Calculate when analyzing a company's profitability and leverage, particularly when evaluating changes in net income and sales.

* When NOT to Use:
  - Do not use this formula when analyzing companies with complex capital structures or debt instruments that affect financial leverage. Also, do not apply it if the company does not provide sales data for different periods.

* Common Mistakes:
  - Incorrectly assuming DTL is a direct measure of profitability or return on investment.
  - Misinterpreting changes in %Δ Net Income and %Δ Sales without considering other factors such as changes in operating expenses or revenue recognition policies.

* Calculator Steps:
  - N/A

---

## COR-F010: Cash Conversion Cycle

**Formula:** CCC = DOH + DSO - DPO

* Variables:
  - DOH (Days Outstanding from Hours Sold): The number of days it takes for a company to collect payment from its customers after they have sold goods or services.
  - DSO (Days Sales Outstanding): The average number of days it takes for a company to sell its inventory.
  - DPO (Days Payable Outstanding): The average number of days it takes for a company to pay its suppliers.

* When to Use:
  - This formula is used to calculate the cash conversion cycle, which helps investors and analysts determine how efficiently a company can convert its sales into cash.

* When NOT to Use:
  - This formula should not be applied when considering credit risk or the company's ability to manage its accounts receivable and payable.

* Common Mistakes:
  - Candidates often incorrectly assume that DPO is equal to DOH, which is incorrect as DPO refers to payment terms, while DOH refers to collection from customers.
  - Another common mistake is not accounting for inventory turnover when calculating the cash conversion cycle.

* Calculator Steps:
  - N/A

---

## COR-F011: Cost of Trade Credit (EAR)

**Formula:** EAR = [1 + d/(1-d)]^(365/(Payment Period - Discount Period)) - 1

* **Variables:** 
  * `d`: discount rate (as a decimal)
  * `Payment Period`: the total number of days within which the payment must be made
  * `Discount Period`: the number of days within which a discount is available

* **When to Use:**
  When calculating the cost of trade credit for an investment with a periodic discount, and you need to calculate the effective interest rate.

* **When NOT to Use:**
  When the payment period equals the discount period (i.e., there is no discount available), or when the payment period is not fixed.

* **Common Mistakes:** 
  - Incorrectly entering the discount rate as a percentage instead of a decimal
  - Failing to correctly handle cases where `d` and/or `Payment Period - Discount Period` are equal to zero

* **Calculator Steps:**
  N/A

---

## COR-F012: Modigliani-Miller Proposition I (With Taxes)

**Formula:** V_L = V_U + tD

* Variables:
  - $V_L$ : The present value of a dividend
  - $V_U$ : The present value of the equity (share price) without taxes
  - $t$ : The tax rate on dividends
  - $D$ : The amount of dividends paid out per share

* When to Use:
  Apply this formula when you want to calculate the present value of a dividend payment, considering the effects of corporate income taxes.

* When NOT to Use:
  Do not apply this formula for equity issuances or purchases, as it only considers dividend payments. For these types of transactions, use other formulas such as Modigliani-Miller Proposition II.

* Common Mistakes:
  - Candidates may incorrectly assume that all dividends are taxed at the same rate, when in fact different types of dividends (e.g., ordinary vs. capital gains) have different tax rates.
  - They may forget to consider other factors that can affect a company's dividend payments, such as payout ratios or earnings volatility.

* Calculator Steps:
  N/A

---

## COR-F013: Modigliani-Miller Proposition II (With Taxes)

**Formula:** r_e = r₀ + (r₀ - r_d)(1-t)(D/E)

* Variables:
  * $r_0$: The cost of equity without taxes
  * $r_d$: The cost of debt
  * $t$: The tax rate (tax on earnings after dividends)
  * $D$: The total dividends paid by the company
  * $E$: The market value of the firm's common stock

* When to Use:
  Apply this formula when calculating the expected return on equity for a company with both debt and equity financing, considering taxes.

* When NOT to Use:
  Do not use this formula when: 
    - there are no taxes involved
    - the company does not pay dividends
    - the tax rate is zero or unknown

* Common Mistakes:
  Candidates often mistake $t$ for $(1-t)$ or incorrectly calculate the dividend yield ($D/E$), which can lead to incorrect results.

* Calculator Steps:
  N/A

---

## COR-F014: Return on Invested Capital (ROIC)

**Formula:** ROIC = NOPAT / Invested Capital

**Variables:**
- NOPAT (Net Operating Profit After Tax): The net income of a company after taxes
- Invested Capital: The sum of total debt and equity capital employed by a company

**When to Use:**
- To evaluate the profitability of an investment or a business, providing insight into the return on invested capital
- When analyzing a company's financial performance in relation to its capital structure

**When NOT to Use:**
- In situations where the company has high levels of debt, as it may mask underlying financial issues related to cash flow and liquidity
- When considering short-term investments or opportunities, as ROIC is typically a long-term metric

**Common Mistakes:**
- Failing to consider the cost of capital in conjunction with ROIC when evaluating investment opportunities
- Incorrectly assuming that high ROIC necessarily means an attractive investment opportunity
- Not accounting for changes in working capital and its impact on invested capital

**Calculator Steps:**
N/A

---

# EQUITY INVESTMENTS FORMULAS

## EQU-F001: Gordon Growth Model (Constant Growth DDM)

**Formula:** V₀ = D₁ / (r - g) = D₀(1+g) / (r - g)

* Variables:
  * V₀: Initial value of the asset
  * D₁: Dividend per share
  * r: Expected return of the market portfolio (WACC)
  * g: Growth rate of dividends

* When to Use:
  * To estimate the initial value of a dividend-paying stock when there is no historical data available.

* When NOT to Use:
  * When estimating the present value of an existing cash flow stream from a dividend-paying stock. The Gordon Growth Model assumes constant growth, which may not be representative in reality.
  * When estimating the initial value of a non-dividend paying asset or a bond.

* Common Mistakes:
  * Over-estimating the expected return of the market portfolio (r), leading to an over-valued estimate for V₀.
  * Under-estimating the growth rate of dividends (g), leading to an under-valued estimate for V₀.
  * Ignoring the impact of inflation on the expected return and dividend growth.

* Calculator Steps:
  N/A

---

## EQU-F002: Sustainable Growth Rate

**Formula:** g = ROE × Retention Ratio = ROE × (1 - Payout Ratio)

* **Variables:** 
  - $g$: Sustainable growth rate
  - $ROE$ (Return on Equity): Return on equity of a company
  - $Retention Ratio$: The percentage of earnings kept in the business
  - $Payout Ratio$: The percentage of earnings paid out to shareholders

* **When to Use:** 
  This formula is used when calculating the sustainable growth rate of a company, which can be compared with its cost of capital.

* **When NOT to Use:** 
  Do not use this formula when calculating short-term returns or returns that are not directly related to equity.

* **Common Mistakes:** 
  Common errors candidates make include miscalculating retention and payout ratios as decimal values instead of percentages, or forgetting to subtract the payout ratio from 1.

* **Calculator Steps:**
  - Enter $ROE$ into the calculator.
  - Press $÷$ (division) key
  - Enter $Retention Ratio$ as a percentage and press $×$ (multiplication) key
  - Subtract $Payout Ratio$ from 1 (using $-$ (minus) key) and multiply by the result of step 2.

---

## EQU-F003: Trailing P/E Ratio

**Formula:** P₀/E₀ or P/E = (D₁/E₁) / (r - g) = Payout Ratio / (r - g)

**Variables:**
- $P_0$ (Initial Earnings Per Share)
- $E_0$ (Initial Enterprise Value per Share)
- $D_1$ (Discretionary Earnings in Period 1)
- $E_1$ (Enterprise Value in Period 1)
- $r$ (Market Rate of Return)
- $g$ (Growth Rate)

**When to Use:**
- When the company is expected to grow at a constant rate and there is no information about future dividend payments.
- When calculating the implied price per share for a growth stock.

**When NOT to Use:**
- When the company has a history of paying dividends, as this affects the payout ratio.
- When the company's growth rate or market return may vary significantly over time.

**Common Mistakes:**
- Assuming that $g$ is constant when in fact it can change over time due to various factors such as changes in industry conditions or management strategies.
- Forgetting to adjust for payout ratio, which can impact the calculated P/E ratio.

**Calculator Steps:**
- N/A

---

## EQU-F004: Forward P/E Ratio

**Formula:** P₀/E₁ = (D₁/E₁) / (r - g)

* **Variables:**
  + D₁: The dividend yield in decimal form
  + E₁: The expected earnings per share for the current year
  + r: The risk-free rate of return (usually measured by a government bond with similar maturity to the stock)
  + g: The growth rate of earnings

* **When to Use:**
  + To estimate a company's intrinsic value based on its expected earnings growth and the market's required return
  + When comparing the forward P/E ratio of a company to that of peers or an industry average
  + In situations where historical dividend yields are not available

* **When NOT to Use:**
  + When a company has no earnings history (e.g., startups)
  + When the growth rate is significantly different from past performance
  + When the risk-free rate and expected earnings are unknown or unrepresentative

* **Common Mistakes:**
  + Forgetting to adjust for dividend yield when estimating P/E ratio
  + Incorrectly assuming that a high dividend yield means a low risk
  + Not considering growth rate changes when using historical values to estimate future P/E ratios

---

## EQU-F005: Price-to-Book Ratio (P/B)

**Formula:** P/B = Market Price per Share / Book Value per Share

* Variables:
  - Market Price per Share: The current market price of a single share of the stock.
  - Book Value per Share: The total book value of a single share of the stock, including retained earnings and dividends.

* When to Use:
  - Calculating the P/B ratio can be useful for estimating a company's valuation relative to its underlying assets. It is particularly relevant when analyzing companies in industries where asset values are more easily quantifiable than market capitalization.

* When NOT to Use:
  - The P/B ratio should not be used as the sole basis for determining investment decisions, especially in a liquid market or during times of high volatility. Additionally, it may not accurately reflect the value of intangible assets such as brand equity.

* Common Mistakes:
  - Misinterpretation of the formula: Candidates often mistakenly assume that the P/B ratio is always lower than 1, which is incorrect. A higher ratio indicates a more undervalued stock relative to its book value.
  - Failure to consider market fluctuations: The ratio may fluctuate significantly based on changes in the market price and book value of the shares. This can lead to inaccurate conclusions if not taken into account.

* Calculator Steps:
  N/A

---

## EQU-F006: Enterprise Value

**Formula:** EV = Market Cap + Market Value of Preferred + Market Value of Debt - Cash and Equivalents

* **Variables:** 
  * EV (Enterprise Value)
  * Market Cap (Market Capitalization)
  * MV P (Market Value of Preferred)
  * MV D (Market Value of Debt)
  * C&E (Cash and Equivalents)

* **When to Use:**
  * To calculate the total value of a company, including its liquid assets
  * When valuing a company with preferred stock or debt
  * In situations where cash and equivalents are significant contributors to a company's overall value

* **When NOT to Use:**
  * When calculating intrinsic value or expected future cash flows
  * When comparing the market value of different types of debt (e.g. senior vs junior debt)
  * When assessing a company's capital structure in isolation from its overall financials

* **Common Mistakes:**
  * Forgetting to consider the tax implications of issuing new debt
  * Incorrectly accounting for the difference between face value and market value of preferred stock or debt
  * Failing to recognize that cash and equivalents may not always be immediately liquid

* **Calculator Steps:**
  * N/A

---

## EQU-F007: EV/EBITDA

**Formula:** EV/EBITDA = Enterprise Value / EBITDA

* **Variables:** 
  - EV (Enterprise Value)
  - EBITDA (Earnings Before Interest, Taxes, Depreciation, and Amortization)

* **When to Use:**
  When calculating Enterprise Value for a company and needing to compare it to the profit generated by the company's operations.

* **When NOT to Use:**
  When evaluating the overall profitability of a company over time, as EV/EBITDA does not consider other factors that can impact profitability such as debt or cash flow.

* **Common Mistakes:**
  - Failing to account for the impact of interest expenses on EBITDA
  - Not considering the tax implications of depreciation and amortization

* **Calculator Steps:** 
  N/A

---

## EQU-F008: Preferred Stock Valuation

**Formula:** V₀ = D / r

* **Variables:** 
  - D: Dividend yield of the preferred stock
  - r: Current market risk-free rate (discount rate)

* **When to Use:** 
  Use this formula when you need to calculate the present value of a perpetual, fixed-coupon dividend-paying preferred stock. This is typically done in situations where the company issuing the preferred stock has an excellent credit rating and there are no restrictions on dividends.

* **When NOT to Use:**
  Do not use this formula for stocks that pay variable or floating-rate coupons, or when calculating present values for different classes of preferred stock with varying characteristics (e.g., multiple dividend payments per year).

* **Common Mistakes:** 
  Candidates often incorrectly assume that the risk-free rate is constant over time. Another common error is failing to consider other factors like inflation or the effects of changes in market conditions on the risk-free rate.

* **Calculator Steps:**
  N/A

---

## EQU-F009: Two-Stage DDM

**Formula:** V₀ = Σ Dₜ/(1+r)^t (high growth stage) + V_n/(1+r)^n (terminal value)

**Variables:**
- `V₀`: initial investment
- `Dₜ`: dividend per share in the high growth stage
- `r`: discount rate (cost of capital)
- `t`: time period in years for each stage
- `V_n`: terminal value
- `n`: number of years in the terminal growth phase

**When to Use:**
- When estimating the present value of dividends from a company with a two-stage dividend discount model, where one stage has high growth and another stage is characterized by stable or declining growth.

**When NOT to Use:**
- When estimating the present value of dividends from a company with a single-stage dividend discount model.
- When analyzing companies that do not pay consistent dividends.
- When forecasting future dividend payments if the actual payout pattern is unknown.

**Common Mistakes:**
- Incorrectly assuming the terminal growth rate is constant over time, when in fact it may change.
- Ignoring non-deductible expenses when calculating the cost of capital.
- Not considering the impact of inflation on the terminal value.

**Calculator Steps:**
N/A

---

## EQU-F010: Margin Call Price

**Formula:** P_call = P₀ × (1 - Initial Margin) / (1 - Maintenance Margin)

**Variables:**
- `P_call`: The price at which a margin call is triggered
- `P₀`: The initial purchase price of the underlying asset
- `Initial Margin`: The percentage of the purchase price funded by the investor's equity (expressed as a decimal)
- `Maintenance Margin`: The minimum equity percentage required to keep the position open without a margin call (expressed as a decimal)

**When to Use:**
- When determining the stock price below which a long margin investor will receive a margin call.
- When solving for leverage limits on long positions.

**When NOT to Use:**
- When dealing with short margin positions (use P_call = P₀ × (1 + Initial Margin) / (1 + Maintenance Margin) instead).

**Common Mistakes:**
- Mixing up the position of Initial Margin and Maintenance Margin. Remember, Initial Margin is always larger than Maintenance Margin, so the numerator (1 - Initial Margin) is smaller than the denominator (1 - Maintenance Margin), making P_call less than P₀.
- Forgetting to convert percentages to decimals before calculating.

**Calculator Steps:**
- Calculate numerator: 1 [-] Initial Margin [=]
- Store in memory: [STO] 1
- Calculate denominator: 1 [-] Maintenance Margin [=]
- Store in memory: [STO] 2
- Divide numerator by denominator: [RCL] 1 [/] [RCL] 2 [=]
- Multiply by P₀: [x] P₀ [=]


## EQU-F011: Price-Weighted Index

**Formula:** Index Value = Σ Pᵢ / Divisor

**Variables:**
- Index Value (IV): The calculated value of the price-weighted index.
- Pᵢ: The price at which a particular security is traded.
- Divisor (D): A constant used to normalize the weighted sum.

**When to Use:**
- When calculating a price-weighted index, where you want to determine the overall market average return based on individual security prices.

**When NOT to Use:**
- In situations where you need to calculate an equal-weighted index or a modified price-weighted index that takes into account dividends or other non-monetary factors.

**Common Mistakes:**
- Forgetting to specify the divisor constant, which can lead to incorrect calculations if not properly set.
- Not accounting for changes in divisor value over time, such as when there are no trades or splits.

**Calculator Steps:**
N/A

---

## EQU-F012: Market Cap-Weighted Index

**Formula:** Index Value = Σ(Pᵢ × Qᵢ) / Divisor

**Variables:**
- Pᵢ: Market price of stock i at a given time
- Qᵢ: Weight of each stock in the index (usually market capitalization)
- Divisor: A divisor to adjust for the number of stocks in the index
- Σ: Sigma, representing the sum of the weighted products

**When to Use:**
- Calculate a market cap-weighted index when you want to track the performance of a portfolio or index that is composed of a group of stocks with varying market capitalizations.

**When NOT to Use:**
- Do not use this formula when calculating individual stock prices, as it requires knowledge of multiple stock prices and their corresponding weights.

**Common Mistakes:**
- Failing to specify the divisor accurately, leading to incorrect results.
- Misinterpreting the index value as representing an actual price change, rather than a percentage return.
- Incorrectly applying the formula without proper understanding of market capitalization and its implications on stock weights.

**Calculator Steps:**
- Use Σ (Sum) key
- Enter each Pᵢ (Market price) and corresponding Qᵢ (Weight)
- Multiply Pᵢ and Qᵢ, then sum using Σ key
- Divide result by Divisor

---

## EQU-F013: Total Return (Index)

**Formula:** Total Return = (P₁ - P₀ + Dividends) / P₀

* **Variables:** 
  * P0: The initial price of the security
  * P1: The current price of the security
  * Dividends: The dividends received by the security
* **When to Use:** 
  * When calculating the total return on an investment, such as a stock or mutual fund.
* **When NOT to Use:** 
  * When the formula is not applicable due to no dividend payments (e.g., bonds).
* **Common Mistakes:**
  * Forgetting to include dividends in the numerator.
  * Incorrectly calculating P0 versus P1 (i.e., using P1 as the initial price instead of P0).
* **Calculator Steps:** 
  N/A

---

## EQU-F014: ROE

**Formula:** ROE = Net Income / Shareholders' Equity

* Variables:
  - Net Income
  - Shareholders' Equity

* When to Use:
  - To calculate a company's return on equity (ROE) when you have net income and shareholders' equity.

* When NOT to Use:
  - When you don't have both net income and shareholders' equity. 

* Common Mistakes:
  - Rounding or truncating values without considering the impact on the result.
  - Failing to ensure that all numbers are in the same units (e.g., calculating with dollars, but then dividing by thousands).

* Calculator Steps:
  - N/A

---

## EQU-F015: Price-to-Sales (P/S)

**Formula:** P/S = Market Price per Share / Sales per Share

**Variables:**
- Market Price per Share (Market Price): The current market price of one share of the stock
- Sales per Share (Sales): The total sales revenue generated by one share of the stock over a given period

**When to Use:**
- To estimate the intrinsic value of a company based on its historical sales performance
- When a company's financial statements do not provide sufficient information about its cash flows or earnings
- As an alternative to the Price-to-Earnings (P/E) ratio, when the earnings data is not available

**When NOT to Use:**
- When the company has a high level of debt or leverage, as this can significantly impact sales revenue
- In industries with rapidly changing sales trends or business models
- When the market price per share is highly volatile or sensitive to short-term events

**Common Mistakes:**
- Assuming that all shares sold are actual cash received by the company (i.e., excluding dividends, interest, and other non-cash items)
- Ignoring the fact that sales revenue can be affected by external factors such as seasonality, economic downturns, or regulatory changes
- Failing to adjust for differences in accounting methods or currencies between companies

**Calculator Steps:**
N/A

---

## EQU-F016: Price-to-Cash Flow (P/CF)

**Formula:** P/CF = Market Price per Share / Cash Flow per Share

**Variables:**
- `Market Price per Share`: The current market price of one share of common stock.
- `Cash Flow per Share`: Net cash flow from operations divided by the number of shares outstanding. (Often approximated as Net Income + Depreciation & Amortization per share).

**When to Use:**
- When valuing companies with negative earnings or highly volatile earnings where P/E cannot be applied.
- When cash flow is considered a more stable and reliable indicator of value than reported net income (which is subject to accounting adjustments).

**When NOT to Use:**
- When comparing companies with vastly different capital structures (as CFO is after interest expense).
- When free cash flow (FCFF or FCFE) is preferred to account for capital expenditure requirements.

**Common Mistakes:**
- Confusing Cash Flow (CFO) with Free Cash Flow (FCF) or EBITDA.
- Forgetting to use consistent per-share figures in both numerator and denominator.

**Calculator Steps:**
- Price [/] Cash Flow per Share [=]


# FIXED INCOME FORMULAS

## FIX-F001: Bond Price

**Formula:** P = Σ C/(1+r)^t + FV/(1+r)^n

* **Variables:** 
  - r: The discount rate (interest rate) of the bond
  - t: Time in years for each cash flow
  - n: Number of periods until maturity
  - P: Present value of the bond
  - C: Annual coupon payment
  - FV: Face value or par value of the bond

* **When to Use:** 
  Apply when calculating the present value of a bond, including all periodic cash flows and the face value.

* **When NOT to Use:** 
  Do not use if the bond has a call feature or put option, as these affect the calculation of the bond price.

* **Common Mistakes:**
  - Incorrectly calculating the interest rate (r)
  - Forgetting to include all periodic cash flows
  - Not accounting for time value of money correctly

* **Calculator Steps:** 
  N/A

---

## FIX-F002: Current Yield

**Formula:** Current Yield = Annual Coupon / Bond Price

* **Variables:**
  - Annual Coupon (Annual interest payment from the bond)
  - Bond Price (The current market value of the bond)
  
* **When to Use:**
  - When calculating the current yield on a bond with an existing annual coupon, i.e., you have the bond's face value and know its annual interest rate but need the current price.
  
* **When NOT to Use:**
  - When there is no outstanding principal balance on the bond (i.e., it's a zero-coupon bond) or when calculating yield on a convertible security.
  
* **Common Mistakes:**
  - Incorrectly applying the formula for bonds with multiple coupon payments per year; this can lead to incorrect calculations.
  
* **Calculator Steps:**
  - N/A

---

## FIX-F003: Accrued Interest

**Formula:** AI = (PMT / m) × (Days since last coupon / Days in coupon period)

**Variables:**
- `PMT`: The annual coupon payment.
- `m`: The number of coupon payments per year (e.g., m = 2 for semi-annual bonds).
- `Days since last coupon`: The number of days from the last coupon payment date to the settlement date.
- `Days in coupon period`: The total number of days in the coupon payment period (e.g., 180 days under 30/360, or actual days under Actual/Actual).

**When to Use:**
- When calculating the interest that has accumulated on a bond since the last interest payment date up to the trade settlement date.
- Needed to reconcile clean and dirty bond prices.

**When NOT to Use:**
- For zero-coupon bonds.
- When trading exactly on a coupon payment date (accrued interest is zero).

**Common Mistakes:**
- Using the annual coupon (PMT) directly without dividing by the compounding frequency (m).
- Using the wrong day-count convention (e.g., 30/360 for government bonds, or Actual/Actual for corporates).

**Calculator Steps:**
- Calculate periodic coupon: PMT [/] m [=] [STO] 1
- Calculate day fraction: Days since last [/] Days in period [=]
- Multiply by periodic coupon: [x] [RCL] 1 [=]


## FIX-F004: Full (Dirty) Price

**Formula:** Full Price = Flat Price + Accrued Interest

* **Variables:** 
  - Flat Price: The price of an asset without considering interest charges or fees.
  - Accrued Interest: The total amount of interest that has accrued on an investment since its inception.

* **When to Use:** 
  - When calculating the full price of an investment that has been held for a period of time and has accumulated interest.

* **When NOT to Use:** 
  - When pricing a new investment or when the interest rate is constant over time, as this formula assumes compounding interest.

* **Common Mistakes:** 
  - Forgetting to include accrued interest on existing investments.
  - Assuming flat price increases linearly with time (when in reality it may be subject to fees or other market fluctuations).

* **Calculator Steps:** 
  - Use the "+" key for addition
  - Use the "*" and "/" keys to calculate the interest rate if necessary

---

## FIX-F005: Macaulay Duration

**Formula:** MacDur = Σ[t × PV(CFₜ)] / Σ PV(CFₜ)

* **Variables:**
  - t: Time in years
  - PV(CFₜ): Present value of a cash flow at time t
  - Σ: Sigma, indicating summation
  - MacDur: Macaulay duration

* **When to Use:**
  - Calculate the Macaulay duration for a series of cash flows, especially when analyzing bond yields and interest rate risk.

* **When NOT to Use:**
  - When dealing with fixed income securities that do not have a series of periodic cash flows; use other methods such as coupon yield or credit spread.
  - When the cash flows are irregularly spaced; the Macaulay duration only considers evenly spaced cash flows.

* **Common Mistakes:**
  - Forgetting to consider all periods in the summation; ensure that all relevant cash flows are included.
  - Incorrectly applying the formula, especially when dealing with time-varying cash flows or non- periodic payments.

---

## FIX-F006: Modified Duration

**Formula:** ModDur = MacDur / (1 + r)

* Variables:
  * ModDur: Modified Duration
  * MacDur: Modified Accumulated Value
  * r: Interest Rate
* When to Use:
  * Calculate the modified duration of a bond when you need to understand its interest rate sensitivity.
* When NOT to Use:
  * Apply it when calculating the yield to maturity (YTM) or coupon payment amount, as these calculations are distinct from modified duration.
* Common Mistakes:
  * Incorrectly substituting the yields for MacDur and r in the formula.
  * Forgetting to discount cash flows at their respective macdur values
* Calculator Steps:
  - Use a financial calculator with a BOND function

---

## FIX-F007: Effective Duration

**Formula:** EffDur = (P_down - P_up) / (2 × P₀ × Δy)

* Variables:
  * P_down: The price of a zero-coupon bond at the end of the period
  * P_up: The price of a zero-coupon bond at the beginning of the period
  * P₀: The price of a zero-coupon bond at time 0 (the current market value)
  * Δy: The time between two periods

* When to Use:
  * When calculating the effective duration of a portfolio or a single security with multiple coupon payments and different maturities.

* When NOT to Use:
  * When dealing with non-zero-coupon bonds, such as bonds with coupons. Effective duration is typically used for zero-coupon bonds.
  * When time is not measured in years, but rather in some other unit (e.g., months).

* Common Mistakes:
  * Incorrectly assuming that the time period Δy is constant across all periods, when it may be variable or non-linear.
  * Not accounting for compounding effects on coupon payments.

* Calculator Steps:
  N/A

---

## FIX-F008: Approximate Convexity

**Formula:** Conv = (P_down + P_up - 2P₀) / (P₀ × (Δy)²)

* **Variables:** 
  - P₀: The zero coupon price of a bond
  - P_down: The down curve price of an option portfolio (i.e., the total value of all options that would sell for less than their face value if exercised)
  - P_up: The up curve price of an option portfolio (i.e., the total value of all options that would sell for more than their face value if exercised)
  - Δy: The annual yield on the risk-free rate

* **When to Use:** 
  When analyzing the convexity of a bond, such as when calculating the price of a bond with a complex structure or non-standard instrument.

* **When NOT to Use:** 
  When calculating the convexity of an individual bond; it is more relevant for option portfolios. It can also be used in other financial applications where the relationship between yield and time is not linear.

* **Common Mistakes:** 
  Calculating the wrong value of Δy, or using incorrect P_down or P_up values, which could lead to incorrect results. 

* **Calculator Steps:**
  N/A

---

## FIX-F009: Price Change (Duration + Convexity)

**Formula:** %ΔP ≈ -ModDur × Δy + ½ × Conv × (Δy)²

* Variables:
  * ModDur: Modified duration of an investment
  * Δy: Yield curve slope (in decimal form)
  * Conv: Convexity of the yield curve
  * %ΔP: Approximate price change for a given duration and convexity

* When to Use:
  * To estimate the approximate price change of an investment over a specific duration, considering both time value of money effects and yield curve curvature.

* When NOT to Use:
  * In situations where other factors like market volatility, interest rate levels, or specific security characteristics have significant impacts on prices.
  * For precise calculations requiring detailed financial data beyond yield curve slope and convexity.

* Common Mistakes:
  * Incorrectly applying the formula for investments with short durations or those far removed from the yield curve's curvature.
  * Misinterpreting yield curve slope as a percentage (it should be in decimal form).
  * Overlooking the interaction between duration, convexity, and yield curve changes on price movements.

* Calculator Steps:
  N/A

---

## FIX-F010: Money Duration

**Formula:** MoneyDur = ModDur × Price (per 100 par value)

* Variables:
  - ModDur: Modified duration of an investment, calculated by adjusting for compounding
  - Price: The price per $100 face value (par value) of a security
* When to Use:
  - To calculate the money duration of a security at a specific price point
  - When comparing the duration of different securities or periods with varying interest rates
* When NOT to Use:
  - When calculating duration for a fixed income security that does not have a variable interest rate (e.g., a bond with a fixed coupon)
  - When the price per $100 par value is not available or known (in this case, the formula would require additional information)
* Common Mistakes:
  - Misinterpreting modified duration as a direct measure of price sensitivity
  - Not accounting for compounding in interest rate changes when calculating ModDur
* Calculator Steps:
  N/A

---

## FIX-F011: PVBP (Price Value of a Basis Point)

**Formula:** PVBP = (P_down - P_up) / 2

* Variables:
  * P_down: The price at which you expect to sell an option (usually a downward movement in the market)
  * P_up: The price at which you expect to buy an option (usually an upward movement in the market)

* When to Use:
  * You should use this formula when you are expecting a basis point move (1/100 of 1%) change in the market.

* When NOT to Use:
  * This formula should not be used for scenarios involving a large percentage move, where the effect of the option on the price is more significant than a single basis point.

* Common Mistakes:
  * Calculating PVBP incorrectly by using P_down or P_up as if they were equal (when in fact, the difference between them represents a change of one basis point).

* Calculator Steps:
  * N/A

---

## FIX-F012: Implied Forward Rate

**Formula:** (1+z_A)^A × (1+IFR)^{B-A} = (1+z_B)^B

* Variables:
  * z_A: The forward rate for asset A
  * z_B: The forward rate for asset B
  * A: The time period (in years) for which we want to calculate the implied forward rate for asset A
  * B: The time period (in years) for which we want to calculate the implied forward rate for asset B

* When to Use:
  * Use this formula when you need to find an implied forward rate based on two given forward rates with different time periods.

* When NOT to Use:
  * Do not use this formula if the time periods for the two assets are equal or if one of the forward rates is already known and the other needs to be calculated.

* Common Mistakes:
  * Incorrectly applying the formula when the time periods (A and B) have different units (e.g., days instead of years).
  * Not checking whether the given forward rates can be used to calculate an implied forward rate, or if they are actually the actual forward rates.

* Calculator Steps:
  N/A

---

## FIX-F013: G-Spread

**Formula:** G-Spread = Bond YTM - Benchmark Government Bond YTM

* Variables:
  * G-Spread: The spread between a bond's yield-to-maturity (YTM) and a benchmark government bond YTM
  * Bond YTM: The yield-to-maturity of the bond in question
  * Benchmark Government Bond YTM: The yield-to-maturity of a benchmark government bond

* When to Use:
  * To calculate the yield spread of a non-governmental corporate bond relative to a benchmark government bond

* When NOT to Use:
  * When comparing the yield spread of different types of bonds (e.g. investment-grade vs high-yield)
  * When calculating the yield spread for a bond that is not trading at par
  * When using this formula as part of an overall credit assessment or valuation model

* Common Mistakes:
  * Failing to use a comparable government bond with similar maturity and credit characteristics
  * Not accounting for any differences in credit spreads due to market conditions or other factors
  * Rounding intermediate calculations too aggressively, leading to inaccurate results

* Calculator Steps:
  N/A

---

## FIX-F014: Z-Spread

**Formula:** P = Σ C/(1+z_t + Z)^t + FV/(1+z_n + Z)^n

* Variables:
  - P: Present value of an annuity due
  - C: Cash flow per period
  - z_t: Interest rate for a time period t
  - Z: Z-spread (the difference between the yield on a fixed-income security and the risk-free rate)
  - FV: Future value
  - n: Number of periods

* When to Use:
  - To calculate the present value of an annuity due with compound interest, including any accrued interest.
  - When you want to determine the initial price of a loan or other financial instrument that includes compound interest.

* When NOT to Use:
  - When calculating the future value of a single payment; use the FV formula instead.

* Common Mistakes:
  - Incorrectly applying the Z-spread, which can lead to inaccurate calculations.
  - Forgetting to account for accrued interest in the present value calculation.
  - Not correctly handling the annuity due component.

* Calculator Steps:
  - N/A

---

## FIX-F015: Option-Adjusted Spread (OAS)

**Formula:** OAS = Z-Spread - Option Value

* **Variables:** 
  * Z-Spread: The difference between the yield to maturity (YTM) on a bond and the risk-free rate
  * Option Value: The present value of all options embedded in the bond
* **When to Use:** 
  When calculating the Option-Adjusted Spread (OAS), use this formula when you need to adjust the yield of a bond for embedded options, such as call or put options.
* **When NOT to Use:** 
  Do not apply this formula when calculating yields on bonds without options, or when using other types of securities that do not have embedded options.
* **Common Mistakes:** 
  Common errors candidates make include: incorrectly assuming the option value is zero for bonds with no embedded options, failing to account for changes in time until maturity when calculating option values, and misinterpreting the meaning of Z-Spread in relation to the bond's cash flows.
* **Calculator Steps:** 
  N/A

---

## FIX-F016: Discount Rate (Money Market)

**Formula:** DR = (FV - P)/FV × (360/n)

* **Variables:**
  - FV: Future Value
  - P: Present Value
  - n: Number of times interest is compounded per year

* **When to Use:**
  - When calculating the discount rate for a money market investment, or when determining the price at which an asset should be sold to yield a specific future cash flow.

* **When NOT to Use:**
  - When calculating interest earned on an investment, as it is based on the present value of future cash flows rather than the amount accumulated in the account.

* **Common Mistakes:**
  - Forgetting to adjust the number of times interest is compounded per year (n) for non-annual compounding.
  - Not considering that the formula calculates the discount rate, not the interest rate.

* **Calculator Steps:**
  - Use 4 ^{+} -key to raise 360
  - Divide FV by P using ^/÷ keys 
  - Multiply result by [result from previous step]/(360)

---

## FIX-F017: Add-On Rate (Money Market)

**Formula:** AOR = (FV - P)/P × (360/n)

* Variables:
  * AOR: The add-on rate
  * FV: The future value of an investment
  * P: The present value of an investment
  * n: The number of times interest is compounded per year

* When to Use:
  * Calculate the add-on rate when you need to find the extra amount earned on an investment over a period of time, taking into account compounding frequency.

* When NOT to Use:
  * Do not use this formula for non-money market investments or if compounding frequency is unknown.

* Common Mistakes:
  * Incorrectly applying compounding frequency (n) as a decimal instead of a whole number.
  * Forgetting to consider the case where n is zero (compounded annually).

* Calculator Steps:
  * Use N/A

---

## FIX-F018: Bond Equivalent Yield (BEY)

**Formula:** BEY = [(FV - P)/P] × (365/n)

* **Variables:** 
  * FV: Future Value of the bond
  * P: Present Value of the bond
  * n: Number of times interest is compounded per year

* **When to Use:** 
  When calculating the yield on a fixed-income security, such as a bond.

* **When NOT to Use:** 
  When the coupon payments are not periodic (e.g. semi-annually), and the frequency needs to be adjusted in the formula.

* **Common Mistakes:** 
  - Assuming that the interest rate is already compounded, when it may or may not be.
  - Not considering the compounding period correctly.
  - Using an incorrect value for n when the coupon payments are not periodic.

---

## FIX-F019: Single Monthly Mortality (SMM)

**Formula:** SMM = 1 - (1 - CPR)^(1/12)

* Variables:
  * CPR: Continuous Probability of Survival (a decimal value representing the probability of surviving for one month)
 
* When to Use:
  * To calculate the single monthly mortality rate from a given continuous probability of survival.

* When NOT to Use:
  * When you are given an annualized mortality rate, as CPR is based on monthly survival rates.

* Common Mistakes:
  * Misinterpreting CPR as a percentage value instead of a decimal.
  * Not correctly handling the power of -1 and the exponentiation operation (the ^ symbol).
 
* Calculator Steps:
  N/A

---

## FIX-F020: Conditional Prepayment Rate (CPR)

**Formula:** CPR = 1 - (1 - SMM)^12

* **Variables:** 
  * CPR: Conditional Prepayment Rate
  * SMM: Scheduled Monthly Mortgage Payment
  * n: Number of years (constant in this formula)

* **When to Use:** 
  * Apply when calculating the potential prepayments on an amortizing loan, where the monthly payments vary over time.

* **When NOT to Use:** 
  * Do not use if the interest rate remains constant throughout the life of the loan, as this would result in a fixed monthly payment and no change in CPR.

* **Common Mistakes:** 
  * Ignoring the importance of SMM, which is crucial for accurately calculating CPR.
  * Not considering the impact of changes in the scheduled payment amount over time on CPR.

* **Calculator Steps:** 
  N/A

---

## FIX-F021: Yield to Call (YTC)

**Formula:** Same as bond pricing formula, but using call price as FV and time to call as n

* **Variables:**
  * P0: Present value of the bond
  * FV0: Face value (or call price) of the bond
  * C: Call price of the bond
  * r: Risk-free rate
  * t: Time to maturity of the bond in years
  * n: Number of periods until expiration (time to call)
  * K: Strike price (not applicable for YTC formula)

* **When to Use:**
  * To calculate the yield to call (YTC) of a callable bond, when the market price is lower than the call price.

* **When NOT to Use:**
  * When the market price is higher than the call price.
  * When calculating yields on fixed income securities without any call options.

* **Common Mistakes:**
  * Not using the correct time value of money formula, which can result in incorrect calculations.
  * Forgetting to adjust for the call option's strike price, if applicable (in this case K is not used).
 
* **Calculator Steps:**
  * N/A

---

## FIX-F022: Yield to Worst (YTW)

**Formula:** Lowest of YTM, YTC (all call dates), YTP (all put dates)

* Variables:
  * YTM (Year-to-Maturity)
  * YTC (Total Cumulative Return on all Call dates)
  * YTP (Total Price Paid on all Put Dates)
  * Worst return ( Lowest of YTM, YTC, and YTP)

* When to Use:
  * Calculate the Yield to Worst when calculating the overall return of an option position that includes both calls and puts.

* When NOT to Use:
  * Do not use this formula for calculating the cost basis or intrinsic value of a single call or put option.

* Common Mistakes:
  * Candidates often confuse YTM with YTW, thinking they are interchangeable terms.
  * Failing to account for all dates (call and put options) when using this formula can lead to incorrect results.

* Calculator Steps:
  * N/A

---

# DERIVATIVES FORMULAS

## DER-F001: Forward Price (No Cash Flows)

**Formula:** F₀(T) = S₀ × (1 + r)^T

**Continuous:** F₀(T) = S₀ × e^(rT)

**Variables:**
- F₀(T) = Forward price at time 0 for maturity T
- S₀ = Spot price of the underlying asset at time 0
- r = Risk-free rate
- T = Time to maturity in years

**When to Use:** Pricing a forward contract on an asset that has no cash flows (e.g., non-dividend paying stock)
**When NOT to Use:** If the underlying pays dividends or has a known yield/income
**Common Mistakes:** Forgetting to annualize T (e.g., using 30 instead of 30/365 for a 30-day contract)
**Calculator Steps:** Use [y^x] for compounding. S₀ × (1+r) [y^x] T [=]

---

## DER-F002: Forward Price (With Known Income)

**Formula:** F₀(T) = [S₀ - PV(I)] × (1 + r)^T

**Variables:**
- PV(I) = Present value of known cash flows/income during the forward term
- Other variables same as DER-F001

**When to Use:** Asset pays known discrete cash flows (e.g., bond paying coupons, stock with fixed dividends)
**When NOT to Use:** When yield is a continuous percentage (use known yield formula)
**Common Mistakes:** Subtracting the future value of income instead of present value from S₀
**Calculator Steps:** First calculate PV of income, subtract from S₀, then multiply by (1+r) [y^x] T

---

## DER-F003: Forward Price (With Known Yield)

**Formula:** F₀(T) = S₀ × (1 + r - q)^T

**Variables:**
- q = Continuous dividend yield or income yield

**When to Use:** Asset pays a continuous yield (e.g., stock index, foreign currency)
**When NOT to Use:** Discrete known cash flows
**Common Mistakes:** Adding q instead of subtracting it from r
**Calculator Steps:** S₀ × (1 + r - q) [y^x] T [=]

---

## DER-F004: Forward Value (During Life)

**Formula:** V_t = (F_t - F₀) / (1 + r)^(T-t)

**Variables:**
- V_t = Value of the forward contract at time t (for the long position)
- F_t = Current forward price at time t for maturity T
- F₀ = Original forward price

**When to Use:** Valuing an existing forward contract before maturity (mark-to-market)
**When NOT to Use:** To find the forward *price* (this finds *value*)
**Common Mistakes:** Confusing price (F) and value (V). At initiation, V=0 but F>0.
**Calculator Steps:** (F_t - F₀) / (1+r) [y^x] (T-t) [=]

---

## DER-F005: Currency Forward Price

**Formula:** F = S × [(1 + r_d) / (1 + r_f)]^T

**Variables:**
- r_d = Domestic interest rate (price currency)
- r_f = Foreign interest rate (base currency)

**When to Use:** Covered interest rate parity for currency forwards
**When NOT to Use:** Uncovered parity scenarios
**Common Mistakes:** Flipping domestic and foreign rates. Rule: Price/Base -> (1+r_price)/(1+r_base).
**Calculator Steps:** Simple arithmetic with [y^x]

---

## DER-F006: Put-Call Parity (European)

**Formula:** c₀ + X/(1+r)^T = p₀ + S₀

**Interpretation:** Fiduciary call = Protective put

**Variables:**
- c₀ = Call option price
- p₀ = Put option price
- X = Strike price
- S₀ = Spot price

**When to Use:** Pricing European options, arbitrage identification
**When NOT to Use:** American options (due to early exercise premium)
**Common Mistakes:** Using FV of S₀ instead of X. Fiduciary call = c + PV(X), Protective put = S + p.
**Calculator Steps:** PV of X: X / (1+r) [y^x] T

---

## DER-F007: Put-Call-Forward Parity

**Formula:** c₀ + X/(1+r)^T = p₀ + F₀(T)/(1+r)^T

**Variables:**
- c₀ = Call option price
- p₀ = Put option price
- X = Strike price
- F₀(T) = Forward price
- r = Risk-free rate

**When to Use:** Arbitrage pricing involving forwards and options
**When NOT to Use:** When spot price is available and preferred (use standard put-call parity)
**Common Mistakes:** Using S₀ instead of PV(F₀)
**Calculator Steps:** Discount X and F₀(T) to present value using [y^x]

---

## DER-F008: Binomial Model — Up/Down Factors

**Formula:** u = S_up/S₀, d = S_down/S₀

**Variables:**
- u = Up factor multiplier
- d = Down factor multiplier
- S_up = Spot price in up state
- S_down = Spot price in down state

**When to Use:** Constructing binomial trees for option valuation
**When NOT to Use:** Black-Scholes continuous models
**Common Mistakes:** Forgetting that d = 1/u in a recombining tree
**Calculator Steps:** S_up / S₀ [=]

---

## DER-F009: Risk-Neutral Probability

**Formula:** π = (1 + r - d) / (u - d)

**Variables:**
- π = Risk-neutral probability of an up move
- r = Risk-free rate per period
- u, d = Up and down factors

**When to Use:** Calculating expected payoffs in a binomial option pricing model
**When NOT to Use:** Real-world probability forecasting
**Common Mistakes:** Using actual expected return of the stock instead of the risk-free rate
**Calculator Steps:** (1 + r - d) / (u - d)

---

## DER-F010: Option Value (One-Period Binomial)

**Formula:** c₀ = [π × c_up + (1-π) × c_down] / (1+r)

**Variables:**
- c₀ = Option value today
- π = Risk-neutral probability
- c_up, c_down = Option payoffs in up/down states

**When to Use:** Pricing options using a one-period binomial tree
**When NOT to Use:** American options with early exercise (requires checking exercise value at each node)
**Common Mistakes:** Forgetting to discount the expected payoff by (1+r)
**Calculator Steps:** Find expected payoff: π × c_up + (1-π) × c_down. Then divide by (1+r)

---

## DER-F011: Hedge Ratio

**Formula:** h = (c_up - c_down) / (S_up - S_down)

**Variables:**
- h = Hedge ratio (Delta)
- c_up, c_down = Call option values in up/down states
- S_up, S_down = Stock prices in up/down states

**When to Use:** Determining the number of shares to buy/sell to perfectly hedge an option position
**When NOT to Use:** Delta hedging in continuous time (use Black-Scholes Delta)
**Common Mistakes:** Reversing the numerator and denominator
**Calculator Steps:** Δc / ΔS

---

## DER-F012: Swap Fixed Rate

**Formula:** r_fix = (1 - PV factor_n) / Σ PV factors

**Variables:**
- r_fix = Swap fixed rate
- PV factor_n = Present value of $1 received at maturity
- Σ PV factors = Sum of present value factors for all payment dates

**When to Use:** Pricing a plain vanilla interest rate swap at initiation
**When NOT to Use:** Currency swaps (different pricing mechanics)
**Common Mistakes:** Forgetting that the fixed rate is per period, and must be annualized if asked for the annual rate
**Calculator Steps:** 1 - PV_n. Divide by sum of PVs.

---

# ALTERNATIVE INVESTMENTS FORMULAS

## ALT-F001: Management Fee

**Formula:** Management Fee = Fee Rate × AUM (beginning or ending)

**Variables:**
- AUM = Assets Under Management
- Fee Rate = Annual percentage (e.g., 2%)

**When to Use:** Calculating base fees for hedge funds/PE
**When NOT to Use:** Incentive/performance fees
**Common Mistakes:** Applying fee to committed capital instead of invested capital/AUM if terms specify otherwise
**Calculator Steps:** AUM × Fee Rate

---

## ALT-F002: Incentive Fee (Basic)

**Formula:** Incentive Fee = Fee Rate × (Ending Value - Beginning Value - Management Fees)

**Variables:**
- Ending Value = Portfolio value at end of period
- Beginning Value = Portfolio value at start
- Management Fees = Base fees deducted

**When to Use:** Standard "2 and 20" fee structures with return net of management fee
**When NOT to Use:** When a hurdle rate or high-water mark applies
**Common Mistakes:** Calculating incentive fee on gross return instead of net of management fee (if specified as net)
**Calculator Steps:** (Ending - Beginning - Mgmt Fee) × Incentive Rate

---

## ALT-F003: Incentive Fee with Hurdle Rate

**Formula:** Incentive Fee = Fee Rate × max(0, Profit above hurdle)

**Variables:**
- Hurdle Rate = Minimum return required before incentive fees are paid

**When to Use:** Calculating hedge fund / PE fees with a hard or soft hurdle
**When NOT to Use:** When no hurdle exists
**Common Mistakes:** Soft hurdle (fee applied to ALL profits if hurdle cleared) vs Hard hurdle (fee applied ONLY to profits above hurdle)
**Calculator Steps:** Max(0, Return - Hurdle) × Fee Rate

---

## ALT-F004: Incentive Fee with High-Water Mark

**Formula:** Only earned on profits above previous highest AUM

**Variables:**
- HWM = High-Water Mark (highest past value net of fees)

**When to Use:** Calculating incentive fees when funds must recover past losses first
**When NOT to Use:** Base management fee calculations
**Common Mistakes:** Applying fee to total profit instead of (Ending Value - HWM)
**Calculator Steps:** Max(0, Ending Value - HWM) × Fee Rate

---

## ALT-F005: MOIC (Multiple on Invested Capital)

**Formula:** MOIC = (Realized Value + Unrealized Value) / Total Invested Capital

**Variables:**
- Realized Value = Cash distributed to investors
- Unrealized Value = Value of remaining holdings
- Total Invested Capital = Called capital

**When to Use:** Evaluating Private Equity fund performance
**When NOT to Use:** When timing of cash flows matters (use IRR instead)
**Common Mistakes:** Excluding unrealized value
**Calculator Steps:** (Realized + Unrealized) / Invested

---

## ALT-F006: Commodity Total Return

**Formula:** Total Return = Spot Return + Roll Yield + Collateral Yield

**Variables:**
- Spot Return = Change in spot price
- Roll Yield = Return from rolling futures contracts
- Collateral Yield = Interest earned on margin

**When to Use:** Decomposing commodity futures index returns
**When NOT to Use:** Physical commodity returns (no roll/collateral yield)
**Common Mistakes:** Assuming spot return equals total return
**Calculator Steps:** Sum the three components

---

## ALT-F007: Roll Yield

**Formula:** Roll Yield = (F_near - F_far) / F_near (for long position)

**Positive in backwardation, negative in contango**

**Variables:**
- F_near = Price of near-term futures contract
- F_far = Price of farther-term contract

**When to Use:** Calculating the yield from maintaining a futures position as contracts expire
**When NOT to Use:** Equities or bonds
**Common Mistakes:** Misinterpreting contango (negative roll yield) vs backwardation (positive roll yield for long)
**Calculator Steps:** (F_near - F_far) / F_near

---

## ALT-F008: Net-of-Fee Return

**Formula:** Net Return = Gross Return - Management Fee - Incentive Fee

**Variables:**
- Gross Return = Return before any fees
- Management Fee = Base fee
- Incentive Fee = Performance fee

**When to Use:** Calculating the actual return passed on to investors
**When NOT to Use:** Gross performance evaluation
**Common Mistakes:** Subtracting incentive fee before checking hurdle/HWM conditions
**Calculator Steps:** Gross - Mgmt - Incentive

---

# PORTFOLIO MANAGEMENT FORMULAS

## PRT-F001: Portfolio Expected Return

**Formula:** E(R_p) = Σ wᵢ × E(Rᵢ)

**Variables:**
- wᵢ: Weight of each asset in the portfolio (0 ≤ wᵢ ≤ 1)
- Rᵢ: Expected return of each individual asset
- Σ: Summation symbol indicating the sum of the weighted returns of all assets in the portfolio

**When to Use:**
- Calculate the expected return of a portfolio when you know the expected returns of its constituent assets and their respective weights.

**When NOT to Use:**
- Use alternative methods, such as CAPM or APT models, when calculating expected returns for specific asset classes like bonds or currencies.
- When the relationship between expected returns is not linear and cannot be represented by a simple weighted average.

**Common Mistakes:**
- Overlooking the fact that Rᵢ should be the expected return of each individual asset, not its realized return.
- Assuming all assets in the portfolio have equal weights when calculating the expected return (when some may have different or variable weights).

**Calculator Steps:**
N/A

---

## PRT-F002: Portfolio Variance (Two Assets)

**Formula:** σ²_p = w₁²σ₁² + w₂²σ₂² + 2w₁w₂Cov(R₁,R₂)

* Variables:
  - `w₁`: Weight of asset 1 in the portfolio (between 0 and 1)
  - `σ₁²`: Variance of asset 1
  - `w₂`: Weight of asset 2 in the portfolio (between 0 and 1)
  - `σ₂²`: Variance of asset 2
  - `Cov(R₁,R₂)`: Covariance between returns of assets 1 and 2

* When to Use:
  - Calculate portfolio variance when analyzing risk associated with a diversified investment portfolio.
  - Determine the expected volatility of a portfolio holding two or more assets.

* When NOT to Use:
  - For portfolios with three or more assets, as the formula assumes only two assets. More complex formulas are required for larger portfolios.
  - When calculating portfolio variance is not relevant (e.g., during initial investment or when asset weights remain constant).

* Common Mistakes:
  - Incorrectly assuming covariance between returns of all pairs of assets in the portfolio instead of just the specific pair used in the formula.
  - Misinterpreting the effect of weights on portfolio variance, such as incorrectly applying a weight that is not within the valid range (0-1).

---

## PRT-F003: Capital Allocation Line (CAL)

**Formula:** E(R_p) = R_f + [(E(R_i) - R_f) / σ_i] × σ_p

**Variables:**
- `E(R_p)`: Expected return of the portfolio (combined risk-free asset and risky portfolio).
- `R_f`: Risk-free rate of return.
- `E(R_i)`: Expected return of the active risky asset/portfolio.
- `σ_i`: Standard deviation of the active risky asset/portfolio.
- `σ_p`: Target standard deviation of the combined portfolio.

**When to Use:**
- When constructing an investment portfolio combining a risk-free asset and a single risky asset or a specific portfolio of risky assets.
- To determine the expected return for a target level of total portfolio risk.

**When NOT to Use:**
- When the risky asset is specifically the optimal Market Portfolio (in that case, use the Capital Market Line (CML) instead).
- When evaluating systematic risk (use the Security Market Line (SML) / CAPM instead).

**Common Mistakes:**
- Using Beta (β) instead of standard deviation (σ) as the risk measure (this is the key difference between CAL/CML and SML).
- Confusing the active portfolio's return and standard deviation with the combined portfolio's target values.

**Calculator Steps:**
- Calculate the slope (Sharpe ratio of risky asset): (E(R_i) - R_f) [/] σ_i [=] [STO] 1
- Multiply by target portfolio risk: [x] σ_p [=]
- Add risk-free rate: [+] R_f [=]


## PRT-F004: Capital Market Line (CML)

**Formula:** E(R_p) = R_f + [(E(R_m) - R_f) / σ_m] × σ_p

* Variables:
  * E(R_p): Expected return on portfolio
  * R_f: Risk-free rate of return
  * E(R_m): Expected return of market
  * σ_m: Standard deviation of market returns
  * σ_p: Standard deviation of portfolio returns

* When to Use:
  * To determine the expected return of a portfolio, given its level of risk and the risk-return trade-off of the capital market.

* When NOT to Use:
  * When there is no available historical data on market returns or when no estimate of expected market return can be made.
  * When the goal is not to determine the expected return of a portfolio but rather another aspect of investment decision-making, such as portfolio optimization.

* Common Mistakes:
  * Incorrectly assuming that σ_p is equal to σ_m, which would result in an incorrect expected return for any portfolio with a standard deviation greater than σ_m.
  * Not considering non-linear effects of standard deviations on the formula or incorrectly applying the calculation.

* Calculator Steps:
  N/A

---

## PRT-F005: CAPM / Security Market Line (SML)

**Formula:** E(R_i) = R_f + β_i × [E(R_m) - R_f]

* Variables:
  - \(R_i\) : Expected return of investment
  - \(R_f\) : Risk-free rate
  - \(\beta_i\) : Beta of the investment
  - \(E(R_m)\) : Expected market return

* When to Use:
  - This formula is used when estimating the expected return of a security based on its beta and the risk-free rate, as well as the relationship between market returns and risk.

* When NOT to Use:
  - Do not use this formula when there is no available data for the required variables, or when using it in situations that do not meet the assumptions of CAPM, such as small sample size or outliers.

* Common Mistakes:
  - Incorrectly assuming that the expected market return (\(E(R_m)\)) is always equal to its historical value.
  - Misinterpreting the formula as a direct calculation of security returns when it's actually an expected return estimate based on market and risk assumptions.

* Calculator Steps:
  - N/A

---

## PRT-F006: Beta

**Formula:** β_i = Cov(R_i, R_m) / Var(R_m) = ρ(i,m) × σ_i / σ_m

* **Variables:** 
  - β_i: The i-th element of the beta matrix
  - Cov(R_i, R_m): The covariance between variables R_i and R_m
  - Var(R_m): The variance of variable R_m
  - ρ(i,m): The correlation coefficient between variables R_i and R_m
  - σ_i: The standard deviation of variable R_i
  - σ_m: The standard deviation of variable R_m

* **When to Use:** 
  - When calculating the beta matrix, which is a measure used in risk modeling to express the sensitivity of one return relative to another.

* **When NOT to Use:** 
  - When the correlation between variables is unknown or not estimable, as this formula requires the calculation of covariance and correlation coefficients.

* **Common Mistakes:** 
  - Incorrectly assuming that the formula can be applied without checking for estimation issues.
  - Failing to verify if the correlation coefficient has been properly estimated.
  - Not considering the limitations of using beta when dealing with non-normal distributions or multiple correlations between variables.

* **Calculator Steps:** 
  - N/A

---

## PRT-F007: Sharpe Ratio

**Formula:** Sharpe = (R_p - R_f) / σ_p

* Variables:
  * \(R_p\): The return of the portfolio
  * \(R_f\): The risk-free rate
  * \(\sigma_p\): The standard deviation of the portfolio returns

* When to Use:
  * Calculating the Sharpe Ratio to evaluate a portfolio's risk-adjusted performance.

* When NOT to Use:
  * Using when calculating individual investment holding returns, as it assumes a portfolio.

* Common Mistakes:
  * Failing to calculate \(\sigma_p\) correctly, using incorrect standard deviation formula or failing to account for non-normal distributions.
  * Incorrectly ignoring the risk-free rate in calculations, assuming no correlation with portfolio return.

* Calculator Steps:
  N/A

---

## PRT-F008: Treynor Ratio

**Formula:** Treynor = (R_p - R_f) / β_p

* Variables:
  * \(Treynor\): The Treynor ratio value
  * \(R_p\): The expected return of the portfolio (before fees)
  * \(R_f\): The risk-free rate
  * \(\beta_p\): The beta of the portfolio

* When to Use:
  Apply this formula when you want to calculate the excess return of a portfolio relative to the risk-free rate, and have already calculated or know the beta of the portfolio.

* When NOT to Use:
  Do not use this formula if you don't know the expected return of the portfolio (\(R_p\)) or the beta (\(\beta_p\)), as these values are necessary inputs for the Treynor ratio calculation.

* Common Mistakes:
  Candidates often forget to calculate or properly interpret the Treynor ratio, especially when interpreting it in the context of investment decisions. Another common mistake is using incorrect units (e.g., not accounting for decimal places) and failing to consider whether the beta value should be squared.

* Calculator Steps:
  N/A

---

## PRT-F009: Jensen's Alpha

**Formula:** α_p = R_p - [R_f + β_p(R_m - R_f)]

* **Variables:** 
  * \(α_p\): The Jensen's Alpha of the portfolio
  * \(R_p\): The portfolio return
  * \(R_f\): The risk-free rate
  * \(\beta_p\): The beta of the portfolio, representing its systematic risk
  * \(R_m\): The market return

* **When to Use:** 
  Apply Jensen's Alpha when you want to measure the excess return of a portfolio over the expected return of the same asset class or market as measured by the risk-free rate.

* **When NOT to Use:**
  Do not apply Jensen's Alpha if the formula is applied incorrectly, or if it is used in conjunction with other measures that might mask its true meaning. Additionally, use caution when applying Jensen's Alpha to small portfolios or those with non-normal returns due to fat tails.

* **Common Mistakes:** 
  Common errors include neglecting to consider the effect of systematic risk (beta) on the portfolio return, misinterpreting Jensen's Alpha as a measure of performance over other metrics such as Sharpe ratio, and failing to account for diversification benefits across different asset classes.

* **Calculator Steps:**
  N/A

---

## PRT-F010: M² (M-Squared)

**Formula:** M² = (R_p - R_f) × (σ_m/σ_p) - (R_m - R_f)

* **Variables:** 
  - R_p: The return on portfolio
  - R_f: The risk-free rate
  - σ_m: The standard deviation of market returns
  - σ_p: The standard deviation of portfolio returns
  - M² (M-Squared): The modified Sharpe ratio


* **When to Use:** 
  - When evaluating the performance of a portfolio relative to the market and its risk profile, especially for investment decisions or when comparing different portfolios.


* **When NOT to Use:** 
  - When the focus is solely on traditional risk-adjusted measures like the traditional Sharpe ratio (M1 = R_p - R_f) or when market returns are not available.
  - In scenarios where the portfolio does not align with the overall market, and therefore σ_m/σ_p cannot be accurately estimated.


* **Common Mistakes:**
  - Incorrectly assuming that σ_p = σ_m for portfolios that do not track the market's performance closely.
  - Not considering the impact of non-traditional risk sources or factors such as taxes on investment decisions using M².

---

## PRT-F011: Information Ratio

**Formula:** IR = (R_p - R_b) / Tracking Error

* Variables:
  - \(IR\): Information Ratio
  - \(R_p\): Portfolio Return
  - \(R_b\): Benchmark Return
  - \(Tracking Error\): Tracking Error (a measure of portfolio risk)

* When to Use:
  Apply the Information Ratio when evaluating a portfolio's risk-adjusted performance relative to a benchmark. It is used to assess whether the portfolio returns are better than the benchmark returns.

* When NOT to Use:
  Do not use the Information Ratio when comparing the risk-adjusted performance of two different benchmarks, as it is specific to one benchmark and cannot be directly compared to another.

* Common Mistakes:
  - Failing to calculate Tracking Error correctly.
  - Not using a consistent method for calculating the portfolio return.
  - Incorrectly assuming that the information ratio is always positive or negative, when in fact it can be both.

* Calculator Steps:
  N/A

---

## PRT-F012: Covariance from Correlation

**Formula:** Cov(R_i, R_j) = ρ(i,j) × σ_i × σ_j

* Variables:
  - \(ρ(i,j)\): The correlation coefficient between two variables \(R_i\) and \(R_j\)
  - \(R_i\): The value of variable i
  - \(R_j\): The value of variable j
  - \(\sigma_i\): The standard deviation of variable i
  - \(\sigma_j\): The standard deviation of variable j

* When to Use:
  - To calculate the covariance between two variables when the correlation coefficient is known and the standard deviations are available.

* When NOT to Use:
  - When the correlation coefficient is not known or cannot be estimated from the available data.
  - When the standard deviations of either variable are unknown.

* Common Mistakes:
  - Assuming that a zero correlation coefficient implies a covariance of zero; this may not always be true due to limitations in measurement accuracy.
  - Failing to check for any errors in calculating the correlation coefficient, which can lead to incorrect results.

* Calculator Steps:
  - N/A

---

## PRT-F013: Portfolio Beta

**Formula:** β_p = Σ wᵢ × βᵢ

* Variables:
  - β_p: The portfolio beta of the calculated portfolio.
  - βᵢ: The individual stock beta of each security in the portfolio.
  - wᵢ: The weight of each security in the portfolio (i.e., its proportion of total portfolio value).
 
* When to Use:
  - To calculate the overall performance of a portfolio relative to the market or another benchmark.

* When NOT to Use:
  - For calculating individual stock betas, which require specific data on returns and volatility for each stock.
  
* Common Mistakes:
  - Misinterpreting β_p as a measure of risk: while it does relate to standard deviation, it's actually a measure of systematic risk relative to the market.
  - Not using the correct weights (wᵢ) in the calculation.

* Calculator Steps:
  N/A

---

## PRT-F014: Required Return (CAPM)

**Formula:** r_required = R_f + β × (Market Risk Premium)

* Variables:
  * `r_required`: The required return on investment
  * `R_f`: The risk-free rate of return
  * `β`: The beta coefficient representing the market risk premium sensitivity

* When to Use:
  * To calculate the minimum expected return an investor requires from an asset, considering both the risk-free rate and the market risk premium.

* When NOT to Use:
  * When calculating the required return on a portfolio with more than one security, as this formula only accounts for market risk and not other factors like size or value effects.
  * When the market risk premium is unknown or difficult to estimate, as it relies heavily on historical data of the stock's performance relative to the overall market.

* Common Mistakes:
  * Incorrectly applying the CAPM without considering the specific requirements of the investment or project being evaluated.
  * Failing to adjust for size or value effects, which can be significant factors in certain industries or asset classes.

* Calculator Steps:
  * N/A (can be calculated manually with simple arithmetic operations)

---

## PRT-F015: Utility Function

**Formula:** U = E(R) - ½ × A × σ²

* Variables:
  * U (Utility Function): measures an individual's satisfaction with a consumption bundle of goods and services
  * E(R) (Expected Utility): a measure of the expected utility a consumer would derive from consuming a good or service
  * A (Discounted Rate of Time Preference): a measure of a consumer's preference for immediate gratification over future consumption
  * σ² (Variance of Time Preference): measures the volatility or risk associated with time preferences

* When to Use:
  * When evaluating the relative satisfaction that consumers derive from different consumption bundles, and understanding how changes in consumption affect their utility.

* When NOT to Use:
  * In situations where the discount rate is not explicitly stated or known; in these cases, an approximation using average rates of interest may be necessary.
  * In scenarios involving investments with a high level of risk; in such cases, other valuation methods like expected returns are more suitable.

* Common Mistakes:
  * Incorrectly assuming that the variance of time preference (σ²) is zero, which can lead to an oversimplification of consumer behavior and neglect of potential biases.
  * Failing to consider the importance of risk aversion in evaluating utility functions; this can result in incorrect estimates of expected utilities.

* Calculator Steps:
  N/A

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
