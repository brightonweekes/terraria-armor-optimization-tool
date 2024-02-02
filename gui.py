import customtkinter as tk


class myGUI:

    def __init__(self):

        self.root = tk.CTk(className='armorOptimizationTool')
        self.root_width, self.root_height = (800, 600)
        self.root.geometry(f'{self.root_width}x{self.root_height}')
        tk.set_appearance_mode("dark")

        self.titleLabel = tk.CTkLabel(self.root, width=500, height=70, corner_radius=20, text='Armor Optimization Tool', font=('Garamond', 28), text_color='#006699')
        self.titleLabel.pack()

        self.mainFrame = tk.CTkFrame(self.root, width=700, height=500, fg_color='#37515f')
        self.mainFrame.pack()

        self.stageOptionMenu = tk.CTkOptionMenu(self.mainFrame, values=['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 
                                                                   'Pre-Mech Bosses', 'Pre-Plantera', 'Pre-Golem', 'Pre-Lunar Events', 'Endgame'
                                                                   ], fg_color='#0093E9', dropdown_fg_color='#0093E9')
        self.stageOptionMenu.grid(row=0, column=0, padx=10, pady=10)

        class_selected = tk.StringVar()
        class_selected.set('Melee')
        self.classOptionMenu = tk.CTkOptionMenu(self.mainFrame, values=['Melee', 'Ranged', 'Magic', 'Summoner'], fg_color='#0093E9', 
                                                dropdown_fg_color='#0093E9')
        self.classOptionMenu.grid(row=1, column=0, padx=10, pady=10)

        self.redarm_state = tk.BooleanVar()
        self.redarmButton = tk.CTkButton(self.mainFrame, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Exclude Redundant Armors', command=self.toggle_redundant_armor)
        self.redarmButton.grid(row=2, column=0, padx=10, pady=10)


        self.calamity_state = tk.BooleanVar()
        self.calamity_state.set(False)
        self.calamityButton = tk.CTkButton(self.mainFrame, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Vanilla', command=self.toggle_calamity)
        self.calamityButton.grid(row=3, column=0, padx=10, pady=10)

        self.calculateButton = tk.CTkButton(self.mainFrame,  width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text='Calculate')
        self.calculateButton.grid(row=4, column=0, padx=100, pady=10)
        self.root.mainloop()
    

    def toggle_redundant_armor(self):
        self.redarm_state.set(not self.redarm_state.get())
        if self.redarm_state.get():
            self.redarmButton.configure(text='Include Redundant Armor')
        else:
            self.redarmButton.configure(text='Exclude Redundant Armor')

    def toggle_calamity(self):
        self.calamity_state.set(not self.calamity_state.get())
        if self.calamity_state.get():
            self.calamityButton.configure(text='Calamity')
        else:
            self.calamityButton.configure(text='Vanilla')


myGUI()