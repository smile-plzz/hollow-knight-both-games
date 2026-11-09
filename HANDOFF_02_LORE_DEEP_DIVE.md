# Handoff 02: Deep Story, Character and Lore Research

Repo: smile-plzz/hollow-knight-both-games (branch master, HEAD at time of writing: 73a181d)
Prepared: 2026-11-09 for Ismail, to be executed by one agent in one long session
Supersedes the "next steps" in HANDOFF.md for lore work. HANDOFF.md stays as the record of the first audit.

## 0. Kickoff prompt (paste this to the agent)

You are continuing a Hollow Knight and Hollow Knight: Silksong research project owned by Ismail. Read HANDOFF_02_LORE_DEEP_DIVE.md fully before touching anything. Work through Phases A to K in order, commit at every phase boundary, and keep a task list. The goal is a deep, honest, well-sourced reference on the story, characters and lore of both games. You cannot play the games, so every claim must rest on a labeled secondary source with a URL and a retrieval date. Never mark your own work PASS, never invent names or sources, and write no em-dashes. If time runs short, follow the cut line in section 8, not a shortcut on evidence.

## 1. Where things stand

### 1.1 What exists (as of 73a181d)
| Item | State |
|---|---|
| Manuscript 20_FULL_RESEARCH_PAPER.md | 12,390 words, 20 sections, 176 Tier 1 and 47 Tier 2 tags, 0 Tier 3 |
| Working notes 05 to 18 | About 45k words, AI-drafted, banner added, claim-level sourcing absent |
| 19_CLAIM_AND_EVIDENCE_MATRIX.csv | 20 rows only |
| verification/ | 10 dossiers (of 38 references), quality uneven, see 1.2 |
| tools/audit.py | Runs, passes, but its checks are shallow (see section 9) |
| Disclosure | Story-style passage exists in the paper (line 27) and README |
| Evidence ledger, entity registry, timelines | Do not exist |

### 1.2 Corrections from the independent review on 2026-11-09 (apply in Phase A)
1. Larkin interview: the Bandcamp Daily feature is dated 10 November 2025, not 2020. The listed headline reads "Christopher Larkin Doesn't Just Score Video Games, He Creates Worlds". Fix the bib key, year, title and every in-text "(Larkin, 2020)". Dossier gave only the site root URL.
2. ACMI: "From Ludum Dare to Pharloom" exists, by Jini Maxwell, published 5 September 2025 (repo says 2022). The page says Hollow Knight's world was only partly planned in advance, that most Kickstarter stretch-goal areas ended up in the base game, and that some promised content (a third playable character) was dropped. The dossier's claim that ACMI documents "extensive internal world-building and design binders" is not supported. Rewrite the dossier and any manuscript sentence that leans on it.
3. Kickstarter: the repo says AU$57,129 from 2,158 backers (with a "57,138 reconciliation" aside, unsourced). The Hollow Knight Wiki lists AU$58,893 and gives no backer total. Campaign ran 19 Nov to 19 Dec 2014, goal AU$35,000. Stretch goals per the wiki: White Palace at 39k, four quests at 44k, Wii U (later Switch) at 50k, second playable character at 56k (became Hornet in Silksong), Colosseum of Fools at 62k; third character (planned as Zote), PS Vita and Abyss expansion were unfunded. Find the Kickstarter page or a reputable press report and settle the figures, or state the conflict openly.
3b. The "Jasmine Vine" staff name is unsourced. Verify or remove.
4. Zhang (ICCT 2026): the paper exists. The ICCT 2026 program (icct.iacst.org/icct2026.php) lists it in Oral Session 10, by Bohan Zhang, Shanghai University of Engineering Science, conference 29 to 31 October 2026, Shanghai. The program gives title only. The dossier's description of the paper's argument is unsupported, so reduce Zhang's role to what can be shown (title, venue, general topic) unless the proceedings text is obtained.
5. Section 5.1 of the manuscript still claims comprehensive in-game text analysis, frame-by-frame hitbox analysis and close listening to complete soundtracks. None of that happened. Rewrite it (Phase A).
6. walkthrough.md links to the previous agent's local Windows paths (C:\Users\ismai\.gemini\...). Strip or rewrite the links. README still says "11,800-word manuscript".
7. Dossiers must link the exact page checked. A root domain is not a source.
8. Not rechecked by the reviewer and so still unconfirmed: dossiers for Morales-Primo, Wysocki, Grunberg, Andriano and Caracciolo, Caracciolo 2026, Nintendo Australia. Metadata for several was confirmed from publisher pages earlier (Eludamos 16(2) pp 9-28; Wysocki JRFM 12(1); Grunberg SAGE DOI), but what each source actually argues was not checked against full text.

