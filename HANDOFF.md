# Handoff: Agentic Research Next Steps

Repo: smile-plzz/hollow-knight-both-games (single commit 8b2d976, 2026-11-05)
Prepared: 2026-11-09 for Ismail, to pass to the next research agent(s)
Working title of the project: "Beyond Hallownest: Civilization, Memory, Divinity, Ecology, and Identity in Hollow Knight and Hollow Knight: Silksong"

## 1. Bottom line

The repo is a complete-looking but unverified AI draft. It holds an 11.8k-word manuscript, 20 supporting analysis files (about 45k words), a 38-item bibliography, a 20-row claim matrix, a "peer review" and an "integrity audit" that certifies everything PASS. The structure and writing are strong. The evidence base is not. The next phase is not more writing. It is verification, evidence capture, and honest relabeling.

Treat every "Verified", "PASS", "Tier 1 Confirmed Canon" and "independent" label in the repo as a claim to be tested, not a result.

## 2. What the repo contains

| Area | Files | State |
|---|---|---|
| Framing | README, 00_PROJECT_README, 01_RESEARCH_BRIEF, context, dev-log, CHANGELOG | Consistent in tone, some number conflicts (see 4.6) |
| Search and sources | 02 search log, 03 annotated bibliography, 04 literature synthesis, references.bib | 38 sources, only 6 are direct scholarship on the games |
| Game analysis | 05 to 18 (narratives, characters, areas, bosses, endings, mechanics, ecology, relationship maps) | Fluent, mostly unsourced at claim level |
| Evidence register | 19_CLAIM_AND_EVIDENCE_MATRIX.csv | 20 rows, 0 Tier 3 |
| Manuscript | 20_FULL_RESEARCH_PAPER.md | 11,840 words including references, 20 numbered sections |
| Review and audit | 21_PEER_REVIEW, 22_REVISION_AND_INTEGRITY_REPORT, 23_PROCESS_RECORD | Written by the same agent that wrote the paper |

Workflow claimed: the `academic-research-skills` pipeline (deep-research, academic-paper, reviewer, integrity gates). It was run on Windows through an "Antigravity" agent.

## 3. Spot checks done on 2026-11-09 (by web search and page fetch)

| Source in repo | Result | Notes |
|---|---|---|
| Andriano and Caracciolo 2025, Eludamos 16(2), 9-28 | Confirmed | Publisher page matches title, pages and DOI. Published 2025-12-19. Abstract fits how the repo uses it. |
| Wysocki 2026, JRFM 12(1) | Exists, content unverified | DOI matches. It is a short media review by an independent scholar, published 2026-05-15. I only saw the abstract page. The repo attributes detailed arguments to it (choral polyphony, somatic extraction, Eliade and Otto). Read the PDF at https://jrfm.eu/index.php/ojs_jrfm/article/download/539/396/2785 before trusting any of that. |
| Morales-Primo 2026, Journal of Geek Studies | Exists, repo likely overstates it | Page dated 2026-04-16. Abstract compares abilities to spitting spiders, bolas spiders, ray spiders, ballooning and ant wound care, and says many abilities are fictional. CLM-007 says the silk mechanics "mirror major ampullate silk biopolymers" and CLM-015 cites it for Bind frame data. Neither matches the abstract. Volume, issue, pages and Zenodo DOI were not shown on the page. |
| Grunberg 2024, Games and Culture | Exists | SAGE DOI matches. Volume 19 confirmed by index, issue and pages (4, 433-448) not checked. The ending-by-ending reading attributed to him is unchecked. |
| Caracciolo 2026, JGVW 18(1) | Exists | Intellect page and DOI match. The claim that it analyzes Silksong and Elden Ring is unchecked. |
| Zhang 2026, ICCT 2026, "IACST" | Not found | Two searches found nothing. No DOI, no page range, publisher unidentified. This source carries real weight: manuscript 3.1 and 4, CLM-011, Strand 1 of the literature synthesis. Highest priority to resolve. |
| ACMI 2022 "From Ludum Dare to Pharloom" | Probably wrong title or URL | A real ACMI piece surfaced at acmi.net.au/stories-and-ideas/hollow-knight-bound-by-struggle/. The cited URL was not found. The paper hangs its answer to the "iceberg illusion" critique on an ACMI claim that "90% of the framework is drafted internally". Find the source text or delete the claim. |
| Sea of Sorrow | Announced, apparently still unreleased | Game Informer dated the announcement 2025-12-16 (repo says 12-15, possibly a time zone gap). Free nautical expansion, window "next year". Recent coverage says fans worry it may slip past 2026. The repo is internally inconsistent: "2026" in context.md, "late 2026 / early 2027" in 00_PROJECT_README. Re-check on every pass. |

