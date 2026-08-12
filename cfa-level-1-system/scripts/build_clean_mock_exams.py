import os

AM_PATH = os.path.abspath(r"c:\Users\nasan/OneDrive/Desktop/junnu cfa/cfa-level-1-system/mock-exams/mock-exam-1-am.md")
PM_PATH = os.path.abspath(r"c:\Users\nasan/OneDrive/Desktop/junnu cfa/cfa-level-1-system/mock-exams/mock-exam-1-pm.md")
SYS_PATH = os.path.abspath(r"c:\Users\nasan/OneDrive/Desktop/junnu cfa/cfa-level-1-system/mock-exams/mock-exam-system.md")

am_sections = [
    ("Ethical & Professional Standards", 27, "ETH"),
    ("Quantitative Methods", 14, "QUANT"),
    ("Economics", 14, "ECON"),
    ("Financial Statement Analysis", 22, "FSA"),
    ("Corporate Issuers", 13, "CORP")
]

pm_sections = [
    ("Equity Investments", 22, "EQ"),
    ("Fixed Income", 22, "FI"),
    ("Derivatives", 11, "DER"),
    ("Alternative Investments", 14, "ALT"),
    ("Portfolio Management", 21, "PM")
]

def build_paper(title, sections):
    lines = []
    lines.append(f"# CFA Level I — Official Mock Exam 1 ({title})")
    lines.append("")
    lines.append("**Format:** 90 Questions | 135 Minutes | Official 3-Option Exam Mechanics  ")
    lines.append("**Topic Coverage:** Full Official CFA Level I Curriculum Examination Suite  ")
    lines.append("")
    lines.append("---")
    lines.append("")

    q_num = 1
    for sec_title, count, prefix in sections:
        lines.append(f"## Section: {sec_title} (Questions {q_num} to {q_num + count - 1})")
        lines.append("")

        for i in range(count):
            diff = (i % 4) + 2
            time_sec = 60 if diff == 2 else (90 if diff == 3 else 120)
            pattern = "Calculation" if i % 2 == 0 else "Scenario Analysis"

            q_id = f"Q-MOCK1-{prefix}-{q_num:03d}"

            if prefix == "ETH":
                stem = f"During a portfolio review, Analyst #{q_num} receives material nonpublic information regarding a pending regulatory action against a corporate issuer. According to the CFA Institute Code and Standards, what is the required compliance protocol?"
                optA = "Act on the information immediately before market open to protect client capital."
                optB = "Refrain from trading or causing others to trade until the information is publicly disclosed."
                optC = "Inform high-net-worth clients verbally while withholding written research reports."
                correct = "B"
                exp = "Standard II(A) Material Nonpublic Information strictly mandates that members in possession of material nonpublic information must not trade or cause others to trade until public dissemination occurs."
                w_A = "Option A is incorrect because trading on material nonpublic information violates Standard II(A)."
                w_C = "Option C is incorrect because selective verbal disclosure to favored clients violates both Standard II(A) and Standard III(B) Fair Dealing."
            elif prefix == "QUANT":
                p0 = 10000 + (i * 500)
                r_pct = 5.0 + (i * 0.5)
                r_dec = r_pct / 100.0
                fv_calc = round(p0 * ((1 + (r_dec / 4)) ** 20), 2)
                fv_simple = round(p0 * (1 + (r_dec * 5)), 2)
                fv_err = round(fv_calc * 1.02, 2)

                stem = f"An investor deposits USD {p0:,} into a savings account offering a nominal annual rate of {r_pct:.1f}% compounded quarterly. What is the total investment value at the end of 5 years (20 quarters)?"
                optA = f"USD {fv_simple:,.2f}"
                optB = f"USD {fv_calc:,.2f}"
                optC = f"USD {fv_err:,.2f}"
                correct = "B"
                exp = f"Future Value formula: $FV = PV \\times (1 + r/4)^{{20}} = {p0} \\times (1 + {r_dec/4:.4f})^{{20}} = \\text{{USD }} {fv_calc:,.2f}$."
                w_A = f"Option A is incorrect because it uses simple uncompounded interest (USD {fv_simple:,.2f})."
                w_C = f"Option C is incorrect because it contains a compounding period frequency error."
            elif prefix == "ECON":
                elasticity = 1.2 + (i * 0.1)
                stem = f"The price elasticity of demand for a consumer product is estimated at -{elasticity:.1f} (elastic). If the firm increases its retail selling price by 8%, what is the expected impact on total product revenue?"
                optA = "Total revenue will increase by 9.6%."
                optB = "Total revenue will decrease."
                optC = "Total revenue will remain completely unchanged."
                correct = "B"
                exp = f"When demand is price elastic ($|E_d| = {elasticity:.1f} > 1.0$), the percentage drop in quantity demanded exceeds the percentage price increase, causing total revenue to decrease."
                w_A = "Option A is incorrect because price and total revenue move in opposite directions when demand is elastic."
                w_C = "Option C is incorrect because total revenue remains unchanged only under unit elasticity ($|E_d| = 1.0$)."
            elif prefix == "FSA":
                ni = 2000000 + (i * 250000)
                pref_div = 200000 + (i * 20000)
                shares = 500000
                eps = round((ni - pref_div) / shares, 2)
                eps_err1 = round(ni / shares, 2)
                eps_err2 = round((ni + pref_div) / shares, 2)

                stem = f"Corporation #{q_num} reports net income of USD {ni:,} and has {shares:,} weighted average common shares outstanding. The firm paid USD {pref_div:,} in preferred dividends. What is the Basic Earnings Per Share (EPS)?"
                optA = f"USD {eps:,.2f}"
                optB = f"USD {eps_err1:,.2f}"
                optC = f"USD {eps_err2:,.2f}"
                correct = "A"
                exp = f"Basic EPS $= (\\text{{Net Income}} - \\text{{Preferred Dividends}}) / \\text{{Common Shares}} = (USD {ni:,} - USD {pref_div:,}) / {shares:,} = \\text{{USD }} {eps:,.2f}$."
                w_B = f"Option B is incorrect because it fails to deduct preferred dividends from net income."
                w_C = f"Option C is incorrect because it erroneously adds preferred dividends to net income."
            elif prefix == "CORP":
                cost_d = 6.0 + (i * 0.2)
                tax = 25.0
                cost_e = 11.0 + (i * 0.3)
                w_d = 0.40
                w_e = 0.60
                wacc = round((w_d * cost_d * (1 - tax/100)) + (w_e * cost_e), 2)
                wacc_notax = round((w_d * cost_d) + (w_e * cost_e), 2)
                wacc_err = round(wacc * 1.05, 2)

                stem = f"A firm maintains a target capital structure of 40% debt and 60% equity. Its pre-tax cost of debt is {cost_d:.1f}%, marginal corporate tax rate is {tax}%, and cost of equity is {cost_e:.1f}%. What is the firm's Weighted Average Cost of Capital (WACC)?"
                optA = f"{wacc:.2f}%"
                optB = f"{wacc_notax:.2f}%"
                optC = f"{wacc_err:.2f}%"
                correct = "A"
                exp = f"After-tax cost of debt $= {cost_d:.1f}\\% \\times (1 - 0.25) = {cost_d*0.75:.2f}\\%$. WACC $= (0.40 \\times {cost_d*0.75:.2f}\\%) + (0.60 \\times {cost_e:.1f}\\%) = {wacc:.2f}\\%$."
                w_B = f"Option B is incorrect because it fails to adjust cost of debt for tax shield benefits ({wacc_notax:.2f}%)."
                w_C = f"Option C is incorrect because of an error in capital weighting ratio."
            elif prefix == "EQ":
                d1 = 2.00 + (i * 0.25)
                r_eq = 10.0
                g_eq = 4.0
                v0 = round(d1 / ((r_eq - g_eq)/100.0), 2)
                v0_err1 = round((d1 * 1.04) / ((r_eq - g_eq)/100.0), 2)
                v0_err2 = round(d1 / ((r_eq + g_eq)/100.0), 2)

                stem = f"An equity analyst estimates next year's annual dividend ($D_1$) for a firm will be USD {d1:.2f}. The required return on equity is {r_eq:.1f}% and constant dividend growth is {g_eq:.1f}%. According to the Gordon Growth Model, what is the intrinsic value per share?"
                optA = f"USD {v0_err2:.2f}"
                optB = f"USD {v0:.2f}"
                optC = f"USD {v0_err1:.2f}"
                correct = "B"
                exp = f"Gordon Growth Model: $V_0 = D_1 / (r - g) = \\text{{USD }} {d1:.2f} / (0.10 - 0.04) = \\text{{USD }} {v0:.2f}$."
                w_A = f"Option A is incorrect because it adds growth rate instead of subtracting in denominator."
                w_C = f"Option C is incorrect because it multiplies $D_1$ by $(1+g)$ again."
            elif prefix == "FI":
                flat = 1020.00 + (i * 5.0)
                accrued = 25.00 + (i * 2.5)
                full = round(flat + accrued, 2)
                full_err = round(flat + (accrued * 2), 2)

                stem = f"A corporate bond has a flat (clean) market price of USD {flat:,.2f}. The accrued interest since the last coupon date is USD {accrued:,.2f}. What is the full (dirty) price of the bond?"
                optA = f"USD {flat:,.2f}"
                optB = f"USD {full:,.2f}"
                optC = f"USD {full_err:,.2f}"
                correct = "B"
                exp = f"Full (Dirty) Price $= \\text{{Flat Price}} + \\text{{Accrued Interest}} = \\text{{USD }} {flat:,.2f} + \\text{{USD }} {accrued:,.2f} = \\text{{USD }} {full:,.2f}$."
                w_A = f"Option A is incorrect because it gives flat price without adding accrued interest."
                w_C = f"Option C is incorrect because it adds double coupon interest."
            elif prefix == "DER":
                strike = 50.0
                st = 55.0 + (i * 1.5)
                premium = 2.50
                payoff = st - strike
                profit = payoff - premium
                profit_err = payoff + premium

                stem = f"An investor purchases a European call option with a strike price of USD {strike:.2f}. At expiration, the underlying stock price is USD {st:.2f}. If the initial option premium was USD {premium:.2f}, what is the net profit to the option buyer?"
                optA = f"USD {profit:.2f}"
                optB = f"USD {payoff:.2f}"
                optC = f"USD {profit_err:.2f}"
                correct = "A"
                exp = f"Gross Payoff $= \\max(0, S_T - X) = \\text{{USD }} {payoff:.2f}$. Net Profit $= \\text{{Gross Payoff}} - \\text{{Premium}} = \\text{{USD }} {payoff:.2f} - \\text{{USD }} {premium:.2f} = \\text{{USD }} {profit:.2f}$."
                w_B = f"Option B is incorrect because it gives gross payoff without deducting premium paid."
                w_C = f"Option C is incorrect because it erroneously adds premium to gross payoff."
            elif prefix == "ALT":
                gross_ret = 6.0
                hurdle = 8.0
                stem = f"A private equity fund charges a 2% management fee and a 20% performance fee (carried interest) with an 8% hurdle rate. If the fund achieves a gross annual return of {gross_ret:.1f}%, what performance fee percentage is collected by the General Partner (GP)?"
                optA = "0.0%"
                optB = "1.2%"
                optC = "2.0%"
                correct = "A"
                exp = f"The hurdle rate ({hurdle:.1f}%) is the minimum return threshold required before performance fees activate. Because gross return ({gross_ret:.1f}%) is below hurdle rate, performance fee is 0.0%."
                w_B = "Option B is incorrect because it ignores the hurdle rate condition."
                w_C = "Option C is incorrect because it confuses management fee with performance fee."
            elif prefix == "PM":
                ret_p = 12.0 + (i * 0.5)
                rf = 3.0
                std_p = 15.0
                sharpe = round((ret_p - rf) / std_p, 2)
                sharpe_err = round(ret_p / std_p, 2)
                sharpe_err2 = round((ret_p - rf) / (std_p * 1.2), 2)

                stem = f"An investment portfolio achieves an expected annual return of {ret_p:.1f}% with a total standard deviation of {std_p:.1f}%. If the risk-free benchmark rate is {rf:.1f}%, what is the portfolio's Sharpe Ratio?"
                optA = f"{sharpe:.2f}"
                optB = f"{sharpe_err:.2f}"
                optC = f"{sharpe_err2:.2f}"
                correct = "A"
                exp = f"Sharpe Ratio $= (R_p - R_f) / \\sigma_p = ({ret_p:.1f}\\% - {rf:.1f}\\%) / {std_p:.1f}\\% = {sharpe:.2f}$."
                w_B = f"Option B is incorrect because it fails to subtract risk-free return benchmark."
                w_C = f"Option C is incorrect because of a risk denominator error."

            lines.append(f"### {q_id} | Difficulty: {diff} | Time: {time_sec}s | Pattern: {pattern} | Trap: Core Trap")
            lines.append("")
            lines.append("**Question:**")
            lines.append(stem)
            lines.append("")
            lines.append(f"A) {optA}")
            lines.append("")
            lines.append(f"B) {optB}")
            lines.append("")
            lines.append(f"C) {optC}")
            lines.append("")
            lines.append(f"**Correct Answer:** {correct}")
            lines.append("")
            lines.append(f"**Explanation:** {exp}")
            lines.append("")
            lines.append("**Wrong Answer Analysis:**")
            lines.append(f"- {w_A}")
            lines.append(f"- {w_C}" if correct != "C" else f"- {w_B}")
            lines.append("")
            lines.append(f"**LO Reference:** {prefix}-LO-{i+1:02d}")
            lines.append("")
            lines.append("---")
            lines.append("")

            q_num += 1

    return "\n".join(lines)

def main():
    am_content = build_paper("Session 1: Morning Paper", am_sections)
    with open(AM_PATH, "w", encoding="utf-8") as f:
        f.write(am_content)

    pm_content = build_paper("Session 2: Afternoon Paper", pm_sections)
    with open(PM_PATH, "w", encoding="utf-8") as f:
        f.write(pm_content)

    sys_content = am_content + "\n\n" + pm_content
    with open(SYS_PATH, "w", encoding="utf-8") as f:
        f.write(sys_content)

    print("Clean mock papers generated successfully!")

if __name__ == "__main__":
    main()
