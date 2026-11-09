import os

tier_a_specs = [
    ('tier_a_the_knight', 'The Knight', 'Ghost, Little Ghost, Vessel', 'Discarded Vessel infused with Void', 'HK', "King's Pass", 'Mute protagonist; white horned mask, dark cloak; voiced by silence.',
     'The silent protagonist of Hollow Knight, a discarded Vessel returned to Hallownest to unseal the Black Egg and confront the source of the Infection.',
     "Begins in King's Pass -> explores Crossroads -> battles Hornet in Greenpath -> acquires Mantis Claw and Mothwing Cloak -> enters City of Tears -> navigates Deepnest, Basin, and Peak -> unseals the three Dreamers -> reclaims Birthplace memory to obtain Void Heart -> destroys the Radiance in Dream No More or ascends to Shade Lord in Godhome.",
     'EDG-003, EDG-004, EDG-007, EDG-008, EDG-023, EDG-024, EDG-074',
     'CLM-HK01-001, CLM-HK01-007, CLM-HK01-011, CLM-HK04-001, CLM-HK04-007, CLM-HK05-009, CLM-HK12-001, CLM-HK12-004, CLM-HK12-008, CLM-HK12-012',
     'Whether the Knight possessed latent will prior to exploration or developed will through ergodic player experience remains an active debate [Tier 3].',
     'Sacrifice, Ergodic Agency, and Muteness. The Knight embodies the return of the repressed eugenic victims.'),

    ('tier_a_the_hollow_knight', 'The Hollow Knight', 'The Sealed Vessel, Pure Vessel', 'Chosen Vessel infused with Void', 'HK', 'Temple of the Black Egg', 'Mute, armored, towering vessel; roars only when infection bursts.',
     'The chosen Vessel selected by the Pale King to contain the Radiance within its physical shell, bound inside the Temple of the Black Egg.',
     'Selected as prime Vessel in the Abyss -> raised in the White Palace -> bonded emotionally with the Pale King -> sealed inside Black Egg with three Dreamers -> tarnished by idea instilled -> shell cracked by Radiance -> stabs itself in combat -> freed or destroyed in endings.',
     'EDG-001, EDG-002, EDG-007, EDG-022, EDG-025, EDG-080',
     'CLM-HK04-002, CLM-HK04-004, CLM-HK04-005, CLM-HK04-008, CLM-HK11-007, CLM-HK12-005, CLM-HK12-007, CLM-HK12-008',
     'The exact nature of the bond shared with the Pale King in the Path of Pain remains an open emotional question [Tier 3].',
     'The Tragedy of Utilitarian Eugenics. Represents the horrific price of demanding absolute purity from sentient beings.'),

    ('tier_a_the_pale_king', 'The Pale King', 'The Wyrm, Sovereign of Hallownest', 'Reincarnated Higher Being Wyrm', 'HK', 'Ancient Basin / White Palace', 'Pristine white crown-horned visage; represented in stone tablets and dream throne corpse.',
     'The deific founder and autocratic monarch of Hallownest, who expanded insect intellect through his beacon of light.',
     "Perished at Kingdom's Edge as giant Wyrm -> molted and reincarnated into small luminous king -> founded City of Tears -> commissioned Five Great Knights -> initiated Vessel eugenics to stop Radiance -> struck bargain with Dreamers -> retreated palace into dream realm -> perished upon throne.",
     'EDG-001, EDG-003, EDG-005, EDG-010, EDG-011, EDG-012, EDG-013, EDG-015, EDG-021',
     'CLM-HK02-001, CLM-HK02-004, CLM-HK02-006, CLM-HK03-001, CLM-HK03-002, CLM-HK03-007, CLM-HK03-008, CLM-HK04-001, CLM-HK04-004',
     'Whether his retreat was cowardly abandonment or an attempt to preserve the court from infection is debated [Tier 3].',
     'Autocratic Hubris and the Denial of Decay. Explores the tragic failure of sovereign power seeking eternal stasis.'),

    ('tier_a_the_white_lady', 'The White Lady', 'Root, Queen of Hallownest', 'Higher Being Root / Tree Divinity', 'HK', "Queen's Gardens", 'Immense bioluminescent white plant root; soft maternal whispers.',
     "Consort to the Pale King, whose boundless fertility contributed to the creation of the Vessels, living in voluntary self-binding.",
     "Reigned alongside the Pale King in the capital -> birthed eggs for the Vessel project -> experienced overwhelming guilt over dead children -> retreated to Queen's Gardens -> bound herself in brambles -> guides the Knight to seek Void Heart.",
     'EDG-002, EDG-004, EDG-010, EDG-016',
     'CLM-HK02-004, CLM-HK04-001, CLM-HK04-004, CLM-HK04-010, CLM-HK08-004, CLM-HK08-006, CLM-HK12-004, CLM-HK12-011',
     'The extent of her foreknowledge regarding the failure of the Hollow Knight remains an open interpretive question [Tier 3].',
     'Guilt, Maternal Complicity, and Ecological Boundlessness. Represents the tragic remorse of the ruling elite.'),

    ('tier_a_the_radiance', 'The Radiance', 'The Forgotten Light, Absolute Radiance', 'Primordial Light Divinity', 'HK', 'Dream Realm', 'Massive luminous deific moth with blazing golden crown and crystalline spears.',
     'The primordial goddess of dreams and light, creator of the Moth Tribe, and source of the orange Infection.',
     'Created Moth Tribe in Resting Grounds -> betrayed by tribe in favor of Pale King -> retreated into subconscious dream realm -> reemerged in bug dreams as golden light -> spread physical infection -> sealed in Hollow Knight -> cracked vessel -> slain by unified Void in endings.',
     'EDG-021, EDG-022, EDG-023, EDG-027, EDG-028, EDG-041',
     'CLM-HK02-002, CLM-HK02-007, CLM-HK02-011, CLM-HK06-001, CLM-HK06-002, CLM-HK06-003, CLM-HK11-008, CLM-HK11-009, CLM-HK12-007, CLM-HK12-008',
     'Whether her infection was purely vengeful wrath or an instinctive deific urge to remain remembered is debated [Tier 3].',
     'Totalitarian Light, Memory, and the Return of the Repressed. Explores the destructive power of divine erasure.'),

    ('tier_a_hornet', 'Hornet', 'Princess-Protector, Gendered Child', 'Spider-Wyrm Royal Hybrid', 'BOTH', 'Greenpath / Moss Grotto', 'Red dress, white horned mask, long silver needle; voiced by Makoto Koji (Shaw!, Adino!).',
     "Daughter of the Pale King and Herrah the Beast, fierce protector of Hallownest's ruins and central protagonist of Silksong.",
     'Born in Deepnest as sovereign bargain -> raised by Weavers and Midwife -> defended ruins after fall -> tested Knight in Greenpath and Edge -> assisted Knight inside Black Egg -> captured by Pharloom convoy -> fell into Moss Grotto -> climbed Pharloom verticality -> defeated Last Judge -> dismantled the summit Loom.',
     'EDG-005, EDG-006, EDG-008, EDG-024, EDG-025, EDG-045, EDG-048, EDG-051, EDG-052, EDG-074',
     'CLM-HK05-008, CLM-HK08-004, CLM-HK08-007, CLM-HK08-009, CLM-HK08-011, CLM-SS02-001, CLM-SS02-006, CLM-SS03-010, CLM-SS10-010, CLM-SS12-002',
     "How her needle combat style was originally formalized before the Weavers' departure is an unresolved historical puzzle [Tier 3].",
     'Hybrid Agency, Voice, and the Refusal of Martyrdom. Bridges the two worlds from sacrificial guard to liberator.'),

    ('tier_a_quirrel', 'Quirrel', "Monomon's Apprentice, Wanderer", 'Scholar Explorer Bug', 'HK', 'Temple of the Black Egg', "Round blue cap, Monomon's mask, light rapier nail; gentle philosophical voice.",
     'Curious, wandering scholar and faithful former apprentice to Monomon the Teacher who aids the Knight across Hallownest.',
     "Entrusted with Monomon's mask -> wandered outer wastes losing memory -> drawn back to Hallownest -> meets Knight in crossroads, Mantis Village, and capital -> aids Knight against Uumuu in Archives -> relinquishes mask -> rests at Blue Lake before departing.",
     'EDG-014, EDG-020',
     'CLM-HK03-004, CLM-HK05-005, CLM-HK05-006, CLM-HK05-012, CLM-HK06-012, CLM-HK07-001, CLM-HK12-003',
     'Whether Quirrel died of rapid aging or simply walked away into the outer wilderness remains poignantly unresolved [Tier 3].',
     'Curiosity, Loyalty, and the Somatic Cost of Duty. Exemplifies intellectual devotion to breaking false stasis.'),

    ('tier_a_zote_the_mighty', 'Zote the Mighty', 'A Knight of Great Renown', 'Elderly Delusioned Bug', 'HK', 'Greenpath', 'Carved wooden nail Life Ender, ragged cloak; blustering, arrogant vocal conlang.',
     'Comic, boastful wanderer from outside Hallownest who constantly proclaims his greatness while requiring repeated rescue.',
     'Trapped by Vengefly King in Greenpath -> rescued by Knight -> trapped in Deepnest webs -> rescued again -> enters Colosseum of Fools -> serves as joke boss in Trial of the Fool -> captivates Bretta in Dirtmouth -> spawns dream boss Grey Prince Zote -> recites Fifty-Seven Precepts.',
     'EDG-038, EDG-040',
     'CLM-HK06-004, CLM-HK08-001, CLM-HK09-001, CLM-HK12-002',
     'The truth behind his references to a distant homeland and a demanding father remains ambiguous [Tier 3].',
     'Egotistical Compensation, Absurdity, and Fragile Masculinity. Provides comic relief while deconstructing knightly myth.'),

    ('tier_a_elderbug', 'Elderbug', 'Town Elder', 'Common Dirtmouth Elder', 'HK', 'Dirtmouth', 'Hunched, weathered bug with walking staff; voiced by William Pellen with gentle hospitality.',
     'The sole remaining inhabitant of Dirtmouth at the beginning of the journey, welcoming travelers to the subterranean ruins.',
     "Greets Knight upon arrival -> provides local history on the fading town and King's Pass -> watches citizens return -> receives Delicate Flower gift from Knight, finding joy -> witnesses endings.",
     'EDG-010',
     'CLM-HK03-001, CLM-HK03-004, CLM-HK06-004, CLM-HK12-001',
     'Why Elderbug never succumbed to the Infection while mining bugs nearby did is an open question [Tier 3].',
     'Domestic Stability, Memory, and the Dignity of Everyday Survival amidst cosmic cataclysms.'),

    ('tier_a_cornifer', 'Cornifer', 'Cartographer of Hallownest', 'Mosquito Explorer', 'HK', 'Forgotten Crossroads', 'Spectacles, oversized backpack with drafting parchment; cheerful rhythmic humming.',
     'Adventurous, optimistic cartographer who braves dangerous caverns ahead of the player to chart topographical maps.',
     'Explores each cavern before player -> leaves paper trail and humming clues -> sells maps to Knight -> returns to Dirtmouth shop to sleep peacefully alongside his wife Iselda.',
     'EDG-036',
     'CLM-HK03-005, CLM-HK06-004, CLM-HK07-001, CLM-HK08-001, CLM-HK09-001',
     'How Cornifer navigated extreme hazards like the acid pools of Fog Canyon without combat abilities is a humorous puzzle [Tier 3].',
     'The Spatial Ethics of Cartography. Proves that mapping alien ruins transforms terrifying darkness into navigable space.'),

    ('tier_a_troupe_master_grimm', 'Troupe Master Grimm', 'Nightmare King Grimm', 'Nightmare Vessel / Fire Master', 'HK', 'Dirtmouth', 'Tall, slender theatrical figure with crimson-lined cape; dramatic stage bow voice.',
     'Master of the nomadic Grimm Troupe who orchestrates the ritual of harvesting nightmare flames from fallen kingdoms.',
     'Summoned by striking lantern in Howling Cliffs -> sets up tents in Dirtmouth -> tasks Knight with feeding Grimmchild -> duels Knight in scarlet tent -> fought as Nightmare King Grimm in dream realm -> departs or banished.',
     'EDG-043',
     'CLM-HK02-005, CLM-HK10-001, CLM-HK10-002, CLM-HK10-004, CLM-HK10-005, CLM-HK10-006, CLM-HK10-010, CLM-HK10-013',
     'The degree of autonomy Grimm possesses separate from the primordial Nightmare Heart is disputed [Tier 3].',
     'Cyclical Ritualism and Fire Parasitism. Explores the performance of tragedy as sustenance for cosmic forces.'),

    ('tier_a_lurien_the_watcher', 'Lurien the Watcher', 'The Watcher', 'Aristocratic Dreamer', 'HK', "City of Tears (Watcher's Spire)", 'Ornate single-lensed brass mask, aristocratic robes; silent contemplative slumber.',
     'Aristocratic Dreamer who watched over the City of Tears from his high spire, devoted unconditionally to the Pale King.',
     'Governed capital affairs -> agreed to become Dreamer out of personal love for King -> guarded by Watcher Knights -> slain in dream slumber by the Knight to break Black Egg seal.',
     'EDG-011, EDG-019',
     'CLM-HK03-002, CLM-HK05-001, CLM-HK05-002, CLM-HK05-003, CLM-HK05-004, CLM-HK05-010, CLM-HK07-002, CLM-HK12-003',
     "Whether Lurien's devotion to the King had romantic dimensions is an active interpretive theory [Tier 3].",
     "Aristocratic Devotion and Surveillance. Embodies the ruling class's blind obedience to sovereign authority."),

    ('tier_a_monomon_the_teacher', 'Monomon the Teacher', 'The Teacher', 'Scholarly Dreamer Jellyfish', 'HK', 'Fog Canyon (Archives)', 'Single-eyed oval mask, aquatic membrane body; calm intellectual telepathy.',
     "Intellectual Dreamer who archived Hallownest's knowledge and foresaw the necessity of breaking the seals for renewal.",
     "Directed the Teacher's Archives -> studied natural ecosystems -> agreed to become Dreamer -> entrusted mask to Quirrel -> aided Quirrel and Knight in breaking Uumuu shield -> accepted demise to break seal.",
     'EDG-012, EDG-014, EDG-020',
     'CLM-HK05-001, CLM-HK05-002, CLM-HK05-005, CLM-HK05-006, CLM-HK05-010, CLM-HK05-011, CLM-HK12-003',
     'How Monomon communicated with Quirrel across the memory-wiping outer wastes remains a subtle mystery [Tier 3].',
     'Scientific Foresight and Generational Succession. Exemplifies intellect that accepts mortality to permit renewal.'),

    ('tier_a_herrah_the_beast', 'Herrah the Beast', 'Queen of Deepnest', 'Arachnid Matriarch Dreamer', 'HK', 'Deepnest (Distant Village)', 'Horned multi-eyed spider mask, feral chitinous form; maternal feral presence.',
     'Common bug queen of Deepnest who agreed to become a Dreamer in exchange for bearing a royal child with the Pale King.',
     'Ruled Deepnest independently -> negotiated royal bargain with King -> gave birth to Hornet -> entered perpetual slumber in Distant Village -> slain in dream by Knight with Hornet present.',
     'EDG-006, EDG-013, EDG-044',
     'CLM-HK05-001, CLM-HK05-007, CLM-HK05-008, CLM-HK05-010, CLM-HK08-002, CLM-HK08-004, CLM-HK08-011, CLM-HK12-003',
     "Herrah's feelings toward the Pale King outside their transactional reproductive pact are unrecorded [Tier 3].",
     'Maternal Ambition and Frontier Power. Demonstrates how marginalized rulers secured lineage through royal compacts.'),

    ('tier_a_soul_master', 'Soul Master', 'Soul Tyrant', 'Scholarly Headmaster', 'HK', 'City of Tears (Soul Sanctum)', 'Corpulent floating scholar with golden trim; megalomaniacal laughter and soul projectiles.',
     'Head scholar of the Soul Sanctum who harvested citizen souls in a catastrophic, hubristic quest for immortality.',
     'Conducted soul research in the capital -> defied royal ban on living extraction -> tortured hundreds of citizens -> amassed soul hoards -> succumbed to madness -> slain by Knight in sanctum and dream realm.',
     'EDG-029, EDG-030',
     'CLM-HK03-006, CLM-HK06-004, CLM-HK07-003, CLM-HK07-004, CLM-HK07-005, CLM-HK07-006, CLM-HK07-009, CLM-HK07-012',
     'Whether his soul teleportation was a natural bug ability or an artificial spell formula is debated [Tier 3].',
     'Technocratic Megalomania and the Atrocities of Expedient Science.'),

    ('tier_a_mantis_lords', 'Mantis Lords', 'Sisters of Battle', 'Trio of Mantis Monarchs', 'HK', 'Mantis Village', 'Slender, elongated mantis warriors with curved claw blades; proud rhythmic clicks and battle cries.',
     'Trio of proud sisters who governed the Mantis Tribe, resisted the Infection through honor, and held back Deepnest.',
     'Signed truce with Pale King -> banished traitor brother -> defended lower gates -> duel Knight in village throne room -> bow in respect upon defeat, opening gate to Deepnest -> fought together in Godhome.',
     'EDG-024, EDG-026',
     'CLM-HK03-011, CLM-HK06-007, CLM-HK08-001, CLM-HK09-001, CLM-HK09-002, CLM-HK09-003, CLM-HK09-012, CLM-HK11-008',
     'The exact training methods used by the Mantis Tribe to maintain absolute mental immunity are an open study [Tier 3].',
     'Martial Honor, Interspecies Truce, and Cultural Discipline as Resistance to Cosmic Infection.'),

    ('tier_a_grand_mother_silk', 'Grand Mother Silk', 'The Golden Weaver', 'Supreme Weaver Matriarch Divinity', 'SS', 'Peak of Song (The Loom)', 'Colossal crowned arachnid divinity weaving golden threads; thundering liturgical choral voice.',
     'The supreme theocratic sovereign of Pharloom, presiding over the Loom of Pharloom to weave reality and extract pilgrim life.',
     'Consolidated power at Pharloom summit -> constructed High Citadel -> instituted the Great Pilgrimage -> centralized all silk into the Loom -> suppressed dissident Weavers -> confronted and unravelled by Hornet.',
     'EDG-049, EDG-050, EDG-051, EDG-072, EDG-075',
     'CLM-SS01-004, CLM-SS03-001, CLM-SS03-002, CLM-SS03-006, CLM-SS03-007, CLM-SS03-008, CLM-SS04-004, CLM-SS10-007',
     'Whether Grand Mother Silk was biological mother to all ancient Weavers or an ascended queen is open [Tier 3].',
     'Totalitarian Deification, Acoustic Domination, and the Politics of Somatic Extraction.'),

    ('tier_a_lace', 'Lace', 'The Agile Fencer', 'Weaver/Citadel Rapier Duelist', 'SS', 'Deep Docks / High Citadel', 'Flowing white silk cloak, elegant fencing needle; sharp sarcastic laughter and theatrical banter.',
     "Acrobatic, white-cloaked rapier fencer who serves as Hornet's primary rival, critic, and mirror across Pharloom.",
     "Duels Hornet in Deep Docks foundry -> applauds and retreats -> mocks Hornet's earnestness across mid-game -> rematches Hornet in High Citadel -> falls into corruption as Lost Lace -> liberated by Hornet.",
     'EDG-052, EDG-057, EDG-080',
     'CLM-SS06-001, CLM-SS06-002, CLM-SS06-003, CLM-SS06-004, CLM-SS06-005, CLM-SS06-006, CLM-SS06-007, CLM-SS06-008, CLM-SS06-009, CLM-SS06-010',
     'Her precise biological lineage and relation to the ancient Weavers remains an unconfirmed mystery [Tier 3].',
     'Sarcastic Detachment, Martial Foil, and the Tragic Limits of Nihilism.'),

    ('tier_a_sherma', 'Sherma', 'Pilgrim of the Song', 'Humble Pious Pilgrim', 'SS', 'The Marrow', 'Tattered burlap cloak, prayer staff, small bronze hand-bell; rhythmic devotional chanting.',
     'Clumsy, earnest, and deeply pious pilgrim ascending toward the High Citadel, who befriends and relies upon Hornet.',
     'Arrives in Pharloom on pilgrimage -> navigates The Marrow -> repeatedly trapped by monsters and machinery -> rescued by Hornet -> visits roadside shrines -> reflects on the beauty and terror of the Citadel.',
     'EDG-061, EDG-069',
     'CLM-SS01-007, CLM-SS05-003, CLM-SS05-004, CLM-SS08-004, CLM-SS08-005, CLM-SS08-006, CLM-SS08-010',
     'Whether Sherma realizes the exploitative nature of the pilgrimage before the climax is left ambiguous [Tier 3].',
     'Uncritical Faith, Pathos, and the Tragic Exploitation of Religious Innocence.'),

    ('tier_a_shakra', 'Shakra', 'Cartographer of Pharloom', 'Warrior Scout Explorer', 'SS', 'Greymoor', 'Iron ring weapons, banded leather armor; sharp confident map-seller voice.',
     "Fierce warrior cartographer who explores Pharloom's hazardous verticality in search of her lost master, mapping territories.",
     "Ascends from lower caves into Greymoor -> sells regional maps and navigational tools to Hornet -> shares observations on the Citadel's defenses -> tracks master's trail to high peaks.",
     'EDG-058',
     'CLM-SS01-003, CLM-SS02-007, CLM-SS10-004, CLM-SS11-001',
     "The identity and fate of Shakra's missing master remains an intriguing open questline [Tier 3].",
     'Active Female Cartography, Independence, and the Pursuit of Kinship in Alien Geography.'),

    ('tier_a_garmond_and_zaza', 'Garmond and Zaza', 'Traveler Knight and Hound', 'Nomadic Knight Duo', 'SS', 'Greymoor', 'Heavily armored knight mounted atop an ancient, talkative bug hound; boisterous comedic banter.',
     'Adventurous traveler duo wandering Pharloom, offering witty commentary, combat companionship, and side quest tasks.',
     'Encounters Hornet in Greymoor -> assists with local beast hunts -> shares meals and campfire lore -> appears in High Citadel fringes offering aid.',
     'EDG-062',
     'CLM-SS01-003, CLM-SS10-004, CLM-SS11-002',
     'The homeland from which Garmond and Zaza journeyed is unrecorded in kingdom archives [Tier 3].',
     'Interspecies Symbiosis, Comedic Resiliency, and Nomadic Solidarity.'),

    ('tier_a_the_last_judge', 'The Last Judge', 'The Judicial Executor', 'Golden-Masked Gatekeeper', 'SS', 'Citadel Gates (Southern Gate)', 'Spiked crown, golden death mask, massive bronze gavel; thundering flame roars.',
     'Towering theocratic judicial executor guarding the monumental threshold between the lower provinces and the High Citadel.',
     'Stationed at Citadel Gate -> executes unverified pilgrims -> battles Hornet in sweeping flame duel -> destroyed by Hornet -> drops Judicial Crest allowing passage into Gilded City.',
     'EDG-053, EDG-054',
     'CLM-SS01-003, CLM-SS07-001, CLM-SS07-002, CLM-SS07-003, CLM-SS07-005, CLM-SS07-006, CLM-SS07-007, CLM-SS10-005',
     'Whether the Judge is an ascended mortal or clockwork automaton is actively debated [Tier 3].',
     'Sovereign Exception, Gatekeeping Cruelty, and the Violent Threshold of Paradise.'),

    ('tier_a_forge_daughter', 'Forge-Daughter', 'Blacksmith of the Docks', 'Towering Artisan Beetle', 'SS', 'Deep Docks', 'Massive carapace, blacksmith apron, heavy smelting hammer; deep resonant artisan voice.',
     "Towering, genial blacksmith in the volcanic foundry of Deep Docks who refines Hornet's needle and crafts heavy tools.",
     "Operates molten foundry -> welcomes Hornet after carriage fall -> refines initial needle upgrade using Rosaries -> crafts advanced throwing pins and explosive canisters -> shares local lore.",
     'EDG-059',
     'CLM-SS01-002, CLM-SS02-007, CLM-SS09-008, CLM-SS11-006, CLM-SS12-011',
     'Her past training relationship with Citadel master mechanics remains an unexplored background thread [Tier 3].',
     'Artisan Independence, Material Resistance, and the Ethics of Weapon Crafting.'),

    ('tier_a_eva', 'Eva', 'Old Weaver Eva', 'Weaver Hermit Seer', 'SS', "Weavers' Cradle / Wilds", 'Ancient arachnid robes, multiple wise eyes, spinning spindle; quiet mystical voice.',
     "Reclusive Weaver seer who recognizes Hornet's maternal lineage and teaches her the forgotten rites of ancient silk spinning.",
     'Dwelling in hidden cavern retreat -> welcomes Hornet -> tests her knowledge of thread -> reveals secrets of Deepnest migration -> unlocks the Weaver Crest and advanced spool arts.',
     'EDG-060',
     'CLM-SS03-010, CLM-SS04-006, CLM-SS04-007, CLM-SS12-009',
     'Whether Eva remained in Pharloom to preserve knowledge or was left behind during the migration is open [Tier 3].',
     'Ancestral Wisdom, Maternal Heritage Reclamation, and the Preservation of Subjugated Lore.'),

    ('tier_a_trobbio', 'Trobbio', 'Master of the Stage', 'Flamboyant Butterfly Dramatist', 'SS', 'Citadel Theatres', 'Ornate ruffled collar, dramatic feathered wings, theatrical rapier; boisterous operatic laughter.',
     'Vain, flamboyant stage master and butterfly dramatist who challenges Hornet to an acrobatic duel amidst stage pyrotechnics.',
     'Rehearses dramatic performances in Citadel theatre -> challenges Hornet as an uninvited critic -> fights amidst fireworks and spotlight lasers -> defeated with grand theatrical flair.',
     'EDG-056',
     'CLM-SS01-004, CLM-SS10-006, CLM-SS11-002',
     "The degree to which Trobbio's plays were approved state propaganda versus eccentric vanity is open [Tier 3].",
     'Aesthetic Vanity, Theatrical Absurdity, and the Diversionary Spectacles of Autocracy.')
]

