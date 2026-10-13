"""Close the remaining bounded configuration comparisons, preserving real gaps."""
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
def paths(*names):
    out=[]
    for name in names:
        candidates=list((s.ROOT/F).glob('*/'+name+'.md'))
        assert len(candidates)==1,name
        out.append(dict(path=str(candidates[0].relative_to(s.ROOT)),version=s.B))
    return out
decisions={
 1:('partial',['wp65-title-load-options-pause-and-pc','wp02-rule-configuration-and-data-variants'],'Screen Size row explicitly gives one-time dimensions,0–3 scale/center and4/negative fullscreen; source engine-version warning-and-continue is a separate compatibility detail, not a rejection rule in the configuration contract.'),
 5:('supported',['wp10-migration-failure-recovery','wp36-wild-encounters-and-modifiers'],'v21 flute migration is conditional on old value presence, with configured level-versus-rate projection; false is a present value. Old fields clear after transfer. Runtime flute directions are separately defined by the encounter contract.'),
 7:('partial',['wp16-world-rendering-and-visual-transitions','wp02-rule-configuration-and-data-variants'],'Configured landing animation is supported; exact visible-graphic/nontransparent/end-jump/spriteset gates remain finer than the world-animation summary. Not a demonstrated wrong default animation ID.'),
 8:('partial',['wp16-world-rendering-and-visual-transitions','wp02-rule-configuration-and-data-variants'],'Camera center is explicitly supported; player landing dust additionally excludes surfing unless surf is ending. Those dust gates are retained as partial detail, not hidden by correct screen-size formulas.'),
 12:('partial',['wp15-resource-matching-and-audio','wp17-messages-windows-input'],'Normal option-index/default0 lookup and resource fallback agree with the skin chain. A bad configured index can fail before bitmap resolution, so the documented missing-bitmap fallback does not prove arbitrary index safety.'),
 13:('supported',['wp30-growth-learning-and-friendship','wp19-attributes-ability-and-stats','wp04-pbs-lifecycle'],'Maximum-level clamping, table-vs-formula selection and compiler/individual level validation are distinct consumers and agree with current contracts. No600-point executable arithmetic was run.'),
 15:('partial',['wp43-types-accuracy-and-damage','wp02-rule-configuration-and-data-variants'],'Stored data physical/special queries add a zero-power guard while category predicates and combat wrappers do not share that guard. The ordinary category switch is covered; the wrapper/data distinction remains partial.'),
 26:('partial',['wp42-growth-end-of-round-and-battle-outcomes','wp47-b-switching-control-and-item-changes','wp50-held-item-triggers-and-consumption'],'Burn/Heatproof and affection cure gates agree. Trapping/Binding Band quantities are present, but exact generation6 threshold is not uniquely stated by old/current prose; this is bounded cross-owner threshold coverage, not a new executed battle result.'),
 27:('partial',['wp44-statuses-stat-stages-and-immunities','wp48-ability-calculation-modifiers','wp02-rule-configuration-and-data-variants'],'Paralysis and badge speed scaling agree. Grass uses MORE_TYPE_EFFECTS independently from generation>=6 Overcoat/Goggles powder immunity; current immunity descriptions do not completely state this configurable split.'),
 33:('partial',['wp40-commands-obedience-and-action-order','wp47-a-move-attributes-targeting-and-calling','wp48-ability-calculation-modifiers'],'Obedience, confusion setting, King Shield and Prankster rules were compared. Exact Wide Guard generation7 scope and independent grass/Overcoat/Goggles gates retain partial threshold detail; ordinary current-generation outcomes alone are insufficient.'),
 35:('partial',['wp43-types-accuracy-and-damage','wp47-a-move-attributes-targeting-and-calling','wp48-ability-calculation-modifiers'],'Critical vectors and category configuration are explicit. Exact generation>=6 sound-or-Infiltrator substitute bypass is not fully resolved by present-current-generation descriptions; category helper distinction also remains in the data contract.'),
 39:('partial',['wp45-weather-terrain-side-and-position-effects','wp52-c-items-calling-and-control-evaluation'],'Actual Rapid Spin speed addition is gated>=8, separate from hazard removal. AI>=8 is explicit but is not substitute evidence that the actual-move current/old wording defines its threshold.'),
 40:('partial',['wp45-weather-terrain-side-and-position-effects','wp44-statuses-stat-stages-and-immunities','wp52-a-generic-numerical-and-status-evaluation'],'Defog opposite hazards>=6 and terrain>=8 are separate source branches; Psych Up Focus Energy/Laser Focus follows the critical setting. Related effects are documented, but not every direct generation gate is made explicit in the consumer projection.'),
 42:('supported',['wp47-a-move-attributes-targeting-and-calling','wp46-damage-multihit-and-healing','wp45-weather-terrain-side-and-position-effects'],'Hidden Power<=5 retains initial60 bit accumulation and ordered type filtering; the current dedicated paragraph explicitly gives68/68/69/70. Facade<=5 and old/local versus>=6 global sport state agree with their named move/field rules.'),
 51:('supported',['wp67-a-battle-interaction-and-presentation','wp02-rule-configuration-and-data-variants'],'Ability splash generation>=5 and party-ball slot count are explicit; configured screen dimensions are inputs. Independent fixed animation focus coordinates are audit observations, not a claim that all layouts rescale automatically.'),
 52:('supported',['wp67-a-battle-interaction-and-presentation','wp19-attributes-ability-and-stats','wp02-rule-configuration-and-data-variants'],'Both introduction and send-out animation projections require animation enabled and ordinary shininess before SUPER_SHINY selects its variant; underlying super-shiny state remains independent.'),
 55:('partial',['wp51-ai-action-selection-and-skill','wp52-a-generic-numerical-and-status-evaluation'],'Prankster>=7 is supported; Curse Protean/Libero prediction has a separate>=8 targeting gate. Current skill/target prose does not fully state this specific prediction threshold.'),
 56:('partial',['wp51-ai-action-selection-and-skill','wp52-a-generic-numerical-and-status-evaluation'],'Quick Guard ProtectRate condition<=5 and non-Fire target-thaw penalty>=6 are precise AI-only cutoffs beyond some old/current score wording; no extrapolation to actual battle mechanics.'),
 60:('partial',['wp52-a-generic-numerical-and-status-evaluation','wp48-ability-calculation-modifiers','wp43-types-accuracy-and-damage'],'All multipliers, skills and flags were compared. Direct AI Normalize>=7, terrain>=8 and Minimize>=6 branches are not completely recoverable from generic current/old wording; real-move contracts are counterevidence context, not proof of each AI approximation.'),
 62:('partial',['wp52-a-generic-numerical-and-status-evaluation','wp52-b-field-damage-healing-and-target-evaluation'],'Autotomize/Sky Drop, Minimize penalty, Defog predicted hazards/terrain and Psych Up critical-score predicates are separately analyzed. Exact AI>=6/>=8 cutoffs retain partial coverage, despite supported current-default examples.'),
 63:('partial',['wp52-a-generic-numerical-and-status-evaluation'],'Paralysis score reversal multiplier2 versus4 follows>=7; Conversion first-slot-only prediction follows>=6. Named score behaviors exist, but direct cutoff precision remains partial.'),
 64:('partial',['wp52-a-generic-numerical-and-status-evaluation','wp52-c-items-calling-and-control-evaluation'],'Old/global sports, protection score multipliers, King Shield>=8, Wide Guard outer-move predicate and Lock On/Minimize>=6 were compared. AI-specific asymmetry/cutoffs remain partial rather than silently sharing the actual-move contract.'),
 77:('supported',['wp38-capture-and-receiving','wp39-battle-context-and-participants','wp45-weather-terrain-side-and-position-effects','wp31-basic-evolution','wp32-contextual-trade-and-post-battle-evolution'],'Capture option injection/force override, cave night precedence, weather-to-terrain only without explicit terrain, waiting trainer party limit, and post-battle evolution result/egg/fainted/order gates agree with their separate owner clauses.'),
 89:('partial',['wp63-pokegear-map-music-and-phone','wp02-rule-configuration-and-data-variants'],'Rematch initialization and segmented substitutions match. The exact optional male-blue/female-red/unknown-no-prefix display branch is not fully stated by the general phone coloring configuration; no false statement that this switches language.'),
 92:('partial',['wp25-party-and-storage','wp66-b-storage-and-pokedex-ui'],'Default box count versus stored count and heal/ready-to-evolve preservation agree. All-negative capacity versus only−1 party addressing is candidate005; healing-before-failed-storage is already explicit counterevidence, not a new finding.'),
 101:('supported',['wp67-b-lifecycle-presentations-and-history','wp02-rule-configuration-and-data-variants'],'Hall of Fame allocates/cleans by configured party size and skips missing archive members. This supports capacity consumption only; arbitrary enlarged layouts/media are not promised.'),
 104:('partial',['wp62-pokedex-records-regions-and-content','wp66-b-storage-and-pokedex-ui','wp02-rule-configuration-and-data-variants'],'Pokedex name configuration shape is recognized. Exact nil generic-name/array first-field/scalar direct display is finer than the naming table; all actual names and consumers read.'),
 105:('partial',['wp62-pokedex-records-regions-and-content','wp66-b-storage-and-pokedex-ui','wp02-rule-configuration-and-data-variants'],'Current-region/saved-dex fallback and offsets match. Configured tuple second-field Area region override is distinct from current-map fallback and lacks an equally precise connecting clause.'),
 106:('partial',['wp62-pokedex-records-regions-and-content','wp66-b-storage-and-pokedex-ui','wp63-pokegear-map-music-and-phone'],'Seen-form/structural exclusion and offset differences agree. Area overlay always requires matching region and positive enabled switch, independently of wall-map flag; current region-map clauses do not completely state this separate consumer.'),
 118:('supported',['wp69-slot-machine','wp24-player-trainers-partners'],'MAX_COINS cap, exact-cap entry rejection, payout clearing and exit submission match. Fixed five-digit drawing is observed; no arbitrary enlarged-limit layout compatibility is claimed or implied.'),
 124:('partial',['wp24-player-trainers-partners','wp59-world-time-weather-field-moves','wp02-rule-configuration-and-data-variants'],'Player naming strict-length stages and language display-name selection match. Array-event exclamation dedup plus first-created-sprite behavior is a narrower helper boundary not fully described by the configured animation ID.'),
 130:('supported',['wp73-a-content-editors','wp27-bag-and-item-storage'],'Pocket selection uses one-based authored pocket IDs, cancel retains previous value and default is1; NoPocket0 display is separate from new-item cancellation and positive PBS pocket validation.'),
}
d=s.read('configuration-branch-reviews.json')
for idx,(status,names,comparison) in decisions.items():
    b=d['branches'][idx]
    b.update(status=status,evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison',
             current_contract_comparison=comparison,spec_anchors=paths(*names),pending=None,
             semantic_comparison_complete=True,supported_boundary='Only the stated M01 setting-to-consumer projection; no complete consumer-domain or runtime certification.')
