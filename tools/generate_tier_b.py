import os

tier_b_specs = [
    ('tier_b_sly', 'Sly', 'Great Nailsage Sly, Shopkeeper', 'Fly / Nailsage Master', 'HK', 'Forgotten Crossroads / Dirtmouth',
     'Rescued shopkeeper in Dirtmouth who secretly mastered all Great Nail Arts and taught the three master brothers.',
     'Saved by the Knight in abandoned shack -> opens merchant shop in Dirtmouth -> recognizes Knight holding all Nail Arts -> reveals past -> fought as final boss of Pantheon of the Master.',
     'EDG-031, EDG-032, EDG-033', 'CLM-HK03-001, CLM-HK11-004'),

    ('tier_b_iselda', 'Iselda', 'Map Shopkeeper', 'Retired Warrior Bug', 'HK', 'Dirtmouth',
     'Cornifer\'s wife and former warrior who retired to operate the map and supply shop in Dirtmouth, sighing "Bapanada".',
     'Settled in Dirtmouth with Cornifer -> sells navigational quill, pins, and markers to Knight -> provides commentary on explorers.',
     'EDG-036', 'CLM-HK03-005, CLM-HK12-001'),

    ('tier_b_tiso', 'Tiso', 'Shield Warrior', 'Ant Warrior', 'HK', 'Dirtmouth',
     'Boastful warrior equipped with a curved shield seeking lethal combat in the Colosseum of Fools.',
     'Meets Knight in Dirtmouth, Crossroads, and Blue Lake -> enters Colosseum -> slain offscreen during trial -> body found in Kingdom\'s Edge.',
     'EDG-040', 'CLM-HK06-004, CLM-HK09-001'),

    ('tier_b_cloth', 'Cloth', 'Warrior of the Wastes', 'Cicada Warrior', 'HK', 'Fungal Wastes',
     'Nomadic cicada warrior seeking courage in battle, wandering Hallownest with a heavy club.',
     'Hides in Fungal Wastes underground -> inspired by Knight -> assists Knight against Traitor Lord in Queen\'s Gardens -> slain in mutual kill -> ghost rests peacefully.',
     'EDG-039', 'CLM-HK06-007, CLM-HK09-004'),

    ('tier_b_bretta', 'Bretta', 'Lovesick Maiden', 'Common Maiden Bug', 'HK', 'Fungal Wastes / Dirtmouth',
     'Timid bug rescued from Fungal Wastes who projects romantic fantasies onto her saviors in her personal diary.',
     'Rescued by Knight -> moves to Dirtmouth writing romantic fanfiction -> falls infatuated with Zote -> spawns dream boss Grey Prince Zote -> becomes disillusioned and leaves Hallownest.',
     'EDG-037, EDG-038', 'CLM-HK06-004, CLM-HK12-001'),

    ('tier_b_myla', 'Myla', 'Singing Miner', 'Crystal Miner Bug', 'HK', 'Forgotten Crossroads / Crystal Peak',
     'Joyful mining bug whose cheerful singing gradually succumbs to the psychic resonance of the Radiance.',
     'Sings cheerfully while mining crystal ore -> infected thoughts intrude after Soul Master -> fully turns into aggressive infected husk -> slain or left wandering.',
     'EDG-041', 'CLM-HK06-004, CLM-HK06-006'),

    ('tier_b_ogrim', 'Ogrim', 'Dung Defender, White Defender', 'Great Knight / Scarab', 'HK', 'Royal Waterways',
     'Loyal member of the Five Great Knights guarding the Waterways pump controls, dreaming of the King\'s court.',
     'Guards Waterways with dung balls -> defeated by Knight and recognizes heroic chivalry -> crafts sculptures of Five Knights -> fought as White Defender in dream realm.',
     'EDG-015, EDG-018', 'CLM-HK03-003, CLM-HK07-007, CLM-HK07-008'),

    ('tier_b_the_nailsmith', 'The Nailsmith', 'Weaponsmith of Hallownest', 'Master Artisan', 'HK', 'City of Tears',
     'Master blacksmith who refines the Knight\'s nail through multiple tiers, culminating in the Pure Nail.',
     'Refines nail using Pale Ore and Geo -> achieves perfection with Pure Nail -> asks to be slain by his masterpiece -> if spared, moves to Greenpath to paint with Sheo.',
     'EDG-035', 'CLM-HK03-002, CLM-HK12-002'),

    ('tier_b_the_collector', 'The Collector', 'Void Collector', 'Four-Armed Void Construct', 'HK', 'Tower of Love',
     'Four-armed Void entity obsessed with preserving grubs inside glass jars to keep them safe from ruin.',
     'Constructed in White Palace workshops -> went rogue in Tower of Love -> captured forty-six grubs across Hallownest -> defeated by Knight, freeing grubs.',
     'EDG-003', 'CLM-HK01-004, CLM-HK07-002'),

    ('tier_b_nosk', 'Nosk', 'Mimic Hunter', 'Predatory Mimic Arachnid', 'HK', 'Deepnest',
     'Predatory arachnid shapeshifter that mimics the appearance of familiar loved ones or the Knight to lure prey.',
     'Lures Knight through Deepnest mimic trail -> reveals monstrous arachnid neck and scuttling body -> fought in lair surrounded by suspended bug corpses -> Winged Nosk in Godhome.',
     'EDG-044', 'CLM-HK08-001, CLM-HK11-008'),

    ('tier_b_traitor_lord', 'Traitor Lord', 'Fallen Mantis Monarch', 'Infected Mantis Lord', 'HK', "Queen's Gardens",
     'Fourth mantis lord who embraced the Radiance\'s Infection for colossal muscular strength after being exiled.',
     'Banished by Mantis Lords for treason -> seized Queen\'s Gardens -> mourned loss of his daughter (Traitor\'s Child) -> slain by Knight and Cloth.',
     'EDG-017, EDG-026', 'CLM-HK06-007, CLM-HK06-010, CLM-HK09-004'),

    ('tier_b_broken_vessel', 'Broken Vessel', 'Lost Kin', 'Reanimated Sibling Vessel', 'HK', 'Ancient Basin',
     'Discarded Vessel corpse puppeteered by orange Lightseeds and infection cords guarding Monarch Wings.',
     'Fell into Abyss during eugenics -> shell broke open -> infected by lightseeds in Ancient Basin -> defeated by Knight -> fought as Lost Kin in dream realm -> spirit finds peace.',
     'EDG-009', 'CLM-HK04-003, CLM-HK04-011, CLM-HK12-002'),

    ('tier_b_hive_knight', 'Hive Knight', 'Protector of the Hive', 'Armored Bee Sentinel', 'HK', 'The Hive',
     'Loyal champion of the Hive who continues defending Queen Vespa\'s chambers, unaware of her death.',
     'Guards royal amber chambers -> battles Knight with rapier stabs and explosive spikes -> mourns fallen Queen upon defeat.',
     'EDG-010', 'CLM-HK02-008, CLM-HK09-009, CLM-HK09-010'),

    ('tier_b_the_seer', 'The Seer', 'Last of the Moth Tribe', 'Ancient Moth Hermit', 'HK', 'Resting Grounds',
     'Ancient moth guide who bestows the Dream Nail and gathers Essence to repent for her tribe\'s apostasy.',
     'Awakens the Knight\'s Dream Nail -> rewards Essence milestones -> repents for forgetting the Radiance -> dissolves into pure dream light.',
     'EDG-027, EDG-028', 'CLM-HK02-002, CLM-HK09-005, CLM-HK09-007, CLM-HK09-008'),

    ('tier_b_godseeker', 'Godseeker', 'Seeker of the Gods', 'Hive-Minded Priestess', 'HK', 'Junk Pit / Godhome',
     'Priestess from the Land of Storms who uses the Godtuner to attune to the gods of Hallownest.',
     'Rests in Junk Pit sarcophagus -> invites Knight into Godhome -> stages Pantheons -> consumed by Shade Lord or saved by Delicate Flower.',
     'EDG-023', 'CLM-HK11-001, CLM-HK11-002, CLM-HK11-003, CLM-HK11-010, CLM-HK11-011'),

    ('tier_b_bell_beast', 'Bell Beast', 'Enslaved Transport Behemoth', 'Subterranean Armored Beast', 'SS', 'The Marrow',
     'Colossal transport beast enslaved by heavy bronze bells clamped around its neck, freed by Hornet to serve as transit.',
     'Attacks Hornet in bell-induced madness -> freed by Hornet upon collar severance -> carries Hornet across subterranean bellways.',
     'EDG-063', 'CLM-SS01-007, CLM-SS09-004, CLM-SS09-005, CLM-SS09-006, CLM-SS09-009'),

    ('tier_b_steel_assassin_sharpe', 'Steel Assassin Sharpe', 'The Mechanical Hunter', 'Foreign Clockwork Hunter', 'SS', 'Greymoor',
     'Lethal robotic assassin from a distant land dispatched to hunt Hornet and eliminate her royal bloodline.',
     'Tracks Hornet across outer moors -> ambushes with mechanical drill needles and blade extensions -> driven back after fierce combat.',
     'EDG-055', 'CLM-SS01-003, CLM-SS10-004'),

    ('tier_b_pinstress', 'Pinstress', 'Needle Crafter', 'Artisan Bug', 'SS', 'Bonebottom',
     'Local craftswoman in Bonebottom who fashions throwing pins and projectile needle heads from salvaged metals.',
     'Operates crafting stall in refugee camp -> provides Hornet with initial throwing tools -> sells pin upgrades for Rosaries.',
     'EDG-066', 'CLM-SS01-002, CLM-SS09-008, CLM-SS12-011'),

    ('tier_b_the_huntress', 'The Huntress', 'Ancient Predator of Pharloom', 'Prehistoric Predatory Bug', 'SS', 'Pharloom Wilds',
     'Towering predatory insect offering ancient combat crests and hunting wisdom in exchange for organ harvests.',
     'Dwells in overgrown subterranean lair -> tasks Hornet with hunting specific beasts -> unlocks specialized Hunter Crest modifications.',
     'EDG-067', 'CLM-SS01-002, CLM-SS11-002, CLM-SS12-006'),

    ('tier_b_carmelita', 'Carmelita', 'Ant Warrior Queen', 'Ant Queen Sovereign', 'SS', 'Greymoor Fringe',
     'Fierce ant warrior queen commanding an aggressive colonial legion of specialized soldiers in the outer mounds.',
     'Governs territorial ant mound -> challenges Hornet to a duel of blades and leaping strikes -> grants ant crest upon defeat.',
     'EDG-056', 'CLM-SS01-003, CLM-SS11-002')
]

for spec in tier_b_specs:
    fn, name, aliases, species, game, first_app, role, arc, edges_ref, claims_ref = spec
    content = f'''# Character Dossier: {name} (Tier B)

- **Name:** {name}
- **Aliases:** {aliases}
- **Species / Entity Type:** {species}
- **Game:** {game}
- **First Appearance:** {first_app}

## 1. Role in the Story and Place in the World
{role}

## 2. Character Narrative Arc
{arc}

## 3. Motivations and Key Relationships
- Linked Graph Edges: `{edges_ref}`
- Interpersonal Dynamics: Mapped systematically in `characters/relationship_maps.md`.

## 4. Key Evidence and Verified Claims
- Associated Project Claims: `{claims_ref}`
- Epistemic Status: Secondary-confirmed via official game encyclopedias and developer dispatches.
'''
    assert '\u2014' not in content, f'em-dash in {fn}'
    assert '\u2013' not in content, f'en-dash in {fn}'
    with open(f'characters/{fn}.md', 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Generated {len(tier_b_specs)} Tier B character dossiers')

