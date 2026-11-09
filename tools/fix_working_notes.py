#!/usr/bin/env python3
"""Add working notes notice banner and remove em-dashes across files 05 to 18."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

BANNER = "> **Notice:** Working notes, drafted with AI, sources not yet checked line by line.\n"

def process_file(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        
    new_lines = []
    banner_added = False
    
    # Check if banner already present
    full_text = "".join(lines)
    has_banner = "Working notes, drafted with AI" in full_text
    
    for idx, line in enumerate(lines):
        # Replace em-dashes
        # Common patterns:
        # "word—word" -> "word: word" or "word, word" depending on context, or "word - word"
        # " — " -> " - "
        # "—" -> " - " or ": "
        # In quotes: "* — The Pale King" -> "*: The Pale King" or "* (The Pale King)"
        cleaned_line = line
        if "\u2014" in cleaned_line:
            # Handle specific patterns cleanly
            cleaned_line = cleaned_line.replace(" — ", " - ")
            cleaned_line = cleaned_line.replace("—", " - ")
            
        new_lines.append(cleaned_line)
        
        # Insert banner after line 1 or line 2 (after initial H1)
        if not has_banner and not banner_added:
            if line.startswith("# "):
                new_lines.append("\n" + BANNER)
                banner_added = True

    with open(filepath, "w", encoding="utf-8") as fp:
        fp.writelines(new_lines)
    print(f"Processed: {filepath.name}")

def main():
    for num in range(5, 19):
        pattern = f"{num:02d}_*.md"
        matches = list(REPO_ROOT.glob(pattern))
        for m in matches:
            process_file(m)

if __name__ == "__main__":
    main()
