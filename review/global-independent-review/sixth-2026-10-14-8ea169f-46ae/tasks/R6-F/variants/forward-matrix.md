# Forward matrix — source unit → fact → consumer → specification

All ranges are inclusive. `path-map.json` supplies exact source/formal paths for each short name. A traced row is a fresh semantic observation, not an acceptance verdict. Focal comments, headers, whitespace and class/module terminators are included within the contiguous ranges below; they add no independent behavioral clause.

| Unit | Focal source | Independent behavior/fact | Necessary consumer / gate | Formal destination and review note |
| --- | --- | --- | --- | --- |
| P01 | palace1–59 | 25 normal/pinch nature triples; effective gates differ from raw triples | palace105–125; ai utilities5 | WP56 27–55,65–66; all50 triples compared |
| P02 | palace60–66 | Palace-mode AI flag; initialization | ai48–68; palace184–185 | WP56 63,74,117 |
| P03 | palace67–77 | Self/Bide defense precedes status/counter support; rest attack | palace127–130 | WP56 19–23; P04/P05 |
| P04 | palace78–96 | Partial move existence, PP>0, active ChoiceBand lock and Torment-last-move checks | command42–64, checks10–99 | WP56 67,70,118–119; standard player gate distinct |
| P05 | palace97–104 | Move or -2 registered with unresolved target; no legality recheck | record80–91; checks183–205 | WP56 68–69; WP58 75,128–130; RC-W07 |
| P06 | palace105–141 | Global AI random category, uniform eligible slot or -2 | command60–86; ai48–68 | WP56 63–70; WP58103/129; V003 ordinary Mega route bypass |
| P07 | palace142–159 | Living/non-sleeping half-HP pinch latch and four message groups | eor597–781; Initialize93–260 | WP56 59,122; P08/P23 |
| P08 | palace160–169 | Pinch after ordinary round end only if undecided | eor597–781 | WP5659/122 |
| P09 | palace170–183 | AI marker initialized per battler; ordinary switching delegated outside Palace | ai48–68 | WP5674,79–81 |
| P10 | palace184–194 | Song1 or no ordinary move after5 rounds skips probability | battle attacks20–31; switch77–105 | WP5676–77,80–81; P09/P12 |
| P11 | palace195–210 | Legal reserves, integer HP percentage, first strict maximum above0 | switch9–33,77–105 | WP5678–80; V005 zero-percent live reserve |
| P12 | palace211–228 | <50 base then <25 overwrite; status bonuses; marker penalty/clamp | palace229–243 | WP5678; P10/P11 |
| P13 | palace229–245 | Best-index hit early returns; later branch writes marker, first legal reserve or false | record105–110; switch99–105 | WP5679–81; P12/P24/P25; V005 qualification |
| A01 | arena1–36 | Full/partial clear; state1 protected preservation; state2 effectiveness assignment | use238–248,369–438,501–516; attack176–182 | WP5687–95,123; V001 actual producer and survivor preconditions |
| A02 | arena37–51 | Intro flag, zero score/baseline/count/party positions, Arena AI flag | StartAndEnd109–118,279–314 | WP5699,117 |
| A03 | arena52–57 | All ordinary candidate-entry requests false; UI-context message | switch77–105,113–135; switching moves24–245 | WP56109/120–121; WP58118; P21/RC-W25 |
| A04 | arena58–73 | Judge before sequential fainted replacement; stop on decision/party end | switch248–307,316–374; StartAndEnd557–566 | WP56108–110; WP58130; P20/P28 |
| A05 | arena74–84 | Opening all-entry initializes both score totals/baselines/count | StartAndEnd314; ordinary switch303–311 | WP5699; P28 |
| A06 | arena85–95 | Additional reset operation exists but has no script caller | arena_reset_callers.txt; switch334/376–383 uses participation instead | WP56110; no actual replacement-reset inference |
| A07 | arena96–110 | Mind -1 three named functions,0 three counter/Bide and statuses,+1 rest | arena111–125; actual recorded command choices | WP5687; P13 |
| A08 | arena111–126 | Intro consumed once; normal commands; mind only while undecided and UseMove object exists | command174–265; record121–125 | WP5699; WP58130 |
| A09 | arena127–140 | Normal EOR then current skill accumulation/count; ≥3 judgment; cancellation | eor597–781; use75–95 | WP56100,122; V004 recharge retained |
| A10 | arena141–170 | Per-axis2/0 or1/1; HP/max(initialHP,1) with no upper clamp | arena171–200 | WP5687/101; P17–P19 |
| A11 | arena171–201 | Judgment presentation; tie/loser HP0, faint, growth, replacement | Battler107–112; ChangeSelf64–99; StartAndEnd557–566 | WP56102/106–108/124; P17/P18/P28 |
| A12 | arena202–217 | AI never chooses ordinary switching in Arena | ai48–68 | WP56109/117/120 |
| A13 | arena218–258 | Running totals, names/VS, axes and result icons | arena265–349 | WP56102; graphics resources/runtime unverified |
| A14 | arena259–264 | First command introduction with battler names | arena111–116 | WP5699 |
| A15 | arena265–366 | Dimming, axis order, total/winner/draw messages; resource disposal | Scene85–109; ordinary messaging | WP56102/136; no broad runtime recovery promise |
| R01 | record1–27 | Four command tags, fresh arrays/indices/properties, default mode0 | wrapper13–35; record70–72/121–125 | WP5811/39/61/69/172 |
| R02 | record28–46 | Nil/array trainer snapshots; player4/NPC5; strings/badges cloned | battle119–122 normalization; record147–161/270–286 | WP5841/46–47/144; scalar branch outside ordinary construction |
| R03 | record47–69 |18 initial keys before normal start; snapshots and direct assignments vary | wrapper59–66; prepare209–304 | WP5839–65/144; V002 prepared-value qualification |
| R04 | record70–73 | Opaque serialization of five semantic fields | wrapper84–88/102–127 | WP5811/21–35/39 |
| R05 | record74–79 | Every completed owner inquiry appends its return, including negative | switch132–215; switching-move37–143; items/abilities | WP58107–122; RC-W16/W24–W26 |
| R06 | record80–87 | Successful normal registration overwrites move seat | ordinary attacks70–78; palace97–103 | WP5873/75/81–83; RC-W05/W07 |
| R07 | record88–92 | Target write extends current seat | command92–97; attacks97–99 | WP5879; RC-W08/W09 |
| R08 | record93–98 | Run records post-attempt decision, regardless success | command238–246; ordinary run consumer | WP5878; RC-W10 |
| R09 | record99–104 | Automatic selector writes whole -1 seat after return | attacks36–67, including target cancellation | WP5874/81; RC-W06 |
| R10 | record105–112 | Successful voluntary switch writes reserve index | switch77–105; palace229–243 | WP5877; Arena candidate rejection |
| R11 | record113–120 | Successful item registration writes full item seat | item34–74; playback214–215 | WP5876/147/154; RC-W23 |
| R12 | record121–126 | Every command phase starts next four empty seats | command174–265; arena111–125 | WP5861/69; RC-W01/W02 |
| R13 | record127–128 | Capture storage override does nothing | facility trainer battle; normal capture outside scope | WP5865; WP38/WP62 dependency |
| R14 | record129–138 | Battle random result append and return | battle93; execution/priority/target mechanisms; ai utilities5 separate | WP5889–103/134; RC-W11/W12 |
| R15 | record139–162 | Playback indices reset; party/trainer copies reconstructed | helper270–286; battle98–174 | WP58144–148; defaults/layout limitations |
| R16 | record163–181 | Initial fields restored before ordinary start; no layout factory or terrain restore | StartAndEnd247–314; layouts rule17–25 | WP5859/144; RC-W20 |
| R17 | record182–187 | Stored queried-switch result returned in sequence, no validation | ordinary replacement consumers listed in R05 | WP58107–122/134; negative/insufficient entries |
| R18 | record188–193 | Stored random result returned in sequence, requested bound ignored | recorded battle random callers | WP5889/134; RC-W12 |
| R19 | record194–197 | Pause-style battle display becomes ordinary display | Scene184–265 | WP58158 |
| R20 | record198–224 | Player loop only; fixed4 seats; normal/-1/-2 targets/items/switch/run | command174–196; ordinary registration consumers | WP58154/158; RC-W07/W20/W21/W23 |
| R21 | record225–257 | Recording/playback preserve three variants with type0/1/2 | wrapper13–35/111–128 | WP5613/125; WP5811/128–130; P22 |
| R22 | record258–287 | Opponent/music helper; trainer reconstruction by4-vs5 fields | wrapper124–127; ordinary trainer BGM | WP58140/144; future file producer uncertainty retained |

Supplementary facts required by formal clauses outside the focal units: facility temporary clearing/export decisions at wrapper40–97; promotion and dispatch at wrapper102–144; saved global metadata at SaveValues76–81 and Metadata34/89; normal-vs-abort paths at StartAndEnd247–343/405–511; live bag effects at item34–74; BURMY gate at FormHandlers189–199, Peers53–58 and Pokémon159–165; send-out participation at switch289–296 versus terminal read StartAndEnd506–509. Their selected line ranges were freshly read and recorded in the ledger. They do not certify entire neighboring modules.