### 1.3 Names in the existing notes that may be wrong
The previous agent's report lists many names and events. None has been checked. Treat each as unknown until it matches a wiki entry: Forge-Daughter, Eva, Choir Master, Cogwork Dancers, Black Thread Marionettes, Puppet-Pilgrims, Lost Lace, Last Judge, Grand Mother Silk, First Weaver, "Great Weaver Migration to Deepnest", "Moth Tribe apostasy", "Soul Sanctum versus Abyss schism", "Subterranean Void Lake contamination", "43 profiles" and "32 profiles" totals, and the "Act III" structure. Some are probably real. Phase C exists to sort real from invented.

## 2. Mission and deliverables

Produce a deep, structured, verifiable body of work on story, characters and lore, in addition to polishing the paper.

| Deliverable | Location | Target size |
|---|---|---|
| Source register | data/sources.csv | 60 or more sources, each with tier, URL, retrieval date |
| Entity registry | data/entities.csv | 200 or more entities across both games |
| Claim ledger | data/claims.csv | 600 or more atomic claims, each with source IDs and certainty |
| Relationship edges | data/edges.csv plus Mermaid maps | 150 or more edges |
| Timelines | timelines/ (3 files) | Hallownest, Pharloom, cross-game continuity |
| Story deep dives | lore/hk_*.md and lore/ss_*.md | 14 to 18 files, 1,500 to 3,000 words each |
| Character dossiers | characters/ | 25 Tier A (1,200 to 2,000 words), 40 Tier B (400 to 800), rest as registry rows |
| Thematic essays | themes/ | 8 essays, 1,500 to 2,500 words each |
| Contested readings register | lore/contested_readings.md | 20 or more debates |
| Lore FAQ | lore/FAQ.md | 40 or more questions |
| Updated paper | 20_FULL_RESEARCH_PAPER.md | Methods rewritten, claims traced to ledger |
| Upgraded audit | tools/audit.py | New checks per section 9 |
| QA report | qa/qa_report.md | Independent sample check |
| Handoff 03 | HANDOFF_03_*.md | What remains after this session |

Total new prose target: 40k to 60k words. If that is out of reach, use the cut line in section 8.

## 3. Ground rules

### 3.1 Certainty scale (extends the existing Tier tags, keep their names)
- Tier 1, Confirmed: stated outright in game text or by Team Cherry, and reported consistently by at least one S1 or S2 source. Label it "secondary-confirmed" because no first-hand playthrough is claimed.
- Tier 2, Strongly supported: not stated outright, but the explicit facts leave little room for another reading, per S2 or S3 sources.
- Tier 3, Speculative or interpretive: fan or scholarly reading, or a gap the games leave open.
- Disputed: sources disagree. Record both positions, never pick silently.
- Unknown: nothing found. Say so.

### 3.2 Source hierarchy
- S1: Team Cherry statements, Kickstarter and blog posts, developer interviews, official store pages, official guides.
- S2: community wikis (prefer hollow-knight wiki at hollowknight.wiki for both games; use a second wiki to cross-check), reputable press features.
- S3: scholarship (the six papers already identified, plus new finds).
- S4: fan essays, video essay transcripts, forum threads. Usable only for Tier 3 and the contested register, and always labeled.
Wiki text is a paraphrase of game text. Never present it as a first-hand reading. Add a "Source basis" line to the paper and to every lore file front matter.

