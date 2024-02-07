import customtkinter as tk
import armor
import calamity_armor

calamity = False
redundant_armor = False

# Set the target class and stats to maximize
target_stat = 'balance'
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


class MyGUI:

    def __init__(self):

        self.root = tk.CTk()
        self.root.title("What are you lookin' at!")
        self.root_width, self.root_height = (1920, 1080)
        self.root.geometry(f'{self.root_width}x{self.root_height}')
        tk.set_appearance_mode("dark")

        self.titleLabel = tk.CTkLabel(self.root, width=500, height=70, corner_radius=20, text='Armor Optimization Tool', font=('Garamond', 28), text_color='#006699')
        self.titleLabel.pack()

        self.mainFrame = tk.CTkFrame(self.root, width=700, height=500, fg_color='#37515f')
        self.mainFrame.pack()

        stages = ['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 'Pre-Mech Bosses', 'Post-First Mech Boss', 'Pre-Plantera', 'Pre-Golem', 
                      'Pre-Lunatic Cultist', 'Endgame']
        self.stageOptionMenu = tk.CTkOptionMenu(self.mainFrame, values=stages, fg_color='#0093E9', dropdown_fg_color='#0093E9', command=self.change_stage)
        self.stageOptionMenu.grid(row=0, column=0, padx=10, pady=10)

        classes = ['Melee', 'Ranged', 'Magic', 'Summoner']
        self.classOptionMenu = tk.CTkOptionMenu(self.mainFrame, values=classes, fg_color='#0093E9', dropdown_fg_color='#0093E9', command=self.change_class)
        self.classOptionMenu.grid(row=1, column=0, padx=10, pady=10)

        self.redarmButton = tk.CTkButton(self.mainFrame, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Exclude Redundant Armors', command=self.toggle_redundant_armor)
        self.redarmButton.grid(row=2, column=0, padx=10, pady=10)

        self.calamityButton = tk.CTkButton(self.mainFrame, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Vanilla', command=self.toggle_calamity)
        self.calamityButton.grid(row=3, column=0, padx=10, pady=10)

        self.calculateButton = tk.CTkButton(self.mainFrame,  width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Calculate', command=self.main)
        self.calculateButton.grid(row=4, column=0, padx=100, pady=10)

        self.output = 'Usage instructions: Select your current class and stage of the game from the dropdowns above. Then, you may also choose to include redundant armor or Calamity mod armor. \nPress Calculate. Enjoy! Please note that depending on your hardware, the program may take a few seconds to calculate.'
        self.outputTextbox = tk.CTkLabel(self.root, width=800, height=100, text=self.output)
        self.outputTextbox.pack()

        self.root.mainloop()
    
    def change_class(self, val):
        global target_class
        target_class = val

    def change_stage(self, val):
        global game_stage
        game_stage = val

    def toggle_redundant_armor(self):
        global redundant_armor
        redundant_armor = not redundant_armor
        if redundant_armor:
            self.redarmButton.configure(text='Include Redundant Armor')
        else:
            self.redarmButton.configure(text='Exclude Redundant Armor')

    def toggle_calamity(self):
        global calamity
        calamity = not calamity
        if calamity:
            self.calamityButton.configure(text='Calamity')
            stages = ['Pre-Boss', 'Pre-Brain of Cthulhu/Eater of Worlds', 'Pre-Perforators/Hive Mind', 'Pre-Skeletron', 'Pre-Wall of Flesh', 'Pre-Mech Bosses', 
                      'Post-Mech Boss 1', 'Post-Mech Boss 2', 'Pre-Calamitas Clone/Plantera', 'Pre-Golem', 'Pre-Lunar Events', 'Pre-Moon Lord', 'Pre-Providence',
                      'Pre-Polterghast', 'Pre-Devourer of Gods', 'Pre-Yharon', 'Pre-Exo-Mechs/Supreme Witch', 'Pre-Calamitas', 'Endgame']
            classes = ['Melee', 'Ranged', 'Magic', 'Summoner', 'Rogue']

        else:
            self.calamityButton.configure(text='Vanilla')
            stages = ['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 'Pre-Mech Bosses', 'Post-First Mech Boss', 'Pre-Plantera', 'Pre-Golem', 
                      'Pre-Lunatic Cultist', 'Endgame']
            classes = ['Melee', 'Ranged', 'Magic', 'Summoner']
        self.stageOptionMenu.configure(values=stages)
        self.classOptionMenu.configure(values=classes)

    def update_output(self, text):
        self.outputTextbox.configure(text=text)

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
        if target_stat == 'balance':
            defense_weight, damage_weight, crit_weight, movement_weight = 1, 1, 1, .1
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
                    mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, 0, 0, 0, 0, 0, 0, 1, 30, 0, 0, 0
            elif target_class == 'Rogue':
                melee_damage_weight, melee_crit_weight, melee_speed_weight, ranged_damage_weight, ranged_crit_weight, magic_damage_weight, magic_crit_weight, \
                    mana_weight, summon_damage_weight, minion_slots_weight, rogue_damage_weight, rogue_crit_weight, stealth_weight = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, .1


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
        #     output += f'\n{score[0]}, {score[1][0].name}, {score[1][1].name}, {score[1][2].name}'

        self.update_output(output)


main = MyGUI()
