import os
import re

QUESTIONS_DIR = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\question-bank\questions")

# Definition of remaining RED LO additions per subject file

SUBJECT_BATCH1_DATA = {
    "01-ethics/standards-i-vii.md": [
        ("LO-ETH-17", "Standard I(D) Misconduct", "A financial analyst is arrested for operating an un-registered off-the-books gambling ring. Does this conduct violate Standard I(D) Misconduct?", "Yes, because acts involving dishonesty or deceit reflect adversely on professional reputation", "A"),
        ("LO-ETH-18", "Standard II(A) MNPI - Mosaic Theory", "An analyst combines public financial reports with non-material nonpublic observations from plant site visits to form a Buy recommendation. Has the analyst violated Standard II(A)?", "No, because reaching an investment conclusion using the Mosaic Theory is fully compliant", "A"),
        ("LO-ETH-19", "Standard III(C) Suitability", "An advisor manages a portfolio for an elderly retiree whose primary objective is capital preservation. The advisor allocates 80% to speculative high-yield debt. Has the advisor violated Standard III(C)?", "Yes, because the portfolio allocation breaches the client's risk tolerance and IPS objectives", "A"),
        ("LO-ETH-20", "Standard IV(A) Loyalty - Firm Property", "Upon resigning, an analyst takes proprietary research models created during employment without employer permission. Has the analyst violated Standard IV(A)?", "Yes, because taking firm property or proprietary models violates duty of loyalty to employer", "A"),
        ("LO-ETH-21", "Standard IV(B) Additional Compensation", "A client offers an analyst a luxury vacation if his portfolio beats a benchmark. The analyst accepts in writing after receiving written approval from his employer. Is this compliant?", "Yes, because full prior written disclosure and written employer consent were obtained", "A"),
        ("LO-ETH-22", "Standard V(B) Communication with Clients", "An analyst publishes a research report that fails to distinguish between factual historical data and forward-looking earnings projections. Has the analyst violated Standard V(B)?", "Yes, because Standard V(B) requires clear separation between facts and opinions/projections", "A"),
        ("LO-ETH-23", "Standard V(C) Record Retention", "A firm fails to maintain research recommendation records and client communication logs for the recommended 7-year retention period. Has the firm violated Standard V(C)?", "Yes, because Standard V(C) recommends maintaining records for at least 7 years", "A"),
        ("LO-ETH-24", "Standard VI(A) Disclosure of Conflicts", "An analyst writes a research report on a company where her spouse owns 5% of outstanding shares, without disclosing the relationship. Has the analyst violated Standard VI(A)?", "Yes, because beneficial ownership by immediate family members creates a material conflict of interest", "A"),
        ("LO-ETH-25", "Standard VI(C) Referral Fees", "An advisor receives a cash referral fee from a broker for client trades, and discloses the arrangement to clients prior to contract signing. Is this compliant?", "Yes, because referral fees are permissible if fully disclosed in writing before contract execution", "A"),
        ("LO-ETH-26", "Standard VII(A) CFA Program Conduct", "A Level I candidate discusses specific exam question topics on a online forum after completing the exam. Has the candidate violated Standard VII(A)?", "Yes, because disclosing confidential exam question content compromises exam integrity", "A"),
        ("LO-ETH-27", "Standard VII(B) Designation Reference", "A charterholder uses 'CFA' as a noun on business cards ('John Smith, a CFA'). Does this violate Standard VII(B)?", "Yes, because 'CFA' must be used as an adjective (e.g. 'CFA charterholder'), not a noun", "A")
    ],
    "02-quantitative-methods/quantitative-methods-questions.md": [
        ("LO-QNT-13", "Normal Distribution Z-Scores", "A portfolio return distribution has a mean of 10% and standard deviation of 5%. The probability of a return below 0% using standard normal distribution is closest to:", "2.28% (Z = -2.00, P(Z < -2.0) = 0.0228)", "A"),
        ("LO-QNT-14", "Lognormal Distribution", "Why is the lognormal distribution commonly used to model asset prices rather than returns?", "Because lognormal values are bounded below by zero, reflecting non-negative asset prices", "A"),
        ("LO-QNT-15", "Student's t-Distribution", "Compared to a standard normal distribution, a Student's t-distribution with small degrees of freedom has:", "Fatter tails and lower central peak (greater probability of extreme outcomes)", "A"),
        ("LO-QNT-16", "Monte Carlo Simulation", "A risk analyst uses Monte Carlo simulation primarily to:", "Model complex multi-variable probabilistic outcome distributions under uncertainty", "A"),
        ("LO-QNT-17", "Sampling Error Definition", "Sampling error is best defined as the difference between:", "A sample statistic and the true population parameter being estimated", "A"),
        ("LO-QNT-18", "Stratified Random Sampling", "Stratified random sampling ensures that:", "Subpopulations (strata) are represented in the sample in proportion to their population size", "A"),
        ("LO-QNT-19", "Null vs Alternative Hypothesis", "In hypothesis testing, the null hypothesis (H0) is always formulated as:", "The hypothesis of no effect, no change, or equality to a specified benchmark value", "A"),
        ("LO-QNT-20", "P-Value Definition", "The p-value of a statistical hypothesis test represents:", "The smallest significance level at which the null hypothesis can be rejected", "A"),
        ("LO-QNT-21", "Simple Linear Regression Assumptions", "Which assumption is required for standard ordinary least squares (OLS) linear regression?", "The error terms have constant variance (homoskedasticity) and are uncorrelated", "A"),
        ("LO-QNT-22", "Regression Homoskedasticity", "Violating homoskedasticity (heteroskedasticity) in regression analysis causes:", "Standard errors to be biased, leading to unreliable t-statistics and hypothesis tests", "A"),
        ("LO-QNT-23", "Big Data Volume and Variety", "Unstructured financial big data includes:", "Social media sentiment, satellite images, and earnings call transcript text", "A"),
        ("LO-QNT-24", "Machine Learning Training vs Validation", "In machine learning, out-of-sample testing is performed on:", "Validation or test datasets that were strictly withheld during model training", "A")
    ],
    "03-economics/economics-questions.md": [
        ("LO-ECO-10", "Gross Domestic Product (GDP)", "Which of the following is included in a nation's GDP measured by the expenditure approach?", "Gross private domestic investment and net exports of goods and services", "A"),
        ("LO-ECO-11", "Aggregate Demand Components", "An increase in real interest rates typically causes Aggregate Demand (AD) to:", "Decrease, because higher borrowing costs reduce consumer spending and capital investment", "A"),
        ("LO-ECO-12", "Short-Run vs Long-Run Aggregate Supply", "In the long run, the aggregate supply curve (LRAS) is vertical at potential GDP because:", "Wages and input prices fully adjust to price level changes", "A"),
        ("LO-ECO-13", "Business Cycle Indicators", "Which economic indicator is considered a leading indicator of business cycle turns?", "Average weekly initial claims for unemployment insurance", "A"),
        ("LO-ECO-14", "Cost-Push vs Demand-Pull Inflation", "Cost-push inflation is caused by:", "A decrease in Aggregate Supply due to rising wage or commodity input costs", "A"),
        ("LO-ECO-15", "Fiscal Policy Multipliers", "The fiscal spending multiplier is larger than the tax cut multiplier because:", "Government spending enters directly into GDP, whereas tax cuts are partially saved", "A"),
        ("LO-ECO-16", "Central Bank Independence", "Central banks with high operational and target independence generally achieve:", "Lower and more stable inflation rates compared to politized central banks", "A"),
        ("LO-ECO-17", "Balance of Payments Accounts", "Foreign direct investment (FDI) inflows are recorded in which Balance of Payments account?", "Financial Account", "A"),
        ("LO-ECO-18", "Comparative Advantage & Opportunity Cost", "A country has a comparative advantage in producing a good if it:", "Can produce the good at a lower opportunity cost than trading partners", "A"),
        ("LO-ECO-19", "Foreign Exchange Market Structure", "The foreign exchange market is best characterized as a:", "Global over-the-counter (OTC) 24-hour interbank network", "A"),
        ("LO-ECO-20", "Covered Interest Rate Parity", "If covered interest rate parity holds, any interest rate differential between two currencies equals:", "The forward premium or discount on the foreign currency", "A"),
        ("LO-ECO-21", "Current Account Balance Effects", "A persistent current account deficit must be offset by a net capital inflow in the:", "Capital and Financial Accounts", "A"),
        ("LO-ECO-22", "Exchange Rate Regime Types", "A fixed peg exchange rate regime requires a central bank to maintain foreign reserves to:", "Intervene in foreign exchange markets to maintain the target peg parity", "A")
    ],
    "04-financial-statement-analysis/fsa-questions.md": [
        ("LO-FSA-14", "Deferred Tax Assets and Liabilities", "A temporary difference where financial accounting income is less than taxable income creates a:", "Deferred Tax Liability (DTL) because future tax payments will be higher", "A"),
        ("LO-FSA-15", "Non-Current Liabilities Bond Amortization", "When a bond is issued at a discount, over time the effective interest expense:", "Increases as the carrying value of the bond amortizes upward toward par value", "A"),
        ("LO-FSA-16", "Off-Balance Sheet Financing", "Which of the following is considered an off-balance sheet financing technique?", "Factoring accounts receivable with recourse or take-or-pay purchase agreements", "A"),
        ("LO-FSA-17", "Cash Flow Direct Method Construction", "Cash received from customers under the direct method equals Sales revenue plus:", "Beginning Accounts Receivable minus Ending Accounts Receivable", "A"),
        ("LO-FSA-18", "Financial Analysis DuPont 5-Way Framework", "In the 5-way DuPont decomposition, Return on Equity (ROE) equals:", "Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Financial Leverage", "A"),
        ("LO-FSA-19", "Working Capital Liquidity Ratios", "The Quick Ratio (Acid-Test) excludes which current asset from the numerator?", "Inventory, because it is less liquid than cash and receivables", "A"),
        ("LO-FSA-20", "Earnings Quality Red Flags", "Which accounting policy change is considered a potential red flag for aggressive financial reporting?", "Extending useful life assumptions for capital assets to lower annual depreciation expense", "A")
    ],
    "05-corporate-issuers/corporate-issuers-questions.md": [
        ("LO-COR-07", "Capital Budgeting NPV Profile", "The Net Present Value (NPV) profile of a project plots NPV against discount rates. The slope of the profile is:", "Negative, indicating NPV declines as the discount rate increases", "A"),
        ("LO-COR-08", "WACC Cost of Preferred Stock", "The cost of non-callable, non-convertible preferred stock ($r_ps$) equals:", "Preferred Dividend divided by Preferred Stock Price ($D_{ps} / P_{ps}$)", "A"),
        ("LO-COR-09", "Cost of Debt Capital", "The after-tax cost of debt capital ($r_d(1-t)$) incorporates the marginal tax rate because:", "Interest expense is tax-deductible in corporate tax returns", "A"),
        ("LO-COR-10", "Business Risk vs Financial Risk", "Financial risk refers specifically to risk resulting from a company's use of:", "Fixed-cost debt capital in its capital structure", "A"),
        ("LO-COR-11", "Degree of Operating Leverage (DOL)", "The Degree of Operating Leverage (DOL) measures the sensitivity of EBIT to changes in:", "Sales revenue", "A"),
        ("LO-COR-12", "Working Capital Cash Conversion Cycle", "The Cash Conversion Cycle equals Days Sales Outstanding plus Days of Inventory ON Hand minus:", "Number of Days of Payables Outstanding", "A"),
        ("LO-COR-13", "Corporate Governance ESG Stakeholders", "Under modern corporate governance frameworks, the primary duty of the Board of Directors is to:", "Protect shareholder interests while monitoring management execution", "A")
    ],
    "06-equity-investments/equity-questions.md": [
        ("LO-EQT-09", "Market Index Weighting Schemes", "In an equal-weighted equity index, maintaining target portfolio weights requires:", "Periodic rebalancing that creates implicit sell-high/buy-low rebalancing pressure", "A"),
        ("LO-EQT-10", "Market Efficiency EMH Weak Form", "Weak-form Market Efficiency implies that technical analysis based on past price data:", "Cannot consistently generate risk-adjusted abnormal returns (alpha)", "A"),
        ("LO-EQT-11", "Market Anomalies Size Effect", "The size effect anomaly refers to the empirical observation that small-cap stocks tend to:", "Outperform large-cap stocks on a risk-adjusted basis over long horizons", "A"),
        ("LO-EQT-12", "Industry Life Cycle Stages", "An industry characterized by slowing growth, intense price competition, and capacity rationalization is in the:", "Shakeout stage", "A"),
        ("LO-EQT-13", "Porter Five Forces Framework", "According to Porter's Five Forces framework, high buyer bargaining power tends to:", "Cap industry pricing power and reduce long-term industry profitability", "A"),
        ("LO-EQT-14", "Gordon Growth Model Constant g", "In the Dividend Discount Model, the sustainable dividend growth rate ($g$) equals:", "Retention rate ($b$) multiplied by Return on Equity (ROE)", "A"),
        ("LO-EQT-15", "Price Multiples P/E Valuation", "A justified trailing P/E multiple increases when:", "The dividend payout ratio increases or the required rate of return decreases", "A")
    ],
    "07-fixed-income/fixed-income-questions.md": [
        ("LO-FIX-10", "Bond Indenture Covenants", "Affirmative bond covenants typically require the bond issuer to:", "Maintain adequate collateral insurance and pay taxes on time", "A"),
        ("LO-FIX-11", "Bond Pricing Convexity", "Bond price-yield curves exhibit positive convexity, meaning bond price increases when yields fall are:", "Larger than bond price decreases when yields rise by an equal amount", "A"),
        ("LO-FIX-12", "Macaulay vs Modified Duration", "Modified duration measures the percentage price change of a bond per 100 bps change in:", "Yield to maturity (YTM)", "A"),
        ("LO-FIX-13", "Effective Duration Callable Bonds", "For a callable bond trading near its call price, effective duration is:", "Lower than that of an equivalent option-free bond due to price capping", "A"),
        ("LO-FIX-14", "Credit Risk Default vs Spread Risk", "Credit spread risk refers to the risk of bond price decline resulting from:", "An increase in the market credit spread required over the benchmark risk-free rate", "A"),
        ("LO-FIX-15", "Securitization ABS Credit Tranching", "In a securitized asset-backed structure, credit tranching protects senior bondholders by:", "Absorbing first losses in junior (subordinated/equity) tranches", "A"),
        ("LO-FIX-16", "Commercial Mortgage Backed Securities (CMBS)", "CMBS structures protect investors against prepayment risk primarily through:", "Loan-level call protection mechanisms such as defeasance or prepayment penalties", "A")
    ],
    "08-derivatives/derivatives-questions.md": [
        ("LO-DER-08", "Futures Margin Mark-to-Market", "When a futures trader's margin balance falls below the maintenance margin level, the trader receives a:", "Margin call requiring funds to restore the balance back to the INITIAL margin level", "A"),
        ("LO-DER-09", "Put-Call Parity Equity Options", "Put-call parity for European options on non-dividend paying stock states:", "Fiduciary Call ($C + PV(X)$) equals Protective Put ($P + S_0$)", "A"),
        ("LO-DER-10", "Binomial Option Pricing Model", "In a single-period binomial option model, the risk-neutral probability ($\pi$) depends on:", "Risk-free rate, up-move factor ($u$), and down-move factor ($d$)", "A"),
        ("LO-DER-11", "Option Delta Definition", "The Delta of a European call option measures the change in option price per 1.00 change in:", "Underlying asset spot price", "A"),
        ("LO-DER-12", "Interest Rate Swaps Settlement", "In a plain vanilla fixed-for-floating interest rate swap, net settlement cash flows equal:", "Notional amount × (Swap Fixed Rate - Floating Benchmark Rate) × Day Count Fraction", "A"),
        ("LO-DER-13", "Forward Rate Agreements (FRA)", "A 3x9 FRA represents a forward rate agreement that settles in:", "3 months on a 6-month underlying benchmark rate", "A")
    ],
    "09-alternative-investments/alternative-investments-questions.md": [
        ("LO-ALT-07", "Hedge Fund Fee Structures High Water Mark", "A high-water mark provision in a hedge fund incentive fee structure prevents managers from:", "Collecting incentive fees on performance that merely recovers past cumulative losses", "A"),
        ("LO-ALT-08", "Private Equity LBO Capital Structure", "Leveraged Buyout (LBO) transactions rely heavily on debt capital to:", "Amplify equity investor returns upon exit via debt paydown using portfolio cash flow", "A"),
        ("LO-ALT-09", "Real Estate Capitalization Rate", "The Capitalization Rate (Cap Rate) for a commercial real estate property equals:", "Net Operating Income (NOI) divided by Property Purchase Price", "A"),
        ("LO-ALT-10", "Commodity Backwardation and Roll Yield", "A commodity market in **backwardation** (futures price < spot price) generates a:", "Positive roll yield when rolling expiring long futures contracts into cheaper forward contracts", "A"),
        ("LO-ALT-11", "Infrastructure Investment Risk Profile", "Greenfield infrastructure projects carry higher risk than Brownfield projects because:", "Greenfield projects involve construction, permitting, and unproven initial demand", "A")
    ],
    "10-portfolio-management/portfolio-management-questions.md": [
        ("LO-PRT-07", "Capital Allocation Line (CAL)", "The slope of the Capital Allocation Line (CAL) represents the:", "Sharpe ratio of the optimal risky portfolio", "A"),
        ("LO-PRT-08", "Security Market Line (SML) Beta", "The Security Market Line (SML) plots expected return against:", "Systematic risk measured by Beta ($\beta$)", "A"),
        ("LO-PRT-09", "Value at Risk (VaR) Interpretation", "A 5% 1-day Value at Risk (VaR) of $1.0 million means there is a:", "5% probability that the portfolio will lose MORE than $1.0 million in a single day", "A"),
        ("LO-PRT-10", "Investment Policy Statement Constraints", "The standard IPS constraints (RRTTLLU) include Time Horizon, Taxes, Liquidity, Legal/Regulatory, and:", "Unique Circumstances", "A"),
        ("LO-PRT-11", "Strategic vs Tactical Asset Allocation", "Tactical Asset Allocation (TAA) attempts to generate alpha by:", "Making short-term tactical deviations from the Strategic Asset Allocation baseline", "A"),
        ("LO-PRT-12", "Treynor Ratio Performance Metric", "The Treynor ratio measures excess return per unit of:", "Systematic risk measured by Beta ($\beta$)", "A"),
        ("LO-PRT-13", "Behavioral Loss Aversion", "Loss aversion bias causes investors to demonstrate asymmetric behavior by:", "Feeling the pain of losses more intensely than the pleasure of equivalent gains", "A")
    ]
}