os.makedirs('characters', exist_ok=True)

for spec in tier_a_specs:
    fn, name, aliases, species, game, first_app, voice_design, role, arc, edges_ref, claims_ref, interp, theme = spec
    content = f'''# Character Dossier: {name} (Tier A)

- **Name:** {name}
- **Aliases:** {aliases}
- **Species / Entity Type:** {species}
- **Game:** {game}
- **First Appearance:** {first_app}
- **Voice and Design:** {voice_design}

## 1. Role in the Story and Place in the World
{role}

## 2. Character Narrative Arc (Chronological with Spoilers)
{arc}

## 3. Motivations and Key Relationships
- Linked Graph Edges: `{edges_ref}`
- Interpersonal Dynamics: Governed by structural alliances, familial bonds, and ideological resistance detailed in `characters/relationship_maps.md`.

## 4. Key Evidence and Verified Claims
- Associated Project Claims: `{claims_ref}`
- Epistemic Status: Derived from verified secondary encyclopedic transcriptions and primary developer dispatches.

## 5. Interpretations and Gaps (Tier 3 and Disputed)
{interp}

## 6. Thematic Significance to the Project
{theme}

## 7. Open Questions and Sources to Chase
- Sources to consult: `data/sources.csv` and `data/entities.csv`.
'''
    assert '\u2014' not in content, f'em-dash in {fn}'
    assert '\u2013' not in content, f'en-dash in {fn}'
    with open(f'characters/{fn}.md', 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Generated {len(tier_a_specs)} Tier A character dossiers')

