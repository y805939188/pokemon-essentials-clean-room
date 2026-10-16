import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11k.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
F='Complete refund fixtureF: ordinary internal wild2v1/no partner, both player users remain alive/actionable, nonactive ableT missing1HP/noEgg/Embargo/Hyper; Potionexact2, refund capacity always sufficient, both ordinary selections/register sameT eligible; no cancel/switch/plugin/reentry; solefoe ordinaryPoison/count0/HP1/noPoisonHeal/MagicGuard/healing/otherterminalwriter, legal non-damaging turn actions do not change playerHP/status/inventory; all messages/scenes/callbacks normallyreturn. Each control independently changes only its named condition.'
row(956,[
 'The U04 refund suite explicitly uses source-derived static designs with executionNOT_EXECUTED and no reference/engine/model case run.',
 'FixtureF fixes ordinary internal wild2v1/no partner and two living actionable player item users, preventing faint/switch/cancel from silently clearing the item identities.',
 'Both normal registrations target the same nonactive able nonEgg T missing1HP, without Embargo/Hyper; POTION quantity2 and each selection qualifies before either effect.',
 'Refund capacity is sufficient in the principal fixture, and no plugin/reentry/other inventory mutation is allowed.',
 'The sole opponent ordinaryPoison/count0/HP1 with no healing/immunity/other result source ensures the specified later residual terminal condition; normal non-damaging actions preserve that setup.',
 'Presentation and callbacks normally return; independent changed cases must not silently inherit the principal final inventory2 when they alter capacity/liveness/next-round cleanup.',
 'WP28/40/42 shared lifecycle contract is already accepted; this review does not introduce a new finding or promise future compatibility policy.'
],['items','command','bag','battleitems','eor','normal_end'],'explicit complete fixture -> separate registration/execution/identity/terminal consumers -> static no execution.',premise=F,support='SUPPORTED_BOUNDED_SCOPE_QUALIFICATION')
rows.append(dict(number=957,layout_reason='U04 refund table column heading only.'))
row(958,[
 'RF01 keeps all ofF and normally registers both POTIONs, consuming Bag2to1to0 before their effects.',
 'The first executor current eligibility passes, requests20 healing but actual missingHP1 caps recovery to1 and leaves T full.',
 'After the normal first effect it clears only the first user choice item identity.',
 'The second executor checks the now-full T and fails current CanUse eligibility, gives no-effect feedback and refunds one toBag1.',
 'That failure path does not clear the second choice item identity.',
 'The later foe ordinary poison tick makes HP0 and formally faints it; ordinary actual judgment reaches win1 as F excludes other living opponents/result sources.',
 'Normal terminal CancelChoice sees the still-present second identity, refunds again toBag2 and clears that choice.',
 'Final principal state is Tfull, actual therapy once and POTION2; the second refund is a retained-identity anomaly, not an extra healing or automatic idempotent refund guard.'
],['items','command','bag','battleitems','itemhandlers','pokemon_growth_qual','eor','b_change','switching','start_end_full','normal_end','potionpbs'],'two consume -> firstheal1/clear -> second eligibilityfail/refund1 identityretained -> foePoisonFaint/Judge1 -> normalCancelrefund2.',premise=F)
row(959,[
 'RF02 changes only the foe to survive EOR without another terminal writer and reaches the next normal command phase.',
 'The same two registrations/firstheal/secondfailedrefund leaveBag1 and second item identity initially present.',
 'At command start pbCanShowCommands? allows this still-live non-multiturn user, so pbClearChoice directly removes the identity.',
 'That direct clear does not invoke ReturnUnusedItemToBag, unlike CancelChoice.',
 'Inventory stays1, T remains full and battle continues under the control premise; no normal end refund follows this now-cleared identity.'
],['items','command','bag','eor','normal_end'],'same refund1 identity -> next eligible command directClear -> no extra refund ->1.',premise=F+' Independent change: foe survives and no other result, next normal command reached.')
row(960,[
 'RF03 changes only a legal later event causing the second user to undergo formal fainting before normal victory terminal cleanup, with first user alive and no other inventory/therapy change.',
 'After second failed item execution, inventory1 and its retained identity exist as inF.',
 'Formal pbFaint eventually calls direct pbClearChoice and removes that identity without refund.',
 'Normal EndOfBattle no longer finds this item identity to refund, so final POTION1.',
 'Merely writing HP0 without reaching formal faint/choice cleanup is insufficient to claim the same inventory result.',
 'Earlier scene/faint-helper failure before ClearChoice can leave the identity, so exact reached prefix remains decisive.'
],['items','command','b_change','bag','normal_end'],'refund1/identity -> actual formalFaint directClear -> terminal no identity ->1.',premise=F+' Independent change: second user actual formalFaint before terminal, first alive.')
row(961,[
 'RF04 changes the input point to only the first item registered, second not yet registered, then second command menu backs to the previous user.',
 'First registration consumes Bag2to1 but has not invoked healing.',
 'The command loop back branch explicitly CancelChoice on the preceding user.',
 'CancelChoice returns its unused consumable under normal capacity/owner rules and then clears it, restoring1to2.',
 'T remains missing1HP because no executor has healed it; normal menu withdrawal is not a rollback of a previously completed heal.',
 'This unused-choice control is distinct from an executed eligibility-failure refund that retains identity.'
],['command','items','bag','battleitems'],'first registeredunused2to1 -> prior-user CancelChoice -> refundto2+clear -> noheal.',premise=F+' Independent input point: second notregistered and Back to prior user before effects.')
row(962,[
 'RF05 A independently makes can_add? false at the second item execution refund; this external capacity change is a named control, not a claim default Bag is necessarily full.',
 'A reaches ReturnUnusedItemToBag, raises the local internal error without adding, and retains Bag0 plus the already completed Tfull/first identity clear/earlier consumption prefixes.',
 'A item refund path itself still has not cleared the second identity; outer diagnostics/retry/cleanup are not forced to complete by this local claim.',
 'RF05 B independently allows the first refund then makes can_add? false for the later normal-terminal second refund.',
 'B retains Bag1/Tfull/first refund when that later addition fails; normal CancelChoice subsequent unregister/direct-clear statements are not guaranteed after the raise.',
 'Neither control is assigned the main successful finalBag2, and no rollback or host recovery is inferred from a diagnostic wrapper.'
],['items','command','bag','normal_end','pbdebug','errors'],'A execution refund reject -> noadd Bag0; B laterterminal refund reject -> noadd Bag1; reached prior heal/consumes persist.',premise=F+' Independent named external capacity failure A at firstrefund or B at laterterminal refund.')
row(963,[
 'RF06 is separate legal configured Direct5 consumableI with no effect/eligibility handler or conditional match, nonimportant/nonball/nonSnag, internal live player and Bag1.',
 'Default eligibility passes, registration consumes1to0 and the normal executor invokes no meaningful effect then clears its item identity.',
 'Normal terminal cancellation finds no residual item identity and leavesBag0.',
 'Changing only data family1 or3 makes their effect-existence check reject before consumption, retainingBag1.',
 'This is the existing CM32/B008 bounded control, not arbitrary unknown items or a reason to equate effect-false with eligibility-false refund.'
],['command','items','itemhandlers','bag','itemdata','normal_end','ui_command'],'legal Direct5 nohandler -> default eligibility -> consume0/normalclear -> terminalnorefund; family1/3 earlierreject.')
row(964,[
 'The refund suite leaves future repair/compatibility policy to the user rather than mandating permanent retention of the anomaly.',
 'The principal fixture is a normal nonexceptional lifecycle; only capacity controls introduce their named failure points.',
 'Those controls retain actual committed prefixes without claiming later recovery or complete terminal success.',
 'No real menu/assets/host/Demo certification or business execution is granted by these static vectors.'
],['items','command','normal_end','pbdebug'],'source anomaly + bounded error-prefix documentation -> future policy separate and NOT_EXECUTED.',support='SUPPORTED_BOUNDED_SCOPE_QUALIFICATION')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11l.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
