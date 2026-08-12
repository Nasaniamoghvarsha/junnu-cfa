import os
import re

AM_PATH = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\mock-exams\mock-exam-1-am.md")

with open(AM_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Split questions by ### Q-
blocks = text.split("### Q-")
print(f"Total blocks split by '### Q-': {len(blocks) - 1}")

parsed_count = 0
for idx, b in enumerate(blocks[1:]):
    lines = b.strip().split("\n")
    header = lines[0]
    has_stem = any("Question:" in l for l in lines)
    has_opts = any("A)" in l and "B)" in l for l in lines) or (any("A)" in l for l in lines) and any("B)" in l for l in lines))
    has_ans = any("Correct Answer:" in l for l in lines)
    
    if has_stem and has_opts and has_ans:
        parsed_count += 1
    else:
        print(f"Block {idx+1} ({header[:30]}) missing fields: stem={has_stem}, opts={has_opts}, ans={has_ans}")

print(f"Successfully verified {parsed_count} / 90 questions complete!")
