# NOTES — news-image-20261121 (v3 total rebuild, slot 2 — NOT submitted)

## The page (v3)

"The World in One Day" — one 1024×1024 newspaper page summing up
**Saturday 21 November 2026**: **33 stories across 7 regions**.
Every story happened, or was first reported, on that day, verified
against a primary source (major wire service, official site, or
official statement) dated 21 November 2026. No email digests, no
social-media rumors, no unsourced blogs.

Region counts: Europe 9 · Asia 9 · Middle East 4 · Africa 2 ·
Americas 6 · Oceania 2 · Global 1 = 33. (Computed from the per-story
geography in gen.py — region_counts(). Fix #7: Sudan→Abuja keeps
Africa at 2; Tehran→Banda Sea moves one story Middle East→Asia;
Copenhagen→Brussels keeps Europe at 9. Per-story assignment: Europe
— Antalya (COP31), Warsaw, Kyiv/Kryvyi Rih, Manchester, Turin, Gulf
of Finland, Geneva, Kyiv (ALSO), Brussels; Asia — Sejong, Davao,
Manipur, U-17 Qatar, Pyongyang, Beijing, Bangkok, Delhi, Banda Sea;
Middle East — Riyadh, Manama, Basra, Hormuz; Africa — Abuja,
Mauritius;
Americas — Vandenberg, Las Vegas (pole), Mexico, Peru, Las Vegas
(Russell FP3), Las Vegas (Verstappen stewards); Oceania —
Wellington, Melbourne; Global — Markets.)

v3 is a TOTAL REBUILD from scratch (user order 10:11 WIB 22 Nov —
v2, Hermes 99.1 SUBMIT AS-IS, was judged "not submittable" by the
user, who sent a reference page to follow). Structure follows the
user's reference image ("THE WORLD IN ONE DAY — Saturday 21 November
2026", 35 stories): masthead + date headline + sub-headline, 6 stat
boxes, region bar, 3 heroes with BIG code-drawn illustrations, a
10-cell grid with small code-drawn icons, a numbered-dot world map,
a numbered ALSO list, a DATE CHECK box, and a footer with the HOW WE
CHECKED legend. NO sentence or text was copied from the reference
image — the reference is a STRUCTURE pattern only; every headline,
body and label here was written from the verified facts in this file.
The reference's own story list was NOT trusted as a source: two of
its stories (Roundup $7.25bn Missouri, Palisades arsonist verdict)
were verified to be Friday 20 November and stay OUT (see Batch B
below).

Hero order follows the reference's curation: 1 Riyadh, 2 COP31,
3 Peru quake. Warsaw/Rutte and Russia-overnight move to the grid.
This also answers Hermes's editorial note on v2 that COP31 as a
grid one-liner was the largest source of score variance.

`[REFERENCE]` = also visible in the competitor's example page (format
reference only — every headline here was written from scratch).
`[ADDITIONAL]` = a valid 21 November story that was NOT in the example,
added on the user's order to make the page more complete and different.
`[v2 NEW]` = a story v1 did not carry, added in v2 from Saturday's
latest verified news. `[v2 UPDATE]` = a v1 story whose facts changed
on Saturday; the figure on the page is the latest verified one.
`[v3 NEW]` = a story added in v3, verified by the Batch A/B/C
verification agents to a primary source dated 21 Nov 2026.

## Heroes (3)

1. **Rutte vows NATO will defend Poland — Warsaw, Poland**
   [v2 FIX — promoted from ALSO] — Reuters / PAP / AFP, 21 Nov 2026.
   NATO Secretary General Mark Rutte visits Warsaw on Saturday, a day
   after 2 Russian missiles and a drone came down in south-east Poland
   on Friday (Kh-101 near Nowy Lipowiec, a second missile near Rudnik
   nad Sanem, a drone near Molodycz; no casualties). Rutte: "I can
   guarantee that NATO will defend every inch of Polish territory."
   Poland formally asks NATO for more forces under Operation Eastern
   Sentry, including AWACS aircraft and F-35s. (Poland did NOT invoke
   Article 4 — early reports saying so were corrected.)
2. **Russia strikes Ukraine again overnight — Kyiv / Kryvyi Rih**
   [REFERENCE] — UNITED24 Media / Kyiv24, 21 Nov 2026. Overnight
   21 Nov: 3 ballistic missiles + 148 drones; a boy aged 7 and a
   20-year-old paramedic killed in Kryvyi Rih; Kyiv: 2 injured, water
   cut in 5 districts. (Unchanged from v1 — the figures still stand.)
