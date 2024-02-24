import customtkinter as tk
from PIL import Image
import armor
import calamity_armor

calamity = False
redundant_armor = False

# Set the target class and stats to maximize
target_stat = 'Balanced'
target_class = 'Melee'
game_stage = 'Pre-Boss'


vanilla_stage_tranlsation = {
    'Pre-Boss': 0,
    'Pre-Brain of Cthulhu/Eater of Worlds': 1,
    'Pre-World Evil Boss': 1,
    'Pre-Skeletron': 2,
    'Pre-Wall of Flesh': 3,
    'Pre-Mech Bosses': 4,
    'Post-First Mech Boss': 5,
    'Pre-Plantera': 6,
    'Pre-Golem': 7,
    'Pre-Lunatic Cultist': 8,
    'Endgame': 9
}


calamity_stage_tranlsation = {
    'Pre-Boss': 0,
    'Pre-Brain of Cthulhu/Eater of Worlds': 1,
    'Pre-World Evil Boss': 1,
    'Pre-Perforators/Hive Mind': 2,
    'Pre-Skeletron': 3,
    'Pre-Wall of Flesh': 4,
    'Pre-Mech Bosses': 5,
    'Post-Mech Boss 1': 6,
    'Post-Mech Boss 2': 7,
    'Pre-Plantera': 8,
    'Pre-Calamitas Clone/Plantera': 8,
    'Pre-Golem': 9,
    'Pre-Lunatic Cultist': 10,
    'Pre-Lunar Events': 10,
    'Pre-Moon Lord': 11,
    'Pre-Providence': 12,
    'Pre-Polterghast': 13, 
    'Pre-Devourer of Gods': 14, 
    'Pre-Yharon': 15,
    'Pre-Exo Mechs/Supreme Witch, Calamitas': 16, 
    'Endgame': 17
}


root = tk.CTk()
root.title("What are you lookin' at!")
root_width, root_height = (1440, 810)
root.geometry(f'{root_width}x{root_height}')
tk.set_appearance_mode("dark")
tk.set_default_color_theme("./color_themes/DaynNight.json")

title = tk.CTkLabel(root, text='Armor Optimization Tool', font=('Andy Bold', 60))
title.place(relx=.1, rely=.02)

frame1_width, frame1_height = root_width*.6, root_height*.32
frame1 = tk.CTkFrame(root, width=frame1_width, height=frame1_height, corner_radius=20)
frame1.place(relx=.02, rely=.12)

calamity_toggle = tk.CTkButton(frame1, width=frame1_width*.9, height=frame1_height*.30, corner_radius=50)
calamity_toggle.place(relx=.05, rely=.05)

class_label = tk.CTkLabel(frame1, text='Class', font=('Andy Bold', 40))
class_label.place(relx=.02, rely=.4)

classes = ['Melee', 'Ranged', 'Magic', 'Summoner', 'Mixed']
class_selection = tk.CTkOptionMenu(frame1, values=classes, width=frame1_width*.4, font=('Andy Bold', 20))
class_selection.place(relx=.5, rely=.45)

stage_label = tk.CTkLabel(frame1, text='Stage', font=('Andy Bold', 40))
stage_label.place(relx=.02, rely=.7)

stages = ['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 'Pre-Mech Bosses', 'Post-First Mech Boss', 'Pre-Plantera', 'Pre-Golem', 
                'Pre-Lunatic Cultist', 'Endgame']
stage_selection = tk.CTkOptionMenu(frame1, values=stages, width=frame1_width*.4, font=('Andy Bold', 20))
stage_selection.place(relx=.5, rely= .75)

frame2_width, frame2_height = root_width*.6, root_height*.485
frame2 = tk.CTkFrame(root, width=frame2_width, height=frame2_height, corner_radius=20)
frame2.place(relx=.02, rely=.48)

balance_label = tk.CTkLabel(frame2, text='Stat Weighting', font=('Andy Bold', 40))
balance_label.place(relx=.02, rely=.05)

