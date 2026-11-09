#!/usr/bin/env python3
"""Audit script for hollow-knight-both-games research suite.

Checks:
1. File existence and actual word counts vs process record
2. Em-dash linting (Ismail writing style: no em-dashes)
3. Tier tag distribution across manuscript
4. Reference citations in manuscript vs references.bib
5. Integrity / honesty labels (no simulated 'PASS' certificates)
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def count_words(filepath: Path) -> int:
    with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
        text = fp.read()
    return len(text.split())

def check_word_counts():
    print("--- 1. FILE WORD COUNTS ---")
    md_files = sorted(REPO_ROOT.glob("*.md"))
    total_words = 0
    results = {}
    for f in md_files:
        w = count_words(f)
        total_words += w
        results[f.name] = w
        print(f"  {f.name:<45} : {w:>6} words")
    print(f"  {'TOTAL':<45} : {total_words:>6} words\n")
    return results

def check_em_dashes():
    print("--- 2. EM-DASH LINT (Style rule: No em-dashes) ---")
    md_files = sorted(REPO_ROOT.glob("*.md"))
    violations = {}
    em_dash_char = "\u2014"
    for f in md_files:
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            lines = fp.readlines()
        f_violations = []
        for idx, line in enumerate(lines, 1):
            if em_dash_char in line:
                f_violations.append((idx, line.strip()))
        if f_violations:
            violations[f.name] = f_violations
            print(f"  [WARN] {f.name}: {len(f_violations)} line(s) with em-dashes")
    if not violations:
        print("  [OK] Zero em-dashes found across all Markdown files.")
    print()
    return violations

def check_tier_tags():
    print("--- 3. TIER TAG AUDIT (20_FULL_RESEARCH_PAPER.md) ---")
    paper_path = REPO_ROOT / "20_FULL_RESEARCH_PAPER.md"
    if not paper_path.exists():
        print("  [ERROR] 20_FULL_RESEARCH_PAPER.md not found.")
        return {}
    with open(paper_path, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    t1 = len(re.findall(r"\[Tier 1[^\]]*\]", content))
    t2 = len(re.findall(r"\[Tier 2[^\]]*\]", content))
    t3 = len(re.findall(r"\[Tier 3[^\]]*\]", content))
    print(f"  Tier 1 (Confirmed Canon)      : {t1}")
    print(f"  Tier 2 (Strongly Supported)   : {t2}")
    print(f"  Tier 3 (Speculative / Theory) : {t3}")
    print(f"  Total tier tags               : {t1 + t2 + t3}\n")
    return {"t1": t1, "t2": t2, "t3": t3}

def check_citations():
    print("--- 4. BIBLIOGRAPHY CITATION AUDIT ---")
    bib_path = REPO_ROOT / "references.bib"
    paper_path = REPO_ROOT / "20_FULL_RESEARCH_PAPER.md"
    if not bib_path.exists() or not paper_path.exists():
        print("  [ERROR] references.bib or 20_FULL_RESEARCH_PAPER.md missing.")
        return
    with open(bib_path, "r", encoding="utf-8", errors="ignore") as fp:
        bib_text = fp.read()
    
    # Parse entries: key, author, year
    entries = re.findall(r"@(\w+)\{([^,]+),(.*?)(?=@\w+\{|\Z)", bib_text, re.DOTALL)
    with open(paper_path, "r", encoding="utf-8", errors="ignore") as fp:
        paper_full_text = fp.read()
    
    # Isolate body text before references section
    body_parts = re.split(r"\n#{1,4}\s+References\b", paper_full_text, flags=re.IGNORECASE)
    paper_text = body_parts[0] if len(body_parts) > 1 else paper_full_text
    paper_norm = unicodedata.normalize('NFKD', paper_text).encode('ASCII', 'ignore').decode('utf-8')
    paper_norm = paper_norm.replace("’", "'")
        
    found = []
    missing = []
    for entry_type, key, body in entries:
        author_match = re.search(r"author\s*=\s*[\"{]+(.*?)[\"}]+,", body, re.IGNORECASE | re.DOTALL)
        year_match = re.search(r"year\s*=\s*[\"{]?(\d{4})[\"}]?", body, re.IGNORECASE)
        author_surname = ""
        if author_match:
            raw_author = re.split(r"\s+and\s+", author_match.group(1), flags=re.IGNORECASE)[0].strip()
            # Clean latex accents and braces
            raw_author = raw_author.replace("{", "").replace("}", "")
            raw_author = re.sub(r"\\['`^\"~]?([a-zA-Z])", r"\1", raw_author)
            raw_author = unicodedata.normalize('NFKD', raw_author).encode('ASCII', 'ignore').decode('utf-8')
            # If "Last, First"
            if "," in raw_author:
                author_surname = raw_author.split(",")[0].strip()
            else:
                author_surname = raw_author.split()[-1].strip()
        year = year_match.group(1) if year_match else ""
        
        # Check if key or author + year or author alone is cited
        pattern = re.compile(rf"\b{re.escape(author_surname)}(?:'s|s)?\b.*\b{year}\b", re.IGNORECASE)
        pattern_author = re.compile(rf"\b{re.escape(author_surname)}(?:'s|s)?\b", re.IGNORECASE)
        
        if (key in paper_text or 
            (author_surname and pattern.search(paper_norm)) or 
            (author_surname and pattern_author.search(paper_norm)) or
            key.split("20")[0] in paper_norm.lower()):
            found.append((key, author_surname, year))
        else:
            missing.append((key, author_surname, year))
            
    print(f"  Total BibTeX entries          : {len(entries)}")
    print(f"  Referenced in paper body      : {len(found)}")
    print(f"  Unreferenced in paper body    : {len(missing)}")
    if missing:
        for k, a, y in missing:
            print(f"    - {k} ({a}, {y})")
    print()

def check_honesty_labels():
    print("--- 5. HONESTY AND INDEPENDENCE AUDIT ---")
    files_to_check = [
        "README.md",
        "00_PROJECT_README.md",
        "21_PEER_REVIEW.md",
        "22_REVISION_AND_INTEGRITY_REPORT.md",
        "23_PROCESS_RECORD.md"
    ]
    problem_terms = [
        "status: pass",
        "pass (zero violations",
        "certified pass",
        "independent peer review report",
        "5-seat independent review panel",
        "lead authors: academic game studies research collaborative"
    ]
    flagged = False
    for fname in files_to_check:
        fpath = REPO_ROOT / fname
        if not fpath.exists():
            continue
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            txt = fp.read()
        for term in problem_terms:
            if term.lower() in txt.lower():
                print(f"  [FLAG] '{term}' found in {fname}")
                flagged = True
    if not flagged:
        print("  [OK] No unwarranted self-certification or false independence claims found.")
    print()

def main():
    print("==================================================")
    print(" HOLLOW KNIGHT RESEARCH SUITE AUDIT")
    print("==================================================\n")
    check_word_counts()
    check_em_dashes()
    check_tier_tags()
    check_citations()
    check_honesty_labels()
    print("==================================================")
    print(" AUDIT FINISHED")
    print("==================================================")

if __name__ == "__main__":
    main()
