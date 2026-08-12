"""
build_mock_from_qbank.py
Builds proper mock exam JSON files by sampling real questions from the question bank JSON files.
AM Paper: Ethics(27) + Quant(14) + Econ(14) + FSA(22) + Corporate(13) = 90
PM Paper: Equity(22) + Fixed Income(22) + Derivatives(11) + Alt Inv(14) + PM(21) = 90
"""
import json, os, random

BASE = r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system"

QBANK = {
    "ethics": "question-bank/questions/01-ethics/standards-i-vii.json",
    "quant":  "question-bank/questions/02-quantitative-methods/quantitative-methods-questions.json",
    "econ":   "question-bank/questions/03-economics/economics-questions.json",
    "fsa":    "question-bank/questions/04-financial-statement-analysis/fsa-questions.json",
    "corp":   "question-bank/questions/05-corporate-issuers/corporate-issuers-questions.json",
    "equity": "question-bank/questions/06-equity-investments/equity-questions.json",
    "fi":     "question-bank/questions/07-fixed-income/fixed-income-questions.json",
    "deriv":  "question-bank/questions/08-derivatives/derivatives-questions.json",
    "alt":    "question-bank/questions/09-alternative-investments/alternative-investments-questions.json",
    "pm":     "question-bank/questions/10-portfolio-management/portfolio-management-questions.json",
}

def load_qs(key):
    path = os.path.join(BASE, QBANK[key])
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    # Filter: only keep questions with all 3 options populated
    valid = [q for q in data["questions"]
             if q["options"].get("A") and q["options"].get("B") and q["options"].get("C")]
    return valid

def sample(pool, n, prefix):
    """Sample n questions and renumber their IDs with mock exam prefix."""
    random.seed(42)  # deterministic so same seed = same paper
    chosen = random.sample(pool, min(n, len(pool)))
    for i, q in enumerate(chosen, 1):
        q["id"] = f"{prefix}-{i:03d}"
    return chosen

def build_paper(title, sections, out_path):
    """
    sections: list of (label_name, subject_key, count)
    """
    all_questions = []
    for section_name, key, count in sections:
        pool = load_qs(key)
        qs = sample(pool, count, f"MOCK-{key.upper()[:3]}")
        for q in qs:
            q["section"] = section_name
        all_questions.extend(qs)

    data = {
        "title": title,
        "questionCount": len(all_questions),
        "questions": all_questions
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Built: {out_path}  ({len(all_questions)} questions)")
    return data

def main():
    am_sections = [
        ("Section A: Ethical & Professional Standards", "ethics", 27),
        ("Section B: Quantitative Methods",             "quant",  14),
        ("Section C: Economics",                        "econ",   14),
        ("Section D: Financial Statement Analysis",     "fsa",    22),
        ("Section E: Corporate Issuers",                "corp",   13),
    ]
    pm_sections = [
        ("Section F: Equity Investments",               "equity", 22),
        ("Section G: Fixed Income",                     "fi",     22),
        ("Section H: Derivatives",                      "deriv",  11),
        ("Section I: Alternative Investments",          "alt",    14),
        ("Section J: Portfolio Management",             "pm",     21),
    ]

    am_path = os.path.join(BASE, "mock-exams/mock-exam-1-am.json")
    pm_path = os.path.join(BASE, "mock-exams/mock-exam-1-pm.json")

    build_paper("CFA Level I — Official Mock Exam 1 (Session 1: Morning Paper)", am_sections, am_path)
    build_paper("CFA Level I — Official Mock Exam 1 (Session 2: Afternoon Paper)", pm_sections, pm_path)
    print("\nDone! Mock exam JSONs rebuilt from real question bank questions.")

if __name__ == "__main__":
    main()