weight_presets = ['Balanced', 'Damage-focused', 'Defense-focused']
balance_selection = tk.CTkOptionMenu(frame2, values=weight_presets, width=frame2_width*.4, font=('Andy Bold', 20))
balance_selection.place(relx = .5, rely=.08)

frame3_width, frame3_height = root_width*.33, root_height*.94
frame3 = tk.CTkFrame(root, width=frame3_width, height=frame3_height, corner_radius=20)
frame3.place(relx=.65, rely=.03)

root.mainloop()


# Loop through every combination and append to combo_scores along with weighted score
def main(self):
    sets_to_remove = {}
    if calamity:
        filtered_sets = calamity_armor.armor_sets.copy()

        if not redundant_armor:
            sets_to_remove = {calamity_armor.PinkSnowSet, calamity_armor.AncientHallowedSet}
        filtered_sets.difference_update(sets_to_remove)

        for set in filtered_sets.copy():
            if calamity_stage_tranlsation[set.stage] > calamity_stage_tranlsation[game_stage]:
                filtered_sets.remove(set)
    else:
        filtered_sets = armor.armor_sets.copy()

        if not redundant_armor:
            sets_to_remove = {armor.PinkSnowSet, armor.AncientCobaltSet, armor.AncientHallowedSet}
        filtered_sets.difference_update(sets_to_remove)

        for set in filtered_sets.copy():
            if vanilla_stage_tranlsation[set.stage] > vanilla_stage_tranlsation[game_stage]:
                filtered_sets.remove(set)

    combo_scores = []
    # Assign weight values to each stat based on target stat and target class
    if target_stat == 'Balanced':
        defense_weight, damage_weight, crit_weight, movement_weight = .5, 1, 1, .2
        if target_class == 'Melee':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        elif target_class == 'Ranged':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0
        elif target_class == 'Magic':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, 0, 0, 0, 1, 1, .05, 0, 0, 0, 0, 0
        elif target_class == 'Summoner':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, .33, 0, 0, 0, 0, 0, 1, 25, 0, 0, 0
        elif target_class == 'Rogue':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, .1
        elif target_class == 'Mixed':
            melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 1, 1, 1, 1, 1, 1, 1, .05, 1, 25, 1, 1, .1

    for set in filtered_sets:
        for set2 in filtered_sets:
            for set3 in filtered_sets:
                if hasattr(set, 'helmets') and hasattr(set2, 'chestplates') and hasattr(set3, 'leggings'):
                    for helm in set.helmets:
                        for chest in set2.chestplates:
                            helmet_score, chestplate_score, leggings_score, set_bonus_score = 0, 0, 0, 0
                            if hasattr(set, 'helmets'):
                                helmet_score = (helm.defense*defense_weight + helm.damage*damage_weight + helm.crit*crit_weight + helm.movement*movement_weight + helm.melee_damage*melee_damage_weight + 
                                    helm.melee_crit*melee_crit_weight + helm.melee_speed*melee_speed_weight + helm.ranged_damage*ranged_damage_weight + helm.ranged_crit*ranged_crit_weight + 
                                    helm.magic_damage*magic_damage_weight + helm.magic_crit*magic_crit_weight + helm.mana*mana_weight + helm.summon_damage*summon_damage_weight + 
                                    helm.minion_slots*minion_slots_weight)
                                if calamity:
                                    helmet_score += helm.rogue_damage*rogue_damage_weight + helm.rogue_crit*rogue_crit_weight + helm.stealth*stealth_weight
                            if hasattr(set2, 'chestplates'):
                                chestplate_score = (chest.defense*defense_weight + chest.damage*damage_weight + chest.crit*crit_weight + chest.movement*movement_weight + chest.melee_damage*melee_damage_weight + 
                                    chest.melee_crit*melee_crit_weight + chest.melee_speed*melee_speed_weight + chest.ranged_damage*ranged_damage_weight + chest.ranged_crit*ranged_crit_weight + 
                                    chest.magic_damage*magic_damage_weight + chest.magic_crit*magic_crit_weight + chest.mana*mana_weight + chest.summon_damage*summon_damage_weight + 
                                    chest.minion_slots*minion_slots_weight)
                                if calamity:
                                    chestplate_score += chest.rogue_damage*rogue_damage_weight + chest.rogue_crit*rogue_crit_weight + chest.stealth*stealth_weight
                            if hasattr(set3, 'leggings'):
                                leggings_score = (set3.leggings.defense*defense_weight + set3.leggings.damage*damage_weight + set3.leggings.crit*crit_weight + set3.leggings.movement*movement_weight + set3.leggings.melee_damage*melee_damage_weight + 
                                    set3.leggings.melee_crit*melee_crit_weight + set3.leggings.melee_speed*melee_speed_weight + set3.leggings.ranged_damage*ranged_damage_weight + set3.leggings.ranged_crit*ranged_crit_weight + 
                                    set3.leggings.magic_damage*magic_damage_weight + set3.leggings.magic_crit*magic_crit_weight + set3.leggings.mana*mana_weight + set3.leggings.summon_damage*summon_damage_weight + 
                                    set3.leggings.minion_slots*minion_slots_weight)
                                if calamity:
                                    leggings_score += set3.leggings.rogue_damage*rogue_damage_weight + set3.leggings.rogue_crit*rogue_crit_weight + set3.leggings.stealth*stealth_weight
                            if hasattr(set, 'helmets') and hasattr(set2, 'chestplates') and hasattr(set3, 'leggings'):
                                if helm.set_identifier == chest.set_identifier == set3.leggings.set_identifier or helm.set_identifier == chest.set_identifier == 87:   # if combo is a full set, calculate the set_bonus score
                                    if set.set_bonus != None:
                                        set_bonus_score += (set.set_bonus.defense*defense_weight +
                                            set.set_bonus.damage*damage_weight + set.set_bonus.crit*crit_weight + set.set_bonus.movement*movement_weight + 
                                            set.set_bonus.melee_damage*melee_damage_weight + set.set_bonus.melee_crit*melee_crit_weight + set.set_bonus.melee_speed*melee_speed_weight + 
                                            set.set_bonus.ranged_damage*ranged_damage_weight + set.set_bonus.ranged_crit*ranged_crit_weight + 
                                            set.set_bonus.magic_damage*magic_damage_weight + set.set_bonus.magic_crit*magic_crit_weight + set.set_bonus.mana*mana_weight + 
                                            set.set_bonus.summon_damage*summon_damage_weight + set.set_bonus.minion_slots*minion_slots_weight)
                                        if calamity:
                                            set_bonus_score += set.set_bonus.rogue_damage*rogue_damage_weight + set.set_bonus.rogue_crit*rogue_crit_weight + set.set_bonus.stealth*stealth_weight
                                    if helm.set_bonus != None:
                                        set_bonus_score += (helm.set_bonus.defense*defense_weight +
                                            helm.set_bonus.damage*damage_weight + helm.set_bonus.crit*crit_weight + helm.set_bonus.movement*movement_weight + 
                                            helm.set_bonus.melee_damage*melee_damage_weight + helm.set_bonus.melee_crit*melee_crit_weight + helm.set_bonus.melee_speed*melee_speed_weight + 
                                            helm.set_bonus.ranged_damage*ranged_damage_weight + helm.set_bonus.ranged_crit*ranged_crit_weight + 
                                            helm.set_bonus.magic_damage*magic_damage_weight + helm.set_bonus.magic_crit*magic_crit_weight + helm.set_bonus.mana*mana_weight + 
                                            helm.set_bonus.summon_damage*summon_damage_weight + helm.set_bonus.minion_slots*minion_slots_weight)
                                        if calamity:
                                            set_bonus_score += helm.set_bonus.rogue_damage*rogue_damage_weight + helm.set_bonus.rogue_crit*rogue_crit_weight + helm.set_bonus.stealth*stealth_weight
                                    if chest.set_bonus != None:
                                        set_bonus_score += (chest.set_bonus.defense*defense_weight +
                                            chest.set_bonus.damage*damage_weight + chest.set_bonus.crit*crit_weight + chest.set_bonus.movement*movement_weight + 
                                            chest.set_bonus.melee_damage*melee_damage_weight + chest.set_bonus.melee_crit*melee_crit_weight + chest.set_bonus.melee_speed*melee_speed_weight + 
                                            chest.set_bonus.ranged_damage*ranged_damage_weight + chest.set_bonus.ranged_crit*ranged_crit_weight + 
                                            chest.set_bonus.magic_damage*magic_damage_weight + chest.set_bonus.magic_crit*magic_crit_weight + chest.set_bonus.mana*mana_weight + 
                                            chest.set_bonus.summon_damage*summon_damage_weight + chest.set_bonus.minion_slots*minion_slots_weight)
                                        if calamity:
                                            set_bonus_score += chest.set_bonus.rogue_damage*rogue_damage_weight + chest.set_bonus.rogue_crit*rogue_crit_weight + chest.set_bonus.stealth*stealth_weight  
                            
                            total_score = helmet_score + chestplate_score + leggings_score + set_bonus_score
                            if type(set_bonus_score) == float:
                                combo_scores.append((total_score, (helm, chest, set3.leggings), set))
                            else:
                                combo_scores.append((total_score, (helm, chest, set3.leggings), None))     


    # Sort the combo_scores list based on descending scores
    combo_scores.sort(key=lambda x: x[0])

    # Output message
    output = f'\n{combo_scores[-1][1][0].name}, {combo_scores[-1][1][1].name}, and {combo_scores[-1][1][2].name} give the highest score of {combo_scores[-1][0]}, given class is set to {target_class} and stage of game is set to {game_stage}. This combination gives the following stats:\n'

    for piece in combo_scores[-1][1]:
        output += f'\n\n{piece.name}'
        for attr in dir(piece):     # Regular piece attributes
            if type(getattr(piece, attr)) == int and getattr(piece, attr) != 0 and attr != 'set_identifier':
                output += f'\n{getattr(piece, attr)} {attr}'
        if len(piece.ability) > 0:      # Regular piece abilities
            output += f'\n{piece.ability}'


    if combo_scores[-1][2] != None:
        output += '\n\n Set Bonus'
        for piece in combo_scores[-1][1]:
            for attr in dir(piece.set_bonus):       # Set bonus piece specific attribute
                if type(getattr(piece.set_bonus, attr)) == int and getattr(piece.set_bonus, attr) != 0 and attr != 'set_identifier':
                    output += f'\n{getattr(piece.set_bonus, attr)} {attr}'
            if piece.set_bonus != None:
                if len(piece.set_bonus.ability) > 0:      # Set bonus piece specific abilities
                    output += f'\n{piece.set_bonus}'

        if combo_scores[-1][2] != None:
            for attr in dir(combo_scores[-1][2].set_bonus):     # Full set bonus attributes
                if type(getattr(combo_scores[-1][2].set_bonus, attr)) == int and getattr(combo_scores[-1][2].set_bonus, attr) != 0 and attr != 'set_identifier':
                        output += f'\n{getattr(combo_scores[-1][2].set_bonus, attr)} {attr}'
            if combo_scores[-1][2].set_bonus != None:
                if len(combo_scores[-1][2].set_bonus.ability) > 0:      # Full set bonus abilities
                    output += f'\n{combo_scores[-1][2].set_bonus.ability}'

    # for score in combo_scores:
    #     print(f'\n{score[0]}, {score[1][0].name}, {score[1][1].name}, {score[1][2].name}')


