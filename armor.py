class Armor:
    def __init__(self, set_identifier, name, defense, damage, crit, movement, melee_damage, melee_crit, melee_speed, ranged_damage, ranged_crit, 
                 magic_damage, magic_crit, mana, summon_damage, minion_slots, ability):
        self.set_identifier = set_identifier
        self.name = name
        self.defense = defense
        self.damage = damage
        self.crit = crit
        self.movement = movement
        self.melee_damage = melee_damage
        self.melee_crit = melee_crit
        self.melee_speed = melee_speed
        self.ranged_damage = ranged_damage
        self.ranged_crit = ranged_crit
        self.magic_damage = magic_damage
        self.magic_crit = magic_crit
        self.mana = mana
        self.summon_damage = summon_damage
        self.minion_slots = minion_slots
        self.ability = ability     # As a string


class MiningSet_mining:
    helmet = Armor(0, 'Mining Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Provides light when worn')
    chestplate = Armor(0, 'Mining Shirt', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    leggings = Armor(0, 'Mining Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    set_bonus = Armor(0, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    stage = 'Pre-Boss'

class MiningSet_ultrabright:
    helmet = Armor(1, 'Ultrabright Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Improves vivsion and provides light when worn')
    chestplate = Armor(1, 'Mining Shirt', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    leggings = Armor(1, 'Mining Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    set_bonus = Armor(1, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed')
    stage = 'Pre-Boss'

class WoodSet:
    helmet = Armor(2, 'Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(2, 'Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(2, 'Wood Greaves', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(2, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class MahoganySet:
    helmet = Armor(3, 'Rich Mahogany Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(3, 'Rich Mahogany Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(3, 'Rich Mahogany Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(3, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class BorealSet:
    helmet = Armor(4, 'Boreal Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(4, 'Boreal Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(4, 'Boreal Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(4, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class PalmSet:
    helmet = Armor(5, 'Palm Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(5, 'Palm Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(5, 'Palm Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(5, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class EbonwoodSet:
    helmet = Armor(6, 'Ebonwood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(6, 'Ebonwood Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(6, 'Ebonwood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(6, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class ShadewoodSet:
    helmet = Armor(7, 'Shadewood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(7, 'Shadewod Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(7, 'Shadewood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(7, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class AshWoodSet:
    helmet = Armor(8, 'Ash Wood Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(8, 'Ash Wood Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(8, 'Ash Wood Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(8, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class RainSet:
    helmet = Armor(9, 'Rain Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(9, 'Rain Coat', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(9, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(9, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class SnowSet:
    helmet = Armor(10, 'Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(10, 'Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(10, 'Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(10, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be frozen or chilled')
    stage = 'Pre-Boss'

class PinkSnowSet:
    helmet = Armor(11, 'Pink Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(11, 'Pink Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(11, 'Pink Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(11, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be frozen or chilled')
    stage = 'Pre-Boss'

class AnglerSet:
    helmet = Armor(12, 'Angler Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5')
    chestplate = Armor(12, 'Angler Vest', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5')
    leggings = Armor(12, 'Angler Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5')
    set_bonus = Armor(12, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Decreased enemy spawn rate')
    stage = 'Pre-Boss'

class CactusSet:
    helmet = Armor(13, 'Cactus Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(13, 'Cactus Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(13, 'Cactus Leggings', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(13, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attackers take damage from the cactus spikes')
    stage = 'Pre-Boss'

class CopperSet:
    helmet = Armor(14, 'Copper Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(14, 'Copper Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(14, 'Copper Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(14, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class TinSet:
    helmet = Armor(15, 'Tin Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(15, 'Tin Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(15, 'Tin Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(15, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class PumpkinSet:
    helmet = Armor(16, 'Pumpkin Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(16, 'Pumpkin Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(16, 'Pumpkin Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(16, '', 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class NinjaSet:
    helmet = Armor(17, 'Ninja Hood', 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(17, 'Ninja Shirt', 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(17, 'Ninja Pants', 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(17, '', 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class IronSet:
    helmet = Armor(18, 'Iron Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(18, 'Iron Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(18, 'Iron Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(18, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'
   
class LeadSet:
    helmet = Armor(19, 'Lead Helmet', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(19, 'Lead Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(19, 'Lead Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(19, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss' 

class SilverSet:
    helmet = Armor(20, 'Silver Helmet', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(20, 'Silver Chainmail', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(20, 'Silver Greaves', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(20, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class TungstenSet:
    helmet = Armor(21, 'Tungsten Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(21, 'Tungsten Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(21, 'Tungsten Greaves', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(21, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class GoldSet:
    helmet = Armor(22, 'Gold Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(22, 'Gold Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(22, 'Gold Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(22, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class PlatinumSet:
    helmet = Armor(23, 'Platinum Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(23, 'Platinum Chainmail', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(23, 'Platinum Greaves', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(23, '', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Boss'

class FossilSet:
    helmet = Armor(24, 'Fossil Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, '')
    chestplate = Armor(24, 'Fossil Plate', 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(24, 'Fossil Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(24, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo')
    stage = 'Pre-Boss'

class BeeSet:
    helmet = Armor(25, 'Bee Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, '')
    chestplate = Armor(25, 'Bee Breastplate', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, '')
    leggings = Armor(25, 'Bee Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, '')
    set_bonus = Armor(25, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, '')
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class ObsidianSet:
    helmet = Armor(26, 'Obsidian Outlaw Hat', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, '')
    chestplate = Armor(26, 'Obsidian Longcoat', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '')
    leggings = Armor(26, 'Obsidian Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, '')
    set_bonus = Armor(26, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 'Increases whip range by 30%')
    stage = 'Pre-Skeletron'

class GladiatorSet:
    helmet = Armor(27, 'Gladiator Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(27, 'Gladiator Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(27, 'Gladiator Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(27, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants immunity to knockback')
    stage = 'Pre-Boss'

class MeteorSet:
    helmet = Armor(28, 'Meteor Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '')
    chestplate = Armor(28, 'Meteor Suit', 6, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '')
    leggings = Armor(28, 'Meteor Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, '')
    set_bonus = Armor(28, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Space Gun costs 0 mana')
    stage = 'Pre-Skeletron'

class JungleSet:
    helmet = Armor(29, 'Jungle Hat', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, '')
    chestplate = Armor(29, 'Jungle Shirt', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, '')
    leggings = Armor(29, 'Jungle Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, '')
    set_bonus = Armor(29, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs')
    stage = 'Pre-Boss'

class AncientCobaltSet:
    helmet = Armor(30, 'Ancient Cobalt Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, '')
    chestplate = Armor(30, 'Ancient Cobalt Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, '')
    leggings = Armor(30, 'Ancient Cobalt Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, '')
    set_bonus = Armor(30, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs')
    stage = 'Pre-Boss'

class NecroSet:
    helmet = Armor(31, 'Necro Helmet', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(31, 'Necro Breastplate', 7, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(31, 'Necro Greaves', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(31, '', 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, '')
    stage = 'Pre-Wall of Flesh'

class ShadowSet:
    helmet = Armor(32, 'Shadow Helmet', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(32, 'Shadow Scalemail', 7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(32, 'Shadow Greaves', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(32, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '75% increase to player acceleration and 1.15x player max movement speed')
    stage = 'Pre-Skeletron'

class AncientShadowSet:
    helmet = Armor(33, 'Ancient Shadow Helmet', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(33, 'Ancient Shadow Scalemail', 7, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(33, 'Ancient Shadow Greaves', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(33, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '75% increase to player acceleration and 1.15x player max movement speed')
    stage = 'Pre-Boss'

class CrimsonSet:
    helmet = Armor(34, 'Crimson Helmet', 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(34, 'Crimson Scalemail', 7, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(34, 'Crimsow Greaves', 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(34, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increased life regen')
    stage = 'Pre-Skeletron'

class MoltenSet:
    helmet = Armor(35, 'Molten Helmet', 8, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, '')
    chestplate = Armor(35, 'Molten Breastplate', 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, '')
    leggings = Armor(35, 'Molten Greaves', 8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, '')
    set_bonus = Armor(35, '', 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Cannot be set on fire')
    stage = 'Pre-Skeletron'

stage_tranlsation = {
    'Pre-Boss': 0,
    'Pre-Brain of Cthulhu/Eater of Worlds': 1,
    'Pre-Skeletron': 2,
    'Pre-Wall of Flesh': 3,
    'Pre-Mech Bosses': 4,
    'Pre-Plantera': 5,
    'Pre-Golem': 6,
    'Pre-Lunatic Cultist': 7,
    'Post-Moon Lord': 8
}


game_stage = 'Post-Moon Lord'

mining1 = MiningSet_mining
mining2 = MiningSet_ultrabright
wood = WoodSet
rich_mahogany = MahoganySet
boreal = BorealSet
palm = PalmSet
ebonwood = EbonwoodSet
shadewood = ShadewoodSet
ashwood = AshWoodSet
rain = RainSet
snow = SnowSet
pink_snow = PinkSnowSet
angler = AnglerSet
cactus = CactusSet
copper = CopperSet
tin = TinSet
pumpkin = PumpkinSet
ninja = NinjaSet
iron = IronSet
lead = LeadSet
silver = SilverSet
tungsten = TungstenSet
gold = GoldSet
platinum = PlatinumSet
fossil = FossilSet
bee = BeeSet
obsidian = ObsidianSet
gladiator = GladiatorSet
meteor = MeteorSet
jungle = JungleSet
ancient_cobalt = AncientCobaltSet
necro = NecroSet
shadow = ShadowSet
ancient_shadow = AncientShadowSet
crimson = CrimsonSet
molten = MoltenSet

armor_sets = [mining1, mining2, wood, rich_mahogany, boreal, palm, ebonwood, shadewood, ashwood, rain, snow, pink_snow, angler, cactus, copper, tin, pumpkin, 
              ninja, iron, lead, silver, tungsten, gold, platinum, fossil, bee, obsidian, gladiator, meteor, jungle, ancient_cobalt, necro, shadow, ancient_shadow,
              crimson, molten]

helmets = []
chestplates = []
leggings = []

for set in armor_sets:
    if stage_tranlsation[set.stage] > stage_tranlsation[game_stage]:
        armor_sets.remove(set)
    else:
        helmets.append(set.helmet)
        chestplates.append(set.chestplate)
        leggings.append(set.leggings)