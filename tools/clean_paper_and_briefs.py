#!/usr/bin/env python3
"""Clean em-dashes, update authorship, disclosure, and dates in manuscript and briefs."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def clean_em_dashes(text: str) -> str:
    # Replace em-dashes with colon, comma, or hyphen cleanly
    text = text.replace(" — ", " - ")
    text = text.replace("—", " - ")
    return text

def process_paper():
    paper_path = REPO_ROOT / "20_FULL_RESEARCH_PAPER.md"
    with open(paper_path, "r", encoding="utf-8") as fp:
        content = fp.read()
        
    # Replace header block up to Abstract
    header_pattern = re.compile(r"^# Beyond Hallownest:.*?### Abstract", re.DOTALL)
    new_header = """# Beyond Hallownest: Civilization, Memory, Divinity, Ecology, and Identity in *Hollow Knight* and *Hollow Knight: Silksong*

> **Notice:** AI-generated draft. Sources and claims under active verification.

**Lead Author and Curator:** Ismail  
**Drafting Assistance:** AI-assisted qualitative research pipeline  
**Primary Discipline:** Game Studies (Ludology, Spatial Narratology, Environmental Storytelling)  
**Secondary Disciplines:** Environmental Humanities, Ecocriticism, Political Theology, Philosophy, Arthropod Biology  
**Format & Style:** APA 7th Edition  
**Target Manuscript Scope:** Comparative Qualitative Case Study (10,000 to 13,000 words)  
**Research Cutoff Date:** 5 November 2026  
**Status:** Working Draft (Under Source & Claim Verification)

---

### Abstract"""

    content = header_pattern.sub(new_header, content)
    
    # Add Disclosure after Abstract keywords
    disclosure_block = """*Keywords:* Hollow Knight, Silksong, Metroidvania, environmental storytelling, Omelas dilemma, dark ecology, insect mythology, game studies, procedural rhetoric, spatial narratology.

---

### Research Origin and AI Disclosure

This study was initiated by Ismail as an in-depth portfolio and hobby research project exploring the nonhuman world-building, mythological structures, and political philosophy of *Hollow Knight* and *Hollow Knight: Silksong*. 

The initial draft of the monograph across all twenty chapters was generated in an initial exploratory session using an AI research pipeline. While the generated text successfully synthesized high-level theoretical connections and spatial analyses, it contained unverified academic claims, self-certified reviews, and unsourced game lore. The project is now in an active verification phase: every bibliographic entry is being verified against academic registries, game lore claims are being anchored to documented secondary sources in a structured evidence ledger, and all claims are calibrated strictly according to their evidentiary support without inflated certainty."""

    content = re.sub(r"\*Keywords:\*.*?(?=\n\n## 1\. Introduction)", disclosure_block, content, flags=re.DOTALL)
    
    # Fix Ludum Dare dates
    content = content.replace('In August 2014, participating in the Ludum Dare 27 competition under the theme "10 Seconds"',
                              'In August 2013, participating in the Ludum Dare 27 competition under the theme "10 Seconds"')
    content = content.replace('In late 2014, Gibson and Pellen pivoted to a 2D side-scrolling format for Ludum Dare 29',
                              'In April 2014, Gibson and Pellen pivoted to a 2D side-scrolling format for Ludum Dare 29')

    # Remove all em-dashes
    content = clean_em_dashes(content)
    
    with open(paper_path, "w", encoding="utf-8") as fp:
        fp.write(content)
    print("Updated 20_FULL_RESEARCH_PAPER.md")

def process_briefs():
    files = ["01_RESEARCH_BRIEF.md", "03_ANNOTATED_BIBLIOGRAPHY.md", "04_LITERATURE_SYNTHESIS.md"]
    for fname in files:
        fpath = REPO_ROOT / fname
        with open(fpath, "r", encoding="utf-8") as fp:
            text = fp.read()
        cleaned = clean_em_dashes(text)
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(cleaned)
        print(f"Cleaned em-dashes in {fname}")

def main():
    process_paper()
    process_briefs()

if __name__ == "__main__":
    main()
