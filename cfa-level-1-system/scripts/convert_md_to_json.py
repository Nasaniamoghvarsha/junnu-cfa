"""
convert_md_to_json.py  —  Final version
Converts CFA markdown question files to clean JSON.
Handles two formats:
  - Options on SAME line as question (ethics question bank format)
  - Options on SEPARATE lines (mock exam format)
"""
import os, re, json, sys

BASE = r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system"

FILES = {
    "mock-exams/mock-exam-1-am.md":
        "mock-exams/mock-exam-1-am.json",
    "mock-exams/mock-exam-1-pm.md":
        "mock-exams/mock-exam-1-pm.json",
    "question-bank/questions/01-ethics/standards-i-vii.md":
        "question-bank/questions/01-ethics/standards-i-vii.json",
}

# Discover remaining question bank files
qb_root = os.path.join(BASE, "question-bank", "questions")
for subj_dir in sorted(os.listdir(qb_root)):
    subj_path = os.path.join(qb_root, subj_dir)
    if not os.path.isdir(subj_path):
        continue
    for fname in os.listdir(subj_path):
        if fname.endswith(".md"):
            rel_src = f"question-bank/questions/{subj_dir}/{fname}"
            rel_dst = rel_src.replace(".md", ".json")
            FILES.setdefault(rel_src, rel_dst)


def extract_option(text, letter):
    """Extract option text for a given letter (A/B/C) from the question block."""
    next_letters = {"A": "B", "B": "C"}
    next_letter = next_letters.get(letter)

    if next_letter:
        # Match from Letter) up to the next option letter
        pat = rf'(?:^|\n)\s*{letter}\)\s+(.*?)(?=\n\s*{next_letter}\)\s+|\n\s*\*\*Correct|\n\s*---|\Z)'
    else:
        # C is the last option
        pat = rf'(?:^|\n)\s*{letter}\)\s+(.*?)(?=\n\s*\*\*Correct|\n\s*---|\Z)'

    m = re.search(pat, text, re.DOTALL | re.MULTILINE)
    if m:
        return m.group(1).strip().replace('\n', ' ')
    return ""


