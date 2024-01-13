from armor import armor_sets, leggings, chestplates, helmets
from copy import copy


selected_helmet = helmets[0]
selected_chestplate = chestplates[0]
selected_leggings = leggings[0]

optimization = 'defense'
target_class = 'melee'

if optimization == 'defense':
    defense_weight, damage_weight, crit_weight, movement_weight = 1, 0, 0, 0
elif optimization == 'damage_only':
    defense_weight, damage_weight, crit_weight, movement_weight = 0, 1, 0, 0
elif optimization == 'movement_speed':
    defense_weight, damage_weight, crit_weight, movement_weight = 0, 0, 1, 0
elif optimization == 'damage_and_crit':
    defense_weight, damage_weight, crit_weight, movement_weight = 0, 1, 1, 0
elif optimization == 'manual':
    defense_weight, damage_weight, crit_weight, movement_weight = 1, 1, 1, 1




for helm in helmets:
    if helm.defense*defense_weight + helm.damage*damage_weight + helm.crit*crit_weight + helm.movement*movement_weight > (
        selected_helmet.defense*defense_weight + selected_helmet.damage*damage_weight + selected_helmet.crit*crit_weight + 
        selected_helmet.movement*movement_weight
        ):
        selected_helmet = copy(helm)

for chest in chestplates:
    if chest.defense*defense_weight + chest.damage*damage_weight + chest.crit*crit_weight + chest.movement*movement_weight > (
        selected_chestplate.defense*defense_weight + selected_chestplate.damage*damage_weight + selected_chestplate.crit*crit_weight + 
        selected_chestplate.movement*movement_weight
        ):
        selected_chestplate = copy(chest)

for leg in leggings:
    if leg.defense*defense_weight + leg.damage*damage_weight + leg.crit*crit_weight + leg.movement*movement_weight > (
        selected_leggings.defense*defense_weight + selected_leggings.damage*damage_weight + selected_leggings.crit*crit_weight + 
        selected_leggings.movement*movement_weight
        ):
        selected_leggings = copy(leg)

best_score = (selected_helmet.defense*defense_weight + selected_helmet.damage*damage_weight + selected_helmet.crit*crit_weight + 
    selected_helmet.movement*movement_weight + selected_chestplate.defense*defense_weight + selected_chestplate.damage*damage_weight + 
    selected_chestplate.crit*crit_weight + selected_chestplate.movement*movement_weight + selected_leggings.defense*defense_weight + 
    selected_leggings.damage*damage_weight + selected_leggings.crit*crit_weight + selected_leggings.movement*movement_weight)

for set in armor_sets:
    set_score = (set.helmet.defense*defense_weight + set.helmet.damage*damage_weight + set.helmet.crit*crit_weight + 
        set.helmet.movement*movement_weight + set.chestplate.defense*defense_weight + set.chestplate.damage*damage_weight + 
        set.chestplate.crit*crit_weight + set.chestplate.movement*movement_weight + set.leggings.defense*defense_weight + 
        set.leggings.damage*damage_weight + set.leggings.crit*crit_weight + set.leggings.movement*movement_weight + 
        set.set_bonus.defense*defense_weight + set.set_bonus.damage*damage_weight + set.set_bonus.crit*crit_weight + 
        set.set_bonus.movement*movement_weight)

    if  set_score >= best_score:
        selected_helmet = copy(set.helmet)
        selected_chestplate = copy(set.chestplate)
        selected_leggings = copy(set.leggings)

        best_score = copy(set_score)


if optimization == 'defense':
    print(f'\n{selected_helmet.name.capitalize()}, {selected_chestplate.name}, and {selected_leggings.name} give the highest defense of {selected_helmet.defense+selected_chestplate.defense+selected_leggings.defense}\n')
elif optimization == 'manual':
    print(f'\n{selected_helmet.name.capitalize()}, {selected_chestplate.name}, and {selected_leggings.name} give the highest score of {best_score}.\n')
