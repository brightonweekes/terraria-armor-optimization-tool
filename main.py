import armor
from armor import sets, leggings, chestplates, helmets
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


    print(selected_helmet.defense + selected_chestplate.defense + selected_leggings.defense)