def parse_md_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        content = f.read()

    # ─── split into per-question blocks ────────────────────────────────────────
    # split on ### Q-... or #### Q-...
    raw_blocks = re.split(r'\n(?=#{3,4}\s+Q-)', content)

    file_title = ""
    sections   = []           # list of {name, startQ, questions:[]}
    questions  = []
    cur_section = ""

    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue

        # Top-level title
        if re.match(r'^#\s+', block) and not file_title:
            file_title = re.sub(r'^#\s+', '', block.split('\n')[0]).strip()
            # look for section headings inside this block too
            for line in block.split('\n'):
                if re.match(r'^##\s+', line):
                    cur_section = re.sub(r'^##\s+', '', line).strip()
                    sections.append(cur_section)
            continue

        # Pure section heading block (## ...)
        if re.match(r'^##\s+', block) and not re.match(r'^#{3,4}\s+Q-', block):
            cur_section = re.sub(r'^##\s+', '', block.split('\n')[0]).strip()
            if cur_section not in sections:
                sections.append(cur_section)
            continue

        # Question block
        hdr_m = re.match(r'^#{3,4}\s+(Q-[^\n]+)', block)
        if not hdr_m:
            # check for embedded section heading before question
            for line in block.split('\n'):
                if re.match(r'^##\s+', line):
                    cur_section = re.sub(r'^##\s+', '', line).strip()
                    if cur_section not in sections:
                        sections.append(cur_section)
            continue

        header_line = hdr_m.group(1).strip()
        rest        = block[hdr_m.end():].strip()

        # Also look for section heading inside block
        for line in rest.split('\n'):
            if re.match(r'^##\s+', line):
                new_sec = re.sub(r'^##\s+', '', line).strip()
                if new_sec not in sections:
                    sections.append(new_sec)
                    cur_section = new_sec

        # ── parse header fields ──────────────────────────────────────────────
        qid   = (re.search(r'(Q-[\w-]+)', header_line) or re.search(r'', '')).group(1) if re.search(r'(Q-[\w-]+)', header_line) else "Q-UNK"
        diff  = int(re.search(r'Difficulty:\s*(\d+)', header_line, re.I).group(1)) if re.search(r'Difficulty:\s*(\d+)', header_line, re.I) else 3
        time_ = re.search(r'Time:\s*(\d+s?)', header_line, re.I)
        time_ = time_.group(1) if time_ else "90s"
        pat_m = re.search(r'Pattern:\s*([^|]+?)(?:\s*\||\s*$)', header_line, re.I)
        pattern = pat_m.group(1).strip() if pat_m else "Standard"
        trap_m  = re.search(r'Trap:\s*([^|]+?)(?:\s*\||\s*$)', header_line, re.I)
        trap    = trap_m.group(1).strip() if trap_m else ""

        # ── question stem ────────────────────────────────────────────────────
        # Between **Question:** and first A) or **Correct Answer:**
        stem = ""
        stem_m = re.search(
            r'\*\*Question:\*\*\s*([\s\S]*?)(?=(?:^|\n)\s*A\)\s+|(?:^|\n)\s*\*\*Correct|\Z)',
            rest, re.MULTILINE
        )
        if stem_m:
            stem = stem_m.group(1).strip()
        else:
            # Fallback: everything before first A)
            before_a = re.split(r'(?:^|\n)\s*A\)\s+', rest, maxsplit=1)[0]
            stem = before_a.strip()
            # remove leading/trailing markdown bold markers from stem
            stem = re.sub(r'^\*\*[^*]+\*\*\s*', '', stem).strip()

        # Clean stem of leading **Question:** label
        stem = re.sub(r'^\*\*Question:\*\*\s*', '', stem).strip()

        # ── options ──────────────────────────────────────────────────────────
        opt_a = extract_option(rest, 'A')
        opt_b = extract_option(rest, 'B')
        opt_c = extract_option(rest, 'C')

        # ── correct answer ───────────────────────────────────────────────────
        corr_m = re.search(r'\*\*Correct Answer:\*\*\s*([A-C])', rest, re.I)
        correct = corr_m.group(1).upper() if corr_m else "A"

        # ── explanation ──────────────────────────────────────────────────────
        exp_m = re.search(
            r'\*\*Explanation:\*\*\s*([\s\S]*?)(?=\n\*\*Wrong Answer|\n\*\*LO|\n---|\Z)',
            rest, re.I
        )
        explanation = exp_m.group(1).strip() if exp_m else ""

        # ── wrong answer analysis ─────────────────────────────────────────────
        wrong_m = re.search(
            r'\*\*Wrong Answer Analysis:\*\*\s*([\s\S]*?)(?=\n\*\*LO|\n\*\*Related|\n\*\*Common|\n---|\Z)',
            rest, re.I
        )
        wrong = wrong_m.group(1).strip() if wrong_m else ""

        # ── LO Reference ─────────────────────────────────────────────────────
        lo_m = re.search(r'\*\*LO Reference:\*\*\s*([^\n]+)', rest, re.I)
        lo   = lo_m.group(1).strip() if lo_m else ""

        questions.append({
            "id":          qid,
            "section":     cur_section,
            "difficulty":  diff,
            "time":        time_,
            "pattern":     pattern,
            "trap":        trap,
            "lo":          lo,
            "stem":        stem,
            "options": {
                "A": opt_a,
                "B": opt_b,
                "C": opt_c
            },
            "correct":     correct,
            "explanation": explanation,
            "wrongAnalysis": wrong
        })

    return {
        "title":         file_title,
        "questionCount": len(questions),
        "questions":     questions
    }


def main():
    ok = err = skip = 0
    for src_rel, dst_rel in FILES.items():
        src = os.path.join(BASE, src_rel)
        dst = os.path.join(BASE, dst_rel)

        if not os.path.exists(src):
            print(f"  SKIP (not found): {src_rel}")
            skip += 1
            continue

        try:
            data = parse_md_file(src)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            q = data['questionCount']
            # quick validation
            valid = sum(
                1 for q_obj in data['questions']
                if q_obj['options']['A'] and q_obj['options']['B'] and q_obj['options']['C']
            )
            print(f"  OK  {src_rel:<60}  {q:3d} Qs  {valid:3d} valid options")
            ok += 1
        except Exception as e:
            print(f"  ERR {src_rel}: {e}")
            import traceback; traceback.print_exc()
            err += 1

    print(f"\nDone: {ok} converted, {err} errors, {skip} skipped")


if __name__ == "__main__":
    main()
