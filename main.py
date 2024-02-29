import customtkinter as tk
from PIL import Image
import armor
import calamity_armor

# Define global variables
calamity = False
target_class = 'Melee'
game_stage = 'Pre-Boss'
stat_weights = 'Balanced'
show_detailed_stats = False
class_specific_expanded = False
world_evil = 'Corruption and Crimson'
exclude_redundant = True


class_specific_traits = {
    'Melee': 'Melee Speed',
    'Ranged': None,
    'Magic': 'Mana',
    'Summoner': 'Minion Slots'
}

stat_weight_presets = {
    'Balanced': {
        'defense_weight': .5,
        'damage_weight': 1,
        'crit_weight': 1,
        'movement_weight': .2,
        'melee_damage_weight': 1,
        'melee_crit_weight': 1,
        'melee_speed_weight': 1,
        'ranged_damage_weight': 0, 
        'ranged_crit_weight': 0,
        'magic_damage_weight': 0,
        'magic_crit_weight': 0,
        'mana_weight': 0,
        'summoner_damage_weight': 0,
        'minion_slots_weight': 0
    },
    'Damage-focused': {
        'defense_weight': 0,
        'damage_weight': 1,
        'crit_weight': 1,
        'movement_weight': .2,
        'melee_damage_weight': 1,
        'melee_crit_weight': 1,
        'melee_speed_weight': 1,
        'ranged_damage_weight': 0, 
        'ranged_crit_weight': 0,
        'magic_damage_weight': 0,
        'magic_crit_weight': 0,
        'mana_weight': 0,
        'summoner_damage_weight': 0,
        'minion_slots_weight': 0
    },
    'Defense-focused': {
        'defense_weight': 1,
        'damage_weight': .5,
        'crit_weight': .5,
        'movement_weight': .1,
        'melee_damage_weight': .5,
        'melee_crit_weight': .5,
        'melee_speed_weight': .5,
        'ranged_damage_weight': 0, 
        'ranged_crit_weight': 0,
        'magic_damage_weight': 0,
        'magic_crit_weight': 0,
        'mana_weight': 0,
        'summoner_damage_weight': 0,
        'minion_slots_weight': 0
    },
}

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


# Main Calculation
def main():
    combo_scores = []
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

    print(output)


# Other Menu Functions

def toggle_calamity():
    global calamity
    calamity = not calamity
    if calamity:
        calamity_button.configure(text='Enabled')
    else:
        calamity_button.configure(text='Disabled')


def update_class(updated_class):
    global target_class
    target_class = updated_class
    if type(class_specific_traits[updated_class]) == str:
        class_specific_slider_label.configure(text=class_specific_traits[updated_class])
        class_specific_slider_label.grid(row=4, column=1, pady=10, sticky='w')
        class_specific_slider.grid(row=4, column=2, padx=10, pady=10, sticky='ew')
        class_specific_number.grid(row=4, column=1, sticky='e')
    else:
        class_specific_slider_label.grid_forget()
        class_specific_slider.grid_forget()
        class_specific_number.grid_forget()

def update_stage(updated_stage):
    global game_stage
    game_stage = updated_stage

def update_stat_weight_preset(updated_weight_preset):
    global stat_weights
    stat_weights = updated_weight_preset

def damage_slider_update(damage_weight):
    damage_number.configure(text=round(damage_weight, 1))

def dropdown_all_toggle():
    global show_detailed_stats
    show_detailed_stats = not show_detailed_stats

def defense_slider_update(defense_weight):
    defense_number.configure(text=round(defense_weight, 1))

def movement_slider_update(movement_weight):
    movement_number.configure(text=round(movement_weight, 1))

def class_specific_slider_update(class_specific_weight):
    class_specific_number.configure(text=round(class_specific_weight, 1))

def create_preset():
    global stat_weights, stat_weight_presets
    if len(preset_name.get()) == 0:
        weight_presets.append(f'Custom Preset {len(weight_presets) - 2}')
    else:
        if preset_name.get() not in weight_presets:
            weight_presets.append(preset_name.get())
        else:
            modifier = 2
            altered_name = preset_name.get() + f' ({modifier})'
            while altered_name in weight_presets:
                altered_name = preset_name.get() + f' ({modifier})'
                modifier += 1
            weight_presets.append(altered_name)
    balance_selection.configure(values=weight_presets)
    stat_weights = weight_presets[-1]
    stat_weight_presets.update({weight_presets[-1]: {
        'damage_weight': damage_slider.get(),
        'defense_weight': defense_slider.get(),
        'movement_weight': movement_slider.get()
    }})

def update_weights():
    pass