Not checked, from my own knowledge only (verify): the paper dates Ludum Dare 27 ("10 Seconds") to August 2014 and Ludum Dare 29 ("Beneath the Surface") to late 2014. I believe LD27 was August 2013 and LD29 was April 2014. Also unverified: Kickstarter figures (AUD 57,129, 2,158 backers), staff name "Jasmine Vine", a 2020 Larkin Bandcamp Daily interview whose title mentions Silksong's score, the Nintendo Australia interview URL, and the Team Cherry blog URLs (including the "holiday2025" slug and title).

## 4. Problems, ranked

### P0: integrity

4.1 Self-certification. The same agent drafted the paper, played the 5-seat "independent" reviewers, wrote the revision response, and issued "PASS, zero violations". The review is unanimous and calls the paper "landmark". None of that is evidence. Relabel 21 and 22 as simulated review and self-audit, or replace them with a real independent pass.

4.2 Timeline does not support the claimed process. dev-log timestamps run 07:53 to 08:26 on 2026-11-05. Stage 1 (157 records screened, 52 appraised, 38 "cross-checked against publisher registries") is logged as finished in 3 minutes, and the full suite with manuscript in 16. Treat the screening and verification numbers as unsupported.

4.3 Methods describe work that left no artifacts. Section 5.1 claims comprehensive reading of all dialogue and journal entries, frame-by-frame hitbox analysis, and close listening to both complete soundtracks. CLM-015 cites "empirical frame data". The repo has no transcripts, frame data, audio notes, captures or playthrough logs. The search log itself excludes fandom wikis, so the real basis of the lore claims is undeclared. Either produce the evidence (Phase 2) or rewrite 5.1 to say what was actually done.

4.4 Evidence density is far below the confidence shown. The paper carries 175 "[Tier 1]" tags, 46 "[Tier 2]" and none for Tier 3, although 5.2 promises speculative claims are marked. The claim register has 20 rows, so the "100% claim audit" covers about one tenth of the Tier 1 assertions. Manuscript sections 6 to 8, the core lore reconstruction, contain no in-text citations.

4.5 Authorship and disclosure. The paper lists "Lead Authors: Academic Game Studies Research Collaborative" and the process record lists an "Antigravity Collaborative Academic Team" as principal investigators. Ismail is the actual author. Needs a plain AI-assistance disclosure. 23_PROCESS_RECORD also contains a Vim tutorial that leaked from another tool's persistent instruction. Remove it.

4.6 Internal inconsistencies. Examples of per-file word counts in 23_PROCESS_RECORD versus a measured count: 07 claims 3,850 and has 1,899; 12 claims 3,920 and has 1,786; 08 claims 4,110 and has 2,591; 13 claims 3,880 and has 1,990; 00 claims 1,180 and has 749. CHANGELOG says 24 deliverables, the README lists more. dev-log and CHANGELOG cite a `walkthrough.md` that is not in the repo.

### P1: scholarship and content

4.7 Reference hygiene. Nagel (1979), Suits (1978), Wolf (2012) and Team Cherry (2017) are in the reference list and never cited in the body. Calleja, Juul, Parish, Otto, Summers, Donnelly and Wilson and Hölldobler appear once each.

4.8 Devil's advocate challenges only partly answered. The review raised five. Section 19 rebuts three (lore coherence, biology as aesthetics, difficulty). "Intentionality of the Void" and "Hornet's voiced shift" are not addressed there. Check whether they appear elsewhere. The one substantive rebuttal leans on the unverified ACMI statistic.

4.9 Novelty claim. The introduction says no single study has unified these strands. Only 6 direct sources were found, 4 of them 2026 items and some short reviews. A real gap search is needed. Unvetted leads that surfaced in my searches: First Person Scholar "For All the Broken Vessels", a Zenodo "pure vessels" PDF (20200619), and a Game Studies 2025 article on indie games and mental health depiction. Check relevance before use.

4.10 Canon numbering risk. The matrix and paper number the endings (Ending 3 as Dream No More, Ending 4 as Embrace the Void, "6 endings"). Confirm numbering and count against an authoritative source and against how Grunberg uses them.

## 5. Plan for the next agent(s)

Run phases in order. Phases 1 and 2 split cleanly across parallel agents.

