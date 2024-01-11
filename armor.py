import gc

class Armor:
    def __init__(self, set_identifier, slot, defense, damage, crit, movement, summon_capacity, ability):
        self.set_identifier = set_identifier
        self.slot = slot    # 0 --> helmet, 1 --> chestplate, 2 --> leggings
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.summon_capacity = summon_capacity
        self.ability = ability     # As a string
        

class ArmorSet:
    def __init__(self)
        
        
copper_set = (Armor(0, 0, 1, 0, 0, 0, 0, ''), Armor(0, 1, 2, 0, 0, 0, 0, ''), Armor(0, 2, 1, 0, 0, 0, 0, ''), [1, 0, 0, 0, 0, ''])

platinum_set = (Armor(1, 0, 4, 10, 5, 0, 0, ''), Armor(1, 1, 5, 0, 0, 0, 0, ''), Armor(1, 2, 4, 0, 0, 0, 0, ''), [5, 0, 0, 0, 0, 'For each 10 defense, you gain .01 damage'])



helmets = []
chestplates = []
leggings = []

for obj in gc.get_objects():
    if isinstance(obj, Armor):
        if obj.slot == 0:
            helmets.append(obj)
        elif obj.slot == 1:
            chestplates.append(obj)
        elif obj.slot == 2:
            leggings.append(obj)

print(helmets)
print(helmets[0])
