import gc

class Armor:
    def __init__(self, set_identifier, slot, defense, damage, crit, movement, summon_capacity, ability, set_bonus):
        self.set_identifier = set_identifier
        self.slot = slot    # 0 --> helmet, 1 --> chestplate, 2 --> leggings
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.summon_capacity = summon_capacity
        self.ability = ability     # As a string
        self.set_bonus = set_bonus     # As a list containing all other stats included in Armor class except slot
        
copper_helmet = Armor(0, 0, 1, 0, 0, 0, 0, '', '1 defense')
copper_chestplate = Armor(0, 1, 2, 0, 0, 0, 0, '', '1 defense')
copper_leggings = Armor(0, 2, 1, 0, 0, 0, 0, '', '1 defense')

platinum_helmet = Armor(1, 0, 4, 10, 5, 0, 0, '', [5, 0, 0, 0, 0, 'For each 10 defense, you gain .01 damage'])
platinum_chestplate = Armor(1, 1, 5, 0, 0, 0, 0, '', [5, 0, 0, 0, 0, 'For each 10 defense, you gain .01 damage'])
platinum_leggings = Armor(1, 2, 4, 0, 0, 0, 0, '', [5, 0, 0, 0, 0, 'For each 10 defense, you gain .01 damage'])



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