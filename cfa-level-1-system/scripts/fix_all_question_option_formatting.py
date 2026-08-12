import os
import re

BASE_DIR = os.path.abspath(r"c:\Users\nasan\OneDrive\Desktop\junnu cfa\cfa-level-1-system")

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern: A ... B) ... C) ... on a single line
    def replace_options(match):
        opt_a = match.group(1).strip()
        opt_b = match.group(2).strip()
        opt_c = match.group(3).strip()
        return f"\nA) {opt_a}\nB) {opt_b}\nC) {opt_c}\n"

    # Match single-line options: A ... B) ... C) ...
    fixed_content = re.sub(
        r'(?:^|\n)\s*A[\)\.]?\s+(.*?)\s+B[\)\.]?\s+(.*?)\s+C[\)\.]?\s+(.*?)(?=\n|$)',
        replace_options,
        content
    )

    if fixed_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_content)
        print(f"Fixed single-line options in: {filepath}")
        return True
    return False

def main():
    fixed_count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                if fix_file(filepath):
                    fixed_count += 1
    print(f"Total markdown files fixed: {fixed_count}")

if __name__ == "__main__":
    main()
