import os
import sys

# Directory for questions
QUESTIONS_DIR = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\question-bank\questions")

ETHICS_ADDITIONS = r"""---

### Q-ETH-0037 | Difficulty: 3 | Time: 90s | Pattern: Ethics Scenario | Trap: Misrepresentation & Guaranteed Returns

**Question:**
An investment manager presents a pitch deck to prospective clients stating: *"Our proprietary quantitative strategy guarantees a minimum return of 10% per annum under all market environments, backed by historical backtests."* Has the manager violated Standard I(C) Misrepresentation?

A) Yes, because guaranteeing investment returns and misrepresenting backtested results as guaranteed violates Standard I(C)
B) No, provided the firm's legal counsel approved the presentation deck
C) No, because backtested model results constitute empirical proof of strategy performance

**Correct Answer:** A

**Explanation:** Standard I(C) Misrepresentation strictly prohibits members and candidates from making any false, misleading, or guaranteed statements regarding investment returns. Guaranteed returns cannot be promised in equity or debt strategies, and backtested returns do not guarantee future performance.

**Wrong Answer Analysis:**
- B: Incorrect — legal counsel approval does not override the Code and Standards.
- C: Incorrect — backtested returns represent simulated historical models, not guaranteed future results.

**LO Reference:** LO-ETH-13 (Standard I(C) Misrepresentation)
**Related Concepts:** Guaranteed returns, misrepresentation, backtested models
**Common Misconception:** Believing legal approval permits making guaranteed return claims.
"""

QUANT_ADDITIONS = r"""---

### Q-QNT-0036 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Money-Weighted vs Time-Weighted Return

**Question:**
An investor deposits $100 at $t=0$. At $t=1$, the portfolio value is $120$, and she deposits an additional $100$. At $t=2$, the final portfolio value is $240$. The **money-weighted rate of return** (IRR) is closest to:

A) 11.5%
B) 13.1%
C) 15.0%

**Correct Answer:** B

**Explanation:** The money-weighted return is the Internal Rate of Return (IRR) setting Net Present Value (NPV) of cash flows to zero:
$$0 = -100 - \frac{100}{1+r} + \frac{240}{(1+r)^2}$$
Solving for $r$:
$$100(1+r)^2 + 100(1+r) - 240 = 0$$
Using TI BA II Plus CF key:
`CF0 = -100`, `C01 = -100`, `C02 = 240`, `IRR` $\to$ `CPT` $= 13.066\% \approx 13.1\%$.

**TI BA II Plus Keystrokes:**
- `CF` `2nd` `CLR WORK`
- `CF0 = -100` `ENTER` `↓`
- `C01 = -100` `ENTER` `↓` `F01 = 1` `↓`
- `C02 = 240` `ENTER`
- `IRR` `CPT` $\to 13.066\%$

**Wrong Answer Analysis:**
- A: Incorrect — miscalculated time-weighted return.
- C: Incorrect — simple average return calculation.

**LO Reference:** LO-QNT-11 (Money-Weighted vs Time-Weighted Return)
**Related Concepts:** Money-weighted return, IRR, cash flow timing
**Common Misconception:** Using simple arithmetic average instead of solving for IRR.
"""

ECON_ADDITIONS = r"""---

### Q-ECO-0036 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Real Exchange Rate Formula

**Question:**
The nominal exchange rate is $1.25$ USD per EUR ($S_{\text{USD/EUR}} = 1.25$). The price level in the Eurozone ($P_{\text{EUR}}$) is 110, and the price level in the US ($P_{\text{USD}}$) is 100. The **real exchange rate** ($q_{\text{USD/EUR}}$) is closest to:

A) 1.14
B) 1.38
C) 1.50

**Correct Answer:** B

**Explanation:** Real Exchange Rate Calculation:
$$q_{\text{d/f}} = S_{\text{d/f}} \times \left(\frac{P_{\text{foreign}}}{P_{\text{domestic}}}\right)$$
$$q_{\text{USD/EUR}} = 1.25 \times \left(\frac{110}{100}\right) = 1.25 \times 1.10 = 1.375 \approx 1.38$$

**TI BA II Plus Keystrokes:**
$1.25 \times (110 / 100) = 1.375 \to 1.38$

**Wrong Answer Analysis:**
- A: Incorrect — inverted price ratio ($1.25 \times \frac{100}{110} = 1.136$).
- C: Incorrect — added inflation index instead of multiplying ratio.

**LO Reference:** LO-ECO-08 (Real Exchange Rate Calculation)
**Related Concepts:** Real exchange rate, purchasing power parity, nominal exchange rate
**Common Misconception:** Inverting domestic and foreign price indices in the real rate formula.
"""

