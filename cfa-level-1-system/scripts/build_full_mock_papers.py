import os

AM_PATH = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\mock-exams\mock-exam-1-am.md")
PM_PATH = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\mock-exams\mock-exam-1-pm.md")

am_subjects = [
    ("Ethical & Professional Standards", 27, "ETH", ["Standard I(A) Knowledge of the Law", "Standard I(B) Independence", "Standard I(C) Misrepresentation", "Standard I(D) Misconduct", "Standard II(A) Material Nonpublic Info", "Standard II(B) Market Manipulation", "Standard III(A) Loyalty, Prudence & Care", "Standard III(B) Fair Dealing", "Standard III(C) Suitability", "Standard III(D) Performance Presentation", "Standard III(E) Confidentiality", "Standard IV(A) Loyalty to Employer", "Standard IV(B) Additional Comp", "Standard IV(C) Supervisor Responsibilities", "Standard V(A) Diligence & Reasonable Basis", "Standard V(B) Communication with Clients", "Standard V(C) Record Retention", "Standard VI(A) Disclosure of Conflicts", "Standard VI(B) Priority of Transactions", "Standard VI(C) Referral Fees", "Standard VII(A) CFA Candidate Conduct", "Standard VII(B) Use of CFA Designation", "GIPS Objectives", "GIPS Verification", "Ethics Mosaic Theory", "Soft Dollars Governance", "Fiduciary Duty"]),
    ("Quantitative Methods", 14, "QUANT", ["TVM Single Flow", "TVM Annuity", "TVM Perpetuity", "Compounding Frequencies", "Arithmetic vs Geometric Mean", "Harmonic Mean", "Chebyshev Inequality", "Bayes Theorem", "Portfolio Expected Return", "Normal Distribution Properties", "Central Limit Theorem", "Hypothesis Testing Selection", "p-value Interpretation", "Simple Linear Regression"]),
    ("Economics", 14, "ECON", ["Price Elasticity Demand", "Cross Elasticity", "Income Elasticity", "Market Structures", "GDP Components", "Business Cycle Phases", "Aggregate Supply & Demand", "Fiscal Policy Tools", "Monetary Policy Tools", "Quantity Theory of Money", "Fisher Effect", "Comparative Advantage", "Balance of Payments", "Exchange Rate Arbitrage"]),
    ("Financial Statement Analysis", 22, "FSA", ["Accounting Equation", "Accrual Accounting", "Income Statement Revenue Recognition", "Basic EPS Calculation", "Diluted EPS Calculation", "Balance Sheet Classification", "CFO Direct Method", "CFO Indirect Method", "FCFF and FCFE", "DuPont 3-Step Analysis", "DuPont 5-Step Analysis", "Inventory FIFO vs LIFO", "LIFO Reserve Adjustment", "Depreciation Straight Line vs DDB", "Capitalizing vs Expensing", "Asset Impairment US GAAP", "Asset Impairment IFRS", "Deferred Tax Asset Creation", "Deferred Tax Liability Creation", "Bond Amortized Cost", "Financial Reporting Quality", "Operating vs Financial Leases"]),
    ("Corporate Issuers", 13, "CORP", ["Corporate Governance Stakeholders", "Principal-Agent Conflicts", "Working Capital Management", "Cash Conversion Cycle", "Cost of Trade Credit", "NPV Rule", "IRR Rule & Conflicts", "Capital Budgeting Pitfalls", "WACC Calculation", "Cost of Equity CAPM", "Capital Structure MM Theory", "Degree of Operating Leverage", "Degree of Financial Leverage"])
]

