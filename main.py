# Current Issues: due to set identifiers being higher than number of sets of armor availaiable at lower stages, an error is throuwn when mode is set to anything befoee pre wall of flesh
# Better UI needed
# Calamity armor
# Rogue class
# Sets with multiple headpieces show up multiple times in the end results (also hurts performance)


# Import necessary armor pieces, depending on whether Calamity mod is enabled or disabled
calamity = False
if calamity:
    from calamity_armor import armor_sets, leggings, chestplates, helmets
else:
    from armor import armor_sets, leggings, chestplates, helmets

from copy import copy

# Set the target class and stats to maximize
target_stat = 'balance'
target_class = 'melee'

# Assign weight values to each stat based on target stat and target class
if target_stat == 'balance':
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

# Create the list which will contain all combinations of armor and their weighted score
combo_scores = []

# Loop through every combination and append to combo_scores along with weighted score
print('\nCalculating... Please wait\n')
for helm in helmets:
    for chest in chestplates:
        for leg in leggings:
            set_bonus_score = 0
            if helm.set_identifier == chest.set_identifier == leg.set_identifier or (helm.set_identifier < 0 and helm.set_identifier == chest.set_identifier):   # if combo is a full set, calculate the set_bonus score
                set = armor_sets[helm.set_identifier]
                set_bonus_score = (set.set_bonus.defense*defense_weight +
                    set.set_bonus.damage*damage_weight + set.set_bonus.crit*crit_weight + set.set_bonus.movement*movement_weight + 
                    set.set_bonus.melee_damage*melee_damage_weight + set.set_bonus.melee_crit*melee_crit_weight + set.set_bonus.melee_speed*melee_speed_weight + 
                    set.set_bonus.ranged_damage*ranged_damage_weight + set.set_bonus.ranged_crit*ranged_crit_weight + 
                    set.set_bonus.magic_damage*magic_damage_weight + set.set_bonus.magic_crit*magic_crit_weight + set.set_bonus.mana*mana_weight + 
                    set.set_bonus.summon_damage*summon_damage_weight + set.set_bonus.minion_slots*minion_slots_weight)
            combo_scores.append((helm.defense*defense_weight + helm.damage*damage_weight + helm.crit*crit_weight + helm.movement*movement_weight + helm.melee_damage*melee_damage_weight + 
                helm.melee_crit*melee_crit_weight + helm.melee_speed*melee_speed_weight + helm.ranged_damage*ranged_damage_weight + helm.ranged_crit*ranged_crit_weight + 
                helm.magic_damage*magic_damage_weight + helm.magic_crit*magic_crit_weight + helm.mana*mana_weight + helm.summon_damage*summon_damage_weight + 
                helm.minion_slots*minion_slots_weight + chest.defense*defense_weight + chest.damage*damage_weight + chest.crit*crit_weight + chest.movement*movement_weight + chest.melee_damage*melee_damage_weight + 
                chest.melee_crit*melee_crit_weight + chest.melee_speed*melee_speed_weight + chest.ranged_damage*ranged_damage_weight + chest.ranged_crit*ranged_crit_weight + 
                chest.magic_damage*magic_damage_weight + chest.magic_crit*magic_crit_weight + chest.mana*mana_weight + chest.summon_damage*summon_damage_weight + 
                chest.minion_slots*minion_slots_weight + leg.defense*defense_weight + leg.damage*damage_weight + leg.crit*crit_weight + leg.movement*movement_weight + leg.melee_damage*melee_damage_weight + 
                leg.melee_crit*melee_crit_weight + leg.melee_speed*melee_speed_weight + leg.ranged_damage*ranged_damage_weight + leg.ranged_crit*ranged_crit_weight + 
                leg.magic_damage*magic_damage_weight + leg.magic_crit*magic_crit_weight + leg.mana*mana_weight + leg.summon_damage*summon_damage_weight + 
                leg.minion_slots*minion_slots_weight + set_bonus_score, (copy(helm), copy(chest), copy(leg)), set_bonus_score))


# Sort the combo_scores list based on descending scores
combo_scores.sort(key=lambda x: x[0])

# Output message
for i in combo_scores:
        print(i[0], i[1][0].name, i[1][1].name, i[1][2].name, i[2])


print(f'\n{combo_scores[-1][1][0].name}, {combo_scores[-1][1][1].name}, and {combo_scores[-1][1][2].name} give the highest score of {combo_scores[-1][0]}, given class is set to {target_class} and target stat is set to {target_stat}. This combination gives the following stats: \n')

for piece in combo_scores[-1][1]:
    print('\n', piece.name)
    for attr in dir(piece):
        if type(getattr(piece, attr)) == int and getattr(piece, attr) != 0 and attr != 'set_identifier':
            print(getattr(piece, attr), attr)