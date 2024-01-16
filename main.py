calamity = True
if calamity:
    from calamity_armor import armor_sets, leggings, chestplates, helmets
else:
    from armor import armor_sets, leggings, chestplates, helmets

from copy import copy


selected_helmet = helmets[0]
selected_chestplate = chestplates[0]
selected_leggings = leggings[0]

optimization = 'balance'
target_class = 'melee'

if optimization == 'balance':
    defense_weight, damage_weight, crit_weight, movement_weight = 1, 1, 1, .1
    if target_class == 'melee':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
    elif target_class == 'ranged':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 1, 1, 0, 0, 0, 0, 0
    elif target_class == 'magic':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 0, 0, 1, 1, .05, 0, 0
    elif target_class == 'summoner':
        melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
            mana_weight, summon_damage_weight, minion_slots_weight = 0, 0, 0, 0, 0, 0, 0, 0, 1, 10


for helm in helmets:
    if (helm.defense*defense_weight + helm.damage*damage_weight + helm.crit*crit_weight + helm.movement*movement_weight + helm.melee_damage*melee_damage_weight + 
        helm.melee_crit*melee_crit_weight + helm.melee_speed*melee_speed_weight + helm.ranged_damage*ranged_damage_weight + helm.ranged_crit*ranged_crit_weight + 
        helm.magic_damage*magic_damage_weight + helm.magic_crit*magic_crit_weight + helm.mana*mana_weight + helm.summon_damage*summon_damage_weight + 
        helm.minion_slots*minion_slots_weight) > (selected_helmet.defense*defense_weight + selected_helmet.damage*damage_weight + selected_helmet.crit*crit_weight + 
        selected_helmet.movement*movement_weight + selected_helmet.melee_damage*melee_damage_weight + selected_helmet.melee_crit*melee_crit_weight + 
        selected_helmet.melee_speed*melee_speed_weight + selected_helmet.ranged_damage*ranged_damage_weight + selected_helmet.ranged_crit*ranged_crit_weight + 
        selected_helmet.magic_damage*magic_damage_weight + selected_helmet.magic_crit*magic_crit_weight + selected_helmet.mana*mana_weight + 
        selected_helmet.summon_damage*summon_damage_weight + selected_helmet.minion_slots*minion_slots_weight):
        selected_helmet = copy(helm)

for chest in chestplates:
    if (chest.defense*defense_weight + chest.damage*damage_weight + chest.crit*crit_weight + chest.movement*movement_weight + chest.melee_damage*melee_damage_weight + 
        chest.melee_crit*melee_crit_weight + chest.melee_speed*melee_speed_weight + chest.ranged_damage*ranged_damage_weight + chest.ranged_crit*ranged_crit_weight + 
        chest.magic_damage*magic_damage_weight + chest.magic_crit*magic_crit_weight + chest.mana*mana_weight + chest.summon_damage*summon_damage_weight + 
        chest.minion_slots*minion_slots_weight) > (selected_chestplate.defense*defense_weight + selected_chestplate.damage*damage_weight + selected_chestplate.crit*crit_weight + 
        selected_chestplate.movement*movement_weight + selected_chestplate.melee_damage*melee_damage_weight + selected_chestplate.melee_crit*melee_crit_weight + 
        selected_chestplate.melee_speed*melee_speed_weight + selected_chestplate.ranged_damage*ranged_damage_weight + selected_chestplate.ranged_crit*ranged_crit_weight + 
        selected_chestplate.magic_damage*magic_damage_weight + selected_chestplate.magic_crit*magic_crit_weight + selected_chestplate.mana*mana_weight + 
        selected_chestplate.summon_damage*summon_damage_weight + selected_chestplate.minion_slots*minion_slots_weight):
        selected_chestplate = copy(chest)

for leg in leggings:
    if (leg.defense*defense_weight + leg.damage*damage_weight + leg.crit*crit_weight + leg.movement*movement_weight + leg.melee_damage*melee_damage_weight + 
        leg.melee_crit*melee_crit_weight + leg.melee_speed*melee_speed_weight + leg.ranged_damage*ranged_damage_weight + leg.ranged_crit*ranged_crit_weight + 
        leg.magic_damage*magic_damage_weight + leg.magic_crit*magic_crit_weight + leg.mana*mana_weight + leg.summon_damage*summon_damage_weight + 
        leg.minion_slots*minion_slots_weight) > (selected_leggings.defense*defense_weight + selected_leggings.damage*damage_weight + selected_leggings.crit*crit_weight + 
        selected_leggings.movement*movement_weight + selected_leggings.melee_damage*melee_damage_weight + selected_leggings.melee_crit*melee_crit_weight + 
        selected_leggings.melee_speed*melee_speed_weight + selected_leggings.ranged_damage*ranged_damage_weight + selected_leggings.ranged_crit*ranged_crit_weight + 
        selected_leggings.magic_damage*magic_damage_weight + selected_leggings.magic_crit*magic_crit_weight + selected_leggings.mana*mana_weight + 
        selected_leggings.summon_damage*summon_damage_weight + selected_leggings.minion_slots*minion_slots_weight):
        selected_leggings = copy(leg)