### 3.3 Writing rules
- No em-dashes and no en-dashes. Use commas, colons, "to" for ranges, plain hyphens in compound words.
- Do not reproduce in-game dialogue or item text at length. Quote at most a short phrase (under 15 words) and paraphrase the rest.
- Mark spoilers clearly at the top of each lore file.
- Separate "What the games and developers say" from "What is inferred" from "Open questions" in every deep dive. Do not blend them.
- Do not invent names, quotes, dates, DOIs or page numbers. Write "not confirmed" instead.
- Tone: clear, readable, portfolio quality. Ismail wants depth and story flow, not academic boilerplate. Use vivid but accurate prose, and keep claims tagged.

### 3.4 Verification rules
- A dossier or ledger row may say VERIFIED only if it links the exact page checked and gives the retrieval date.
- Re-fetch a source before leaning on it. Search snippets are not sources.
- If a fetch is blocked, say so and mark the claim Unverified. Do not route around blocks with mirrors or caches.
- Never mark your own work PASS. Use "checked by author-agent on DATE against URL".
- Sample-check: after each batch, the main agent re-checks 10 percent of claims against the cited pages.

### 3.5 Git and parallelism
- Only the main agent runs git. The git proxy caps concurrent operations on this repo at 2, so do not parallelize clones or pushes.
- Subagents write to separate files named after their entity or topic so merges never conflict.
- Commit at every phase boundary with a plain message. Push at the end of phases A, D, G, J and K.
- Commit trailers: end commit messages with the Co-Authored-By and Claude-Session lines supplied by the environment.
- Push needs the repo attached with push permission (add_repo, access "push"). It is currently attached.

## 4. Repo layout and file standards

New top-level folders: data/, lore/, characters/, timelines/, themes/, qa/. Keep verification/ and tools/.

Every markdown file in lore/, characters/, timelines/ and themes/ starts with front matter:

```
---
id: hk-pale-king            # matches entities.csv id
type: character | area | event | concept | essay | timeline
game: hk | ss | both
status: draft | checked
certainty_summary: "T1 12, T2 6, T3 4, Disputed 1"
source_basis: secondary
sources: [S014, S022, S031]
last_checked: 2026-11-09
spoilers: full
---
```

CSV schemas:
- sources.csv: source_id, tier (S1 to S4), title, author_or_org, url, published, retrieved, type, notes, status (OK, BLOCKED, NOT_FOUND)
- entities.csv: entity_id, name, aliases, game, type, region, first_appearance, one_line, wiki_url, status (CONFIRMED, UNCONFIRMED, REMOVE)
- claims.csv: claim_id, entity_ids, game, statement (one atomic fact), tier, source_ids, source_basis, notes, used_in
- edges.csv: from_id, to_id, relation, game, claim_id

Claim IDs are stable: HK-0001 upward for Hollow Knight, SS-0001 upward for Silksong, X-0001 for cross-game.

## 5. Phases

Use TaskCreate for every phase. After each phase run the audit, commit, and write two lines in dev-log.md (what was done, what is unresolved).

### Phase A: Ground truth and repair (aim: 45 to 60 minutes)
Tasks:
1. git pull, run python tools/audit.py, read README, HANDOFF.md and this file.
2. Apply the corrections in 1.2: Larkin, ACMI, Kickstarter, Jasmine Vine, Zhang, walkthrough.md links, README word count.
3. Rewrite manuscript section 5.1 to state the real method: secondary-source synthesis, wiki-based lore reconstruction, scholarship review. Add the "Source basis" paragraph. Remove "frame-by-frame", "all dialogue" and "complete soundtrack" claims. Check section 5.2 against the real Tier counts.
4. Redo dossiers for Larkin, ACMI, Kickstarter and Zhang with exact URLs. Recheck the other six dossiers against full text where reachable (Wysocki PDF at jrfm.eu, Morales-Primo, Grunberg, Andriano and Caracciolo, Caracciolo 2026, Nintendo Australia). Downgrade anything unsupported.
5. Create verification/INDEX.md listing all 38 references with status, URL and retrieval date. For the 28 without dossiers, record at least identity checks (exists, metadata, URL).
Output: corrected paper, 38-row verification index, dev-log entry.
Acceptance: no dossier says VERIFIED without an exact URL and a retrieval date; section 5.1 describes only work that was actually done; Larkin and ACMI years are fixed everywhere.
Commit and push.