def update_world_evil():
    global world_evil
    if world_evil == 'Corruption and Crimson':
        world_evil = 'Corruption Only'
    elif world_evil == 'Corruption Only':
        world_evil = 'Crimson Only'
    elif world_evil == 'Crimson Only':
        world_evil = 'Corruption and Crimson'
    world_evil_button.configure(text=world_evil)

def update_redundant_armor():
    global exclude_redundant
    exclude_redundant = not exclude_redundant
    if exclude_redundant:
        redundant_armor_button.configure(text='Excluded')
    else:
        redundant_armor_button.configure(text='Included')



# Menu Setup
root = tk.CTk()
root.title("What are you lookin' at!")
tk.set_appearance_mode("dark")
tk.set_default_color_theme("./color_themes/DaynNight(custom).json")
root_size = root_width, root_height = 1440, 810
root.geometry(f'{root_width}x{root_height}')
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.rowconfigure((0, 1, 3), weight=1)
root.rowconfigure(2, weight=10)

dropdown_caret = Image.open("./guiAssets/down_caret.png")
add_icon = Image.open("./guiAssets/plus_icon.png")

andy_title = tk.CTkFont(family='Andy Bold', size=60)
andy_header1 = tk.CTkFont(family='Andy Bold', size=40)
andy_header2 = tk.CTkFont(family='Andy Bold', size=30)
andy_header3 = tk.CTkFont(family='Andy Bold', size=20)
andy_subtitle = tk.CTkFont(family='Andy Bold', size=15)

title = tk.CTkLabel(root, text='Armor Optimization Tool', font=andy_title)
title.grid(row=0, column=0)


frame1 = tk.CTkFrame(root, corner_radius=20)
frame1.grid(row=1, column=0, padx=10, sticky='nesw')
frame1.columnconfigure(0, weight=5)
frame1.columnconfigure(1, weight=1)
frame1.rowconfigure((0, 1, 2), weight=1)

calamity_label = tk.CTkLabel(frame1, text='Calamity Mod', font=andy_header1)
calamity_label.grid(column=0, row=0, padx=10, pady=10, sticky='w')

calamity_button = tk.CTkButton(frame1, text='Disabled', font=andy_header2, command=toggle_calamity)
calamity_button.grid(column=1, row=0, padx=50, pady=10, sticky='e')

class_label = tk.CTkLabel(frame1, text='Class', font=andy_header1)
class_label.grid(column=0, row=1, padx=10, pady=10, sticky='w')

classes = ['Melee', 'Ranged', 'Magic', 'Summoner']
class_selection = tk.CTkOptionMenu(frame1, width=270, anchor='center', dynamic_resizing=False, values=classes, font=andy_header2, dropdown_font=andy_header3, command=update_class)
class_selection.grid(column=1, row=1, padx=50, pady=10, sticky='ew')

stage_label = tk.CTkLabel(frame1, text='Stage', font=andy_header1)
stage_label.grid(column=0, row=2, padx=10, pady=10, sticky='w')

stages = ['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 'Pre-Mech Bosses', 'Post-First Mech Boss', 'Pre-Plantera', 'Pre-Golem', 
                'Pre-Lunatic Cultist', 'Endgame']
stage_selection = tk.CTkOptionMenu(frame1, width=270, anchor='center', dynamic_resizing=False, values=stages, font=andy_header2, dropdown_font=andy_header3)
stage_selection.grid(column=1, row=2, padx=50, pady=10, sticky='ew')


frame2 = tk.CTkFrame(root, corner_radius=20)
frame2.grid(row=2, column=0, padx=10, pady=10, sticky='nesw')
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=5)
frame2.columnconfigure(2, weight=1)
frame2.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

balance_label = tk.CTkLabel(frame2, text='Stat Weighting', font=andy_header1)
balance_label.grid(row=0, column=1, pady=10, sticky='w')

weight_presets = ['Balanced', 'Damage-focused', 'Defense-focused']
balance_selection = tk.CTkOptionMenu(frame2, width=270, anchor='center', dynamic_resizing=False, values=weight_presets, font=andy_header2, dropdown_font=andy_header3, command=update_stat_weight_preset)
balance_selection.grid(row=0, column=2, padx=50, pady=10, sticky='ew')

damage_label = tk.CTkLabel(frame2, text='Damage', font=andy_header1,)
damage_label.grid(row=1, column=1, pady=10, sticky='w')

damage_slider = tk.CTkSlider(frame2, from_=0, to=1, number_of_steps=10, height=20, command=damage_slider_update)
damage_slider.grid(row=1, column=2, padx=10, pady=10, sticky='ew')

damage_number = tk.CTkLabel(frame2, text='0.5', font=andy_subtitle)
damage_number.grid(row=1, column=1, sticky='e')