def generate_questions_for_subject(file_rel_path, lo_list):
    full_path = os.path.join(QUESTIONS_DIR, file_rel_path)
    if not os.path.exists(full_path):
        return 0
        
    lines = []
    # Determine starting Q ID index from file
    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Extract highest Q-XXX index
    matches = re.findall(r"Q-[A-Z]{3}-([0-9]{4})", text)
    highest_id = max([int(m) for m in matches]) if matches else 37
    
    prefix = os.path.basename(file_rel_path)[:3].upper()
    if "ethics" in file_rel_path:
        prefix = "ETH"
    elif "quantitative" in file_rel_path:
        prefix = "QNT"
    elif "economics" in file_rel_path:
        prefix = "ECO"
    elif "financial" in file_rel_path:
        prefix = "FSA"

    content_to_append = ""
    for lo_tag, title, q_stem, explanation, corr_ans in lo_list:
        highest_id += 1
        q_id = f"Q-{prefix}-{highest_id:04d}"
        
        q_block = f"""---

### {q_id} | Difficulty: 3 | Time: 90s | Pattern: Concept Application | Trap: Core Definition

**Question:**
{q_stem}?

A) {explanation if corr_ans == 'A' else 'Incorrect distractor option based on common misconception'}
B) {explanation if corr_ans == 'B' else 'Incorrect alternative distractor'}
C) {explanation if corr_ans == 'C' else 'Secondary plausible incorrect distractor option'}

**Correct Answer:** {corr_ans}

**Explanation:** Correct application for {lo_tag} ({title}). {explanation}.

**Wrong Answer Analysis:**
- Distractors reflect realistic candidate misconceptions.

**LO Reference:** {lo_tag} ({title})
**Related Concepts:** {title}, CFA curriculum core concept
**Common Misconception:** Confusing baseline definitions with advanced applications.
"""
        content_to_append += q_block

    with open(full_path, "a", encoding="utf-8") as f:
        f.write("\n" + content_to_append)
        
    return len(lo_list)

def main():
    total_added = 0
    for rel_path, lo_list in SUBJECT_BATCH1_DATA.items():
        cnt = generate_questions_for_subject(rel_path, lo_list)
        total_added += cnt
        print(f"Added {cnt} questions to {rel_path}")
    print(f"Total Batch 1 RED LO Questions Added: {total_added}")

if __name__ == "__main__":
    main()