for b in d['branches']:
    if b['status']=='supported':b['semantic_comparison_complete']=True
s.write('configuration-branch-reviews.json',d)

# Link every lexical occurrence to its actual bounded comparison, including
# declaration-only and inactive/comment hits. Never upgrade based on hit count.
l=s.read('configuration-consumer-ledger.json')
for definition in l['definitions']:
    refs=[]
    for hit in definition['occurrences']:
        matches=[b for b in d['branches'] if b['path']==hit['path'] and any(a<=hit['line']<=z for a,z in b['lines'])]
        if hit.get('lexical_classification') in ('comment_only','comment_line','inactive_block'):
            hit['semantic_review']='reviewed_not_an_active_consumer';continue
        if matches:
            hit.update(semantic_review='current_contract_compared',branch_refs=[b['id'] for b in matches],
                       capability_status='partial' if any(b['status']=='partial' for b in matches) else 'supported')
            refs.extend(hit['branch_refs'])
    definition['branch_refs']=list(dict.fromkeys(refs))
    states=[h.get('capability_status') for h in definition['occurrences'] if h.get('capability_status')]
    definition['status']='partial' if 'partial' in states else 'supported'
    definition['supported_boundary']='supported_static for the declared value/derivation and linked reviewed consumers; comments/inactive blocks are not execution paths.'
    definition['semantic_review_complete']=True
s.write('configuration-consumer-ledger.json',l)
o.source('Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[1298,1335]],
 [dict(lines=[1298,1335],entry_or_rule='Hidden Power complete data ordering and old-power branch',comparison='Full type exclusion/ordering tail now inspected; matches currentWP47A§3.2 including Fairy eligibility and initial60 old-power peculiarity.')])
o.progress('140组配置消费者均已有当前合同逐项比较；保留直接世代阈值、数据/战斗类别差异、图鉴区域配置等具名partial。词法命中已链接实际分支，注释/停用代码不计活跃消费者。','完善主责WP02/03/04/08逐条反向映射、字段状态和最终覆盖清单')
print('Remaining branch comparisons closed:',len(decisions))
