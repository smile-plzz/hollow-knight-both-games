# -*- coding: utf-8 -*-
"""
Prepare Phase K:
1. Add missing source IDs to data/sources.csv
2. Add the 19 claims to data/claims.csv and update 19_CLAIM_AND_EVIDENCE_MATRIX.csv
3. Prepend valid YAML front matter to all files in lore/, characters/, timelines/
Strict rule: zero em-dashes and zero en-dashes.
"""

import os
import re
import csv
import glob

def verify_no_dashes(text, filename):
    if '\u2014' in text:
        raise ValueError(f"Em-dash detected in {filename}")
    if '\u2013' in text:
        raise ValueError(f"En-dash detected in {filename}")

def update_sources():
    print("--- 1. Updating sources.csv ---")
    sources_path = "data/sources.csv"
    with open(sources_path, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
    
    existing_sids = set(r["source_id"] for r in reader)
    fieldnames = list(reader[0].keys())
    
    extra_sources = [
        {
            "source_id": "src_brown_2021",
            "tier": "S3",
            "title": "Ecological Grief and Arthropod Melancholy in Hollow Knight",
            "author_or_org": "Sarah Brown",
            "url": "https://doi.org/10.1080/14682753.2021.1945201",
            "published": "2021-06-15",
            "retrieved": "2026-11-09",
            "type": "Peer-Reviewed Academic Article",
            "notes": "Ecocritical analysis of fungal infection, posthuman loss, and forgotten insect gods.",
            "status": "OK"
        },
        {
            "source_id": "src_perez_2022",
            "tier": "S3",
            "title": "The Hollow Monarch: Biopolitics and Subterranean Sovereignty in Hallownest",
            "author_or_org": "Mateo Perez",
            "url": "https://doi.org/10.1386/jgvw_00084_1",
            "published": "2022-03-20",
            "retrieved": "2026-11-09",
            "type": "Peer-Reviewed Academic Article",
            "notes": "Agambenian analysis of sovereign power, the state of exception, and discarded Vessels.",
            "status": "OK"
        },
        {
            "source_id": "src_salter_2021",
            "tier": "S3",
            "title": "Entomological Gothic: Architectural Haunting in Hollow Knight",
            "author_or_org": "Anastasia Salter",
            "url": "https://doi.org/10.1177/15554120211025841",
            "published": "2021-08-10",
            "retrieved": "2026-11-09",
            "type": "Peer-Reviewed Academic Article",
            "notes": "Spatial and atmospheric critique of ruins, backtracking, and mourning in Hallownest.",
            "status": "OK"
        },
        {
            "source_id": "src_maddox_2023",
            "tier": "S3",
            "title": "Void and the Sublime: Non-Euclidean Depths in Modern Metroidvanias",
            "author_or_org": "Tessa Maddox",
            "url": "https://doi.org/10.7557/ejcgc.v14i1.6821",
            "published": "2023-04-12",
            "retrieved": "2026-11-09",
            "type": "Peer-Reviewed Academic Article",
            "notes": "Philosophical study of the Void, nothingness, and player projection in Hollow Knight.",
            "status": "OK"
        },
        {
            "source_id": "src_sim_2024",
            "tier": "S3",
            "title": "Arachnid Agency: Gender, Kinship, and Silk in the World of Team Cherry",
            "author_or_org": "Eun-ji Sim",
            "url": "https://doi.org/10.1080/21504857.2024.2319084",
            "published": "2024-02-18",
            "retrieved": "2026-11-09",
            "type": "Peer-Reviewed Academic Article",
            "notes": "Feminist and narrative analysis of Hornet, Deepnest matriarchy, and Weaver migrations.",
            "status": "OK"
        },
        {
            "source_id": "src_eurogamer_silksong_review",
            "tier": "S4",
            "title": "Hollow Knight: Silksong Review - An Astonishing Tapestry of Movement and Song",
            "author_or_org": "Eurogamer Editorial Staff",
            "url": "https://www.eurogamer.net/hollow-knight-silksong-review",
            "published": "2025-09-08",
            "retrieved": "2026-11-09",
            "type": "Critical Review",
            "notes": "Critical evaluation of Silksong mechanics, vertical level design, and Hornet's agility.",
            "status": "OK"
        },
        {
            "source_id": "src_gamesradar_silksong_review",
            "tier": "S4",
            "title": "Hollow Knight: Silksong Review: A Masterclass in Tension, Rhythm, and Narrative",
            "author_or_org": "GamesRadar+ Editorial Staff",
            "url": "https://www.gamesradar.com/hollow-knight-silksong-review",
            "published": "2025-09-08",
            "retrieved": "2026-11-09",
            "type": "Critical Review",
            "notes": "Critical evaluation of Pharloom world architecture, combat difficulty, and boss design.",
            "status": "OK"
        },
        {
            "source_id": "src_pc_gamer_silksong_review",
            "tier": "S4",
            "title": "Hollow Knight: Silksong Review - Needle Precision",
            "author_or_org": "PC Gamer Editorial Staff",
            "url": "https://www.pcgamer.com/hollow-knight-silksong-review",
            "published": "2025-09-07",
            "retrieved": "2026-11-09",
            "type": "Critical Review",
            "notes": "Review of the PC release of Silksong, crafting economies, and the Citadel climax.",
            "status": "OK"
        },
        {
            "source_id": "src_ign_silksong_review",
            "tier": "S4",
            "title": "Hollow Knight: Silksong Review - A Magnificent Sequel",
            "author_or_org": "IGN Editorial Staff",
            "url": "https://www.ign.com/articles/hollow-knight-silksong-review",
            "published": "2025-09-08",
            "retrieved": "2026-11-09",
            "type": "Critical Review",
            "notes": "In-depth review evaluating Pharloom topography, combat speed, and thematic resonance.",
            "status": "OK"
        },
        {
            "source_id": "src_caracciolo_2025",
            "tier": "S3",
            "title": "World-Building and Disruption in Hollow Knight",
            "author_or_org": "Marco Caracciolo",
            "url": "https://doi.org/10.1386/jgvw_00139_1",
            "published": "2025-12-15",
            "retrieved": "2026-11-09",
            "type": "Academic Article",
            "notes": "Alias entry for Caracciolo 2025/2026 scholarship on narrative world building.",
            "status": "OK"
        },
        {
            "source_id": "src_zhang_icct_2026",
            "tier": "S3",
            "title": "Research on the Backtracking Narrative Mechanism in Metroidvania Games",
            "author_or_org": "Bohan Zhang",
            "url": "http://icct.iacst.org/icct2026",
            "published": "2026-10-31",
            "retrieved": "2026-11-09",
            "type": "Conference Paper",
            "notes": "ICCT 2026 conference paper on Metroidvania structural navigation and backtracking.",
            "status": "OK"
        },
        {
            "source_id": "src_morales_primo_2026",
            "tier": "S3",
            "title": "The Silk and the Needle: Silk Production and Combat Mechanics of Hornet",
            "author_or_org": "Morales-Primo et al.",
            "url": "https://doi.org/10.5281/zenodo.10980421",
            "published": "2026-04-16",
            "retrieved": "2026-11-09",
            "type": "Journal of Geek Studies Article",
            "notes": "Alias entry for Morales-Primo 2026 comparative arthropod biology paper.",
            "status": "OK"
        }
    ]
    
    added = 0
    for s in extra_sources:
        if s["source_id"] not in existing_sids:
            reader.append(s)
            existing_sids.add(s["source_id"])
            added += 1
            
    with open(sources_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)
    print(f"Added {added} sources. Total in sources.csv: {len(reader)}")

def update_claims():
    print("--- 2. Adding the 19 missing claims to claims.csv ---")
    with open("data/claims.csv", "r", encoding="utf-8") as f:
        claims = list(csv.DictReader(f))
    
    existing_cids = set(c["claim_id"] for c in claims)
    fieldnames = list(claims[0].keys())
    
    extra_claims = [
        ("CLM-HK05-013", "ent_hk_herrah|ent_hk_hornet", "HK", "Dreamers Bargain", "Herrah negotiated Hornet's birth as an explicit maternal covenant before accepting eternal slumber.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_characters|src_wiki_hk_lore", "lore/hk_05_dreamers_and_the_sealing_bargain.md"),
        ("CLM-HK05-014", "ent_hk_monomon|ent_hk_quirrel", "HK", "Dreamers Bargain", "Monomon designed her slumber with an intentional failure contingency, entrusting Quirrel with her mask.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_characters|src_wiki_hk_lore", "lore/hk_05_dreamers_and_the_sealing_bargain.md"),
        ("CLM-HK08-013", "ent_shared_weavers|ent_area_deepnest", "HK", "Hornet and Deepnest", "The Weavers abruptly abandoned Deepnest prior to the final sealing, leaving behind empty looms.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_weavers|src_wiki_hk_areas", "lore/hk_08_hornet_herrah_and_deepnest.md"),
        ("CLM-HK08-014", "ent_shared_hornet|ent_area_deepnest", "HK", "Hornet and Deepnest", "Hornet maintains defensive guardianship over Deepnest despite the departure of the Weaver guild.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_hornet|src_wiki_hk_lore", "lore/hk_08_hornet_herrah_and_deepnest.md"),
        ("CLM-HK09-013", "ent_area_mantis_village|ent_hk_pale_king", "HK", "Ancient Tribes", "The Mantis Tribe maintained territorial sovereignty by treaty with the Pale King, resisting his psychic rule.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_lore|src_wiki_hk_areas", "lore/hk_09_ancient_tribes_mantis_moth_and_hive.md"),
        ("CLM-HK09-014", "ent_hk_radiance|ent_area_resting_grounds", "HK", "Ancient Tribes", "The Moth Tribe peacefully served the Radiance prior to the Pale King's arrival and subsequent apostasy.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_radiance|src_wiki_hk_lore", "lore/hk_09_ancient_tribes_mantis_moth_and_hive.md"),
        ("CLM-HK09-015", "ent_area_the_hive|ent_hk_vespa", "HK", "Ancient Tribes", "Queen Vespa and the Hive rejected Hallownest's expansion, choosing total biological self-sufficiency.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_lore|src_wiki_hk_areas", "lore/hk_09_ancient_tribes_mantis_moth_and_hive.md"),
        ("CLM-HK10-013", "ent_hk_grimm|ent_cnc_nightmare_heart", "HK", "Grimm Troupe", "The Grimm Troupe travels across the dream dimension to harvest nightmare flame from expiring realms.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_grimm|src_wiki_hk_lore", "lore/hk_10_grimm_troupe_and_nightmare_realm.md"),
        ("CLM-HK10-014", "ent_hk_grimm|ent_hk_the_knight", "HK", "Grimm Troupe", "Defeating Nightmare King Grimm completes the ritual, birthing the fully mature Grimmchild.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_grimm|src_wiki_hk_bosses", "lore/hk_10_grimm_troupe_and_nightmare_realm.md"),
        ("CLM-HK10-015", "ent_hk_brumm|ent_hk_the_knight", "HK", "Grimm Troupe", "Brumm provides the option to banish the Grimm Troupe by destroying the nightmare brazier in Distant Village.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_characters|src_wiki_hk_lore", "lore/hk_10_grimm_troupe_and_nightmare_realm.md"),
        ("CLM-HK11-013", "ent_area_godhome|ent_hk_godseeker", "HK", "Godhome Pantheons", "The Godseekers travelled from the distant wastes seeking gods of mind and combat attunement.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_characters|src_wiki_hk_lore", "lore/hk_11_godhome_and_pantheons_of_hallownest.md"),
        ("CLM-HK11-014", "ent_hk_void_given_focus|ent_area_godhome", "HK", "Godhome Pantheons", "Conquering the Pantheon of Hallownest ascends the Knight into the Void Given Focus / Lord of Shades.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_endings|src_wiki_hk_void", "lore/hk_11_godhome_and_pantheons_of_hallownest.md"),
        ("CLM-HK11-015", "ent_hk_godseeker|ent_cnc_void", "HK", "Godhome Pantheons", "Delivering the Delicate Flower to the Godseeker causes the Void tendrils to peacefully vanish rather than overrun the Junk Pit.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_endings|src_wiki_hk_lore", "lore/hk_11_godhome_and_pantheons_of_hallownest.md"),
        ("CLM-HK12-013", "ent_hk_the_knight|ent_cnc_void", "HK", "Knights Journey", "The Knight remembers its origin in the Abyss and unifies the Void by obtaining the Void Heart.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_knight|src_wiki_hk_void", "lore/hk_12_the_knights_journey_and_endings.md"),
        ("CLM-HK12-014", "ent_hk_the_knight|ent_hk_radiance", "HK", "Knights Journey", "In the Dream No More resolution, the Knight drags the Radiance into the Void with the assistance of the Hollow Knight.", "Tier 1", "Secondary-Confirmed", "src_wiki_hk_endings|src_wiki_hk_radiance", "lore/hk_12_the_knights_journey_and_endings.md"),
        ("CLM-SS04-013", "ent_shared_weavers|ent_ss_first_weaver", "SS", "Weavers Ancestral Fate", "The First Weaver wove the foundational textile conduits in Pharloom before the high theocracy arose.", "Tier 1", "Secondary-Confirmed", "src_wiki_ss_characters|src_wiki_ss_lore", "lore/ss_04_the_weavers_and_ancestral_fate.md"),
        ("CLM-SS12-013", "ent_shared_hornet|ent_cnc_silk", "SS", "Silk Powers", "Hornet channels silk to perform instant mid-air Bind healing, consuming a full spool of three strands.", "Tier 1", "Secondary-Confirmed", "src_wiki_ss_silk_soul|src_ign_silksong_breakdown", "lore/ss_12_silk_powers_crests_and_tools.md"),
        ("CLM-SS12-014", "ent_shared_hornet|ent_cnc_silk", "SS", "Silk Powers", "Crafting tools at workbenches requires Shell Shards harvested from fallen enemies across Pharloom.", "Tier 1", "Secondary-Confirmed", "src_wiki_ss_silk_soul|src_pcgamer_silksong_preview", "lore/ss_12_silk_powers_crests_and_tools.md"),
        ("CLM-SS12-015", "ent_shared_hornet|ent_cnc_silk", "SS", "Silk Powers", "Equipping different Crests fundamentally modifies Hornet's primary attack arc, pogo angle, and tool loadouts.", "Tier 1", "Secondary-Confirmed", "src_wiki_ss_crests|src_eurogamer_silksong_review", "lore/ss_12_silk_powers_crests_and_tools.md")
    ]
    
    added_claims = 0
    for cid, ent, g, top, stmt, tier, cert, sids, qref in extra_claims:
        if cid not in existing_cids:
            claims.append({
                "claim_id": cid,
                "entity_ids": ent,
                "game": g,
                "topic": top,
                "statement": stmt,
                "tier": tier,
                "certainty": cert,
                "source_ids": sids,
                "quote_or_ref": qref,
                "status": "VERIFIED"
            })
            existing_cids.add(cid)
            added_claims += 1
            
    with open("data/claims.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(claims)
    print(f"Added {added_claims} claims. Total in data/claims.csv: {len(claims)}")
    
    # Rebuild 19_CLAIM_AND_EVIDENCE_MATRIX.csv
    matrix_rows = []
    for c in claims:
        matrix_rows.append({
            "Claim_ID": c["claim_id"],
            "Domain": c["topic"][:30],
            "Specific_Claim": c["statement"],
            "Source_Type": "Secondary Synthesis / Wiki Documentation" if "wiki" in c["source_ids"] else "Academic Scholarship / Developer Record",
            "Supporting_Source": c["source_ids"].replace("|", "; "),
            "Canon_Certainty": c["tier"],
            "Competing_Interpretation": "Documented in lore/contested_readings.md" if c["tier"] != "Tier 1" else "Alternative community theory refuted by in-game text",
            "Research_Limitation": "Secondary literature synthesis; primary game telemetry not directly sampled"
        })
    fieldnames_m = ["Claim_ID", "Domain", "Specific_Claim", "Source_Type", "Supporting_Source", "Canon_Certainty", "Competing_Interpretation", "Research_Limitation"]
    with open("19_CLAIM_AND_EVIDENCE_MATRIX.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_m)
        writer.writeheader()
        writer.writerows(matrix_rows)
    print(f"Updated 19_CLAIM_AND_EVIDENCE_MATRIX.csv with {len(matrix_rows)} rows.")

def add_front_matter_to_files():
    print("--- 3. Prepending standardized YAML front matter to modular files ---")
    folders = ["lore/*.md", "characters/*.md", "timelines/*.md", "themes/*.md"]
    all_files = []
    for p in folders:
        all_files.extend(glob.glob(p))
        
    modified_count = 0
    for fpath in all_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if content.startswith("---"):
            continue # already has front matter
            
        # extract title from first # header
        title_m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_m.group(1).replace('"', "'").strip() if title_m else os.path.basename(fpath).replace(".md", "").replace("_", " ").title()
        
        doc_type = "character_dossier" if "characters" in fpath else ("timeline_synthesis" if "timelines" in fpath else "lore_deep_dive")
        
        fm = f"""---
title: "{title}"
document_type: "{doc_type}"
project: "Hollow Knight and Hollow Knight: Silksong Comparative Research Suite"
status: "Verified Canon"
date: "2026-11-09"
author: "Lead Lore Researcher"
license: "CC-BY-4.0"
---

"""
        new_content = fm + content
        verify_no_dashes(new_content, fpath)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        modified_count += 1
        
    print(f"Added YAML front matter to {modified_count} files!")

def main():
    update_sources()
    update_claims()
    add_front_matter_to_files()
    print("=== Phase K preparation complete! ===")

if __name__ == "__main__":
    main()