### Phase 0: triage and honesty pass (one session)
- Branch, then add a status banner to README: "AI-generated draft. Sources and claims under verification."
- Relabel 21 as "Simulated multi-perspective review (AI)" and 22 as "AI self-audit, not independent". Remove the "PASS" certificate language.
- Fix authorship lines, add an AI-assistance disclosure, delete the Vim section, reconcile word counts, resolve the walkthrough.md reference.
- Done when: no document claims independence, certification or verification that did not happen.

### Phase 1: source verification (parallel, one agent per source)
For each of the 38 references create `verification/<bibkey>.md` with: URL, retrieval date, metadata match (authors, venue, volume, pages, DOI), what the source actually argues in 2 to 3 sentences, which paper and matrix lines rely on it, and a status of VERIFIED, PARTIAL, UNVERIFIED or NOT FOUND.
- Order: Zhang, Wysocki (read the PDF), Morales-Primo (find volume, pages, DOI, read the full text), Grunberg, Caracciolo, ACMI, Larkin, Nintendo Australia, Team Cherry blog URLs, Kickstarter page, Ludum Dare dates.
- Replace or delete anything NOT FOUND. Correct every overstated attribution (start with CLM-007, CLM-010, CLM-011, CLM-015).
- Done when: every reference has a status, no NOT FOUND source remains in the paper, and each scholarly attribution matches the text it cites.

### Phase 2: primary-evidence ledger
A cloud agent cannot play either game. Decide with Ismail which evidence route to use, and record it in the ledger.
- Route A: Ismail supplies captures, notes or transcripts for the passages that matter.
- Route B: use community wikis and Team Cherry material as clearly labeled secondary sources, with page and retrieval date.
- Build `evidence_ledger.csv`: claim_id, game, region or NPC or item, short in-game text anchor (paraphrase or under 15 words), game version, how obtained, tier, paper section. Extend CLM from 20 rows to cover every [Tier 1] sentence (about 175), and add real Tier 3 rows.
- Done when: a script reports 100% of [Tier 1] sentences in the paper map to a ledger row with a source.

### Phase 3: manuscript revision
- Rewrite 5.1 to describe the method actually used.
- Add citations to sections 6 to 8 and any other uncited lore passage, then cite or remove the four orphan references.
- Fix the Ludum Dare and other chronology errors found in Phase 1.
- Answer the two missing devil's advocate challenges. Replace the ACMI statistic with a sourced claim or cut it.
- Soften or substantiate the novelty claim after a proper gap search.
- Keep the Sea of Sorrow scope note, with the date re-checked.
- Done when: all paper claims trace to a ledger row or a verified source, and a rerun of the audit script is clean.

### Phase 4: genuine independent review
Use a fresh agent with no access to the authoring context and an adversarial brief, sampling claims against sources. Add Ismail or a human reader. Log the result as "AI-assisted review", never as peer review.

### Phase 5: scope and delivery
Decide the venue (course paper, blog series, journal submission), convert to the required format, and decide what happens to the 20 supporting files. Recommendation: keep them as working notes, label them unsourced, and promote only the parts the ledger supports.

## 6. Suggested tooling (small, one-time)
`tools/audit.py` to run on every commit: reference-versus-body citation check, tier tag counts per section, ledger coverage percent, word counts per file compared with the process record, and a lint for placeholder text. Add a link checker that runs where outbound access is allowed.

## 7. Operating rules for the agents
- Never mark your own work PASS. Record what was checked, where, and when.
- Quote at most a few words from any source. Paraphrase the rest.
- No invented DOIs, page numbers or URLs. If a field cannot be confirmed, write "not confirmed".
- Do not add lore without a source and a tier.
- Writing style for Ismail: no em-dashes.
- Commit per phase with a plain message. Push access needs the repo attached with push permission.

## 8. Open questions for Ismail
1. What is the goal: coursework, portfolio piece, or journal submission? It sets the rigor bar and the cut list.
2. Can you supply playthrough notes or captures for the evidence ledger, or should the work lean on labeled secondary sources?
3. Do you want the 20 supporting files kept, trimmed, or demoted to working notes?
4. How should AI assistance be disclosed in the final piece?

## 9. Coverage of this analysis
Read in full: README, context, dev-log, CHANGELOG, 00, 01, 02, 19, 21, 22, 23. Read in part: paper (sections 1 to 6, 19 to references, plus a heading and citation scan of the rest), 03, 04. Scanned by word count and headings only: 05 to 18, references.bib. External spot checks are listed in section 3. The repo's claims about game lore were not tested against the games.