best_score = (selected_helmet.defense*defense_weight + selected_helmet.damage*damage_weight + selected_helmet.crit*crit_weight + 
    selected_helmet.movement*movement_weight + selected_helmet.melee_damage*melee_damage_weight + selected_helmet.melee_crit*melee_crit_weight + 
    selected_helmet.melee_speed*melee_speed_weight + selected_helmet.ranged_damage*ranged_damage_weight + selected_helmet.ranged_crit*ranged_crit_weight + 
    selected_helmet.magic_damage*magic_damage_weight + selected_helmet.magic_crit*magic_crit_weight + selected_helmet.mana*mana_weight + 
    selected_helmet.summon_damage*summon_damage_weight + selected_helmet.minion_slots*minion_slots_weight + selected_chestplate.defense*defense_weight + 
    selected_chestplate.damage*damage_weight + selected_chestplate.crit*crit_weight + selected_chestplate.movement*movement_weight + 
    selected_chestplate.melee_damage*melee_damage_weight + selected_chestplate.melee_crit*melee_crit_weight + selected_chestplate.melee_speed*melee_speed_weight + 
    selected_chestplate.ranged_damage*ranged_damage_weight + selected_chestplate.ranged_crit*ranged_crit_weight + 
    selected_chestplate.magic_damage*magic_damage_weight + selected_chestplate.magic_crit*magic_crit_weight + selected_chestplate.mana*mana_weight + 
    selected_chestplate.summon_damage*summon_damage_weight + selected_chestplate.minion_slots*minion_slots_weight + selected_leggings.defense*defense_weight + 
    selected_leggings.damage*damage_weight + selected_leggings.crit*crit_weight + selected_leggings.movement*movement_weight + 
    selected_leggings.melee_damage*melee_damage_weight + selected_leggings.melee_crit*melee_crit_weight + 
    selected_leggings.melee_speed*melee_speed_weight + selected_leggings.ranged_damage*ranged_damage_weight + selected_leggings.ranged_crit*ranged_crit_weight + 
    selected_leggings.magic_damage*magic_damage_weight + selected_leggings.magic_crit*magic_crit_weight + selected_leggings.mana*mana_weight + 
    selected_leggings.summon_damage*summon_damage_weight + selected_leggings.minion_slots*minion_slots_weight)

for set in armor_sets:
    set_score = (set.helmet.defense*defense_weight + set.helmet.damage*damage_weight + set.helmet.crit*crit_weight + 
    set.helmet.movement*movement_weight + set.helmet.melee_damage*melee_damage_weight + set.helmet.melee_crit*melee_crit_weight + 
    set.helmet.melee_speed*melee_speed_weight + set.helmet.ranged_damage*ranged_damage_weight + set.helmet.ranged_crit*ranged_crit_weight + 
    set.helmet.magic_damage*magic_damage_weight + set.helmet.magic_crit*magic_crit_weight + set.helmet.mana*mana_weight + 
    set.helmet.summon_damage*summon_damage_weight + set.helmet.minion_slots*minion_slots_weight + set.chestplate.defense*defense_weight + 
    set.chestplate.damage*damage_weight + set.chestplate.crit*crit_weight + set.chestplate.movement*movement_weight + 
    set.chestplate.melee_damage*melee_damage_weight + set.chestplate.melee_crit*melee_crit_weight + set.chestplate.melee_speed*melee_speed_weight + 
    set.chestplate.ranged_damage*ranged_damage_weight + set.chestplate.ranged_crit*ranged_crit_weight + set.chestplate.magic_damage*magic_damage_weight + 
    set.chestplate.magic_crit*magic_crit_weight + set.chestplate.mana*mana_weight + set.chestplate.summon_damage*summon_damage_weight + 
    set.chestplate.minion_slots*minion_slots_weight + set.leggings.defense*defense_weight + set.leggings.damage*damage_weight + set.leggings.crit*crit_weight + 
    set.leggings.movement*movement_weight + set.leggings.melee_damage*melee_damage_weight + set.leggings.melee_crit*melee_crit_weight + 
    set.leggings.melee_speed*melee_speed_weight + set.leggings.ranged_damage*ranged_damage_weight + set.leggings.ranged_crit*ranged_crit_weight + 
    set.leggings.magic_damage*magic_damage_weight + set.leggings.magic_crit*magic_crit_weight + set.leggings.mana*mana_weight + 
    set.leggings.summon_damage*summon_damage_weight + set.leggings.minion_slots*minion_slots_weight)

    if  set_score >= best_score:
        selected_helmet = copy(set.helmet)
        selected_chestplate = copy(set.chestplate)
        selected_leggings = copy(set.leggings)

        best_score = copy(set_score)


if optimization == 'defense':
    print(f'\n{selected_helmet.name.capitalize()}, {selected_chestplate.name}, and {selected_leggings.name} give the highest defense of {selected_helmet.defense+selected_chestplate.defense+selected_leggings.defense}\n')
elif optimization == 'manual':
    print(f'\n{selected_helmet.name.capitalize()}, {selected_chestplate.name}, and {selected_leggings.name} give the highest score of {best_score}.\n')