FSA_ADDITIONS = r"""---

### Q-FSA-0036 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Lease Accounting IFRS 16 Lessee

**Question:**
Under IFRS 16, a lessee enters into a 5-year equipment lease with annual lease payments of $20,000 paid at the end of each year. The lessee's incremental borrowing rate is 6%. At lease commencement, the lessee recognizes a Right-of-Use (ROU) Asset and Lease Liability of:

A) $84,247
B) $100,000
C) $106,000

**Correct Answer:** A

**Explanation:** Under IFRS 16, lessees recognize a ROU Asset and Lease Liability equal to the Present Value of future lease payments discounted at the interest rate implicit in the lease (or incremental borrowing rate):
$$PV = \text{PMT} \times \left[\frac{1 - (1+r)^{-n}}{r}\right] = 20,000 \times \left[\frac{1 - (1.06)^{-5}}{0.06}\right] = \$84,247.28$$

**TI BA II Plus Keystrokes:**
- `N = 5`, `I/Y = 6`, `PMT = -20000`, `FV = 0`
- `PV` `CPT` $\to 84,247.28$

**Wrong Answer Analysis:**
- B: Incorrect — simple sum of nominal payments ($5 \times 20,000 = \$100,000$).
- C: Incorrect — added interest without discounting.

**LO Reference:** LO-FSA-12 (IFRS 16 Lease Accounting Lessee)
**Related Concepts:** IFRS 16, Right-of-Use asset, lease liability present value
**Common Misconception:** Using nominal lease payments instead of discounted present value.
"""

ECON_ADDITIONS = """---

### Q-ECO-0036 | Difficulty: 3 | Time: 90s | Pattern: Direct Calculation | Trap: Real Exchange Rate Formula

**Question:**
The nominal exchange rate is $1.25$ USD per EUR ($S_{\text{USD/EUR}} = 1.25$). The price level in the Eurozone ($P_{\text{EUR}}$) is 110, and the price level in the US ($P_{\text{USD}}$) is 100. The **real exchange rate** ($q_{\text{USD/EUR}}$) is closest to:

A) 1.14
B) 1.38
C) 1.50

**Correct Answer:** B

**Explanation:** Real Exchange Rate Calculation:
$$q_{\text{d/f}} = S_{\text{d/f}} \times \left(\frac{P_{\text{foreign}}}{P_{\text{domestic}}}\right)$$
$$q_{\text{USD/EUR}} = 1.25 \times \left(\frac{110}{100}\right) = 1.25 \times 1.10 = 1.375 \approx 1.38$$

**TI BA II Plus Keystrokes:**
$1.25 \times (110 / 100) = 1.375 \to 1.38$

**Wrong Answer Analysis:**
- A: Incorrect — inverted price ratio ($1.25 \times \frac{100}{110} = 1.136$).
- C: Incorrect — added inflation index instead of multiplying ratio.

**LO Reference:** LO-ECO-08 (Real Exchange Rate Calculation)
**Related Concepts:** Real exchange rate, purchasing power parity, nominal exchange rate
**Common Misconception:** Inverting domestic and foreign price indices in the real rate formula.

---

### Q-ECO-0037 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Tariff vs Quota Economic Impact

**Question:**
Compared to an import tariff that generates equivalent price increases, an **import quota** results in:

A) Greater government tariff revenue
B) Transfer of quota rents to foreign exporters if licenses are granted to foreign firms
C) Zero deadweight loss to the domestic economy

**Correct Answer:** B

**Explanation:** While both tariffs and quotas restrict trade and cause deadweight welfare loss, a tariff generates tax revenue directly for the domestic government. A quota generates **quota rents**; if foreign exporters receive the quota licenses, those rents accrue to foreign entities rather than domestic government revenues.

**Wrong Answer Analysis:**
- A: Incorrect — quotas do not automatically generate government tariff revenue unless licenses are auctioned.
- C: Incorrect — both tariffs and quotas create deadweight deadweight loss.

**LO Reference:** LO-ECO-09 (Tariffs vs Quotas Economic Effects)
**Related Concepts:** Trade protectionism, import quotas, tariffs, quota rents
**Common Misconception:** Believing tariffs and quotas have identical revenue distribution.
"""

