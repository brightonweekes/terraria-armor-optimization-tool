import customtkinter as tk


class myGUI:

    def __init__(self):

        self.root = tk.CTk(className='armorOptimizationTool')
        self.root_width, self.root_height = (800, 600)
        self.root.geometry(f'{self.root_width}x{self.root_height}')
        tk.set_appearance_mode("dark")

        self.calamityLabel = tk.CTkLabel(self.root, text='Included Armor Sets', font=('Arial', 20), text_color='#FFCC70')
        self.calamityLabel.place(relx=.1, rely=.1, anchor='center')


        self.stageOptionMenu = tk.CTkOptionMenu(self.root, values=['Pre-Boss', 'Pre-World Evil Boss', 'Pre-Skeletron', 'Pre-Wall of Flesh', 
                                                                   'Pre-Mech Bosses', 'Pre-Plantera', 'Pre-Golem', 'Pre-Lunar Events', 'Endgame'
                                                                   ], fg_color='#0093E9', dropdown_fg_color='#0093E9')
        self.stageOptionMenu.pack()

        

        class_selected = tk.StringVar()
        class_selected.set('Melee')
        self.classOptionMenu = tk.CTkOptionMenu(self.root, values=['Melee', 'Ranged', 'Magic', 'Summoner'], fg_color='#0093E9', 
                                                dropdown_fg_color='#0093E9')
        self.classOptionMenu.place(relx=.6, rely=.6, anchor='center')

        self.calamityLabel = tk.CTkLabel(self.root)

        self.calamity_state = tk.BooleanVar()
        self.calamity_state.set(False)
        self.calamityButton = tk.CTkButton(self.root, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text=str(self.calamity_state.get()), command=self.toggle_calamity)
        self.calamityButton.place(relx=.5, rely=.6, anchor='center')

        self.redarm_state = tk.BooleanVar()
        self.redarmButton = tk.CTkButton(self.root, width=140, height=28, corner_radius=50, fg_color='#C850C0', hover_color='#4158D0', text=str(self.redarm_state.get()), command=self.toggle_redundant_armor)
        self.redarmButton.pack()

        self.root.mainloop()

    def toggle_calamity(self):
        self.calamity_state.set(not self.calamity_state.get())
        self.calamityButton.configure(text=str(self.calamity_state.get()))

    def toggle_redundant_armor(self):
        self.redarm_state.set(not self.redarm_state.get())
        self.redarmButton.configure(text=str(self.redarm_state.get()))


myGUI()