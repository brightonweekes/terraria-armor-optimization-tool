from armor import armor_sets, leggings, chestplates, helmets
from copy import copy


selected_helmet = helmets[0]
selected_chestplate = chestplates[0]
selected_leggings = leggings[0]


optimize_for = 'max_defense'

if optimize_for == 'max_defense':

    for helm in helmets:
        if helm.defense > selected_helmet.defense:
            selected_helmet = copy(helm)

    for chest in chestplates:
        if chest.defense > selected_chestplate.defense:
            selected_chestplate = copy(chest)

    for leg in leggings:
        if leg.defense > selected_leggings.defense:
            selected_leggings = copy(leg)
    
    max_defense = selected_helmet.defense + selected_chestplate.defense + selected_leggings.defense
    for set in armor_sets:
        set_defense = set.helmet.defense + set.chestplate.defense + set.leggings.defense + set.set_bonus.defense
        if  set_defense >= max_defense:
            selected_helmet = copy(set.helmet)
            selected_chestplate = copy(set.chestplate)
            selected_leggings = copy(set.leggings)

            max_defense = copy(set_defense)


    print(f"\n{selected_helmet.name.capitalize()}, {selected_chestplate.name}, and {selected_leggings.name} give the highest overall defense of {max_defense}\n")