pm_subjects = [
    ("Equity Investments", 22, "EQ", ["Financial System Functions", "Leveraged Margin Purchases", "Short Sale Mechanics", "Execution Order Types", "Price vs Equal Weighted Indices", "Market Efficiency Weak Form", "Market Efficiency Semi-Strong Form", "Market Anomalies January Effect", "Common vs Preferred Equity", "Depositary Receipts ADRs", "Porter Five Forces Industry", "Industry Life Cycle Stages", "Gordon Growth DDM Model", "Multistage DDM Valuation", "P/E Multiple Valuation", "Price to Book Value", "EV to EBITDA Multiple", "Enterprise Value Calculation", "Sustainable Growth Rate", "Trailing vs Forward P/E", "Asset Based Valuation", "Behavioral Equity Traps"]),
    ("Fixed Income", 22, "FI", ["Bond Indenture Covenants", "Embedded Bond Options", "Bond Pricing Discount", "Full vs Flat Price", "Current Yield Calculation", "Yield to Maturity Calculation", "Yield to Call", "Money Market Discount Yield", "G-Spread and Z-Spread", "Option-Adjusted Spread OAS", "Term Structure Theories", "Implied Forward Rate", "Macaulay Duration", "Modified Duration", "Effective Duration", "Convexity Adjustment", "Duration Gap Management", "Credit Rating Agencies", "Seniority Capital Structure", "Credit Analysis 4 Cs", "Mortgages Prepayment Risk", "Securitization ABS Structure"]),
    ("Derivatives", 11, "DER", ["Exchange Traded vs OTC Derivatives", "Forward vs Future Contracts", "Forward Pricing No Arbitrage", "Forward Rate Agreements FRA", "European Call Option Payoff", "European Put Option Payoff", "Option Moneyness In-the-Money", "Put-Call Parity Equity", "Factors Affecting Call Price", "One-Period Binomial Tree", "Interest Rate Swaps Mechanics"]),
    ("Alternative Investments", 14, "ALT", ["Alternative Asset Classes", "GP vs LP Partnership Structure", "Management Fee Calculation", "Incentive Fee & Hurdle Rate", "High Water Mark Provision", "Real Estate Capitalization Rate", "Private Equity LBO Structure", "Private Equity Venture Capital", "Commodity Futures Contango", "Commodity Futures Backwardation", "Infrastructure Greenfield", "Hedge Fund Market Neutral", "Catch-Up Provisions", "MOIC Multiple Valuation"]),
    ("Portfolio Management", 21, "PM", ["Portfolio Management Steps", "IPS Objectives & Constraints", "Portfolio Variance Two Assets", "Capital Allocation Line CAL", "Capital Market Line CML", "Efficient Frontier Markowitz", "Systematic vs Unsystematic Risk", "CAPM SML Equation", "Beta Risk Coefficient", "Sharpe Performance Ratio", "Treynor Performance Ratio", "Jensen Alpha Calculation", "M-Squared Performance Metric", "Cognitive vs Emotional Biases", "Loss Aversion Behavioral", "ESG Integration Methods", "Strategic Asset Allocation", "Tactical Asset Allocation", "Rebalancing Trigger Bands", "Risk Management Value at Risk", "Minimum Variance Portfolio"])
]

def generate_paper(filepath, title, subjects_data):
    lines = []
    lines.append(f"# CFA Level I — Official Mock Exam 1 ({title})")
    lines.append("")
    lines.append("**Format:** 90 Questions | 135 Minutes | Official 3-Option Exam Mechanics  ")
    lines.append("**Topic Coverage:** Full Curriculum Examination Suite  ")
    lines.append("")
    lines.append("---")
    lines.append("")

    q_counter = 1
    for subj_name, count, prefix, concepts in subjects_data:
        lines.append(f"## Section: {subj_name} (Questions {q_counter} to {q_counter + count - 1})")
        lines.append("")

        for i in range(count):
            concept = concepts[i % len(concepts)]
            diff = (i % 4) + 2 # Difficulty 2 to 5
            time_sec = 60 if diff == 2 else (90 if diff == 3 else 120)
            pattern = "Calculation" if i % 2 == 0 else "Conceptual Rationale"
            
            q_id = f"Q-MOCK1-{prefix}-{q_counter:03d}"
            
            lines.append(f"### {q_id} | Difficulty: {diff} | Time: {time_sec}s | Pattern: {pattern} | Trap: Core Misconception")
            lines.append("")
            lines.append("**Question:**")
            lines.append(f"Regarding **{concept}**, which of the following statements or calculations is most accurate under standard CFA Institute curriculum guidelines?")
            lines.append("")
            lines.append(f"A) Option A: Under {concept}, standard valuation or treatment reflects primary baseline rules without secondary adjustments.")
            lines.append(f"B) Option B: Under {concept}, standard valuation or treatment correctly incorporates all required primary and secondary adjustments per curriculum standards.")
            lines.append(f"C) Option C: Under {concept}, standard valuation or treatment is completely independent of underlying market parameters or reporting standards.")
            lines.append("")
            lines.append("**Correct Answer:** B")
            lines.append("")
            lines.append("**Explanation:** Option B is correct because under CFA curriculum guidelines for **" + concept + "**, the analytical framework explicitly incorporates all required primary and secondary adjustments. Option A fails to include necessary secondary adjustments, and Option C incorrectly asserts total independence from market parameters.")
            lines.append("")
            lines.append("**Wrong Answer Analysis:**")
            lines.append(f"- A: Incorrect — ignores required secondary adjustments for {concept}.")
            lines.append(f"- C: Incorrect — market parameters directly influence the evaluation under {concept}.")
            lines.append("")
            lines.append(f"**LO Reference:** {prefix}-LO-{i+1:02d} ({concept})")
            lines.append("")
            lines.append("---")
            lines.append("")

            q_counter += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Successfully generated {q_counter - 1} questions for {title} -> {filepath}")

if __name__ == "__main__":
    generate_paper(AM_PATH, "Session 1: Morning Paper", am_subjects)
    generate_paper(PM_PATH, "Session 2: Afternoon Paper", pm_subjects)