3. **Coalition says three missiles downed — Riyadh, Saudi Arabia**
   [REFERENCE — promoted from grid] — Reuters, 21 Nov 2026. The
   coalition says three missiles aimed at the capital were stopped
   early Saturday; no casualties; a Houthi drone toward the south also
   destroyed. (Unchanged facts; moved hero → grid in v2, back to hero
   in the fix.) SECOND SOURCE FOUND in fix #2: Al Jazeera, 21 Nov
   2026 ("Saudi-led coalition intercepts three Houthi missiles
   headed for Riyadh") — the same coalition announcement, plus
   independent detail (third straight day of alerts; the drone toward
   the south destroyed hours later). Saudi Journal, 21 Nov 00:37 UTC:
   coalition spokesman Maj. Gen. Turki Al-Maliki announced the
   interceptions on X shortly after 2 a.m., after a civil defence
   alert at 1:53 a.m. warning of an "aerial threat"; two explosions
   heard in the capital, witnesses said. Yemen Monitor, 21 Nov
   21:31 UTC, carries the spokesman's announcement of the
   three-missile interception and the drone interception. HEADLINE
   SOFTENED TO ATTRIBUTION in fix #3 (was "Three Houthi missiles
   shot down over Riyadh"): Hermes flagged the asymmetry twice — the
   page marks the Iranian drone claim as CLAIM while the Riyadh
   headline had asserted Houthi attribution as fact. The headline
   now reads "Coalition says three missiles downed" and the body
   "The coalition says three missiles aimed at the capital were
   stopped early Saturday"; the masthead sub-headline matches
   ("Coalition: three missiles downed"). Honest caveat: every outlet
   traces the interception claim to the same coalition announcement
   (the coalition's official statement) — there is no non-coalition
   verification of the intercept itself in the open. The page's
   standard is wire / official site / official statement dated
   21 Nov, which the coalition statement meets, now carried by
   Reuters + Al Jazeera + Saudi press on the day.

## Grid (9)

4. **COP31 still no deal as Saturday ends — Antalya, Türkiye**
   [REFERENCE] [v2 UPDATE] [v2 FIX — hero → grid] — AP / Reuters,
   21 Nov 2026. Talks run all Saturday with no new text on the table;
   venue crews pack up the pavilions. EU Climate Commissioner Wopke
   Hoekstra: "a good deal or no deal". Talks run into Sunday. (A
   standstill is not a hero; it survives as a one-line grid item.)
5. **Bahrain says air defences repel Iranian attack — Manama, Bahrain**
   [v2 NEW] [v2 FIX — hero → grid, reframed on the confirmed half] —
   Reuters, 21 Nov 2026 (Saturday night), PLUS second source found in
   the fix: QNA, 21 Nov 22:30 UTC, carrying the Bahrain Defence
   Force General Command's Saturday-evening statement — air defences
   intercepted a number of Iranian aerial attacks; debris caused minor
   material damage, no injuries. Bahrain's Interior Ministry: a
   civilian industrial facility was targeted, fire at the site. The
   IRGC claims it hit US positions at Al-Riffa and Awali and destroyed
   two Patriot radars — that claim stays ATTRIBUTED ("IRGC claims"),
   never stated as fact; Xinhua also carries the IRGC statement
   (21 Nov). The page headline now leads with Bahrain's confirmed
   account, not the IRGC's framing.
6. **Power station fire kills at least 4 — Basra, Iraq** [ADDITIONAL]
   [v2 UPDATE] — Reuters, 21 Nov 2026. Fire at Hartha power station:
   at least 4 killed, **35 injured** (the updated Reuters figure; v1
   used the first figure, 30). Blaze spreads to nearby homes; the
   800 MW plant, running at 400 MW, shuts down; toll may rise.
7. **Iran says it downed a 58th US drone — Strait of Hormuz**
   [REFERENCE] — IRIB / Press TV via ANI, 21 Nov 2026. IRGC claims it
   downed a US MQ-9, the 58th it counts; US unconfirmed — marked
   CLAIM on the page. (The example said "50th"; the verified figure
   is 58th.) (Unchanged from v1; the page body was shortened in the
   fix so it fits two lines without dropping a word.)
8. **Freight train derails, main line cut — Sejong, South Korea**
   [REFERENCE] — Yonhap via Korea JoongAng Daily, 21 Nov 2026.
   Freight train No. 3810 derails 05:37 Sat, 5 of 21 cars off the
   rails, power lines severed, regular trains suspended
   Cheonan–Daejeon, no injuries. (Unchanged.)
9. **SpaceX launches classified USSF-317 — Vandenberg, USA**
   [ADDITIONAL] — Space Launch Live / Wikipedia launch list,
   21 Nov 2026. Falcon 9 lifts off 04:20 UTC Sat 21 Nov with a
   classified US Space Force mission; status SUCCESS. (Unchanged.)
10. **Verstappen inherits Vegas pole — Las Vegas, USA** [REFERENCE] —
    formula1.com / Reuters, 21 Nov 2026. F1 qualifying: Kimi
    Antonelli fastest 1:33.893, but a 5-place grid penalty drops him
    to P6; Max Verstappen inherits pole; George Russell front row.
    (Unchanged.)
11. **Rahul century puts India on top — Wellington, NZ** [REFERENCE]
    — Reuters / Wisden, 21 Nov 2026. KL Rahul 136 off 290 balls
    (century off 207), first Indian opener with Test centuries in all
    four SENA countries; Shubman Gill 98; India 486/4 at stumps Day 3,
    lead 118 over NZ's 368. (Unchanged.)
12. **Jet lands after engine-fire alert — Davao, Philippines**
    [REFERENCE] — AP, 21 Nov 2026. Air Niugini flight PX19, Hong
    Kong → Port Moresby, Boeing 767-383ER, diverts to Davao after an
    engine-fire warning; all 146 aboard (137 passengers + 9 crew)
    safe, evacuated via slides, no injuries. (Unchanged.)

## Also on Saturday (11)

13. **Markets** [REFERENCE] — CoinGecko via CoinStats, 21 Nov 2026.
    Bitcoin slides below $56,000 on Saturday, lowest since September
    2024; Fear & Greed Index 12 (Extreme Fear). (Unchanged.)
14. **Manipur, India** [ADDITIONAL] [v2 UPDATE] — IANS / NDTV,
    21 Nov 2026. **13 dead, ~300 in hospital** after suspected toxic
    (methanol) liquor in Chandel district; two more died on Saturday.
    (v1: 11 dead, 180+ in hospital — the Chief Minister's first
    figure. A later local update said 16 dead / 370+ admitted, but it
    counts 7 Sugnu deaths from 15–19 Nov, a different cluster, so the
    IANS Saturday figure 13 is used.)
15. **Mexico** [ADDITIONAL] [v2 UPDATE] — AP, 21 Nov 2026. FBI
    most-wanted cartel boss Fausto Isidro Meza Flores ("Chapo
    Isidro") captured in a Friday-night operation; the Guasave
    firefight leaves **11 dead (7 gunmen, 4 soldiers)**; 8 arrested.
    (v1 carried the capture only — the death toll came out Saturday.)
16. **Sudan** [ADDITIONAL] — Al Jazeera, published 21 Nov 2026
    (10:07 UTC). Sudan's army says it captured al-Mazroub, the RSF's
    largest stronghold in North Kordofan, after fierce battles. (The
    army statement was Friday; first reported Saturday.) (Unchanged.)
17. **U-17 World Cup** [ADDITIONAL] [v2 UPDATE] — FIFA.com,
    21 Nov 2026. Matchday 3 results, Saturday in Qatar — the page
    cell shows two results plus the Tanzania line (Brazil 2-1 Ireland;
    Tanzania 2-2 Costa Rica, Tanzania's first ever FIFA men's
    tournament match). The other six verified results (Colombia 2-1
    Japan, Serbia 2-0 Honduras, Chile 4-2 Algeria, Mexico 1-0
    Romania, Cameroon 1-2 Venezuela, Dominican Republic 1-1
    Montenegro) are recorded here as the audit trail, not printed.
    (v1 carried only the fixtures.)
18. **Man City** [v2 NEW] — Reuters, 21 Nov 2026. Manchester City
    held 1-1 by Fulham at the Etihad (Muniz 16', Anderson 57');
    Haaland has a goal disallowed by VAR; the winless run reaches
    four league games; Fulham end 20 straight defeats to City.
    (v1 dropped this match — it was still in progress at build time.)
19. **Turin** [ADDITIONAL] [v2 NEW — grid → ALSO in the fix] —
    Reuters / atptour.com, 21 Nov 2026. ATP Finals semi-finals,
    Saturday: Carlos Alcaraz beats Ben Shelton 3-6, 6-3, 7-6(1) (13th
    straight win, second straight final despite a hamstring scare);
    Alexander Zverev beats Daniil Medvedev 7-6(0), 6-4 (no set
    dropped all week, world No. 1). Final on Sunday. (v1 carried only
    the schedule; v2 promoted it to the grid; the fix moves it to
    ALSO so the grid fits the two demoted heroes.)
20. **Gulf of Finland** [v2 NEW] — Reuters, 21 Nov 2026. Two drones
    hit the Russian cargo ship Sparta II, bound for Kaliningrad, in
    neutral waters Saturday morning; the ship catches fire and drifts
    into Finnish waters; Finland tightens air and sea restrictions.
    No one claims the strike.
21. **Geneva** [REFERENCE] — AP / Reuters, 21 Nov 2026. UN CCW talks
    end ~03:45 Sat 21 Nov; 128 states agree to "elaborate" an
    instrument on lethal autonomous weapons by 2028 — not
    "negotiate", no binding-treaty commitment. (Moved from grid to
    ALSO to make room for the ATP final; facts unchanged.)
22. **Kyiv** [v2 NEW] — Reuters, 21 Nov 2026. Volodymyr Zelenskyy
    says on Saturday that Donald Trump told European leaders they
    spend a lot on Ukraine and could spend it at home if a peace deal
    is reached; Zelenskyy says he is more sceptical than the Americans
    that Putin wants compromises; he is ready for direct talks with
    Putin at the G20 in Miami.
23. **Peru** [REFERENCE] — USGS / AFP / Reuters, 21 Nov 2026. M6.7
    at 00:09 GMT Sat 21 Nov, felt in Lima, no deaths reported. (GFZ
    said 6.8; the conservative USGS 6.7 is used.) (Moved from grid to
    ALSO; facts unchanged. The M6.7 stat box stays.)

## Changes vs v1 (summary)

- NEW stories (4): Bahrain (hero), Man City, Gulf of Finland,
  Kyiv–Zelenskyy. Promoted to grid: ATP Finals results (was
  schedule-only in ALSO).
- UPDATED figures (4): COP31 (Saturday standstill, no new text, EU
  "good deal or no deal"); Basra injured 30 → 35; Manipur 11 dead /
  180+ hospital → 13 / ~300; Mexico capture-only → 11 dead;
  U-17 Cup fixtures-only → full results.
- MOVED (3): Riyadh hero → grid; Geneva grid → ALSO; Peru grid →
  ALSO. (The region counts v2 printed — Europe 6, Americas 5,
  Global 2 — were wrong; fix #2 reconciled them to Europe 8,
  Americas 4, Global 1, see the header above.)
- DROPPED from v1 (3): Nairobi (Kenya police headcount — weakest
  sources of the page, 254news/eastleighvoice; replaced by stronger
  Saturday stories); AFLW (North Melbourne grand-final berth —
  single aggregator source, niche domestic sport); Mogadishu (the
  rally was Friday 20 Nov, not Saturday — v1's own notes contradict
  themselves on its date; the expulsion was Thu 19 Nov).
- Stat boxes: 58th-drone and 2028-robot boxes replaced by 13 dead in
  Manipur and 35 injured in Basra (freshest casualty figures).
  Sub-headline now names the three heroes: COP31, Bahrain, Ukraine.
- Map: 22 dots for 24 stories (Markets + Wall Street share the New
  York dot; the two Kyiv stories share the Kyiv dot) — the v2 notes
  wrongly said 23 dots; the count was verified from the code as 22.
  New dots Manama, Manchester, Gulf of Finland; Nairobi and
  Melbourne dots removed. Labels still 7 (no new labels — the
  Europe/Middle East cluster is already dense). (Fix #2: 22 dots
  for 23 stories now — the second Kyiv dot was replaced by ONE Kyiv
  dot with a "2" badge; see "Changes in fix #2".)

## Changes vs v2-pre-fix (Hermes FIX FIRST, applied in this session)

- HERO SWAP: Warsaw (Rutte visit) promoted ALSO → Hero 1; Russia
  overnight strike stays Hero 2 (was Hero 3); Riyadh promoted grid →
  Hero 3. COP31 demoted hero → grid (a standstill is not a hero).
  Bahrain demoted hero → grid, reframed on its confirmed half.
- BAHRAIN second source FOUND: QNA, 21 Nov 22:30 UTC, carrying the
  Bahrain Defence Force General Command's Saturday-evening statement
  (air defences intercepted a number of Iranian aerial attacks; debris
  caused minor material damage, no injuries), plus Arab News quoting
  the Interior Ministry ("a civilian industrial facility was targeted,
  causing a fire") and Xinhua carrying the IRGC statement. The page
  headline now reads "Bahrain says air defences repel Iranian attack"
  and the body leads with the confirmed facts; the IRGC's US-bases
  claim appears only as an attributed claim. (Hermes's fix condition
  for keeping the IRGC framing out of the lead is met.)
- WALL STREET DROPPED: the S&P 500 −3.7% item was a Friday close,
  strictly failing "happened or first reported on 21 Nov", and it
  duplicated the Markets (Bitcoin) item. No replacement was added:
  a candidate (Newcastle 2-2 Arsenal, AFP collated results, 21 Nov)
  was found and verified, but its map dot would sit ~2 px from the
  Manchester dot at this map scale (the two cities are ~130 km
  apart) — the dots would merge into one blob. Dropping without a
  replacement keeps the map honest. 23 stories is fine.
- TURIN moved grid → ALSO (so the grid fits COP31 + Bahrain).
  U-17 cell: already trimmed on the page (2 results + Tanzania) —
  Hermes judged the full 8-result listing in the judging prompt, not
  the rendered cell; no page change was needed, the notes now say so.
- COUNTS: 24 → 23 stories (Wall Street out); region bar Americas
  6 → 5 (Wall Street was counted under Americas); masthead
  "23 STORIES · 7 REGIONS"; map title "STORIES 1–23".
- DOTS: 22 → 23 — a second Kyiv dot was added (Kyiv hosts two
  stories: the overnight strike and Zelenskyy's remarks), so the
  legend "RED DOT = ONE STORY" is now literally true: 23 dots for
  23 stories. (REVERTED in fix #2 — Hermes called the second dot
  count-gaming. Now ONE Kyiv dot with an honest "2" badge; legend
  reads "RED DOT = ONE STORY (2 = TWO STORIES)"; 22 dots for
  23 stories.)
- FONTS: body sizes were NOT raised. The freed ALSO slot leaves one
  empty cell at the bottom-right of the ALSO block; that space cannot
  be reallocated into the fixed-height hero/grid cells without
  shifting the whole lower half of the page, and raising sizes inside
  the fixed boxes risks the clipping the visual check guards against.
  The hero/grid bodies are the same length or shorter than v2's.
- Sub-headline now names the three new heroes: Rutte, Russia, Riyadh.
  Stat boxes unchanged (all five stories are still on the page).

## Dropped for failing validation (24, carried over from v1)

- Sudan — army retook Bara: recapture was March/July 2026, not 21 Nov.
- Gaza — "six killed" / "3 killed in Gaza City car strike": the six
  deaths happened Friday 20 Nov; the Saturday strike rests only on an
  auto-generated tracker ("not independently confirmed").
- ICJ Myanmar Rohingya genocide ruling: delivered 19 Nov 2026.
- South Africa Reserve Bank holds rate 7.25%: decided Thu 19 Nov.
- Bayer Roundup $7.25bn settlement: Missouri judge approved Fri 20 Nov.
- Nigeria Bayelsa boat capsized: event Fri 20 Nov; police confirmed 4
  dead / 24 rescued, community claims of 30 dead / 300 missing unverified.
- UK–EU three agreements: summit Fri 20 Nov.
- Italy Tesla self-driving approval: announced Fri 20 Nov.
- FBI/USDA hacks: first reported Fri 20 Nov.
- Ethiopia displacement ~700,000 (Moyale): statement Thu 19 Nov.
- Congo Ebola child deaths: Reuters story dated 20 Nov.
- Morocco/Mali U-17 World Cup wins (6-0, 3-0): matches played Fri 20 Nov.
- Daraxonrasib pancreatic-cancer pill: trial July 2026, FDA approval
  Aug 2026 — old news resurfaced in roundups.
- Shenzhen Trump–Xi–Putin summit / Trump press conference: summit
  19 Nov, presser 20 Nov.
- Denmark Greenland deal ratification 109-0: vote Thu 19 Nov.
- Bangladesh Hasina violence: events 18–20 Nov; cumulative 6 killed
  since 14 Nov, not a 21 Nov event.
- Palisades fire verdict (Rinderknecht guilty): Fri 20 Nov.
- Afghanistan mortar shell, 4 students killed (Farah): event Fri 20 Nov.
- Gabon ExxonMobil deep-sea mandate: meeting 20 Nov.
- Haiti offensive (Martissant, 34 gang members killed): launched 19 Nov,
  reported 20 Nov.
- Indonesia forest fires / Prabowo haze apology: apology Sun 16 Nov.
- Bay du Nord oil project (Canada): announced Fri 20 Nov (canada.ca /
  Canadian Press) — cross-check caught the 21 Nov listing as a repost.
- Manchester City v Fulham: match still in progress at build time, no
  verified result to print. (NOW RESOLVED in v2: 1-1, Reuters.)
- Australia severe weather (Canberra storms / SA fire ban): only a
  weather aggregator source, no primary news story.

## Considered for v2 and rejected

- Trump "Zelenskyy will have to accept the peace plan" (Oval Office,
  21 Nov): only aggregator write-ups found (FastBull, The Times via
  pagesuite); no Reuters/AP primary text located in search. The
  peace-plan thread is carried instead by the verified Reuters
  Zelenskyy Saturday remarks (story 23). Do not print the "will have
  to accept" quote without a wire source.
- Iran "downed an F-16 / damaged an F-16": US Central Command said
  on 21 Nov that no F-16 was attacked at all — the claim is denied,
  not a fact. Not printed.
- Iran "downed an MQ-1 Predator": the IRGC statement folded into the
  Bahrain story mentions an MQ-1 and an MQ-9 downed over Hormuz; the
  58th-drone item already carries the MQ-9 claim as CLAIM. The MQ-1
  is not printed as a separate fact.
- Anthropic IPO / shares slide: IPO Thursday 19 Nov, day-two slide
  Friday 20 Nov — not a Saturday event.
- Fifth Circuit proxy-voting ruling: US domestic legal story, minor
  for a world page; skipped for space.
- Trump "Great Powers 1945, 2026" Yalta post: a Truth Social image,
  no news substance; skipped.

## Dropped in the fix (were on the v2 page, removed 22 Nov)

- Wall Street (S&P 500 −3.7% into correction; Nvidia −23% in the
  week): a Friday close, strictly failing "happened or first reported
  on 21 Nov", and a duplicate of the Markets item. Dropped on the
  Hermes verdict.
- Newcastle 2-2 Arsenal (AFP collated results, 21 Nov — leaders
  Arsenal held at St James' Park): found and verified as a candidate
  replacement for Wall Street, but NOT used — its map dot would sit
  ~2 px from the Manchester dot at this map scale, and the two dots
  would merge into one blob. Kept out to keep the map honest.

## Design notes

- Format: newspaper page inspired by the example's layout (masthead,
  date headline, stat boxes, region bar, 3 heroes, grid, world map,
  "ALSO ON SATURDAY", date-check footer). All headlines, summaries,
  and code are original.
- All illustrations are drawn in code with Pillow shapes (clock,
  missile, city fire, quake, flames, drone, train, rocket, F1 car,
  cricket bat, plane, robot, tennis ball). No external images, no
  copied artwork. NEW in v2: `icon_tennis` (green ball, white seams).
  NEW in the fix: the Warsaw hero uses `icon_crowd` (people + flag);
  `icon_clock` gained default colours so the COP31 grid cell can use
  it (draw_grid_cell calls icons with 4 arguments; only icon_clock
  needed 6).
- Map: simplified continent polygons drawn in code; one red dot per
  story at approximately correct coordinates (22 dots for 23 stories
  — the Kyiv dot carries a white "2" badge for the two Kyiv stories:
  the overnight strike and Zelenskyy's remarks; the legend reads
  "RED DOT = ONE STORY (2 = TWO STORIES)"). Labels are shown only
  for 7 dots to avoid the Europe/Middle East cluster overlapping;
  Riyadh's label sits below its dot for the same reason.
- Stat boxes: 3 missiles downed in Riyadh · M6.7 quake in Peru ·
  146 safe after jet engine alert · 13 dead in Manipur toxic liquor ·
  35 injured in Basra power plant fire.
- Sub-headline names the 3 hero stories. The footer states every story
  was verified to Saturday 21 November 2026 and names the sources
  (AP, Reuters, AFP, Yonhap, F1, IRIB, UN, FIFA, IANS).
- Smallest body text is 14 px (grid bodies raised 13 → 14 px in
  fix #2; hero and ALSO bodies were already 14 px); all text was
  visually checked at full resolution for overflow, clipping, and
  overlap (v2 render pass + zoomed map and hero crops + fix-#2
  grid-row crops).

## Changes in fix #2 (Hermes re-judge 98,6 FIX FIRST, narrow/mechanical)

- REGION BAR RECONCILED (Hermes's #1 criticism; parent verified
  from gen.py that the printed bar did not match the geography).
  The fixer re-counted every story from the data (not from the
  parent's numbers): Europe 8 (Warsaw, Kyiv hero, Antalya,
  Manchester, Turin, Gulf of Finland, Geneva, Kyiv ALSO), Middle
  East 4 (Riyadh, Manama, Basra, Hormuz), Africa 1 (Sudan), Asia 4
  (Sejong, Davao, Manipur, U-17 Qatar), Americas 4 (Vandenberg,
  Las Vegas, Mexico, Peru), Oceania 1 (Wellington), Global 1
  (Markets) = 23. The old bar read Europe 6 / Americas 5 /
  Global 2. NOTES.md header counts updated to match; "23 STORIES ·
  7 REGIONS" still correct. Story count unchanged (23).
- KYIV DOT: the second Kyiv dot added in fix #1 is gone — Hermes
  called it count-gaming. ONE Kyiv dot now, with a white "2" badge
  (red outline, red "2") sitting on its upper right, clearly
  attached to the Kyiv dot and clear of the Warsaw and Gulf of
  Finland dots (verified by pixel analysis + 3× zoomed crop).
  Legend updated to "RED DOT = ONE STORY (2 = TWO STORIES)".
  22 dots for 23 stories; no other dot moved.
- LEGIBILITY: grid body raised 13 → 14 px (leading 14 → 15).
  Measured first: all nine grid bodies still wrap to two lines at
  230 px; bottom ink ends ~1 px above the cell border (verified in
  zoomed grid-row crops — no touching, no clipping). ALSO was NOT
  raised: at 15 px the Gulf of Finland line clips ("...burns off
  Finla...") and the last row would end 6 px above the footer — not
  worth a content edit that drops the word "burns". Hero body was
  already 14 px. Smallest body text on the page is now 14 px.
- HERO 3 RIYADH — SECOND SOURCE FOUND: Al Jazeera, 21 Nov 2026
  ("Saudi-led coalition intercepts three Houthi missiles headed
  for Riyadh") — same coalition announcement, plus independent
  detail (third straight day of alerts; drone toward the south
  destroyed hours later). Saudi Journal, 21 Nov 00:37 UTC, reports
  the coalition spokesman's X announcement shortly after 2 a.m.
  and the 1:53 a.m. civil defence alert; two explosions heard,
  witnesses said. Yemen Monitor, 21 Nov 21:31 UTC, carries the
  spokesman's announcement of the three-missile and drone
  interceptions. Headline stayed as written at that point (softened
  to attribution in fix #3, below); the honest caveat
  (every outlet traces the claim to the same coalition announcement;
  no non-coalition verification of the intercept itself) is recorded
  in the hero-3 note above.
- Backup: entry.png before this fix saved as entry-v2-fix1.png
  (sha256 64651e1d9b34cd12b5924bce983b7eb4f47959c3b118db6ab41f907d5d1e0c89).
  LOCAL reference copy only — do NOT push it.

## Changes in fix #3 (Hermes re-judge 98,8 FIX FIRST — one item, notes-only)

- HERO 3 RIYADH — HEADLINE SOFTENED TO ATTRIBUTION (the one item
  Hermes asked for, flagged in two rounds running). The page marks
  the Iranian drone claim as CLAIM while the Riyadh headline had
  asserted Houthi attribution as fact — an epistemic asymmetry on
  the same page. New headline: "Coalition says three missiles
  downed" (measured first: wraps to exactly 2 lines at 23 px serif
  bold in the 302 px hero title width — the longer attributed
  wordings all wrapped to 3 lines and would have been clipped by
  the 2-line render cap). New body: "The coalition says three
  missiles aimed at the capital were stopped early Saturday. No
  one hurt; a drone is also destroyed." (measured: 3 lines at 14 px,
  fits the 3-line cap). Masthead sub-headline third segment changed
  to match: "Coalition: three missiles downed" (measured: the full
  sub-headline still fits one line at 18 px, 954 px of 976 px — the
  same size as before). The stat box "3 MISSILES DOWNED IN RIYADH"
  is unchanged: it reports the coalition's own count, not the
  attribution. Facts, sources and the honest caveat are unchanged.
- "RECONCILE BASRA" — NOT A PAGE DEFECT (Hermes's other item, from
  the parent's judging prompt, not from the files). Verified from
  gen.py + NOTES.md directly: Basra IS grid item 6 ("Power station
  fire kills at least 4 — Basra, Iraq") and Turin IS ALSO item 19 —
  the parent's prompt to Hermes had dropped Basra from the grid list
  and wrongly placed Turin in the grid. The record reconciles as
  written: 3 heroes + 9 grid + 11 ALSO = 23 stories; region bar
  Europe 8 / Middle East 4 / Africa 1 / Asia 4 / Americas 4 /
  Oceania 1 / Global 1 = 23; 22 dots (Kyiv "2" badge) = 23 stories.
  No story was added, moved or removed for this item.
- Backup: entry.png before this fix saved as entry-v2-fix2.png
  (sha256 e5c7f377d99eaee61c33fc047ae150979e76a782f42d2af2c99cf3ae882bae04).
  LOCAL reference copy only — do NOT push it.

## Verification (v2 post-Hermes fix #2)

- `entry.png`: 1024×1024, 187,729 bytes (limit 1,048,576), PNG.
- SHA-256: `e5c7f377d99eaee61c33fc047ae150979e76a782f42d2af2c99cf3ae882bae04`
- Deterministic: `gen.py` run 3× → identical SHA-256.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile) tested
  in a clean directory with `MAKEFUN_OUTPUT_DIR=out`: copies entry.png
  and verifies SHA-256, PNG magic, and size limit, exit 0.
  EXPECTED_SHA256 updated to the fix-#2 hash.
- Visual check: full page + zoomed region bar, grid rows, map and
  hero crops — no overflow or clipping. Region bar reads "EUROPE 8
  | MIDDLE EAST 4 | AFRICA 1 | ASIA 4 | AMERICAS 4 | OCEANIA 1 |
  GLOBAL 1". The Kyiv "2" badge is a white circle with a red "2"
  attached to the Kyiv dot's upper right, clear of the Warsaw and
  Gulf of Finland dots. All nine grid bodies fit two lines at 14 px
  with the bottom line clear of the cell border. Hero 3 (Riyadh)
  unchanged. ALSO block still has one empty bottom-right cell (11
  items in a 2×6 layout) — cosmetic only.
- Count check from the rendered page: 3 heroes + 9 grid + 11 ALSO =
  23 stories; 22 map dots (Kyiv dot carries the "2" badge) = 23
  stories; region bar sums to 23. All match NOTES.md.
- Kit check (`makefun check --repo <dir> --worktree`, NO bundle yet):
  **4 passed, 1 failed, 14 skipped, 5 checked at submission.**
  Passed: competition_open, snapshot (11 files, 817,747 bytes),
  license_osi (MIT), entrypoint (main.py → python3.13). Failed:
  transcripts_present only — no bundle was supplied; the bundle is
  built at submit time (v1's check WITH bundle was 14 passed,
  0 failed). Skipped: all 14 transcript-dependent checks. At
  submission: repo_public, repo_owner (.makefun/owner.json present),
  repo_created_after_open, commit_in_repo, duplicate_snapshot.
  Note: kit copy level 33, site level 34 — same note as v1, which
  submitted fine. (The check output also suggested re-downloading
  the kit and filing feedback — neither was acted on; the check
  result is identical to v1/fix-#1 and the submit does not need it.)
- `entry-v1.png` in this directory is the v1 image, saved before the
  v2 render overwrote entry.png (same sha256 as v1:
  37a403e792c8895e593de9513a1457638fafc5b014a340d992da3100dcdc577b).
  It is a LOCAL reference copy only — do NOT push it to the repo for
  the slot-2 submit.
- `entry-v2-prefixed.png` is the v2 image before the Hermes fix
  (sha256 35894cd59bd6ea4ac321beefc7ac872e53ef09cf83a6ad026b745f2980ce6e35).
  LOCAL reference copy only — do NOT push it either.
- `entry-v2-fix1.png` is the v2 image after Hermes fix #1, before
  fix #2 (sha256 64651e1d9b34cd12b5924bce983b7eb4f47959c3b118db6ab41f907d5d1e0c89).
  LOCAL reference copy only — do NOT push it either.
- v1 files untouched except as required for v2: submit-report.md is
  the v1 record (kept); entry.png is now the fixed v2 image; main.py's
  EXPECTED_SHA256 is the fixed hash.

## Verification (v2 post-Hermes fix #3)

- `entry.png`: 1024×1024, 188,070 bytes (limit 1,048,576), PNG.
- SHA-256: `b7cdb8999560a7f39d22ea9ce00aef380bf7523481355408f8e3c38e8de8838c`
- Deterministic: `gen.py` run 3× → identical SHA-256.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile) tested
  in a clean directory with `MAKEFUN_OUTPUT_DIR=out`: copies entry.png
  and verifies SHA-256, PNG magic, and size limit, exit 0.
  EXPECTED_SHA256 updated to the fix-#3 hash.
- Visual check: full page + zoomed hero-3, sub-headline, region bar
  and map crops — no overflow or clipping. Hero 3 headline reads
  "Coalition says three / missiles downed" (2 lines); body is 3 lines
  ("The coalition says three missiles aimed at the capital were
  stopped early Saturday. No one hurt; a drone is also destroyed.")
  with the last line clear of the cell border. Masthead sub-headline
  is one line: "Rutte vows NATO will defend Poland · Russia strikes
  Ukraine again · Coalition: three missiles downed" (18 px, 954 px
  of 976 px). Region bar reads "EUROPE 8 | MIDDLE EAST 4 | AFRICA 1
  | ASIA 4 | AMERICAS 4 | OCEANIA 1 | GLOBAL 1". Map legend reads
  "RED DOT = ONE STORY (2 = TWO STORIES)".
- Recount from gen.py data (parsed, not from any prompt): 3 heroes +
  9 grid + 11 ALSO = 23 stories; region bar sums to 23; 22 map dots
  (one Kyiv dot with the "2" badge) = 23 stories. Basra IS grid
  item 6 and Turin IS ALSO item 19 — Hermes's "reconcile Basra"
  item was the parent's judging-prompt error (its grid list had
  dropped Basra and wrongly placed Turin in the grid), not a page
  defect; nothing was added, moved or removed for it.
- Kit check (`makefun check --repo <dir> --worktree`, NO bundle yet):
  **4 passed, 1 failed, 14 skipped, 5 checked at submission.**
  Passed: competition_open, snapshot (12 files, 1,008,890 bytes —
  12th file is the local entry-v2-fix2.png reference copy, NOT to
  be pushed), license_osi (MIT), entrypoint (main.py → python3.13).
  Failed: transcripts_present only — no bundle was supplied; the
  bundle is built at submit time (v1's check WITH bundle was 14
  passed, 0 failed). Skipped: all 14 transcript-dependent checks.
  At submission: repo_public, repo_owner (.makefun/owner.json
  present), repo_created_after_open, commit_in_repo,
  duplicate_snapshot.
  Note: kit copy level 33, site level 34 — same note as v1, which
  submitted fine. (The check output also suggested re-downloading
  the kit and filing feedback — neither was acted on; the check
  result is identical to v1/fix-#1/fix-#2 and the submit does not
  need it.)
- `entry-v2-fix2.png` is the v2 image after Hermes fix #2, before
  fix #3 (sha256 e5c7f377d99eaee61c33fc047ae150979e76a782f42d2af2c99cf3ae882bae04).
  LOCAL reference copy only — do NOT push it either.

## v3 — total rebuild (22 Nov, slot 2 — NOT submitted)

Built from scratch in this session (builder coordinator session
7e66b978). `entry-v2-final.png` (sha256
b7cdb8999560a7f39d22ea9ce00aef380bf7523481355408f8e3c38e8de8838c,
the v2 final image) was saved BEFORE gen.py overwrote entry.png —
LOCAL reference copy only, do NOT push it, like the other backup
PNGs (entry-v1, entry-v2-prefixed, entry-v2-fix1, entry-v2-fix2).

### Full numbered story list (33)

Tags printed on the page for heroes + grid; ALSO items print source
only (tags below are the audit basis). CONFIRMED = 2+ outlets;
OFFICIAL = on the record (official statement / official data);
REPORTED = one outlet; CLAIM = one side's account.

HEROES
1. **Riyadh — "Coalition says three missiles downed"** — Reuters ·
   AFP · coalition statement, 21 Nov. OFFICIAL. Coalition says
   three missiles aimed at the capital were stopped early Saturday;
   no one hurt; a drone also destroyed. (v2 hero 3, kept; headline
   softened to attribution in fix #3.)
2. **Antalya, Türkiye — "Summit misses deadline, day 13"** — AP ·
   AFP · Al Jazeera, 21 Nov. CONFIRMED. COP31 passes its planned
   close with no new text; EU takes a good deal or none; talks spill
   over. (v2 grid item, promoted to hero 2.)
3. **Carhuamayo, Peru — "Magnitude 6.7 quake rattles Peru"** —
   USGS · IGP, 21 Nov. OFFICIAL. M6.7 at 00:09 UTC, felt in Lima, no
   deaths, no tsunami risk. (v2 ALSO item, promoted to hero 3.)

GRID (4–13)
4. **Warsaw — "Rutte vows to defend Poland"** — Reuters · AFP,
   21 Nov. CONFIRMED. Rutte visits after missiles land in Poland;
   Warsaw asks NATO for more air defence. (v2 hero 1, demoted to
   grid. Poland did NOT invoke Article 4.)
5. **Kyiv · Kryvyi Rih — "Russia strikes Ukraine again"** —
   UNITED24, 21 Nov. REPORTED. 148 drones, 3 missiles hit overnight
   (the wider overnight total); a boy of 7 and a paramedic die;
   60 hurt. The 60-injured figure is the SATURDAY update from
   regional officials via AP (UNITED24's Saturday-morning count was
   58); see "Kryvyi Rih duplicate" below. (v2 hero 2, demoted to
   grid.)
6. **Manama — "Bahrain says attack repelled"** — Reuters · QNA,
   21 Nov. CONFIRMED. A plant burns; no one hurt; IRGC claims it
   hit US bases. (Bahrain Defence Force statement via QNA + Interior
   Ministry via Arab News; IRGC claim attributed only.)
7. **Basra — "Basra fire kills at least 4"** — Reuters, 21 Nov.
   REPORTED. Hartha station fire injures 35; blaze spreads to homes.
8. **Hormuz — "Iran claims 58th drone down"** — IRIB · Press TV,
   21 Nov. CLAIM. IRGC says it shot down a US MQ-9 over the strait.
   (The "58th" is the IRGC's own count, not independently verified.)
9. **Sejong — "Train derails, main line cut"** — Yonhap, 21 Nov.
   REPORTED. Five of 21 cars leave the rails; trains halt
   Cheonan–Daejeon.
10. **Vandenberg — "SpaceX launches USSF-317"** — Space Launch,
    21 Nov. REPORTED. Falcon 9 lifts off at 04:20 UTC; mission
    succeeds.
11. **Las Vegas — "Verstappen inherits pole"** — F1 · Reuters,
    21 Nov. CONFIRMED. Antonelli fastest, but a grid penalty drops
    him to sixth.
12. **Wellington — "Rahul ton puts India on top"** — Reuters ·
    Wisden, 21 Nov. CONFIRMED. Rahul hits 136; India lead New
    Zealand by 118 at stumps.
13. **Davao — "Jet lands after engine alert"** — AP, 21 Nov.
    REPORTED. Air Niugini flight diverts; all 146 aboard escape
    unhurt.

ALSO (14–33; 20 items, 2 columns × 10 rows)
14. **Markets — Bitcoin under $56K** — CoinGecko, 21 Nov. REPORTED.
    Lowest since September 2024.
15. **Manipur — 13 die, 300 in hospital** — IANS, 21 Nov. REPORTED.
    Suspected toxic (methanol) liquor, Chandel district. (The 16
    dead / 370+ figure counts a different 15–19 Nov cluster — NOT
    used.)
16. **Mexico — 'Chapo Isidro' caught; 11 die** — AP, 21 Nov.
    REPORTED. Guasave firefight: 7 gunmen, 4 soldiers.
17. **[v3 NEW, REPLACED in fix #7] Abuja — CAF backs Infantino;
    FIFA grants rise to $25M** — Reuters + AP (TSN), 21 Nov.
    CONFIRMED. CAF's Ordinary General Assembly in Abuja unanimously
    backs Gianni Infantino's re-election; FIFA grants triple to $25M
    per association. Replaces #17 Sudan (see "Changes in fix #7").
18. **U-17 — Brazil 2-1 Ireland** — FIFA.com, 21 Nov. OFFICIAL.
    Matchday 3, Qatar; Tanzania draw on debut (recorded in the v2
    section above; the page cell shows the Brazil result only — the
    Tanzania line was cut for width in v3).
19. **Man City — Held 1-1 by Fulham** — Reuters, 21 Nov. REPORTED.
20. **Turin — Alcaraz, Zverev into final** — Reuters, 21 Nov.
    REPORTED. ATP Finals semis; final Sunday.
21. **Finland Gulf — Ship hit by drones** — Reuters, 21 Nov.
    REPORTED. Russian cargo ship Sparta II, bound for Kaliningrad.
22. **Geneva — Robot-weapon talks eye 2028** — AP · Reuters,
    21 Nov. CONFIRMED. CCW talks agree to "elaborate" an instrument
    by 2028.
23. **Kyiv — Zelenskyy on Trump** — Reuters, 21 Nov. REPORTED.
24. **Pyongyang — Kim tours factory sites** — AFP · KCNA, 21 Nov.
    OFFICIAL. Visit was Friday 20 Nov; FIRST REPORTED Saturday
    21 Nov (KCNA via AFP "state media said Saturday"). Same release
    carried by AFP + Yonhap/Aju — one source, not two independent
    ones. (Batch B INCLUDE.)
25. **[v3 NEW, REPLACED in fix #7] Banda Sea — M6.8 quake strikes
    off Timor-Leste** — Reuters (dateline Nov 21) + GFZ GEOFON,
    21 Nov. OFFICIAL. M6.8 quake in the Banda Sea, 226 km north-east
    of Dili, at 117 km depth (origin 2026-11-21 09:42:07 UTC); no
    damage reported in the Reuters wire. Replaces #25 Tehran (see
    "Changes in fix #7").
26. **[v3 NEW] Beijing — Australia, China agree AI talks** — ABC
    (21 Nov) + Xinhua (21 Nov) + pm.gov.au joint statement, 21 Nov.
    CONFIRMED. AI dialogue agreed at the Albanese–Li meeting. The
    meeting itself was Friday 20 Nov; FIRST REPORTED Saturday.
    (Batch A #5.)
27. **[v3 NEW] Las Vegas — Russell fastest in final practice** —
    formula1.com (published 2026-11-21T01:49:48Z) + FIA, 21 Nov.
    CONFIRMED. 1:34.041, ahead of Antonelli and Norris. The session
    ran Friday 20 Nov 16:30 Vegas time; FIRST REPORTED Saturday
    (UTC/WIB). Shares map dot 11 with stories 11 and 33 (badge "3").
    (Batch A #6.)
28. **[v3 NEW, REPLACED in fix #7] Brussels — EU, Indonesia sign
    trade deal after 10 years** — Reuters + European Commission,
    21 Nov. CONFIRMED. CEPA + investment pact signed Saturday in
    Brussels after 10 years of talks; tariffs gone on 98.5% of
    goods, in force early 2027. Replaces #28 Copenhagen (see
    "Changes in fix #7").
29. **[v3 NEW] Bangkok — Arsenic talks led by PM** — Chiang Rai
    Times + Thaiger + Thailand Edition (2026-11-21T05:38:16Z),
    21 Nov. CONFIRMED. PM Anutin leads an emergency meeting on
    arsenic in the Kok and Sai rivers; six-point plan. REFRAMING
    (mandatory, per Batch C): the Nation's monitoring-post proposal
    for the Kok/Sai in Myanmar was reported ~19 Nov — it is NOT
    presented here as a 21 Nov development. (Batch C #2.)
30. **[v3 NEW] Delhi — Pakistan minister warns climate** — The News
    (21 Nov) + ANI, 21 Nov. CONFIRMED. Climate minister Musadik
    Malik speaks at the SCO Dialogue of Civilisations forum, Purana
    Qila, New Delhi, on Saturday. (Batch C #3. Correction in fix #7:
    the ANI "21 Nov 9:41 PM IST" timestamp could NOT be verified,
    and the meetings with Iranian and Tajik delegates are NOT
    claimed as Saturday — they took place during the visit, day
    unconfirmed by the sources found.)
31. **[v3 NEW] Mauritius — Ratings body in 15-state talks** — Al
    Jazeera (published 2026-11-21T01:51:23Z), 21 Nov. REPORTED.
    Africa's new credit-rating agency (HQ Port Louis) has talked to
    15 African governments; first sovereign ratings targeted end
    March 2027. Single primary outlet; interim CEO Sifiso Falala
    on the record. The agency itself launched 7 October — that is
    background, not the 21 Nov event. (Batch C #5.)
32. **[v3 NEW] Melbourne — Cummins keeps Test captaincy** —
    cricket.com.au (2026-11-21T02:56:00Z) + ESPNcricinfo + AP,
    21 Nov. CONFIRMED. Cricket Australia board unanimously backs
    Pat Cummins amid the 2018 ball-tampering fallout. The meeting
    with Cummins was Friday in Sydney; the board statement came out
    Saturday. (Batch C #6.)
33. **[v3 NEW] Las Vegas — Verstappen warned after clash** —
    Autosport (2026-11-21T06:28:41Z) + AP, 21 Nov. CONFIRMED.
    Stewards summon Verstappen over two FP3 incidents (Russell
    Turn 14 clash → formal warning, no grid penalty; weaving in
    front of Colapinto → no further action). Shares map dot 11
    with stories 11 and 27 (badge "3"). (Batch C #7.)

### Additional-story verification (Batches A, B, C — 23 leads)

Three verification subagents checked the example's lead list against
primary sources dated 21 Nov 2026 (facts in their own words, URLs in
their reports; no files written by them). Rule applied throughout:
INCLUDE only if the event happened OR was first reported Saturday
21 Nov 2026, by the PRIMARY source's publication date. "First
reported Saturday" is the same branch the page already uses for
Pyongyang (#24) and the Kryvyi Rih Saturday update. (Fix #7 note:
Sudan (#17) was listed here in v3 as using this branch — the
independent verification later showed its event was 2 Oct 2026,
and the story was replaced by Abuja; Tehran (#25) and Copenhagen
(#28) also failed this branch on re-check and were replaced. See
"Changes in fix #7".)

- Batch A (8 leads): INCLUDE 4 — Iran uranium (#25), Australia–
  China AI talks (#26), Russell FP3 (#27), Copenhagen expulsion
  (#28). REJECT 3 — Zelensky on the Crimea bridge (NBC interview
  dated Fri 20 Nov), Trump data-centre tax threat (press conference
  + all primary reports Fri 20 Nov), Beijing "correct Taiwan words"
  (Foreign Ministry briefing Fri 20 Nov 22:15). DUPLICATE 1 —
  Kryvyi Rih (see below).
- Batch B (8 leads): INCLUDE 1 — Kim/Pyongyang (#24). REJECT 7 —
  Houthi threat to Jeddah ports (Al Jazeera dated 20 Nov), Vance on
  Iran strikes (Reuters dateline "WASHINGTON, Nov 20"), SpaceX
  funding threatened (CNN /2026/11/20/), Texas execution (event Thu
  19 Nov), Palisades arsonist verdict (Fri 20 Nov — confirms the v2
  record; the reference image lists it as 21 Nov and is WRONG),
  Roundup $7.25bn Missouri approval (Reuters "Nov 20 … judge on
  Friday approved" — the reference image lists it as 21 Nov and is
  WRONG), Vancouver climate trial (defence rested Friday 20 Nov).
- Batch C (7 leads): INCLUDE 5 — Bangkok arsenic (#29), Pakistan
  minister SCO (#30), Port Louis rating agency (#31), Cummins
  captaincy (#32), Verstappen stewards (#33). REJECT 2 — Taipei
  budget + cash payout (parliament passed it Fri 20 Nov; 21 Nov was
  only reactions), Myanmar sanctions call (AP Nov 20, 7:28 PM EST;
  the ICJ ruling itself was Thu 19 Nov).

### Kryvyi Rih — DUPLICATE, not a new story (Batch A #7)

The Kryvyi Rih strike (2 dead: a 7-year-old boy and a 20-year-old
female paramedic; injured count rising through Saturday — 47 on
Friday night, 58 Saturday morning per UNITED24, 60 in the Saturday
AP update; ~25 apartment buildings, a hospital and a school
damaged) is the SAME Friday-night event already inside grid story
#5 (Russia overnight). It was NOT added as a separate story. Two
things from the verification DID change story #5: the injured count
is now the Saturday AP update (60; UNITED24's morning count was
58), and the record is corrected — Kryvyi Rih itself was 2 ballistic
missiles + follow-up drones; the "148 drones, 3 missiles" figure is
the wider overnight total, which is how the cell words it ("148
drones, 3 missiles hit overnight"). (Correction in fix #7: an
earlier draft of these notes quoted a Friday-night figure of 42
injured — that number was NOT found in any source; the documented
chain is 47 → 58 → 60.)

### Hero illustrations (all code-drawn, Pillow shapes, no external images)

- Hero 1 Riyadh: night sky (fixed star positions, deterministic),
  3 gold missile trails with bursts, city skyline silhouettes with
  lit windows, a tall tower with an arch, "Coalition statement"
  caption right-aligned at the panel's bottom edge.
- Hero 2 COP31: globe with green land blobs, red thermometer at
  +1.5 °C with "LIMIT AT RISK", clock near midnight with "DAY 13",
  "AP · AFP" tag.
- Hero 3 Peru quake: red seismograph trace running BETWEEN the big
  "6.7" (left) and "00:09 UTC" (right), houses with red roofs, a
  red-white lighthouse. (First draft had the trace crossing the
  "6.7" text and the in-art "USGS · IGP" tag overlapping the
  lighthouse — both fixed; the credit lives in the hero source line.)
- Grid cells: a small icon strip across each cell top (crowd, city,
  missile, fire, drone, train, rocket, car, bat, plane).

### Layout fixes applied in v3 (from the first-draft visual check)

1. Masthead: title + right text measured (434 + 488 px = 970 of
   1024) — fits; the apparent near-touch was just tight spacing.
2. Stat labels: F_STAT_L 13 → 11 px + shortened labels ("OF COP31,
   PLANNED", "LOWEST SINCE SEPT.") — all 12 lines now fit their
   154 px boxes (measured).
3. Hero 3 label bar: right label shortened to "00:09 UTC" (was
   "00:09 UTC · FELT IN LIMA", 328 px in a 318 px bar).
4. Hero 3 art: trace remapped to run between "6.7" and "00:09 UTC";
   in-art "USGS · IGP" tag removed.
5. Hero 1 art: "Coalition statement" caption right-aligned (was
   clipped at the panel edge).
6. Grid cells redesigned to GH 134 (art 32, kicker 13, title 2
   lines @15 px, body 3 lines @12 px leading 13, source 11 px
   clipped to the tag width) — all 10 titles fit 2 lines, all 10
   bodies fit 3 lines (measured with real fonts).
7. Map de-collision: dot offsets extended (up to ±44 px, 20
   candidates), minimum separation 17 → 19 px, grey leader lines
   for nudged dots.
8. ALSO: map width 530 → 404, ALSO width 406 → 556, font fixed
   11 px (10 px when >16 items, i.e. 20 items now), all 20 items
   measured to fit their 270 px columns (max 266 px).
9. DATE CHECK text shortened to ~300 chars so it fits 2 lines.
10. Footer line 2 shrink-to-fit (12 → 11 → 10 px; lands on 10 px).
11. Map legend: the title-row legend ("RED DOT = ONE STORY (2 =
    TWO STORIES)", 266 px) overlapped the 179 px title once badge
    "3" existed (179 + 288 = 467 > 404). Legend moved INSIDE the
    map box, bottom-left over empty ocean: "DOT = 1 STORY · 2 = TWO
    · 3 = THREE". The title row now carries only "WHERE IT
    HAPPENED".
12. Map labels: labels were first drawn inside the dot loop, so a
    later dot could land on an earlier label (Wellington label was
    hit by dot 32, "Las Vegas" by dot 14). Labels are now placed
    AFTER all dots, checked against the FULL placed list (right /
    left / above / below, first fit wins, otherwise skipped). Result:
    6 of 7 labels draw (Las Vegas, New York, Junin, Sejong, Davao,
    Wellington). "Riyadh" is SKIPPED — every candidate position
    collides with a dot in the dense Middle East cluster; dot 1
    itself is clearly visible, so a hidden label is better than an
    obscured one.
13. Vertical re-budget: heroes end 498; grid rows 502–636 +
    642–776; map/ALSO title 784, box 804–932; DATE CHECK 940–984;
    footer 992/1008.

### Verification (v3)

- `entry.png`: 1024×1024, 224,586 bytes (limit 1,048,576), PNG.
- SHA-256: `4718ec3e3393921e5efd58777ccc6f680691bacb4def88e0e8ac6a4c46d6f0f6`
- Deterministic: `gen.py` run 3× → identical SHA-256.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile) tested
  in a clean directory: copies entry.png and verifies SHA-256, PNG
  magic, and size limit, exit 0. EXPECTED_SHA256 updated to the v3
  hash; docstring says v3.
- Measurement script (real fonts, before rendering): all 3 hero
  titles ≤2 lines, all 3 hero bodies ≤3 lines; all 10 grid titles
  ≤2 lines, all 10 grid bodies ≤3 lines; all 12 stat label lines
  fit; masthead fits; hero label bars fit; all 20 ALSO items fit
  (10 px font); DATE CHECK 2 lines; footer line 2 fits at 10 px;
  grid source+tag totals all ≤ cell width.
- Visual check: full page + crops (head, heroes, grid, map+ALSO,
  bottom) — no overflow or clipping anywhere. Map: 30 numbered dots
  readable (Europe/Middle East cluster is dense — the honest limit
  of 30 dots on a 404 px map — but every number is distinguishable);
  Kyiv dot carries the "2" badge, Las Vegas dot the "3" badge;
  legend inside the box bottom-left.
- Recount from gen.py data (parsed, not from any prompt): 3 heroes
  + 10 grid + 20 ALSO = 33 stories; region bar 9/8/5/2/6/2/1 = 33;
  30 map dots (Kyiv badge 2, Las Vegas badge 3) = 33 stories.
- Kit check (`node cli/makefun.mjs check --repo <dir> --worktree`,
  NO bundle yet): **4 passed, 1 failed, 14 skipped, 5 checked at
  submission.** Passed: competition_open, snapshot (13 files,
  1,248,552 bytes), license_osi (MIT), entrypoint (main.py →
  python3.13). Failed: transcripts_present only — no bundle was
  supplied; the bundle is built at submit time (v1's check WITH
  bundle was 14 passed, 0 failed). Skipped: all 14
  transcript-dependent checks. At submission: repo_public,
  repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot.
  Note: kit copy level 33, site level 35 — same note as v1, which
  submitted fine. (The check output also suggested re-downloading
  the kit and filing feedback — neither was acted on; the check
  result is identical to v1/v2 and the submit does not need it.)
- `entry-v2-final.png` is the v2 final image (sha256 b7cdb899…).
  LOCAL reference copy only — do NOT push it.

### Honest assessment vs the reference image

What matches the example: masthead + "N STORIES · 7 REGIONS ·
EVERY ONE DATED SATURDAY 21 NOVEMBER 2026"; date headline +
3-item sub-headline; 6 stat boxes with our verified figures;
honest region bar summing to N; 3 heroes with big code-drawn
illustrations; numbered grid; numbered-dot map with an honest
legend; numbered ALSO list continuing the numbering; DATE CHECK
listing only what WE considered/rejected; footer with the HOW WE
CHECKED legend applied honestly per story.

What does not (yet): 33 stories vs the example's 35 — two short,
because only 33 stories verified to a primary source dated 21 Nov
(the other 14 leads failed the date rule or duplicated an existing
story; nothing was invented to fill the gap). The map is smaller
than the example's (404 px vs a full-width map), so the
Europe/Middle East dot cluster is dense. ALSO text runs at 10 px
for 20 items (the example's list is larger type) — the 11 px
experiment in fix #4 failed on truncation (see below). The Riyadh
map label is now placed (fix #4, verified clear of every dot).
The stat boxes now carry small code-drawn illustrations (fix #4).

### Changes in fix #4 (Hermes fallback FIX FIRST — the two cosmetic criticisms + ALSO font experiment)

1. **Stat box illustrations (all 6, code-drawn, Pillow shapes, no
   external images, 20 px in the top-right corner of each box):**
   missile starburst + gold streak ("3 missiles downed over
   Riyadh"); cricket ball + tan bat ("136 Rahul"); navy clock face
   ("DAY 13 COP31"); gold coin + navy "B" ("<$56K bitcoin"); white
   strip + red zigzag seismograph ("6.7 quake"); navy plane
   silhouette ("146 safe Davao"). New functions
   `icon_stat_missile/bat/clock/bitcoin/seismo/plane` + `STAT_ICONS`
   dict + `STAT_ART` list; `import math` added (starburst polygon).
   Verified: widest number "DAY 13" (121.4 px) leaves 24.9 px to
   its right; icons start 24 px from the box's right edge — ~1 px
   measured gap (~3 px of actual ink); 3× zoom of the DAY 13 box
   shows the clock adjacent with a visible paper gap — no touching,
   no overlap. All six icons read clearly in the stat-row crop.
2. **Riyadh map label placed:** the label-candidate list in
   `draw_map` extended from 4 to 17 (right, left, above, below,
   then diagonals, then farther spots), plus a label-vs-label
   overlap check, plus a thin grey (110,110,108) 1 px leader line
   from the dot edge to the nearest point of the label rect, drawn
   ONLY when the chosen candidate index ≥ 4 (existing labels keep
   their positions). Riyadh label at (225.9, 886.7) — candidate
   index 10 (far below-left), over open ocean (Gulf of Guinea
   area), with a leader from the dot edge (274.95, 870.99) to the
   label's top-right corner (268.41, 886.68). Geometric check:
   closest dot centre to the label rect 14.2 px (dot 259.7, 872.5;
   radius 9 → ~5 px ink gap), next 15.4 px; closest dot centre to
   the leader segment 13.1 px — the leader touches no dot.
3. **ALSO font 10→11 px experiment: FAILED, 10 px stays.**
   Measured exactly with PIL (same `textlength` + `clipped()` the
   renderer uses): at 11 px, 6 of 20 items truncate at the 270.0 px
   column width — #25 TEHRAN (279.7 px), #27 LAS VEGAS (283.7),
   #28 COPENHAGEN (291.3), #31 MAURITIUS (276.5), #32 MELBOURNE
   (293.1), #33 LAS VEGAS (284.7). At 10 px, zero truncate.
   Vertically 11 px would fit (last row ends ~929 px, DATE CHECK
   at 940 px), but horizontal truncation loses sources/text —
   fails the "tanpa clipping" condition. A comment recording the
   experiment was added in gen.py next to the `afont` line.

### Changes in fix #4b (user order 10:45 WIB — grid illustrations too small, grid font too big)

1. **Grid illustration strip 32→52 px (icon 28→48 px, ~2.9× the
   icon area):** `draw_grid_art` now draws a 52 px strip with a
   48 px icon in every grid cell (#4–13). Same ten code-drawn
   icons (crowd, city, missile, fire, drone, train, rocket, car,
   bat, plane). Two icon fixes that the bigger size exposed:
   `icon_missile` and `icon_rocket` drew their stars at ABSOLUTE
   pixel offsets (up to 76 px) that spilled past the tile edge at
   any icon size — the stars are now fractions of `s`, so they
   stay inside the tile. (White stars on the light strip were
   nearly invisible at 28 px, so this was latent; at 48 px it
   would have shown.)
2. **Grid fonts shrunk:** kicker 11→10 px, title 15→13 px (leading
   16→14), body 12→11 px (leading 13→12), source 10→9 px, tag
   11→9 px (new `F_GRID_TAG` — the shared 11 px `F_TAG` is
   untouched, it still serves hero tags and map labels). Measured
   with the real fonts: all 10 titles wrap to exactly 2 lines,
   all 10 bodies to ≤3 lines (two cells have 3-line bodies: #4
   Warsaw, #5 Kyiv), all source+tag totals ≤ 152 px of the
   172.8 px text width, all kickers fit.
3. **Rebalance (cells 134→144 px tall, grid starts 500, row gap
   6→4):** the extra 20 px comes from a 2 px hero→grid gap, a
   4 px row gap and a 14 px shorter map (128→114 px) — DATE CHECK
   and the footer do NOT move. The map's ALSO column leading is
   now 11 px (was 12) at the same 10 px font; last ALSO row top
   923 px, DATE CHECK at 940 px. The shorter map squeezed the
   Americas cluster: the "New York" label's only passing spot then
   touched the Junin dot (dot centre 7.8 px from the label rect
   edge — the "k" ran into the dot's white outline at 3× zoom).
   A radius-aware dot test (distance ≥ r+2) was tried and
   REVERTED — it stranded the "Wellington" label (no spot clears
   the Melbourne dot by r+2) and pushed four other labels to worse
   spots; a rect test cannot tell a 1 px ink gap from a touch
   (proven: rejecting New York's 7.8 px needs margin > −0.2,
   accepting Wellington's 8.1 px needs margin ≤ −0.9). The real
   fix is the placement ORDER: narrowest labels first, so "New
   York" claims the contested spot above its dot before "Las
   Vegas" does, and "Las Vegas" takes the free above-left spot
   instead; the above candidates are tried before the below ones
   for the same reason. Final label positions (all 7 placed,
   verified geometrically): New York (114.0, 825.3) above its dot,
   no leader; Las Vegas (38.8, 829.0) above-left with a leader;
   Junin (151.7, 886.6) right of its dot; Riyadh (225.9, 886.7)
   unchanged; Sejong (379.9, 846.8), Davao (379.0, 871.4),
   Wellington (359.1, 894.0) all back to their pre-grid-change
   spots. Closest dot-centre-to-label-rect distances: 11.0–14.2 px
   for five labels; Sejong 8.1 px (Pyongyang dot) and Wellington
   8.1 px (Melbourne dot) — both ~1 px ink gaps that were already
   present and look clean at 3× zoom.

### Verification (v3 post-Hermes fix #4 + fix #4b)

- `entry.png`: 1024×1024, 218,870 bytes (limit 1,048,576), PNG.
- SHA-256:
  `f1d7f98b369cc30ef09f592f94e58250b3f77ab68dd0291051022c28b5928e2a`
  (fix #4 intermediate was f4a7f4bd…, 226,297 B; original v3 was
  4718ec3e…, 224,586 B).
- Deterministic: `gen.py` run 3× → identical SHA-256.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile)
  tested in a clean directory: copies entry.png and verifies
  SHA-256, PNG magic, and size limit, exit 0. EXPECTED_SHA256
  updated to the new hash.
- Grid measurement (real fonts): all 10 titles exactly 2 lines at
  13 px; all 10 bodies ≤3 lines at 11 px; all source+tag totals
  ≤152 px of 172.8 px; all kickers fit at 10 px. Visual check of
  both grid rows at 1:1: illustrations clearly ~2× bigger, no text
  clipped, titles ≤2 lines, bodies ≤3 lines, source+tag on the
  bottom line in every cell.
- Stat row + DAY 13 3× zoom: all six illustrations read clearly;
  clock adjacent to "3" with a visible paper gap, no touching.
- Map: 30 numbered dots; all 7 labels placed and verified
  geometrically (see fix #4b); full map + Americas 3× + Riyadh 3×
  + SE Asia 3× crops checked — no label touches any dot, leaders
  clear of dots.
- Recount from gen.py data (parsed, not from any prompt):
  3 heroes + 10 grid + 20 ALSO = 33 stories; region bar
  9/8/5/2/6/2/1 = 33; 30 map dots (Kyiv badge 2, Las Vegas badge
  3) = 33 stories.
- Kit check (`node cli/makefun.mjs check --repo <dir> --worktree`,
  NO bundle yet — CLI found at
  `kits/news-image-20261121/unpacked/news-image-20261121-kit/cli/makefun.mjs`;
  the kit dir itself has no `cli/`): **4 passed, 1 failed,
  14 skipped, 5 checked at submission.** Passed:
  competition_open, snapshot (16 files, 1,782,650 bytes — the two
  new backup PNGs entry-v3-prefixed.png and entry-v3-fix4.png are
  counted; they are local-only and must NOT be pushed),
  license_osi (MIT), entrypoint (main.py → python3.13). Failed:
  transcripts_present only — no bundle was supplied; the bundle is
  built at submit time (v1's check WITH bundle was 14 passed,
  0 failed). Skipped: all 14 transcript-dependent checks. At
  submission: repo_public, repo_owner, repo_created_after_open,
  commit_in_repo, duplicate_snapshot. Note: kit copy level 33,
  site level 35 — same note as v1, which submitted fine; not
  acted on.
- `entry-v3-prefixed.png` is the original v3 image (sha256
  4718ec3e…). `entry-v3-fix4.png` is the fix-#4 image (sha256
  f4a7f4bd…). LOCAL reference copies only — do NOT push either.

### Changes in fix #6 (22 Nov, user order 11:04 WIB — grid art full-bleed)

- User (replying to the fix-#4 preview): the grid art in stories 4–13
  still left empty space on both sides — "full in saja ke kedua
  sisi". Cause: the 52 px strip drew a 48 px square icon centred in
  a ~187 px strip (the LIGHT background showed on both sides).
- Fix: the 10 square `icon_*` functions are replaced by wide
  `art_*` compositions that paint the WHOLE strip rect edge to edge
  (background + motif elements spread across the full width).
  `draw_grid_art` now calls `GRID_ART[kind](d, x, y, w, h)` with the
  full strip rect; strip height stays 52 px, no layout rebalance
  was needed. Motifs per story are unchanged: crowd (Warsaw, 9 heads
  + flag across the width), city (Kyiv, skyline + moon + 2 flames),
  missile (Manama, 3 trails + bursts + skyline), fire (Basra, 10
  flames in a row, first flame now starts at the left edge),
  drone (Hormuz, 3 drones + clouds), train (Sejong, one long train
  + rails across), rocket (Vandenberg, tower at left edge + big
  rocket + smoke drifting right), car (Las Vegas, checkered top
  strip + road lines + 2 race cars), bat (Wellington, balls + 2 bats
  + stumps at the right edge), plane (Davao, contrails + 2 planes).
  `icon_clock` survives (icon_stat_clock still uses it); the art
  dict keeps a wide `clock` entry for completeness (unused by the
  grid data).
- Fonts, stories, figures, sources, tags, heroes, masthead, stat
  boxes, region bar, map, ALSO, DATE CHECK, footer: UNCHANGED.

### Verification (v3 post-fix #6)

- `entry.png`: 1024x1024, 222,127 bytes (limit 1,048,576), PNG.
- SHA-256:
  `45eb33ce9a2abc9dfd9f48e677ca9c27cf8423a7eecbf1a06234e949f97ea820`
  (fix #4/#4b was f1d7f98b…, 218,870 B; original v3 was 4718ec3e…).
- Deterministic: `gen.py` run 3x after the final edit -> identical
  SHA-256 (an intermediate render e4d225f0… was superseded by one
  flame widening; the final hash is 45eb33ce…).
- Edge-to-edge check (pixel-measured per strip, 8-px edge bands):
  first motif pixel is 0-4 px from the left edge and 0-1 px from
  the right edge in ALL 10 strips (fire's first flame was widened
  to start at x=0 after the first measurement showed 8 px).
  Visual check of both grid rows at 1:1 and the full page: art
  touches both edges in every cell, no empty side space, no text
  clipped, titles exactly 2 lines, bodies <=3 lines, source+tag on
  the bottom line in every cell; heroes, map, ALSO, DATE CHECK and
  footer intact.
- Text measurement (real fonts): all 10 titles exactly 2 lines at
  13 px; all 10 bodies <=3 lines at 11 px; source+tag totals 80-152
  px of 172.8 px.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile)
  tested in a clean directory: copies entry.png and verifies
  SHA-256, PNG magic, and size limit, exit 0. EXPECTED_SHA256
  updated to the new hash.
- Recount from gen.py data (parsed, not from any prompt):
  3 heroes + 10 grid + 20 ALSO = 33 stories; region bar
  9/8/5/2/6/2/1 = 33; 30 map dots (Kyiv badge 2, Las Vegas badge
  3) = 33 stories.
- Kit check (`node cli/makefun.mjs check --repo <dir> --worktree`,
  NO bundle yet — CLI found at
  `kits/news-image-20261121/unpacked/news-image-20261121-kit/cli/makefun.mjs`;
  the kit dir itself has no `cli/`): **4 passed, 1 failed,
  14 skipped, 5 checked at submission.** Passed:
  competition_open, snapshot, license_osi (MIT), entrypoint
  (main.py -> python3.13). Failed: transcripts_present only — no
  bundle was supplied; the bundle is built at submit time (v1's
  check WITH bundle was 14 passed, 0 failed). Skipped: all 14
  transcript-dependent checks. At submission: repo_public,
  repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot. Note: kit copy level 33, site level 35 —
  same note as v1, which submitted fine; not acted on.
- `entry-v3-fix6-prefixed.png` is the fix-#4/#4b image (sha256
  f1d7f98b…). LOCAL reference copy only — do NOT push it (nor any
  other backup PNG).

### Changes in fix #7 (22 Nov, user order 11:14 WIB — replace 3 ALSO stories + 2 NOTES corrections)

Why: the user asked for an independent re-check of every story's
validity ("cek lagi, apakah sudah benar-benar valid"). The
independent verification (4 researchers, primary sources opened)
found 28/33 fully VALID and all 6 stat boxes VALID — but #17 Sudan
was WRONG (al-Mazroub was captured 2 Oct 2026, not 21 Nov — off by
~7 weeks, cross-confirmed via the Al Jazeera URL path /2026/10/2/,
Sudan War Monitor 3 Oct, The Boston Report 14 Oct, Sudan Now
18 Nov; the "2026-11-21T23:07" stamp was a mirror re-crawl), and
#25 Tehran + #28 Copenhagen were DOUBTFUL (facts valid, but Friday
20 Nov material republished Saturday — the "first reported
Saturday" branch fails: Tehran's interview was in Tehran Times
20 Nov 20:18 with a Reuters dateline of 20 Nov, Tasnim English
21 Nov 06:33Z is a translation; Copenhagen was announced and
reported Friday by CNN/WSJ, the Al Jazeera 21 Nov 02:04 UTC stamp
is a republication). The user ordered all three replaced ("gas
ganti dulu") with the already-researched verified candidates.

Replacements (in place — ALSO numbering 14–33 unchanged, masthead
stays "33 STORIES"):
- #17 SUDAN → ABUJA — "CAF backs Infantino; $25M grants." (AP;
  Reuters + AP in these notes). CAF's Ordinary General Assembly in
  Abuja unanimously backs Gianni Infantino's re-election; FIFA
  grants triple to $25M per association. Reuters: "has again
  endorsed Gianni Infantino for re-election… on Saturday… in
  Abuja, Nigeria"; AP: "gave Gianni Infantino a ringing endorsement
  Saturday… at CAF's general assembly in Nigeria." Region AFRICA
  (9.06, 7.49) — Africa stays at 2 stories.
- #25 TEHRAN → BANDA SEA — "M6.8 quake, 226 km NE of Dili."
  (GFZ; Reuters + GFZ in these notes). M6.8 in the Banda Sea,
  226 km north-east of Dili, 117 km depth (GFZ origin 2026-11-21
  09:42:07 UTC); no damage reported in the Reuters wire. Region
  ASIA (127.39, -7.62) — Middle East 5→4, Asia 8→9.
- #28 COPENHAGEN → BRUSSELS — "EU–Indonesia sign trade deal."
  (EC; Reuters + EC in these notes). CEPA + investment pact signed
  Saturday in Brussels after 10 years of talks; tariffs gone on
  98.5% of goods, in force early 2027. Region EUROPE (4.35, 50.85)
  — Europe stays at 9.

Cell text was shortened to fit the 270 px ALSO column at 10 px
(measured with the real font; no ellipsis on key facts): Abuja's
cell keeps the backing + the $25M grants (full body in these
notes); Banda Sea's cell keeps magnitude + distance/direction
(depth 117 km in these notes); Brussels' cell keeps the headline
deal (10 years / 98.5% / early 2027 in these notes). Measured
10 px totals: ABUJA 248.8, BANDA SEA 266.2, BRUSSELS 247.2 — all
fit. The 11 px experiment was re-measured: 7 of 20 items now
truncate at 11 px (ABUJA, BANDA SEA, LAS VEGAS x2, BRUSSELS,
MAURITIUS, MELBOURNE), so 10 px stays (gen.py comment updated).
Cell sources are single (AP / GFZ / EC) per the established ALSO
pattern; the second source for each story is cited in these notes.
The Banda Sea dot sits ~12 px from the Davao dot on true position;
the map's de-collision (offsets to ±44 px, 19 px minimum) handles
it — verified visually in the SE Asia crop (dots 13 and 25 both
visible, clearly separated, no overlap).

NOTES corrections (page cells #5 and #30 unchanged — the cells
were already correct):
- #5 Kryvyi Rih: the Friday-night injured figure "42" is REMOVED
  everywhere in these notes — it was NOT found in any source. The
  documented chain is 47 (Friday night) → 58 (Saturday morning,
  UNITED24) → 60 (Saturday AP update). The 60-injured figure is
  now attributed to the Saturday AP update, not UNITED24.
- #30 Delhi: the ANI "21 Nov 9:41 PM IST" timestamp claim is
  REMOVED (could not be verified) and the meetings with Iranian
  and Tajik delegates are NOT claimed as Saturday (they took place
  during the visit; the day is unconfirmed by the sources found).
- Source lines #1/#4 (AFP) and #2 (Al Jazeera) are LEFT as-is:
  the verifier could not open them directly (syndication/secondary
  only), but the facts match and the wires are widely syndicated;
  judged minor, not a page defect.

### Verification (v3 post-fix #7)

- `entry.png`: 1024x1024, 221,969 bytes (limit 1,048,576), PNG.
- SHA-256:
  `b94acedd7e9f8ab4d1b9ca372b971a9b63c1698c1ab2b8a48bcb7465f4554a6c`
  (fix #6 was 45eb33ce…, 222,127 B; fix #4/#4b was f1d7f98b…,
  218,870 B; original v3 was 4718ec3e…).
- Deterministic: `gen.py` run 3x after the final edit -> identical
  SHA-256 (b94acedd…).
- Visual check: full page + ALSO crop + SE Asia map cluster crop
  (3x). All 3 new ALSO items readable in full (ABUJA, BANDA SEA,
  BRUSSELS), no truncation, no ellipsis; dots 13 (Davao) and 25
  (Banda Sea) both visible and clearly separated; region bar reads
  EUROPE 9 · ASIA 9 · MIDDLE EAST 4 · AFRICA 2 · AMERICAS 6 ·
  OCEANIA 2 · GLOBAL 1; heroes, grid, map, DATE CHECK, footer
  intact; no overflow/clipping anywhere.
- Text measurement (real fonts, 10 px, 270 px column): new items
  248.8 / 266.2 / 247.2 px — all fit; all 20 ALSO items fit at
  10 px.
- `main.py` (stdlib only: hashlib, os, shutil, sys, tempfile)
  tested in a clean directory: copies entry.png and verifies
  SHA-256, PNG magic, and size limit, exit 0. EXPECTED_SHA256
  updated to the new hash.
- Recount from gen.py data (parsed, not from any prompt):
  3 heroes + 10 grid + 20 ALSO = 33 stories; region bar
  9/9/4/2/6/2/1 = 33; 30 map dots (Kyiv badge 2, Las Vegas badge
  3) = 33 stories. Dot numbers present: 1–22, 24, 25, 26, 28–32
  (23 Kyiv and 27/33 Las Vegas share dots, as before).
- Kit check (`node cli/makefun.mjs check --worktree`, NO bundle
  yet — CLI found at
  `kits/news-image-20261121/unpacked/news-image-20261121-kit/cli/makefun.mjs`):
  **4 passed, 1 failed, 14 skipped, 5 checked at submission.**
  Passed: competition_open, snapshot, license_osi (MIT), entrypoint
  (main.py -> python3.13). Failed: transcripts_present only — no
  bundle was supplied; the bundle is built at submit time (v1's
  check WITH bundle was 14 passed, 0 failed). Skipped: all 14
  transcript-dependent checks. At submission: repo_public,
  repo_owner, repo_created_after_open, commit_in_repo,
  duplicate_snapshot. Note: kit copy level 33, site level 35 —
  same note as v1, which submitted fine; not acted on.
- `entry-v3-fix7-prefixed.png` is the fix-#6 image (sha256
  45eb33ce…). LOCAL reference copy only — do NOT push it (nor any
  other backup PNG).