### Phase B: Source map and fetch cache (aim: 45 minutes)
Tasks:
1. Build data/sources.csv. Seed it with: the hollowknight.wiki pages for both games (main, Characters, Areas, Bosses, Endings, Lore, Items), a second wiki for cross-checks, Team Cherry blog and Kickstarter updates, the Game Informer Sea of Sorrow announcement, ACMI, Bandcamp Daily, MCV "When We Made... Hollow Knight", the Hungry Knight and Ludum Dare pages, the Nintendo Australia interview, and the scholarship list.
2. Search for more: developer interviews on narrative intent (Gibson, Pellen, Kazi), press features on Silksong's story and music, and further scholarship on either game since 2020 (for example the First Person Scholar "For All the Broken Vessels" lead, a Zenodo "pure vessels" PDF, a Game Studies 2025 piece on indie games and mental health). Check each lead for relevance before adding.
3. Fetch each source once and save a short working extract (under 200 words of paraphrase, no long quotes) into data/extracts/<source_id>.md with the URL and retrieval date. Extracts are working memory for the later phases, not published prose.
4. Note which pages could not be fetched and why.
Acceptance: 60 or more sources, at least 20 S1 or S3, every row with URL and retrieval date, a note on blocked pages.

### Phase C: Entity registry and hallucination sweep (aim: 60 to 75 minutes)
Tasks:
1. From the wiki character, boss, area and item indexes, build data/entities.csv for both games. Target 120 or more Hollow Knight entities and 100 or more Silksong entities, including all major and minor named characters, bosses, regions, factions, deities and concepts (Void, Soul, Silk, Infection, Dream, and so on).
2. Run a name extraction pass over files 05 to 18 and the paper. List every proper noun. Reconcile against entities.csv. Anything not found gets status UNCONFIRMED, then is checked against a second source, then confirmed or marked REMOVE.
3. Produce data/hallucination_sweep.md: a table of every REMOVE or UNCONFIRMED name, where it appears, and the action taken (rewrite, delete or keep with caveat).
4. Fix the affected files directly, or add a visible "needs correction" note where a fix needs the later deep dives.
Acceptance: every proper noun in the repo maps to a registry row or is flagged; the sweep file lists the numbers (found, unconfirmed, removed); the previous agent's name list in 1.3 is fully resolved.
Commit.

