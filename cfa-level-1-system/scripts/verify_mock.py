import json

with open('cfa-level-1-system/mock-exams/mock-exam-1-am.json', encoding='utf-8') as f:
    data = json.load(f)

qs = data['questions']
print("Total:", len(qs), "questions")
for i in [0, 1, 2, 26, 27, 28]:
    q = qs[i]
    sec = q.get('section','')[:35]
    stem = q.get('stem','')[:90]
    optA = q['options'].get('A','')[:60]
    optB = q['options'].get('B','')[:60]
    optC = q['options'].get('C','')[:60]
    print(f"\nQ{i+1} | {q['id']} | Correct: {q['correct']} | {sec}")
    print("  Stem:", stem)
    print("  A)", optA)
    print("  B)", optB)
    print("  C)", optC)

# Check answer distribution
from collections import Counter
answers = Counter(q['correct'] for q in qs)
print("\nAnswer distribution:", dict(answers))
