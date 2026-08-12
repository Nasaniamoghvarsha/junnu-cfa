import os
import re

AM_PATH = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system\mock-exams\mock-exam-1-am.md")

with open(AM_PATH, "r", encoding="utf-8") as f:
    text = f.read()

h3_matches = re.findall(r'^###\s+(.*)', text, re.MULTILINE)
print(f"Total H3 headers starting with ### in mock-exam-1-am.md: {len(h3_matches)}")
for idx, h in enumerate(h3_matches[:15]):
    print(f"  {idx+1}. {h}")