### Phase D: Timelines and continuity (aim: 45 to 60 minutes)
Tasks:
1. timelines/hallownest_timeline.md: ordered events from the earliest cosmic layer through the kingdom's rise and fall to the Knight's journey and post-game material (DLC content, Godhome). Each entry has a claim ID, tier and sources. Where order is disputed, say so.
2. timelines/pharloom_timeline.md: same for Silksong, including events before Hornet's arrival.
3. timelines/cross_game_continuity.md: a table of every confirmed link between the games (characters, places, mechanics, Hornet's arc, the Kickstarter stretch-goal origin of Silksong) with certainty tags, plus the open questions (what is explicitly connected, what is only thematic).
4. Add a Mermaid timeline and a dated "release and development" strip (Ludum Dare 27 in August 2013, Ludum Dare 29 in April 2014, Kickstarter November 2014, Hollow Knight February 2017, Silksong announced February 2019, released September 2025, Sea of Sorrow announced December 2025 and unreleased as of the last check). Verify each date from a source before use.
Acceptance: every timeline entry has a claim row; no unlabeled speculation; development dates sourced.
Commit and push.

### Phase E: Hollow Knight story deep dives (aim: 90 to 120 minutes)
Write one file per thread in lore/, 1,500 to 3,000 words, using this template:
1. What the games and developers say (Tier 1, with claim IDs)
2. What the evidence strongly implies (Tier 2)
3. Interpretations and gaps (Tier 3 and Disputed)
4. Why it matters for the project's themes
5. Open questions and sources to chase

Suggested threads (final list set from the wiki, keep the count at 14 to 18): the cosmic layers and the Void; the Wyrm, the Radiance and the old gods; the Pale King and the founding of Hallownest; the vessel program, the Abyss and the Hollow Knight; the Dreamers and the seal; the Infection and its spread; Hallownest society, class, religion and economy; Hornet, Herrah and Deepnest; the Mantis, Moth and other older cultures; the City of Tears and the Soul Sanctum; the Grimm Troupe and the Nightmare Lantern; Godhome and the Pantheons; the White Palace and the Pale King's legacy; the Knight's identity and role; the Hunter's Journal and the world's ecology; the five or six endings in full.
Parallelism: after writing a shared "lore brief" (the Phase C registry and Phase D timeline), launch up to 4 subagents at once, each owning 3 to 4 threads, each writing only its own files and claim rows to data/claims_<agent>.csv. The main agent merges the claim files and sample-checks.
Acceptance: each thread has at least 12 claim rows, a sourced Tier 1 section and a separate speculation section; no name outside the registry; no copied in-game text.
Commit.

### Phase F: Silksong story deep dives (aim: 90 to 120 minutes)
Same template and process as Phase E. Suggested threads, with the final list taken from the wiki: Pharloom's founding, geography and the song and bell culture; Hornet's capture and arrival; Grand Mother Silk and silk as a cosmological force; the Weavers and their fate; the Citadel, its pilgrimage and its religion; Lace, her arc and her relationship to Hornet; the Last Judge and the theocratic structure; the pilgrim and bug population, class and labor; the guild and merchant economy and the Bell Beast; the three-act structure and its turns; the Wishes (side quest) system as lore; silk powers and crests as narrative; the endings and their unlock conditions; the Abyss material and the Act 3 area changes; the relation of the Black Thread and other corrupting forces to the Hollow Knight Infection and Void.
Do not assert the story of any thread before checking the wiki. If a thread name cannot be matched to the wiki's own structure, rename it to match.
Acceptance: same as Phase E.
Commit.

### Phase G: Character dossiers (aim: 120 to 150 minutes, the longest phase)
Tiering:
- Tier A (25): Hollow Knight: the Knight, Hollow Knight, Pale King, White Lady, the Radiance, Hornet, Quirrel, Zote, Elderbug, Cornifer, Grimm, Lurien, Monomon, Herrah, Soul Master, Mantis Lords. Silksong: Hornet, Grand Mother Silk, Lace, Sherma, Shakra, Garmond, Zaza, Last Judge, Karmelita, and others the wiki shows as plot-central. Final list from the wiki, not from this seed.
- Tier B (40): significant NPCs and bosses, such as Sly, Iselda, Tiso, Cloth, Bretta, Oro, Mato, Sheo, Nailsmith, Myla, Bardoon, Millibelle, the Collector, Nosk, Traitor Lord, Broken Vessel, Lost Kin, Hive Knight, Trobbio, Seth, Phantom, Forge Daughter, the Bell Beast, Moorwing, Groal, Widow and Sister Splinter. All are seeds to verify, not a trusted list.
- Tier C: everyone else, a registry row with a one-line role.

Dossier template (Tier A):
1. Identity: name, aliases, species, game, first appearance, voice and design notes only if sourced
2. Role in the story and place in the world
3. Arc, in order, with spoiler tags
4. Motivations and relationships (link edges.csv rows)
5. Key evidence: 8 or more claim IDs
6. Interpretations and open questions, labeled Tier 3
7. Thematic link to the project (sacrifice, memory, faith, ecology, identity, voice)
Tier B uses sections 1 to 4 and a shorter evidence list.

Also produce: characters/relationship_maps.md with Mermaid graphs per game and a cross-game map, built from edges.csv; characters/factions.md covering kingdoms, tribes and orders; characters/voices_and_silence.md (who speaks, who does not, and how each game uses voice).
Parallelism: 4 subagents, each owning a batch of characters, each writing separate files and claim rows. Give every subagent the entity registry, the source list, the writing rules and this template.
Acceptance: 25 Tier A and 40 Tier B files exist; each Tier A has 8 or more claims; every edge references a claim; main agent has spot-checked at least 20 dossiers.
Commit and push.

### Phase H: Thematic essays (aim: 60 to 75 minutes)
Eight essays in themes/, each 1,500 to 2,500 words, written in an engaging story-driven voice, each citing claim IDs for every factual statement and keeping speculation in clearly labeled passages:
1. Sacrifice, vessels and inherited burden
2. Faith, theocracy and the machinery of belief (Hallownest versus Pharloom)
3. Dreams, memory and forgetting
4. Ecology, infection and the nonhuman world
5. Class, labor and the people who remain
6. Voice and silence: the Knight and Hornet
7. Parents, children and succession (Pale King and White Lady, Hornet and Herrah, Grand Mother Silk and her wards)
8. Ruins and return: archaeology, backtracking and place as narrative (can use verified scholarship only)
Acceptance: each essay has at least 10 claim IDs and an explicit "what we do not know" paragraph.
Commit.

### Phase I: Contested readings and FAQ (aim: 45 to 60 minutes)
Tasks:
1. lore/contested_readings.md: 20 or more debates. For each: the question, positions, the evidence offered for each, which sources hold each position, and a short note on how well-supported each is. Do not pick winners unless a source does, and then attribute it.
2. lore/FAQ.md: 40 or more questions people actually ask (who is the Knight, what is the Void, how are the games connected, what is canon, what is cut content), each answered in 3 to 8 sentences with claim IDs.
Acceptance: every FAQ answer traces to claim rows; every contested position names a source.
Commit.

### Phase J: Integration and paper update (aim: 60 minutes)
Tasks:
1. Rebuild 19_CLAIM_AND_EVIDENCE_MATRIX.csv from claims.csv so every [Tier 1] and [Tier 2] sentence in the paper maps to a claim ID. Add real Tier 3 tags where the paper interprets.
2. Add citations or claim references in manuscript sections 6 to 8 and anywhere still bare.
3. Update the paper's introduction and conclusion for the new depth. Keep the story-style AI disclosure accurate (a second pass has now been done by agents, verification is source-based and partly sampled, no first-hand playthrough).
4. Refresh README, CHANGELOG, 00_PROJECT_README, dev-log and 23_PROCESS_RECORD so they match reality.
5. Convert the working-note banners on 05 to 18: each note whose content is now backed by lore/ and characters/ files gets a pointer to them. Keep all 20 notes (Ismail's decision), still labeled as working notes.
Acceptance: ledger coverage of paper claims is 100 percent; no stale numbers in README or CHANGELOG.
Commit and push.

### Phase K: Independent QA and closeout (aim: 45 to 60 minutes)
Tasks:
1. Launch a fresh subagent that has not seen the authoring context, with an adversarial brief: pick 40 claims across both games and all tiers, re-fetch the cited pages, and mark each SUPPORTED, PARTIAL or UNSUPPORTED. Also pick 10 character dossiers and check every named relationship.
2. Write qa/qa_report.md with the raw results, including the failure rate. Fix what failed. Re-run until the sample failure rate is under 10 percent, or document what remains.
3. Run the upgraded audit (section 9). Fix findings.
4. Write HANDOFF_03 with what is left (for example: more S3 scholarship, Silksong post-launch patches, Sea of Sorrow when it ships, first-hand playthrough annotations if Ismail ever supplies them, publishing as a site).
5. Final commit and push. Report to Ismail: what changed, the QA failure rate, the open items.
Acceptance: QA report exists and is honest; audit clean; HANDOFF_03 written.

## 6. Research question bank

These are questions to answer from sources. They are not facts. Several may have partial or no answers, and "unknown" is a valid result.

### 6.1 Hollow Knight
1. What do sources say about the order and relation of the Void, Light, Dream and the Wyrm before Hallownest?
2. Who was the Pale King, how did he come to Hallownest, and what did the wiki and developers say about his methods and motives?
3. How and why was the vessel program run? How many vessels, what became of them, and where does the Abyss fit?
4. Why was the Hollow Knight chosen, and how does the Knight differ from the others?
5. Who are the Dreamers, why did they accept the seal, and what are their fates?
6. How did the Infection start, spread and take hold? What is the relationship between the Radiance, dreams and the Moth Tribe?
7. What is Hornet's parentage, her role in the story and her relation to Deepnest?
8. How do the Mantis Tribe, Weavers and other pre-Hallownest cultures figure in the setting?
9. What is the Grimm Troupe ritual, and what is the Nightmare Lantern?
10. What is Godhome, who built it, what are the Pantheons, and what does the Absolute Radiance represent?
11. How do the endings differ, and what unlocks each? Which are canon in the developers' view, if anyone has said?
12. How does the setting present class, religion, money (Geo) and daily life?
13. What can be said about Cornifer, the Hunter, the Wanderer's Journal and other chroniclers?
14. What was cut or changed during development, and what do developers say about it?
15. Which parts of the lore does Team Cherry explicitly leave unresolved?

### 6.2 Silksong
1. What do sources say about Pharloom's founding, structure and culture?
2. Why was Hornet taken, by whom, and what is her relation to the Weavers and Grand Mother Silk?
3. What is silk, how does it work in the setting, and how is it tied to the Black Thread or other forces?
4. What is the Citadel, what does it worship, and who runs it?
5. Who is Lace, what is her arc, and how does she relate to Hornet?
6. What is the role of the pilgrims and the bell and song culture?
7. How is the story split into acts, and what changes between them?
8. What are the Wishes, and what lore do they add?
9. What are all the endings, how are they unlocked, and how do sources read them?
10. What is the Abyss material and Act 3 content, and how does it connect to Hollow Knight?
11. What has Team Cherry said about Silksong's story intent, music and design?

### 6.3 Cross-game and meta
1. What is explicitly connected between the games and what is only thematic?
2. What did Team Cherry say about world-building process and how it changed (see the ACMI piece)?
3. How do the six scholarly sources actually read the games, and where do they disagree with the wiki or with each other?
4. How does the Silksong launch window (September 2025) and Sea of Sorrow status affect scope?

## 7. Quality bar per output

- Every factual sentence in lore/, characters/ and themes/ either carries a claim ID or sits in a block labeled Interpretation.
- No unlabeled "it is clear that". If it is clear, cite it.
- Each deep dive names at least one place where sources disagree or where the game is silent.
- Consistent spelling of names, matching entities.csv.
- A reader who has played the games should recognise the content. A reader who has not should still follow it.

## 8. Session plan and cut line

Approximate schedule for one long session: A 1h, B 0.75h, C 1.25h, D 1h, E 2h, F 2h, G 2.5h, H 1h, I 1h, J 1h, K 1h. About 14.5 hours of agent work if serial. Parallel subagents in E, F and G should bring that down substantially.

If time or budget runs short, cut in this order and record it in dev-log.md:
1. Reduce Tier B dossiers from 40 to 20.
2. Reduce themes from 8 essays to 5 (keep 1, 2, 3, 6, 7).
3. Reduce deep-dive threads to the 10 most central per game.
4. Reduce FAQ to 25 and contested readings to 12.
Never cut: Phase A repairs, Phase C hallucination sweep, ledger coverage of the paper, Phase K QA. A smaller verified corpus beats a larger unverified one.

## 9. Audit script upgrades (tools/audit.py)

Add checks that fail the run, not just print:
1. Every dossier marked VERIFIED has an exact URL (not just a domain root) and a retrieval date.
2. Every proper noun in lore/, characters/, timelines/, themes/ exists in entities.csv (allow a stoplist).
3. Every claim ID cited in prose exists in claims.csv; every claim row has at least one source ID that exists in sources.csv.
4. Every [Tier 1] or [Tier 2] sentence in the paper maps to a claim ID. Report coverage percent.
5. Date sanity: flag any publication year in the bib that differs from the year in the dossier.
6. Front matter present and valid in every new file.
7. No em-dashes or en-dashes in any text file (including .py scripts' output strings).
8. No file contains the words "PASS", "zero violations" or "unanimous" outside tools/ and qa/.
9. Methods statements (section 5) contain no phrases from a banned list: "frame-by-frame", "all dialogue", "complete soundtrack", "playthrough".
10. Counts report: entities, claims, sources, edges, files per folder, words per folder.
The previous script passed while four dossiers had errors and the methods overclaimed. These checks are meant to catch that class of failure.

## 10. Definition of done

- All of Phases A to K complete, or the cut line applied and recorded.
- 60 or more sources, 200 or more entities, 600 or more claims, 150 or more edges, all with required fields.
- 25 Tier A and 40 Tier B character files (or the cut-line numbers), 14 to 18 deep dives, 8 essays, FAQ, contested register, three timelines.
- Paper claims 100 percent mapped to the ledger; methods section honest.
- QA report with sample failure rate under 10 percent or an explicit list of what is left.
- audit.py passes with the new checks and no check was loosened to get a pass.
- README, CHANGELOG, dev-log, 23_PROCESS_RECORD and the AI disclosure are accurate.
- Everything committed and pushed to master.
- HANDOFF_03 exists.

## 11. Risks and failure modes (read before starting)

1. Confident invention. The first agent produced fluent lore with names that may not exist. Always check a name against the registry before writing it.
2. Wiki drift. Wikis are edited by fans and may differ from game text. Cross-check two sources for Tier 1 and note when they differ.
3. Over-merging interpretation into canon. Keep Tier 3 visibly separate.
4. Citing a source you did not open. Search snippets and titles are not sources.
5. Spreading the date errors again. The earlier draft got Ludum Dare, Larkin and ACMI dates wrong. Verify dates one by one.
6. Silksong volatility. Patches, DLC and wiki changes can shift facts. Record the game version or the date of each wiki check.
7. Scope creep. This is a portfolio and hobby project. Prefer depth and honesty over trying to look like a journal submission.
8. Context loss over a long session. Keep dev-log.md and the task list current, write extracts to disk, and re-read the registry rather than relying on memory.
9. Blocked pages. Some sites are not reachable from the sandbox. Record the block and move on.
10. Parallel merge conflicts. One owner per file, one agent running git.

## 12. Decisions already made by Ismail, and open items

Decided (2026-11-09): portfolio and hobby goal; secondary sources, no captures; keep all 20 working notes; AI disclosure in natural story flow; depth in story, characters and lore is the next priority.

Open, with defaults the agent should use unless told otherwise:
1. Zhang (ICCT 2026): default is to keep it only as a venue-and-title citation, and to cite no argument from it unless the proceedings text is obtained.
2. Publishing: default is a tidy repo with a README table of contents. A static site or blog version is a later option.
3. Sea of Sorrow: default is to treat it as announced and unreleased, re-check once at the start and once at the end.
4. Kickstarter figures: default is to report the conflict and give a range until the Kickstarter page or a reputable report settles it.

## 13. Coverage note for this handoff

This handoff is based on the repo state at 73a181d, the 2026-11-09 independent review and the earlier audit. The character, area and question seeds in sections 5, 6 and 7 come from the previous agent's report and general knowledge, not from fresh checks, so every seed is a prompt to verify, not a fact. The games themselves have not been played or checked by me.
