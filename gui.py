import customtkinter as tk


class myGUI:

    def __init__(self):

        self.root = tk.Tk(className='armorOptimizationTool')

        self.calamityLabel = tk.Label(self.root, text='Included Armor Sets')
        self.calamityLabel.pack()

        stage_options = [
            'Pre-Boss',
            'Pre-World Evil Boss',
            'Pre-Skeletron',
            'Pre-Wall of Flesh',
            'Pre-Mech Bosses',
            'Pre-Plantera',
            'Pre-Golem',
            'Pre-Lunar Events',
            'Endgame'
        ]

        stage_selected = tk.StringVar()
        stage_selected.set('Endgame') 
        self.stageOptionMenu = tk.OptionMenu(self.root, stage_selected, *stage_options)
        self.stageOptionMenu.pack()

        class_options = [
            'Melee',
            'Ranged',
            'Magic',
            'Summoner'
        ]

        class_selected = tk.StringVar()
        class_selected.set('Melee')
        self.classOptionMenu = tk.OptionMenu(self.root, class_selected, *class_options)
        self.classOptionMenu.pack()

        self.calamity_state = tk.BooleanVar()
        self.calamity_state.set(False)
        self.calamityButton = tk.Button(self.root, text=str(self.calamity_state.get()), width=25, command=self.toggle_calamity)
        self.calamityButton.pack()

        self.redarm_state = tk.BooleanVar()
        self.redarmButton = tk.Button(self.root, text=str(self.redarm_state.get()), width=25, command=self.toggle_redundant_armor)
        self.redarmButton.pack()

        self.root.mainloop()

    def toggle_calamity(self):
        self.calamity_state.set(not self.calamity_state.get())
        self.calamityButton.configure(text=str(self.calamity_state.get()))

    def toggle_redundant_armor(self):
        self.redarm_state.set(not self.redarm_state.get())
        self.redarmButton.configure(text=str(self.redarm_state.get()))


myGUI()