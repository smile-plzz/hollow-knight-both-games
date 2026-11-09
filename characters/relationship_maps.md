# Character and Faction Relationship Maps

## Overview and Source Basis
This document visualizes the interpersonal, political, and metaphysical relationships across *Hollow Knight* (2017) and *Hollow Knight: Silksong* (2025). The graph edges are systematically cataloged in `data/edges.csv` and derived from verified secondary community transcriptions and developer interviews (`src_wiki_hk_lore`, `src_wiki_ss_characters`, `src_wiki_hk_weavers`, `src_larkin_bandcamp_2025`).

---

## 1. Hallownest Relationship Architecture

```mermaid
flowchart TD
    subgraph Royalty ["The Royal Court"]
        PK["The Pale King (Wyrm)"]
        WL["The White Lady (Queen)"]
        FGK["The Five Great Knights (Ogrim, Isma, Ze'mer, Dryya, Hegemol)"]
        PK --- WL
        PK --> FGK
    end

    subgraph TheAbyss ["The Abyss and Void"]
        HK["The Hollow Knight (Chosen Vessel)"]
        KT["The Knight (Discarded Sibling)"]
        BV["Broken Vessel / Lost Kin"]
        SL["Shade Lord (Void Given Form)"]
        PK -->|Eugenics| HK
        PK -->|Eugenics| KT
        PK -->|Eugenics| BV
        KT -->|Apotheosis| SL
    end

    subgraph Dreamers ["The Dreamer Seals"]
        LV["Lurien the Watcher"]
        MT["Monomon the Teacher"]
        HB["Herrah the Beast"]
        QR["Quirrel (Apprentice)"]
        MT --> QR
        PK -.->|Bargain| LV
        PK -.->|Bargain| MT
        PK -.->|Bargain| HB
    end

    subgraph Deities ["Primordial Powers"]
        RAD["The Radiance (Goddess of Light)"]
        NKG["Nightmare King Grimm"]
        UNN["Unn (Slug Goddess)"]
        RAD -.->|Infection| HK
        RAD -.->|Betrayal| MOTH["The Moth Tribe / Seer"]
    end

    subgraph Frontier ["Autonomous Societies"]
        ML["The Mantis Lords"]
        TL["The Traitor Lord"]
        VES["Queen Vespa (The Hive)"]
        ML -->|Exile| TL
        TL -.->|Embrace| RAD
        HB -->|Parentage| HNT["Hornet (Princess-Protector)"]
        PK -->|Parentage| HNT
    end

    KT -->|Deicide| RAD
    HNT -->|Assistance| KT
    HNT -->|Restraint| HK
```

---

## 2. Pharloom Relationship Architecture

```mermaid
flowchart TD
    subgraph Theocracy ["The High Citadel"]
        GMS["Grand Mother Silk (Supreme Matriarch)"]
        LJ["The Last Judge (Executor)"]
        CM["Choir Master & The Chorus"]
        CW["Cogwork Dancers & Sentinels"]
        GMS --> LJ
        GMS --> CM
        GMS --> CW
    end

    subgraph Protagonist ["The Wanderer and Rival"]
        HNT["Hornet (Protagonist)"]
        LC["Lace (Agile Fencer)"]
        LL["Lost Lace (Corrupted Variant)"]
        HNT <-->|Fencing Rivalry| LC
        LC -->|Corruption| LL
        HNT -->|Liberation Duel| LL
    end

    subgraph Allies ["Pilgrims and Grassroots Artisans"]
        SH["Sherma (Pious Pilgrim)"]
        SK["Shakra (Cartographer)"]
        FD["Forge-Daughter (Blacksmith)"]
        EVA["Eva (Weaver Hermit)"]
        GZ["Garmond and Zaza"]
        FC["The Flea Caravan & Flea Master"]
        BB["The Bell Beast (Transport)"]
    end

    subgraph Labor ["The Marrow and Deep Docks"]
        IW["Iron Warden (Overseer)"]
        DR["Drudge (Exhausted Miner)"]
        PP["Puppet-Pilgrims (Thralls)"]
        GMS -.->|Golden Thread| PP
        IW --> DR
    end

    HNT -->|Reforging| FD
    HNT -->|Weaver Lore| EVA
    HNT -->|Rescue| SH
    HNT -->|Rescue| FC
    HNT -->|Liberation| BB
    HNT -->|Deicide| GMS
```

---

## 3. Cross-Game Continuous Conduits

```mermaid
flowchart LR
    subgraph HallownestConduits ["Hallownest (2017)"]
        HN_PK["Pale King"]
        HN_HB["Herrah"]
        HN_WV["Weavers of Deepnest"]
        HN_VD["The Void (Abyss)"]
        HN_SL["Soul (Anima)"]
    end

    subgraph PharloomConduits ["Pharloom (2025)"]
        PH_HNT["Hornet"]
        PH_WVC["Weavers' Cradle"]
        PH_GMS["Grand Mother Silk"]
        PH_SK["Silk (Biopolymer)"]
        PH_LM["The Great Loom"]
    end

    HN_PK -->|Paternal Blood| PH_HNT
    HN_HB -->|Maternal Blood| PH_HNT
    PH_WVC -->|Ancient Exodus| HN_WV
    HN_SL -.->|Metabolic Complement| PH_SK
    HN_VD -.->|Cosmic Antithesis| PH_LM
```

---

## 4. Key Relational Dynamics
1. **Paternal and Maternal Lineage:** Hornet unites the two worlds: her father is the Pale King of Hallownest, while her mother Herrah links her directly to the Weavers whose ancestors originated in Pharloom (`EDG-005`, `EDG-006`, `EDG-046`).
2. **The Fencing Rivalry (Hornet and Lace):** Unlike the silent trials between the Knight and Hornet, the relationship between Hornet and Lace is vocal, theatrical, and intensely physical, evolving from deadly suspicion into mutual comradeship (`EDG-052`).
3. **The Interspecies Alliance (The Flea Caravan and Bell Beast):** Pharloom shifts the player's agency from solitary survival to grassroots collective rescue, emphasizing interspecies kinship and care (`EDG-063`, `EDG-064`).
