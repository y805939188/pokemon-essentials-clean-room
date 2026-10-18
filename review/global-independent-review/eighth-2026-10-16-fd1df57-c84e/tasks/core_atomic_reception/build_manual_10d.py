import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10c.json').read_text());d=base['source_dictionary'];rows=[]
def partial(k,path,ranges):d[k]={'path':path,'complete_units':ranges,'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete specified classes including closing ends actually read; not whole file or inherited family approval'}
partial('screens_lucky_producers','Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[654,669],[751,767],[772,788],[794,815],[821,847]])
partial('mist_tailwind_producers','Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb',[[1826,1841],[1921,1936]])
partial('safeguard_producer','Data/Scripts/011_Battle/003_Move/007_MoveEffects_BattlerOther.rb',[[512,527]])
partial('pledge_parent_complete','Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb',[[530,626]])
partial('pledge_constructor_trio','Data/Scripts/011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb',[[654,661],[668,675],[682,689]])
partial('protect_parent_complete','Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb',[[436,491]])
partial('side_protect_producers','Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[909,925],[930,944],[950,958],[964,972]])
partial('echo_retaliate_producers','Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[349,362],[564,570]])
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
rows.append(dict(number=723,layout_reason='Side-effect table heading only; each of the 22 payload records is decomposed in C724–733. A directory entry is not approval of every external callback.'))
row(724,[
 'Reflect starts at 0. Its Move rejects an existing positive own-side Reflect; success writes 5.',
 'Reflect becomes 8 only if the user has active LIGHTCLAY at the effect write point.',
 'LightScreen starts at 0; its own positive duplicate rejects; success writes 5 or active-LIGHTCLAY 8.',
 'AuroraVeil starts at 0. Its Move first requires user.effectiveWeather Hail, then rejects a positive duplicate.',
 'AuroraVeil success writes 5 or active-LIGHTCLAY 8 on the user side.',
 'The established AuroraVeil damage query does not require Hail to remain; the weather gate belongs to establishment.',
 'Each screen has its own positive side countdown and ending message at 0; member replacement alone does not clear it.',
 'Damage queries skip these screens for ignoresReflect, a critical hit, or active user INFILTRATOR.',
 'When applicable, AuroraVeil has first priority, otherwise Reflect for physical, otherwise LightScreen for special; these branches do not multiply all three reductions.',
 'Damage reduction is 2/3 when target side currently has more than one nonfainted battler, otherwise 1/2; declared side size is not this count.',
 'All writes precede the establishing messages; a later message failure can leave the screen and its assigned duration.'
],['activefield_full','screens_lucky_producers','battlerfull','calculations','battlefull','eor_all'],'own-side duplicate/weather gates -> screen 5/active item 8 -> actual damage branch/count -> local side countdown; no permanent Defense rewrite.')
row(725,[
 'Mist starts at 0; positive duplicate rejects, successful own-side establishment writes 5 before message.',
 'Safeguard starts at 0; positive duplicate rejects, successful own-side establishment writes 5 before message.',
 'LuckyChant starts at 0; positive duplicate rejects, successful own-side establishment writes 5 before message.',
 'Mist is consumed by the recipient side in stat-lowering checks; self effects, user identity, INFILTRATOR and ability-specific gates retain their actual ordering.',
 'Safeguard is consumed by actual status/drowsiness/confusion eligibility paths with their distinct bypass conditions; its field alone is not every-status immunity.',
 'LuckyChant directly rejects critical-hit selection when target side counter is positive, before later critical stages/randomness.',
 'Each positive side counter ticks once in reached side-ending helper; a 0 result gets its corresponding message.',
 'A failure or earlier EOR exit before that helper can retain the counter; no elapsed-time or unconditional round cleanup is inferred.'
],['activefield_full','mist_tailwind_producers','safeguard_producer','screens_lucky_producers','stages','statuses_full','calculations','eor_all'],'per-Move own-side 5 -> recipient-side status/stage/critical consumers -> local side countdown; actual bypasses remain separate.')
row(726,[
 'Tailwind starts at 0; the Move rejects positive own-side Tailwind rather than refreshes.',
 'Successful effect writes own-side Tailwind 4 before feedback.',
 'Battler.pbSpeed multiplies speedMult by 2 while its own-side Tailwind is positive.',
 'The multiplier does not depend on declared side size or how many partners currently occupy that side.',
 'Other speed stages, ability/item modifiers, Swamp, paralysis and badges still compose in the actual speed query.',
 'Reached side-ending helper decrements positive Tailwind and reports its expiry at 0; priority order changes only at the actual recalculation call points.'
],['activefield_full','mist_tailwind_producers','battlerfull','priority','eor_all'],'Tailwind own-side 4 -> speed multiplier 2 -> priority recalc when called -> late side tick.')
row(727,[
 'Rainbow, Swamp and SeaOfFire each initialize to 0 on both side objects.',
 'Pledge combo construction identifies the paired function, combo effect, optional type and animation; the receiver checks actual FirstPledge/setup state.',
 'The complete Pledge parent sets Rainbow on the current user side only if that counter is exactly 0; it writes 4.',
 'It sets Swamp on the opposing side only if exactly 0, writing 4.',
 'It sets SeaOfFire on the opposing side only if exactly 0, writing 4.',
 'An existing nonzero selected combo effect is not refreshed and does not cause that new establishing message/animation.',
 'Rainbow can double ordinary additional-effect chance under the actual generation/function guard; active ShieldDust without MoldBreaker first returns 0, and chances over 100 return before the doubling branch.',
 'Rainbow and SereneGrace share an OR condition for this doubling, so their coexistence does not double twice in that branch; debug override may later choose 100.',
 'The separate flinch helper also doubles its actual computed chance for Rainbow OR SereneGrace after its own exclusion and source gates.',
 'Swamp divides own-side speedMult by 2; it is not a permanent Speed-stat write.',
 'SeaOfFire has an earlier damage/countdown consumer plus the later side countdown; full double-tick vectors require reaching both.',
 'The common side-ending stage also decrements positive Rainbow and Swamp; each expiry message follows its local 0 result.',
 'Pledge setup/action forwarding/damage/type success remains conditional on complete ordinary Move gates; the directory does not approve every possible nested Move interaction.'
],['activefield_full','pledge_parent_complete','pledge_constructor_trio','use','attack','calculations','battlerfull','eor_all'],'actual paired-Pledge state -> only-zero side record 4 -> chance/speed/SeaOfFire consumers -> local late tick, preserving early damage tick.',open=['Full Move-family/default binding and every nested action combination remain separately bounded; named Pledge methods are complete but not all Move semantics.'])
row(728,[
 'Spikes starts at 0 on each side; its Move rejects opposing-side value >=3.',
 'A successful Spikes effect increments the opposing side by 1 before message; the ordinary valid range reaches at most 3.',
 'ToxicSpikes starts at 0; its Move rejects opposing-side value >=2.',
 'Successful ToxicSpikes increments by 1 before message, reaching at most 2 in the ordinary producer domain.',
 'The records belong to the side, not the producer Pokemon; replacing or fainting that producer does not itself erase them.',
 'They have no ordinary positive EOR countdown among the named side-duration consumers; entry and explicit removal are different consumers.',
 'Entry HP/status/absorption and explicit removal contracts are handled by their actual later methods, not inferred from layer count alone.'
],['activefield_full','misc_full','eor_all','switching'],'opposing-side layer guard -> increment -> preserved side record -> actual entry/removal consumer; no per-producer ownership.',open=['Detailed hazards-to-entering-battler HP/status/grounding chain follows C747+; no complete entry approval from this producer-only row.'])
row(729,[
 'StealthRock starts false; its Move rejects an already true opposing-side flag.',
 'Successful StealthRock effect sets that opposing-side flag true before its pointed-stone message.',
 'StickyWeb starts false; its Move rejects an already true opposing-side flag.',
 'Successful StickyWeb sets that opposing-side flag true before its web message.',
 'Neither flag receives ordinary EOR countdown or follows the original producer across replacement.',
 'The copied source comment saying stealth rocks above StickyWeb is not executable semantics: distinct flag and receiver effects must stay distinct.',
 'Their actual HP/type-effectiveness and Speed-lowering entry consumers are separately required, not interchangeable because both are hazards.'
],['activefield_full','misc_full','eor_all','switching'],'separate boolean hazard producers -> same persistent side identity -> distinct actual entry/removal readers.',open=['Detailed StealthRock/StickyWeb entry consumer qualifications follow; generic flag state does not certify every immunity or stat callback.'])
row(730,[
 'CraftyShield, MatBlock, QuickGuard and WideGuard initialize false on each side and are cleared separately in the complete EOR tail.',
 'CraftyShield Move rejects its own-side flag already true and then requires another unmoved UseMove/Shift battler through pbMoveFailedLastInRound.',
 'MatBlock requires user.turnCount<=1 and the same last-action gate; its complete Move does not independently reject an existing own-side MatBlock flag.',
 'QuickGuard and WideGuard set @sidedEffect=true and select their respective side flag through the complete ProtectMove parent.',
 'Protect parent duplicate side flag fails and resets user ProtectRate to 1.',
 'For a side effect in generation>=6, the consecutive-protection random draw is skipped; older<=5 still draws when ProtectRate>1.',
 'The last-action gate remains after that possible draw, even for current generation side protection; failure resets ProtectRate1 and does not establish the side flag.',
 'That gate requires another nonfainted actual battler with UseMove/Shift choice and not moved this round; item-only/switch-only choices do not suffice.',
 'All front gates passed, Protect effect sets side flag true and multiplies user ProtectRate by 3 in gen>=6, otherwise 2, before its message.',
 'Complete EOR tail clears these four side flags, not every user effect or protection counter; an early exit can skip that tail.',
 'Target success consumers distinguish status/multi-target/priority/damaging classes and actual bypass conditions; no single generic immunity is substituted.'
],['activefield_full','side_protect_producers','protect_parent_complete','usagefull','checksfull','battlerfull','eor_all','b_settings'],'distinct Move front gates -> side flag / personal ProtectRate writes -> actual target success checks -> complete tail clear; gen draw exemption not last-action exemption.')
row(731,[
 'EchoedVoiceCounter initializes 0 and EchoedVoiceUsed false on each side.',
 'Usage-counter override captures the old same-side count and calls parent; if Used is false it writes min(old+1,5).',
 'It then writes Used true even when this side already used EchoedVoice in this round.',
 'Later same-round qualifying usage does not increment again while Used is true.',
 'Base damage is multiplied by the actual same-side count at that query; this is neither a per-user nor immutable per-Move count.',
 'Complete tail sets Counter0 only if this side did not use it this round, then clears Used false.',
 'Ordinary same-side Pokemon replacement does not reconstruct ActiveSide or by itself break the count; a skipped tail may preserve Used/count prefix.'
],['activefield_full','echo_retaliate_producers','usagefull','use','eor_all','switching'],'side count capture -> first-use +1 cap5 / Usedtrue -> damage multiplier -> tail conditional reset + Usedfalse.')
row(732,[
 'Round initializes false on each side.',
 'Round base-damage function doubles if current own-side Round is true.',
 'Reached Round EffectGeneral sets own-side Round true before searching allies.',
 'It chooses the first actual ally with UseMove choice, not moved, and the same function code; that ally gets MoveNext true and Quash0, then search stops.',
 'Choice/type assumptions follow actual ordinary registered choices; no empty malformed choice compatibility is invented.',
 'Actual Attack candidate picker consumes MoveNext/Quash according to WP40; field flag alone does not execute the ally.',
 'Complete tail clears Round false; ordinary same-side member replacement does not itself clear this side flag.'
],['activefield_full','switch_effects_full','attack','use','eor_all'],'Round damage read -> side flag true -> first qualifying ally MoveNext/Quash writes -> actual action picker -> tail false.')
row(733,[
 'LastRoundFainted initializes -1 per side.',
 'Formal pbFaint rejects living targets and returns when already formally fainted; later reached path clears choice then records current turnCount in the fainted battler own side.',
 'The record is after scene/initialization/status/happiness/form/Peer steps, so an earlier failure may leave HP0 without this round record.',
 'Retaliate doubles only if that side record>=0 and equals current turnCount-1.',
 'The complete EOR tail does not reset LastRoundFainted to -1 each round; equality against current round creates the time qualification.',
 'A new formal faint on the same side overwrites with its actual current turn number; partner/user identity does not make a separate side record.'
],['activefield_full','echo_retaliate_producers','b_change','eor_all','battlerfull'],'formal Faint reached side write -> turn-number retained -> Retaliate exact previous-round comparison; HP0 alone not sufficient.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10d.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
