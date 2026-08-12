import re

test_text = """
During a portfolio review, Analyst #1 receives nonpublic information regarding a regulatory penalty. According to Standard I(A) Knowledge of the Law and Standard II(A), what is the required compliance protocol?

A) Act on the information immediately before market open.
B) Refrain from trading or inducing others to trade until the information is publicly disclosed.
C) Inform existing high-net-worth clients verbally while withholding written research reports.

Correct Answer: B
Explanation: Standard II(A) strictly mandates...
"""

# Regex that requires A) to be at the start of a line or paragraph, NOT after "Standard I"
stem_match = re.search(r'Question:\s*([\s\S]*?)(?=(?:\n|\r|<br>|<p>|^)\s*A\)\s+)', "Question:" + test_text, re.IGNORECASE)

opt_a_match = re.search(r'(?:\n|\r|<br>|<p>|^)\s*A\)\s+([\s\S]*?)(?=(?:\n|\r|<br>|<p>|^)\s*B\)\s+)', test_text)
opt_b_match = re.search(r'(?:\n|\r|<br>|<p>|^)\s*B\)\s+([\s\S]*?)(?=(?:\n|\r|<br>|<p>|^)\s*C\)\s+)', test_text)
opt_c_match = re.search(r'(?:\n|\r|<br>|<p>|^)\s*C\)\s+([\s\S]*?)(?=(?:\n|\r|<br>|<p>|^)\s*Correct Answer:)', test_text)

print("STEM:")
print(stem_match.group(1).strip() if stem_match else "NOT MATCHED")

print("\nOPTION A:")
print(opt_a_match.group(1).strip() if opt_a_match else "NOT MATCHED")

print("\nOPTION B:")
print(opt_b_match.group(1).strip() if opt_b_match else "NOT MATCHED")

print("\nOPTION C:")
print(opt_c_match.group(1).strip() if opt_c_match else "NOT MATCHED")