FSA_ADDITIONS = """---

### Q-FSA-0036 | Difficulty: 4 | Time: 120s | Pattern: Multi-Step Calculation | Trap: Lease Accounting IFRS 16 Lessee

**Question:**
Under IFRS 16, a lessee enters into a 5-year equipment lease with annual lease payments of $20,000 paid at the end of each year. The lessee's incremental borrowing rate is 6%. At lease commencement, the lessee recognizes a Right-of-Use (ROU) Asset and Lease Liability of:

A) $84,247
B) $100,000
C) $106,000

**Correct Answer:** A

**Explanation:** Under IFRS 16, lessees recognize a ROU Asset and Lease Liability equal to the Present Value of future lease payments discounted at the interest rate implicit in the lease (or incremental borrowing rate):
$$PV = \text{PMT} \times \left[\frac{1 - (1+r)^{-n}}{r}\right] = 20,000 \times \left[\frac{1 - (1.06)^{-5}}{0.06}\right] = \$84,247.28$$

**TI BA II Plus Keystrokes:**
- `N = 5`, `I/Y = 6`, `PMT = -20000`, `FV = 0`
- `PV` `CPT` $\to 84,247.28$

**Wrong Answer Analysis:**
- B: Incorrect — simple sum of nominal payments ($5 \times 20,000 = \$100,000$).
- C: Incorrect — added interest without discounting.

**LO Reference:** LO-FSA-12 (IFRS 16 Lease Accounting Lessee)
**Related Concepts:** IFRS 16, Right-of-Use asset, lease liability present value
**Common Misconception:** Using nominal lease payments instead of discounted present value.

---

### Q-FSA-0037 | Difficulty: 3 | Time: 90s | Pattern: Concept Comparison | Trap: Goodwill Impairment IFRS vs US GAAP

**Question:**
Under US GAAP, goodwill impairment testing is conducted at the **reporting unit** level using a single-step quantitative test. Under IFRS, goodwill impairment testing is conducted at the:

A) Operating segment level using a two-step test
B) Cash-generating unit (CGU) level comparing carrying value to recoverable amount
C) Individual intangible asset level

**Correct Answer:** B

**Explanation:** Under IFRS (IAS 36), goodwill is allocated to **Cash-Generating Units (CGUs)**. Impairment occurs when the CGU's carrying amount exceeds its **recoverable amount** (the higher of fair value less costs of disposal and value in use).

**Wrong Answer Analysis:**
- A: Incorrect — US GAAP formerly used a two-step test; IFRS uses CGUs and single-step recoverable amount comparison.
- C: Incorrect — goodwill cannot be tested individually; it must be tested at CGU level.

**LO Reference:** LO-FSA-13 (Goodwill Impairment IFRS vs US GAAP)
**Related Concepts:** Goodwill impairment, Cash-Generating Unit (CGU), IAS 36, US GAAP reporting unit
**Common Misconception:** Confusing US GAAP reporting units with IFRS Cash-Generating Units.
"""

def append_to_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content)

def main():
    eth_path = os.path.join(QUESTIONS_DIR, "01-ethics", "standards-i-vii.md")
    qnt_path = os.path.join(QUESTIONS_DIR, "02-quantitative-methods", "quantitative-methods-questions.md")
    eco_path = os.path.join(QUESTIONS_DIR, "03-economics", "economics-questions.md")
    fsa_path = os.path.join(QUESTIONS_DIR, "04-financial-statement-analysis", "fsa-questions.md")

    append_to_file(eth_path, ETHICS_ADDITIONS)
    append_to_file(qnt_path, QUANT_ADDITIONS)
    append_to_file(eco_path, ECON_ADDITIONS)
    append_to_file(fsa_path, FSA_ADDITIONS)

    print("Batch 1 execution complete across primary subject files.")

if __name__ == "__main__":
    main()