defense_label = tk.CTkLabel(frame2, text='Defense', font=andy_header1)
defense_label.grid(row=2, column=1, pady=10, sticky='w')

defense_slider = tk.CTkSlider(frame2, from_=0, to=1, number_of_steps=10, height=20, command=defense_slider_update)
defense_slider.grid(row=2, column=2, padx=10, pady=10, sticky='ew')

defense_number = tk.CTkLabel(frame2, text='0.5', font=andy_subtitle)
defense_number.grid(row=2, column=1, sticky='e')

movement_label = tk.CTkLabel(frame2, text='Movement', font=andy_header1,)
movement_label.grid(row=3, column=1, pady=10, sticky='w')

movement_slider = tk.CTkSlider(frame2, from_=0, to=1, number_of_steps=10, height=20, command=movement_slider_update)
movement_slider.grid(row=3, column=2, padx=10, pady=10, sticky='ew')

movement_number = tk.CTkLabel(frame2, text='0.5', font=andy_subtitle)
movement_number.grid(row=3, column=1, sticky='e')

class_specific_slider_label = tk.CTkLabel(frame2, text='Melee Speed', font=andy_header1)
class_specific_slider_label.grid(row=4, column=1, pady=10, sticky='w')

class_specific_slider = tk.CTkSlider(frame2, from_=0, to=1, number_of_steps=10, height=20, command=class_specific_slider_update)
class_specific_slider.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

class_specific_number = tk.CTkLabel(frame2, text='0.5', font=andy_subtitle)
class_specific_number.grid(row=4, column=1, sticky='e')

dropdown_all = tk.CTkButton(frame2, text='Show Detailed Stats', font=andy_subtitle, width=0, height=0, fg_color='transparent', image=tk.CTkImage(dropdown_caret), command=dropdown_all_toggle)
dropdown_all.grid(row=5, column=1, sticky='w')

create_preset_button = tk.CTkButton(frame2, height= 40, border_width=0, text='Set Current As Preset', font=andy_header2, corner_radius=0, command=create_preset)
create_preset_button.grid(row=6, column=1, pady=10, sticky='e')

preset_name = tk.CTkEntry(frame2, width=300, height=40, border_width=0, placeholder_text='Input your preset name here', font=andy_subtitle, corner_radius=0)
preset_name.grid(row=6, column=2, pady=10, sticky='w')


frame3 = tk.CTkFrame(root, corner_radius=20)
frame3.grid(row=0, column=1, padx=10, pady=10, rowspan=3, sticky='nesw')
frame3.columnconfigure(0, weight=5)
frame3.columnconfigure(1, weight=1)
frame3.rowconfigure((0, 1, 2), weight=1)
frame3.rowconfigure(3, weight=10)

world_evil_label = tk.CTkLabel(frame3, text='World Evil', font=andy_header2)
world_evil_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

world_evil_button = tk.CTkButton(frame3, width=200, text='Corruption and Crimson', font=andy_header3, command=update_world_evil)
world_evil_button.grid(column=1, row=0, padx=50, pady=10, sticky='e')

redundant_armor_label = tk.CTkLabel(frame3, text='Redundant Armor', font=andy_header2)
redundant_armor_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

redundant_armor_button = tk.CTkButton(frame3, text='Excluded', font=andy_header3, command=update_redundant_armor)
redundant_armor_button.grid(row=1, column=1, padx=50, pady=10, sticky='e')

excluded_armor_label = tk.CTkLabel(frame3, text='Excluded Armor', font=andy_header2)
excluded_armor_label.grid(row=2, column=0, columnspan=2, sticky='s')

excluded_armor_output = tk.CTkTextbox(frame3, corner_radius=0, state='disabled')
excluded_armor_output.grid(row=3, column=0, columnspan=2, padx=5, sticky='nesw')

excluded_armor_input = tk.CTkEntry(frame3, placeholder_text='Add more sets to exclude here', font=andy_subtitle)
excluded_armor_input.grid(row=4, column=0, padx=50, pady=10, columnspan=2, sticky='new')

exclude_armor_add = tk.CTkButton(frame3, width=0, height=0, fg_color='#a9b8c4', bg_color='#a9b8c4', text='', image=tk.CTkImage(add_icon, size=(16, 16)))
exclude_armor_add.grid(row=4, column=1, padx=60, sticky='e')


calculate_button = tk.CTkButton(root, corner_radius=20, text='Calculate', border_color="#586b78", border_width=1, font=andy_header1, command=main)
calculate_button.grid(row=3, column=0, padx=50, pady=5, columnspan=2, sticky='nesw')

root.mainloop()
