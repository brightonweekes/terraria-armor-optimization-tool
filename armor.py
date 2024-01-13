class Armor:
    def __init__(self, name, defense, damage, crit, movement, ability):
        self.name = name
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.ability = ability     # As a string
        

# Game stages in order: Pre-Boss, Pre-Brain of Cthulhu/Eater of Worlds, Pre-Perforators/Hive Mind, Pre-Skeletron, Pre-Wall of Flesh
        
class CopperSet:
    helmet = Armor('copper helmet', 1, 0, 0, 0, '')
    chestplate = Armor('copper chestplate', 2, 0, 0, 0, '')
    leggings = Armor('copper leggings', 1, 0, 0, 0, '')
    set_bonus = Armor('', 1, 0, 0, 0, '')
    stage = 'Pre-Boss'


class PlatinumSet:
    helmet = Armor('platinum helmet', 4, 10, 5, 0, '')
    chestplate = Armor('platinum chestplate', 6, 0, 0, 0, '')
    leggings = Armor('platinum leggings', 4, 0, 0, 0, '')
    set_bonus = Armor('', 5, 0, 0, 0, 'For each 10 defense, you gain .01 damage')
    stage = 'Pre-Boss'


class MoltenSet:
    helmet = Armor('molten helmet', 8, 0, 0, 0, '')
    chestplate = Armor('molten chestplate', 0, 7, 0, 0, '')
    leggings = Armor('motlen leggings', 1, 0, 0, 0, '')
    set_bonus = Armor('', 8, 0, 0, 0, '')
    stage = 'Pre-Skeletron'


copper = CopperSet()
platinum = PlatinumSet()
molten = MoltenSet()

armor_sets = {copper, platinum, molten}

helmets = []
chestplates = []
leggings = []

for set in armor_sets:
    helmets.append(set.helmet)
    chestplates.append(set.chestplate)
    leggings.append(set.leggings)
