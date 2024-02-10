class Armor:
    def __init__(self, set_identifier, name, defense, damage, crit, movement, melee_damage, melee_crit, melee_speed, ranged_damage, ranged_crit, 
                 magic_damage, magic_crit, mana, summon_damage, minion_slots, rogue_damage, rogue_crit, stealth, ability, set_bonus):
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
        self.rogue_damage = rogue_damage
        self.rogue_crit = rogue_crit
        self.stealth = stealth
        self.ability = ability     # As a string
        self.set_bonus = set_bonus      # Set bonuses linked to a specific piece of armor will be put here (i.e. the beetle scale mail gives a different set bonus than the beetle shell)


class MiningSet:
    helmets = [Armor(0, 'Mining Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Provides light when worn', None), Armor(0, 'Ultrabright Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  'Improves vivsion and provides light when worn', None)]
    chestplates = [Armor(0, 'Mining Shirt', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed', None)]
    leggings = Armor(0, 'Mining Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed', None)
    set_bonus = Armor(0, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased mining speed\n25% chance for an additional ore to drop when mined, with a cooldown of 3-6 seconds', None)
    stage = 'Pre-Boss'

class WoodSet:
    helmets = [Armor(2, 'Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(2, 'Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(2, 'Wood Greaves', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(2, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class MahoganySet:
    helmets = [Armor(3, 'Rich Mahogany Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(3, 'Rich Mahogany Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  '', None)]
    leggings = Armor(3, 'Rich Mahogany Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(3, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class BorealSet:
    helmets = [Armor(4, 'Boreal Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(4, 'Boreal Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, '', None)]
    leggings = Armor(4, 'Boreal Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(4, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class PalmSet:
    helmets = [Armor(5, 'Palm Wood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(5, 'Palm Wood Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(5, 'Palm Wood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(5, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class EbonwoodSet:
    helmets = [Armor(6, 'Ebonwood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(6, 'Ebonwood Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(6, 'Ebonwood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(6, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class ShadewoodSet:
    helmets = [Armor(7, 'Shadewood Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(7, 'Shadewod Breastplate', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(7, 'Shadewood Greaves', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(7, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class AshWoodSet:
    helmets = [Armor(8, 'Ash Wood Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(8, 'Ash Wood Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'', None)]
    leggings = Armor(8, 'Ash Wood Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(8, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class RainSet:
    helmets = [Armor(9, 'Rain Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(9, 'Rain Coat', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    set_bonus = Armor(9, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class SnowSet:
    helmets = [Armor(10, 'Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(10, 'Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(10, 'Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(10, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Multiplies all cold-based debuff damage by 1.25\nCold enemies dealreduced contact damage to the player\nCannot be frozen or chilled', None)
    stage = 'Pre-Boss'

class PinkSnowSet:
    helmets = [Armor(10, 'Pink Snow Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(10, 'Pink Snow Coat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(10, 'Pink Snow Pants', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(10, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Multiplies all cold-based debuff damage by 1.25\nCold enemies dealreduced contact damage to the player\nCannot be frozen or chilled',  None)
    stage = 'Pre-Boss'

class AnglerSet:
    helmets = [Armor(12, 'Angler Hat', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)]
    chestplates = [Armor(12, 'Angler Vest', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)]
    leggings = Armor(12, 'Angler Pants', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases fishing power by 5', None)
    set_bonus = Armor(12, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Decreased enemy spawn rate', None)
    stage = 'Pre-Boss'

class CactusSet:
    helmets = [Armor(13, 'Cactus Helmet', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(13, 'Cactus Breastplate', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(13, 'Cactus Leggings', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(13, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attackers take damage from the cactus spikes', None)
    stage = 'Pre-Boss'

class CopperSet:
    helmets = [Armor(14, 'Copper Helmet', 1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(14, 'Copper Chainmail', 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(14, 'Copper Greaves', 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(14, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+2 to all damage', None)
    stage = 'Pre-Boss'

class TinSet:
    helmets = [Armor(15, 'Tin Helmet', 2, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(15, 'Tin Chainmail', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1 life regen', None)]
    leggings = Armor(15, 'Tin Greaves', 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(15, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+5 armor penetration', None)
    stage = 'Pre-Boss'

class PumpkinSet:
    helmets = [Armor(16, 'Pumpkin Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(16, 'Pumpkin Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(16, 'Pumpkin Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(16, '', 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Boss'

class NinjaSet:
    helmets = [Armor(17, 'Ninja Hood', 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(17, 'Ninja Shirt', 4, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(17, 'Ninja Pants', 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(17, '', 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class IronSet:
    helmets = [Armor(18, 'Iron Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)]
    chestplates = [Armor(18, 'Iron Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)]
    leggings = Armor(18, 'Iron Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)
    set_bonus = Armor(18, '', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces damage taken by 6%\n+2 life regen', None)
    stage = 'Pre-Boss'
   
class LeadSet:
    helmets = [Armor(19, 'Lead Helmet', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)]
    chestplates = [Armor(19, 'Lead Chainmail', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)]
    leggings = Armor(19, 'Lead Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduce damage taken by 3%', None)
    set_bonus = Armor(19, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces damage taken by 3%\n+1 life regen\n grants knockback immunity', None)
    stage = 'Pre-Boss' 

class SilverSet:
    helmets = [Armor(20, 'Silver Helmet', 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(20, 'Silver Chainmail', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+2 life regen', None)]
    leggings = Armor(20, 'Silver Greaves', 3, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(20, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 life regen\nTwo seconds after being hit for 20 or more damage, heal for 10 health; getting hit again during this time will reset the timer', None)
    stage = 'Pre-Boss'

class TungstenSet:
    helmets = [Armor(21, 'Tungsten Helmet', 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(21, 'Tungsten Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 life regen', None)]
    leggings = Armor(21, 'Tungsten Greaves', 3, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(21, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases all knockback by 33%\nIncreases critical strike chance by 100% of the knockback of your currently held weapon, capped at +10% critical strike', None)
    stage = 'Pre-Boss'

class GoldSet:
    helmets = [Armor(22, 'Gold Helmet', 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(22, 'Gold Chainmail', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces damage taken by 5%', None)]
    leggings = Armor(22, 'Gold Greaves', 4, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '',  None)
    set_bonus = Armor(22, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'All enemies have a 4% chance to drop 1 more gold coin, while all bosses killed always drop 3 more\nGain 1% increased critical strike chance for every 5 gold in your inventory, capped at 10%', None)
    stage = 'Pre-Boss'

class PlatinumSet:
    helmets = [Armor(23, 'Platinum Helmet', 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(23, 'Platinum Chainmail', 6, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(23, 'Platinum Greaves', 5, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(23, '', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Every 10 defense grants +1 life regen, 1% damage, and 1% increased critical strike chance, capping at 40 defense', None)
    stage = 'Pre-Boss'

class FossilSet:
    helmets = [Armor(24, 'Fossil Helmet', 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(24, 'Fossil Plate', 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(24, 'Fossil Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(24, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)
    stage = 'Pre-Boss'

class BeeSet:
    helmets = [Armor(25, 'Bee Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, '', None)]
    chestplates = [Armor(25, 'Bee Breastplate', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, '', None)]
    leggings = Armor(25, 'Bee Greaves', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', None)
    set_bonus = Armor(25, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class ObsidianSet:
    helmets = [Armor(26, 'Obsidian Outlaw Hat', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(26, 'Obsidian Longcoat', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, '', None)]
    leggings = Armor(26, 'Obsidian Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, '', None)
    set_bonus = Armor(26, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 'Increases whip range by 30%\nGrants immunity to fire blocks and temporary immunity to lava', None)
    stage = 'Pre-Skeletron'

class GladiatorSet:
    helmets = [Armor(27, 'Gladiator Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, '', None)]
    chestplates = [Armor(27, 'Gladiator Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, '', None)]
    leggings = Armor(27, 'Gladiator Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '3% increased rogue velocity', None)
    set_bonus = Armor(27, '', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 60, '10% increased rogue velocity', None)
    stage = 'Pre-Boss'

class MeteorSet:
    helmets = [Armor(28, 'Meteor Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(28, 'Meteor Suit', 6, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(28, 'Meteor Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(28, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Space Gun mana costs reduced by 50%', None)
    stage = 'Pre-Skeletron'

class JungleSet:
    helmets = [Armor(29, 'Jungle Hat', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(29, 'Jungle Shirt', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(29, 'Jungle Pants', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(29, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs', None)
    stage = 'Pre-Boss'

class AncientCobaltSet:
    helmets = [Armor(29, 'Ancient Cobalt Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 40, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(29, 'Ancient Cobalt Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 20, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(29, 'Ancient Cobalt Leggings', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 20, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(29, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '16% reduced mana costs', None)
    stage = 'Pre-Boss'

class NecroSet:
    helmets = [Armor(31, 'Necro Helmet', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(31, 'Necro Breastplate', 7, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(31, 'Necro Greaves', 6, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(31, '', 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 'Allows you to temporarily survive fatal damage. When this triggers, health is completely refilled, but all healing is disabled and health will drain rapidly until killing the player after at most 7 seconds.', None)
    stage = 'Pre-Wall of Flesh'

class ShadowSet:
    helmets = [Armor(32, 'Shadow Helmet', 6, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)]
    chestplates = [Armor(32, 'Shadow Scalemail', 7, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)]
    leggings = Armor(32, 'Shadow Greaves', 6, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)
    set_bonus = Armor(32, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '15% increased max movement speed and acceleration', None)
    stage = 'Pre-Skeletron'

class AncientShadowSet:
    helmets = [Armor(32, 'Ancient Shadow Helmet', 6, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)]
    chestplates = [Armor(32, 'Ancient Shadow Scalemail', 7, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)]
    leggings = Armor(32, 'Ancient Shadow Greaves', 6, 5, 5, 0, 0, 0, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '7% increased jump speed', None)
    set_bonus = Armor(32, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '15% increased max movement speed and acceleration', None)
    stage = 'Pre-Boss'

class CrimsonSet:
    helmets = [Armor(34, 'Crimson Helmet', 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 life regen', None)]
    chestplates = [Armor(34, 'Crimson Scalemail', 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 life regen', None)]
    leggings = Armor(34, 'Crimsow Greaves', 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 life regen', None)
    set_bonus = Armor(34, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increased life regen', None)
    stage = 'Pre-Skeletron'

class MoltenSet:
    helmets = [Armor(35, 'Molten Helmet', 8, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(35, 'Molten Breastplate', 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(35, 'Molten Greaves', 8, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(35, '', 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% true melee damage\nGrants immunity to fire blocks and temporary immunity to lava', None)
    stage = 'Pre-Skeletron'

class PearlwoodSet:
    helmets = [Armor(36, 'Pearlwood Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(36, 'Pearlwood Breastplate', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(36, 'Pearlwood Greaves', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(36, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    stage = 'Pre-Mech Bosses'

class SpiderSet:
    helmets = [Armor(37, 'Spider Mask', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 0, 0, '', None)]
    chestplates = [Armor(37, 'Spider Breastplate', 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0, 0, 0, '', None)]
    leggings = Armor(37, 'Spider Greaves', 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0, 0, '', None)
    set_bonus = Armor(37, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, '', None)
    stage = 'Pre-Mech Bosses'

class CobaltSet:
    helmets = [Armor(38, 'Cobalt Helmet', 14, 0, 0, 10, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(38, '', 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(38, 'Cobalt Mask', 5, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(38, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)), Armor(38, 'Cobalt Hat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 40, 0, 0, 0, 0, 0, '', set_bonus = Armor(40, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '14% reduced mana costs', None))]
    chestplates = [Armor(38, 'Cobalt Breastplate', 10, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(38, 'Cobalt Leggings', 8, 3, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(38, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased max speed and acceleration. Gain damage and critical strike chance boost based on your current movement speed, up to 10% each', None)
    stage = 'Pre-Mech Bosses'

class PalladiumSet:
    helmets = [Armor(41, 'Palladium Mask', 15, 0, 0, 0, 12, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(41, 'Palladium Helmet', 8, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(41, 'Palladium Headgear', 5, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 60, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(41, 'Palladium Breastplate', 13, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(41, 'Palladium Leggings', 11, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(41, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increases life regeneration after striking an enemy', None)
    stage = 'Pre-Mech Bosses'

class MythrilSet:
    helmets = [Armor(44, 'Mythril Helmet', 16, 0, 0, 0, 10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(44, 'Mythril Hat', 6, 0, 0, 0, 0, 0, 0, 12, 7, 0, 0, 0, 0, 0, 0, 0, 0, '',  set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)), Armor(44, 'Mythril Hood', 3, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 80, 0, 0, 0, 0, 0, '',  set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '17% reduced mana costs', None))]
    chestplates = [Armor(44, 'Mythril Chainmail', 12, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(44, 'Mythril Greaves', 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(44, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemy hits release Mythril flares, which home in on enemies after a short delay. Mythril flares deal 40% of the damage of the attack that spawned them, softcapped at 50 damage, and have a 12 frame delay before another can be spawned', None)
    stage = 'Post-Mech Boss 1'

class OrichalcumSet:
    helmets = [Armor(47, 'Orichalcum Mask', 22, 0, 0, 7, 11, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(47, 'Orichalcum Helmet', 10, 0, 0, 8, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(47, 'Orichalcum Headgear', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 80, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(47, 'Orichalcum Breastplate', 16, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(47, 'Orichalcum Leggings', 14, 8, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(47, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Flower petals will fall on your target for extra damage', None)
    stage = 'Post-Mech Boss 1'

class AdamantiteSet:
    helmets = [Armor(50, 'Adamantite Helmet', 22, 0, 0, 0, 14, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 20, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(50, 'Adamantite Mask', 8, 0, 0, 0, 0, 0, 0, 14, 10, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '25% chance to save ammo', None)), Armor(50, 'Adamantite Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 100, 0, 0, 0, 0, 0, '', set_bonus = Armor(50, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '19% reduced mana costs', None))]
    chestplates = [Armor(50, 'Adamantite Breastplate', 16, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(50, 'Adamantite Leggings', 12, 0, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(50, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Half your damage reduction is added to your critical strike chance. Continuously doing damage grants an increasing amount of defense, up to 15. This defense decays while not dealing damage and can be affected by defense damage.', None)
    stage = 'Post-Mech Boss 2'

class TitaniumSet:
    helmets = [Armor(53, 'Titanium Mask', 23, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(53, 'Titanium Helmet', 8, 0, 0, 0, 0, 0, 0, 16, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(53, 'Titanium Headgear', 4, 0, 0, 0, 0, 0, 0, 0, 0, 16, 7, 100, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(53, 'Titanium Breastplate', 15, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(53, 'Titanium Leggings', 11, 3, 3, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(53, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attacking generates a defensive barrier of titanium shards', None)
    stage = 'Post-Mech Boss 2'

class CrystalAssassinSet:
    helmets = [Armor(56, 'Crystal Assassin Hood', 12, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% reduced mana cost', None)]
    chestplates = [Armor(56, 'Crystal Assassin Shirt', 14, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% chance to save ammo', None)]
    leggings = Armor(56, 'Crystal Assassin Pants', 10, 0, 0, 20, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(56, '', 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Allows the ability to dash', None)
    stage = 'Pre-Mech Bosses'

class FrostSet:
    helmets = [Armor(57, 'Frost Helmet', 10, 0, 0, 0, 16, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(57, 'Frost Breastplate', 20, 0, 0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(57, 'Frost Leggings', 13, 0, 0, 8, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(57, '', 0, 0, 0, 0, 10, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Melee and ranged attacks inflict Frostbite. 15% increased damage which scales based on how far the target is from you. Closer range grants melee damage, while farther range grants ranged damage', None)
    stage = 'Pre-Mech Bosses'

class ForbiddenSet:
    helmets = [Armor(58, 'Forbidden Mask', 6, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 15, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(58, 'Forbidden Robes', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 10, 1, 0, 0, 0, '', None)]
    leggings = Armor(58, 'Forbidden Treads', 8, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 40, 0, 1, 0, 0, 0, '', None)
    set_bonus = Armor(58, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Double tap to call an ancient storm to cursor location', None)
    stage = 'Pre-Mech Bosses'

class SquireSet:
    helmets = [Armor(59, "Squire's Great Helm", 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 'Decreases life regeneration by 1', None)]
    chestplates = [Armor(59, "Squire's Plating", 27, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)]
    leggings = Armor(59, "Squire's Greaves", 18, 0, 0, 15, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', None)
    set_bonus = Armor(59, '', 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 15, 1, 0, 0, 0, 'Ballista pierces more targets and panics when you take damage\nIncreases life regen by 2', None)
    stage = 'Pre-Plantera'

class MonkSet:
    helmets = [Armor(60, "Monk's Bushy Brow Bald Cap", 8, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, '', None)]
    chestplates = [Armor(60, "Monk's Shirt", 22, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)]
    leggings = Armor(60, "Monk's Pants", 16, 0, 0, 20, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', None)
    set_bonus = Armor(60, '', 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 15, 1, 0, 0, 0, 'Lightning Aura can now crit and strikes faster', None)
    stage = 'Pre-Plantera'

class HuntressSet:
    helmets = [Armor(61, "Huntress's Wig", 7, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 1, 0, 0, 0, '', None)]
    chestplates = [Armor(61, "Huntress's Jerkin", 17, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 0, 0, 0, 0, '10% chance to save ammo', None)]
    leggings = Armor(61, "Huntress's Pants", 12, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)
    set_bonus = Armor(61, '', 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 1, 0, 0, 0, 'Explosive Traps recharge faster and oil enemies\nSet oiled enemies on fire for extrs damage', None)
    stage = 'Pre-Plantera'

class ApprenticeSet:
    helmets = [Armor(62, "Apprentice's Hat", 7, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 1, 0, 0, 0, '10% reduced mana cost', None)]
    chestplates = [Armor(62, "Apprentice's Robe", 15, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 20, 0, 0, 0, 0, '', None)]
    leggings = Armor(62, "Apprentice's Trousers", 10, 0, 0, 20, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, '', None)
    set_bonus = Armor(62, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 5, 1, 0, 0, 0, 'FLameburst field of view and range are dramatically increased', None)
    stage = 'Pre-Plantera'

class HallowedSet:
    helmets = [Armor(63, 'Hallowed Mask', 24, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(63, 'Hallowed Helmet', 9, 0, 0, 0, 0, 0, 0, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(63, 'Hallowed Headgear', 5, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 100, 0, 0, 0, 0, 0, '', None), Armor(63, 'Hallowed Hood', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, '', set_bonus = Armor(66, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '',  None))]
    chestplates = [Armor(63, 'Hallowed Plate Mail', 18, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(63, 'Hallowed Greaves', 13, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(63, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Become immune after striking an enemy', None)
    stage = 'Pre-Calamitas Clone/Plantera'

class AncientHallowedSet:
    helmets = [Armor(63, 'Ancient Hallowed Mask', 24, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(63, 'Ancient Hallowed Helmet', 9, 0, 0, 0, 0, 0, 0, 15, 8, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(63, 'Ancient Hallowed Headgear', 5, 0, 0, 0, 0, 0, 0, 0, 0, 12, 12, 100, 0, 0, 0, 0, 0, '', None), Armor(63, 'Ancient Hallowed Hood', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, '', set_bonus = Armor(66, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, '',  None))]
    chestplates = [Armor(63, 'Ancient Hallowed Plate Mail', 18, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(63, 'Ancient Hallowed Greaves', 13, 7, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(63, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Become immune after striking an enemy', None)
    stage = 'Pre-Calamitas Clone/Plantera'

class ChlorophyteSet:
    helmets = [Armor(67, 'Chlorophyte Mask', 20, 0, 0, 0, 16, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(67, 'Chlorophyte Helmet', 13, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None), Armor(67, 'Chlorophyte Headgear', 7, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 80, 0, 0, 0, 0, 0, '17% reduced mana cost', None)]
    chestplates = [Armor(67, 'Chlorophyte Plate Mail', 18, 5, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(67, 'Chlorophyte Greaves', 13, 0, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(67, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Summons a powerful leaf crystal. Every 5 seconds, releases a green, expanding ring that damages enemies for 300 damage and heals players for 10 health. Both the damage and healing amount increase with the player's strongest class damage.\nReduces damage taken by 5%", None)
    stage = 'Pre-Plantera'

class TurtleSet:
    helmets = [Armor(70, 'Turtle Helmet', 21, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    chestplates = [Armor(70, 'Turtle Scale Mail', 27, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    leggings = Armor(70, 'Turtle Leggings', 17, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)
    set_bonus = Armor(70, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Attackers also take double damage\nReduces damage taken by 15%', None)
    stage = 'Pre-Plantera'

class TikiSet:
    helmets = [Armor(71, 'Tiki Mask', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, 'Increases whip range by 10%', None)]
    chestplates = [Armor(71, 'Tiki Shirt', 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, '', None)]
    leggings = Armor(71, 'Tiki Pants', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, '', None)
    set_bonus = Armor(71, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 'Increases whip range by 20%', None)
    stage = 'Pre-Golem'

class BeetleSet:
    helmets = [Armor(72, 'Beetle Helmet', 23, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)]
    chestplates = [Armor(72, 'Beetle Scale Mail', 20, 0, 0, 6, 8, 8, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(72, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Beetles increase your melee damage and speed. Each beetle gives +10% melee damage and +5% melee speed', None)), Armor(72, 'Beetle Helmet', 23, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', set_bonus = Armor(72, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Beetles protect you from damage. Each beetle increases damage reduction by an 10%.', None))]
    leggings = Armor(72, 'Beetle Leggings', 18, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)
    set_bonus = None
    stage = 'Pre-Lunatic Cultist'

class ShroomiteSet:
    helmets = [Armor(73, 'Shroomite Headgear', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to bows', None), Armor(73, 'Shroomite Mask', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to guns', None), Armor(73, 'Shroomite Helmet', 11, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 0, 0, 0, 'Note: 15% ranged damage buff only applies to non-bow and non-gun weapons', None)]
    chestplates = [Armor(73, 'Shroomite Breastplate', 24, 0, 0, 0, 0, 0, 0, 13, 13, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to save ammo', None)]
    leggings = Armor(73, 'Shroomite Leggings', 16, 0, 0, 12, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(73, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Not moving puts you in stealth, increasing ranged ability and reducing chance to enemies to target you', None)
    stage = 'Pre-Golem'

class SpectreSet:
    helmets = [Armor(76, 'Spectre Mask', 18, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 60, 0, 0, 0, 0, 0, '13% reduced mana cost', set_bonus = Armor(76, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Magic damage done will hurt extra nearby enemies', None)), Armor(76, 'Spectre Hood', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus = Armor(77, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces magic dmage done by 20% and converts it to healing force\nMagic damage done to enemies heals the player with the lowest health', None))]
    chestplates = [Armor(76, 'Spectre Robe', 14, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(76, 'Spectre Pants', 10, 0, 0, 8, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Golem'

class SpookySet:
    helmets = [Armor(78, 'Spooky Helmet', 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1, 0, 0, 0, '', None)]
    chestplates = [Armor(78, 'Spooky Breastplate', 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 2, 0, 0, 0, '', None)]
    leggings = Armor(78, 'Spooky Leggings', 10, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1, 0, 0, 0, '', None)
    set_bonus = Armor(78, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, '', None)
    stage = 'Pre-Golem'

class ValhallaKnightSet:
    helmets = [Armor(79, "Valhalla Knight's Helm", 20, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 2, 0, 0, 0, '', None)]
    chestplates = [Armor(79, "Valhalla Knight's Breastplate", 24, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 'Increases life regen by 2', None)]
    leggings = Armor(79, "Valhalla Knight's Greaves", 24, 0, 0, 20, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)
    set_bonus = Armor(79, '', 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, 'Greatly enhances Ballista effectiveness\nIncreases life regen by 6', None)
    stage = 'Pre-Lunatic Cultist'

class ShinobiInfiltratorSet:
    helmets = [Armor(80, "Shinobi Infiltrator's Helmet", 10, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 10, 2, 0, 0, 0, '', None)]
    chestplates = [Armor(80, "Shinobi Infiltrator's Torso", 26, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)]
    leggings = Armor(80, "Shinobi Infiltrator's Pants", 18, 0, 0, 30, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)
    set_bonus = Armor(80, '', 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0, 0, 30, 1, 0, 0, 0, 'Greatly enhances Lightning Aura effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class RedRidingSet:
    helmets = [Armor(81, 'Red Riding Hood', 8, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 10, 2, 0, 0, 0, '', None)]
    chestplates = [Armor(81, 'Red Riding Dress', 24, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 15, 0, 0, 0, 0, '20% chance to save ammo', None)]
    leggings = Armor(81, 'Red Riding Leggings', 16, 0, 0, 20, 0, 0, 0, 0, 10, 0, 0, 0, 25, 0, 0, 0, 0, '', None)
    set_bonus = Armor(81, '', 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 10, 1, 0, 0, 0, 'Greatly enhances Explosive Trap effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class DarkArtistSet:
    helmets = [Armor(82, "Dark Artist's Hat", 7, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 15, 2, 0, 0, 0, '', None)]
    chestplates = [Armor(82, "Dark Artist's Robes", 21, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 25, 0, 0, 0, 0, '15% reduced mana cost', None)]
    leggings = Armor(82, "Dark Artist's Leggings", 14, 0, 0, 20, 0, 0, 0, 0, 0, 0, 10, 0, 10, 0, 0, 0, 0, '', None)
    set_bonus = Armor(82, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 10, 1, 0, 0, 0, 'Greatly enhances Flameburst effectiveness', None)
    stage = 'Pre-Lunatic Cultist'

class SolarFlareSet:
    helmets = [Armor(83, 'Solar Flare Helmet', 24, 0, 0, 0, 0, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)]
    chestplates = [Armor(83, 'Solar Flare Breastplate', 34, 0, 0, 0, 29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)]
    leggings = Armor(83, 'Solar Flare Leggings', 20, 0, 0, 15, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants minor life regeneration\nEnemies are more likely to target you', None)
    set_bonus = Armor(83, '', 0, 0, 0, 0, 0,0 ,0 ,0 ,0 ,0 , 0, 0, 0, 0, 0, 0, 0, 'Solar shields charge over time to protect you and let you dash\nA charge is used to damage enemies you touch\nConsumed carges explode and damage enemies', None)
    stage = 'Pre-Providence'

class VortexSet:
    helmets = [Armor(84, 'Vortex Helmet', 14, 0, 0, 0, 0, 0, 0, 16, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(84, 'Vortex Breastplate', 28, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 0, 0, 0, 0, 0, '25% chance to save ammo', None)]
    leggings = Armor(84, 'Vortex Leggings', 20, 0, 0, 10, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(84, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Double tap to toggle stealth, increasing ranged ability and reducing chance for enemies to target you but slowing movement speed', None)
    stage = 'Pre-Providence'

class NebulaSet:
    helmets = [Armor(85, 'Nebula Helmet', 14, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 60, 0, 0, 0, 0, 0, '15% reduced mana cost', None)]
    chestplates = [Armor(85, 'Nebula Breastplate', 18, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(85, 'Nebula Leggings', 14, 0, 0, 10, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(85, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Magic damage has a chance to spawn buff boosters, pick boosters up to get stacking buffs', None)
    stage = 'Pre-Providence'
    
class StardustSet:
    helmets = [Armor(86, 'Stardust Helmet', 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, 0, 0, 0, '', None)]
    chestplates = [Armor(86, 'Startdust Plate', 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, 0, 0, 0, 'Increases whip range by 15%', None)]
    leggings = Armor(86, 'Stardust Leggings', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 2, 0, 0, 0, 'Increases whip range by 15%', None)
    set_bonus = Armor(86, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'A stardust guardian will protect you from nearby enemies', None)
    stage = 'Pre-Providence'

class WizardSet:
    helmets = [Armor(87, 'Magic Hat', 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, '', Armor(87, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, '', None)), Armor(87, 'Wizard Hat', 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, '', Armor(87, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, '', None))]
    chestplates = [Armor(87, 'Amethyst Robe', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, '-5% mana usage', None), Armor(87, 'Topaz Robe', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, '-7% mana usage', None), Armor(87, 'Sapphire Robe', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, '-9% mana usage', None), Armor(87, 'Emerald Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, '-11% mana usage', None), Armor(87, 'Ruby Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, '-13% mana usage', None), Armor(87, 'Amber Robe', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, '-13% mana usage', None), Armor(87, 'Diamond Robe', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, '-15% mana usage', None), Armor(87, 'Mystic Robe', 2, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, '-10% mana usage', None)]
    set_bonus = None
    stage = 'Pre-Boss'

class WulfrumSet:
    helmets = [Armor(88, 'Wulfrum Hat & Goggles', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', None)]
    chestplates = [Armor(88, 'Wulfrum Jacket', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '5% increased damage reduction', None)]
    leggings = Armor(88, 'Wulfrum Overalls', 1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(88, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 'Wulfrum Bastion - Double tap DOWN while dismounted to equip wulfrum power armor', None)
    stage = 'Pre-Boss'

class SnowRuffianSet:
    helmets = [Armor(89, 'Snow Ruffian Mask', 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, '', None)]
    chestplates = [Armor(89, 'Snow Ruffian Chestplate', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, '', None)]
    leggings = Armor(89, 'Snow Ruffian Greaves', 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(89, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 50, 'You can glide to negate fall damage', None)
    stage = 'Pre-Boss'

class DesertProwlerSet:
    helmets = [Armor(90, 'Desert Prowler Hat', 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, '20% chance to not consume ammo', None)]
    chestplates = [Armor(90, 'Desert Prowler Shirt', 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(90, 'Desert Prowler Pants', 2, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Immunity to the Mighty Wind debuff', None)
    set_bonus = Armor(90, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Ranged attacks deal an extra 1 flat damage\nSandsmoke Bomb - Double tap DOWN to shroud yourself in a small cloud of sand\nWhile the sand cloud is active, gain increased mobility but heavily reduced defense\nUsing a ranged weapon instantly dispels the sand cloak, but guarantees a supercrit for 200% damage\nThe super crit applies only as long as the resulting hit would not exceed 100 damage\nLanding the killing blow on an enemy with this shot shortens the ability cooldown to 1.5 seconds', None)
    stage = 'Pre-Boss'

class MarniteArchitectSet:
    helmets = [Armor(91, 'Marnite Architect Headgear', 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases block placement range by 5', None)]
    chestplates = [Armor(91, 'Marnite Architect Toga', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increases placement speed by 50%', None)]
    set_bonus = Armor(91, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Marnite Lift - You can summon a lift under your feet to reach higher up\nThe lift gets summoned when the mount hotkey gets pressed without any mounts equipped\nUsing the ▲ Up and ▼ Down keys can change the lift's height", None)
    stage = 'Pre-Boss'

class VictideSet:
    helmets = [Armor(92, 'Victide Shellmet', 4, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(92, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you\n+1.5% life regen and 10% increased melee damage while submerged in liquid', None)), Armor(92, 'Victide Coral Turban', 3, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(92, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1.5 HP/s life regen and 10% increased ranged damage while submerged in liquid', None)), Armor(92, 'Victide Hermit Helmet', 2, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(92, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1.5 HP/s life regen and 10% increased magic damage while submerged in liquid', None)), Armor(92, 'Victide Mask', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, '', set_bonus=Armor(92, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, '+1.5 HP/s life regen and 10% increased summon damage while submerged in liquid\nSummons a sea snail to protect you', None)), Armor(92, 'Victide Headcrab', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, '', set_bonus=Armor(92, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, '+1.5 HP/s life regen and 10% increased rogue damage while submerged in liquid', None))]
    chestplates = [Armor(92, 'Victide Breastplate', 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '5% increased damage reduction\n+5 defense and 10% increased damage reduction while submerged in liquid', None)]
    leggins = Armor(92, 'Victide Greaves', 4, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Movement speed increased by 30% while submerged in liquid', None)
    set_bonus = Armor(92, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'When using any weapon you have a 10% chance to throw a returning seashell projectile\This seashell does true damage and does not benefit from any damage class\nProvides increased underwater mobility and slightly reduces breath loss in the abyss', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'

class SulphurousSet:
    helmets = [Armor(93, 'Sulphurous Helmet', 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 0, 'Grants underwater breathing', None)]
    chestplates = [Armor(93, 'Sulphurous Breastplate', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 5, 0, '', None)]
    leggings = Armor(93, 'Sulphurour Leggings', 5, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Movement speed increased by 35% while submerged in liquid', None)
    set_bonus = Armor(93, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 'Attacking and being attacked by enemies inflicts poison\nGrants an additional jump that summons a sulphurous bubble\nProvides increased underwater mobility and reduces the severity of the sulphuric waters', None)
    stage = 'Pre-Brain of Cthulhu/Eater of Worlds'
    
class AerospecSet:
    helmets = [Armor(94, 'Aerospec Helm', 7, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(94, '', 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)), Armor(94, 'Aerospec Hood', 5, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus= Armor(94, '', 0, 0, 0, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, '', None)), Armor(94, 'Aerospec Hat', 3, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 20, 0, 0, 0, 0, 0, '', set_bonus= Armor(94, '', 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, '', None)), Armor(94, 'Aerospec Helmet', 2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', set_bonus=Armor(94, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 1, 0, 0, 0, 'Summons a valkyrie to protect you', None)), Armor(94, 'Aerospec headgear', 4, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, '', set_bonus=Armor(94, '', 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 80, '', None))]
    chestplates = [Armor(94, 'Aerospec Breastplate', 7, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(94, 'Aerospec Leggings', 6, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(94, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Taking over 25 damage in one hit will cause a spread of homing feathers to fall\nAllows you to fall more quickly and disables fall damage', None)
    stage = 'Pre-Skeletron'

class StatigelSet:
    helmets = [Armor(95, 'Statigel Helm', 9, 0, 0, 0, 10, 7, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(95, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you', None)), Armor(95, 'Statigel Headgear', 7, 0, 0, 0, 0, 0, 0, 10, 7, 0, 0, 0, 0, 0, 0, 0, 0, '', None), Armor(95, 'Statigel Cap', 5, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 30, 0, 0, 0, 0, 0, '10% decreased mana cost', None), Armor(95, 'Statigel Hood', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 'Increased minion knockback', set_bonus=Armor(95, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0, 0, 0, 'Summons a mini Slime God to fight for you, the type depends on what world evil you have', None)), Armor(95, 'Statigel Mask', 6, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 7, 0, '34% chance to not consume thrown items', set_bonus=Armor(95, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, '', None))]
    chestplates = [Armor(95, 'Statigel Armor', 10, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(95, 'Statigel Greaves', 8, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(95, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'When you take over 100 damage in one hit you become immune to damage for an extended period of time\nGrants an extra jump and increased jump height\n12% increased jump speed', None)
    stage = 'Pre-Wall of Flesh'

class MolluskSet:
    helmets = [Armor(96, 'Mollusk Shellmet', 18, 5, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'You can move freely through liquids', None)]
    chestplates = [Armor(96, 'Mollusk Shellplate', 22, 10, 6, -15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(96, 'Mollusk Shelleggings', 15, 12, 4, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(96, '', 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Two shellfishes aid you in combat\nYour horizontal movement is slowed', None)
    stage = 'Pre-Mech Bosses'

class TitanHeartSet:
    helmets = [Armor(97, 'Titan Heart Mask', 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, '5% increased rogue knockback\nRogue weapons inflict the Astral Inflection debuff', None)]
    chestplates = [Armor(97, 'Titan Heart Mantle', 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '45% chance to not consume rogue items\n5% boosted rogue knockback but 15% lowered rogue attack speed', None)]
    leggings = Armor(97, 'Titan Heart Boots', 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, '10% increased rogue velocity\n5% increased rogue knockback', None)
    set_bonus = Armor(97, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 100, '15% increased rogue knockback\nStealth strikes deal double knockback and cause an astral explosion\nGrants immunity to knockback', None)
    stage = 'Pre-Mech Bosses'

class DaedalusSet:
    helmets = [Armor(98, 'Daedalus Helm', 23, 0, 0, 0, 15, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(98, '', 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you\nYou reflect projectiles back at enemies\nReflected projectiles deal 50% less damage to you\nThis reflect has a 90 second cooldown which is shared with all other dodges and reflects', None)), Armor(98, 'Daedalus Headgear', 9, 0, 0, 0, 0, 0, 0, 13, 7, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces ammo usage by 20%', set_bonus=Armor(98, '', 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Getting hit causes you to emit a blast of crystal shards', None)), Armor(98, 'Daedalus Hood', 5, 0, 0, 0, 0, 0, 0, 0, 0, 13, 7, 60, 0, 0, 0, 0, 0, '10% reduced mana usage', set_bonus=Armor(98, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, "You have a 10% chance absorb physical attacks and projectiles when hit\nIf you absorb an attack you are healed for 1/2 of that attack's damage", None)), Armor(98, 'Daedalus Mask', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '', set_bonus=Armor(98, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 2, 0, 0, 0, 'A daedalus crystal floats above you to protect you', None)), Armor(98, 'Daedalus Facemask', 7, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 7, 0, '15% increased rogue velocity', set_bonus=Armor(98, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 105, 'Rogue projectiles throw out crystal shards as they travel', None))]
    chestplates = [Armor(98, 'Daedalus Breastplate', 19, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(98, 'Daedalus Leggings', 15, 0, 3, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Calamitas Clone/Plantera'

class BrimflameSet:
    helmets = [Armor(99, 'Brimflame Cowl', 11, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 70, 0, 0, 0, 0, 0, 'Reduces mana usage by 10%\nImmunity to On Fire!, Brimstone Flames, and Frostburn', None)]
    chestplates = [Armor(99, 'Brimflame Robes', 15, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(99, 'Brimflame Boots', 15, 0, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(99, '', 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 'Press Armor Set Bonus to trigger a brimflame frenzy effect\nWhile under this effect, you get an additional 40% increase to magic damage\nHowever, this comes at the cost of rapid life loss and no mana regeneration\nThis can be toggled off, however, a brimflame frenzy has a 30 second cooldown', None)
    stage = 'Pre-Golem'

class FathomSwarmerSet:
    helmets = [Armor(100, 'Fathom Swarmer Visage',10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 'Provides breathing and light underwater', None)]
    chestplates = [Armor(100, 'Fathom Swarmer Breastplate', 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, '6% damage reduction\nIncreases defense by 10 and grants +2.5 HP/s regen while submerged in liquid\nReduces defense lost within the Abyss', None)]
    leggings = Armor(100, 'Fathom Swarmer Greaves', 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 'Grants the abiliy to swim\n<ovement speed increased by 40% while submerged in liguid', None)
    set_bonus = Armor(100, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2, 0, 0, 0, 'Grants the ability to climb walls\n30% increased summon damage while submerged in liquid\nProvides a moderate amount of light and moderately reduces breath loss in the abyss', None)
    stage = 'Pre-Golem'

class UmbraphileSet:
    helmets = [Armor(101, 'Unbraphile Hood', 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, '10% increased rogue velocity', None)]
    chestplates = [Armor(101, 'Umbraphile Regalia', 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, '', None)]
    leggings = Armor(101, 'Umbraphile Boots', 12, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 6, 0, '', None)
    set_bonus = Armor(101, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 110, 'Rogue weapons have a chance to create explosions on hit\nStealth strikes always creat an explosion', None)
    stage = 'Pre-Golem'

class ReaverSet:
    helmets = [Armor(102, 'Reaver Helm', 30, -30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, '15% increased damage reduction\n+50 max life\nRestores 1 HP/s, this applis separately from life regen', set_bonus=Armor(102, '', 10, 0, 0, -20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1.5 HP/s life regen\nEnemies are more lkely to target you\nReduces life regen lost from damage over time debuffs by 20%\n20% reduced flight time\nEnemy damage is reflected and summons a thorn spike\nReaver Rage has a 25% chance to activate when you are damaged', None)), Armor(102, 'Reaver Visage', 13, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased jump speed', set_bonus=Armor(102, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants immunity to fall damage and allows constant jumping\n10% increased flight time and horizontal wing speed\nHooks fly out and retract 10% faster\nReduces the cooldown of dashes', None)), Armor(102, 'Reaver Headgear', 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20% increased mining speed and block/wall placement speed\nGrants immunity to lava and can move freely through liquids', set_bonus=Armor(102, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ' Highlights all treasure nearby\nIncreased item grab range and block placement range\nMining tiles restores breath while underwater\nSummons a reaver orb to light up the area around you\nReduces enemy aggression, even in the abyss\nProvides a small amount of light in the abyss', None))]
    chestplates = [Armor(102, 'Reaver Scale Mail', 19, 9, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+20 max life', None)]
    leggings = Armor(102, 'Reaver Cuisses', 14, 0, 5, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = None
    stage = 'Pre-Golem'

class HydrothermicSet:
    helmets = [Armor(103, 'Hydrothermic Helm', 33, 0, 0, 0, 17, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Melee attacks and melee projectiles inflict On Fire!\n Grants immunity to fire and lava', set_bonus=Armor(103,'', 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you\nMelee attacks and projectiles cause chaos flames to erupt on enemy hits', None)), Armor(103, 'Hydrothermic Headgear', 15, 0, 0, 0, 0, 0, 0, 12, 10, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces ammo usage by 25%/Granys immunity to fire and lava', set_bonus=Armor(103, '', 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'You fire a homing chaos flare when using ranged weapons every 0.33 seconds', None)), Armor(103, 'Hydrothermic Mask', 9, 0, 0, 0, 0, 0, 0, 0, 0, 12, 10, 100, 0, 0, 0, 0, 0, 'Grants immunity to fire and lava', set_bonus=Armor(103, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, '15% reduced mana usage\nMagic attacks summon damaging and healing flare orbs on hit', None)), Armor(103, 'Hydrothermic Helmet', 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 5, 0, 0, 0, 0, '%5 increased minion knockback\nGrants immunity to fire and lava', set_bonus=Armor(103, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 2, 0, 0, 0, 'Summons a hydrothermic vent to protect you', None)), Armor(103, 'Hydrothermic Hood', 12, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 10, 0, '50% chance not to consume rogue items\nGrants immunity to fire and lava', set_bonus=Armor(103, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 110, 'Rogue weapons unleash a volley of himing flames around the player every 2 seconds', None))]
    chestplates = [Armor(103, 'Hydrothermic Armor', 20, 8, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+20 max life', None)]
    leggings = Armor(103, 'Hydrothermic Subligar', 14, 0, 5,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(103, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Inferno effect when below 50% life\nYou emit a blazing explosion when you are hit', None)
    stage = 'Pre-Golem'

class PlagueReaperSet:
    helmets = [Armor(104, 'Plague Reaper Mask', 9, 0, 0, 0, 0, 0, 0, 10, 8, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    chestplate = [Armor(104, 'Plague Reaper Vest', 14, 0, 0, 0, 0, 0, 0, 15, 5, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants immunity to Plague', None)]
    leggings = Armor(104, 'Plague Reaper Striders', 11, 0, 3, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(104, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '25% reduced ammo usage and 5% increased flight time\nEnemies receive 10% more damage from ranged projectiles when afflicted by the Plague\nGetting hit causes the plague cinders to rain from above\nPress Armor Set Bonus to blind yourself for 5 seconds but massively boost your ranged damage\nThis has a 25 second cooldown.', None)
    stage = 'Pre-Lunar Events'
    
class PlaguebringerSet:
    helmets = [Armor(105, 'Plaguebringer Visor', 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, '+20 max life', None)]
    chestplates = [Armor(105, 'Plaguebringer Carapace', 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 'Grants immunity to the Plague\nFriendly bees inflict the plague', None)]
    leggings = Armor(105, 'Plaguebringer Pistons', 8, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 'Ypu grow flowers on the grass beneath you with a chance to grow very random dye plants on grassless dirt', None)
    set_bonus = Armor(105, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 'Grants a plague dash which can slam through enemies without taking damage\nSummons a lil plaguebringer to protect you and empower nearby minions', None)
    stage = 'Pre-Lunar Events'

class AstralSet:
    helmets = [Armor(106, 'Astral Helm', 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants danger detection', None)]
    chestplates = [Armor(106, 'Astral Breastplate', 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 0, '+20 max life\nGrants creature detection', None)]
    leggings = Armor(106, 'Astral Leggings', 21, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants ore detection', None)
    set_bonus = Armor(106,'', 0, 35, 35, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 'Whenever you crit an enemy, a barrage of stars will rain down\nThis effect has a 1 second cooldown before it will trigger again', None)
    stage = 'Pre-Moon Lord'

class LunicCorpsSet:
    helmets = [Armor(107, 'Lunic Corps Helmet', 14, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Grants night vision and creature detection', None)]
    chestplates = [Armor(107, 'Lunic Corps Vest', 20, 0, 0, 0, 0, 0, 0, 3, 11, 0, 0, 0, 0, 0, 0, 0, 0, '', None)]
    leggings = Armor(107, 'Lunic Corps Boots', 18, 0, 0, 15, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, '10% increased max movement speed and acceleration', None)
    set_bonus = Armor(107, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 'Projects a bubble shield that absorbs up to 50 damage\nThe shield starts recharging 5 seconds after being hit\nRecharging from zero to full charge takes 2 seconds\nBeing hit again while recharging restarts the charge timer\n10% increased bullet damage\n10% increased specialist ranged damage\nThese are launchers, dartguns, or anything else that does not shoot arrows/bullets\n20% increased jump speed', None)
    stage = 'Pre-Moon Lord'

class EmpyreanSet:
    helmets = [Armor(108, 'Empyrean Mask', 20, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 0, 'Temporary immunity to lava', None)]
    chestplates = [Armor(108, 'Empyrean Cloak', 27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 0, '+20 max life\nArmor of the cosmos', None)]
    leggings = Armor(108, 'Empyrean Cuisses', 24, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, '', None)
    set_bonus = Armor(108, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 115, '9% increased rogue velocity\nRogue projectiles have special effects on enemy hits/nImbued with cosmic wrath and rage when you are damaged', None)
    stage = 'Pre-Providence'

class TarragonSet:
    helmets = [Armor(109, 'Tarragon Helm', 33, 0, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '5% increased damage reduction', set_bonus=Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you\nYou have a 25% chance to regen health quickly when you take damage\nPress Armor Set Bonus to cloak yourself in life energy that heavily reduces contact damage for 10 seconds\nThis has a 30 second cooldown', None)), Armor(109, 'Tarragon Visage', 21, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, '5% increased damage reduction', set_bonus=Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Reduces enemy spawn rates\nRanged projectiles split into homing life energy and leaves on death', None)), Armor(109, 'Tarragon Mask', 10, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 100, 0, 0, 0, 0, 0, '5% increased damage reduction\n15% reduced mana usage', set_bonus=Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 00, 0, 0, 0, 0, 'Reduces enemy spawn rates\nOn every 5th critical strike you will fire a leaf storm\nMagic projectiles heal you on enemy hits\nAmount healed is based on projectile damage', None)), Armor(109, 'Tarragon Horned Helm', 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, '5% increased damage reduction', set_bonus=Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 3, 0, 0, 0, 'Reduces enemy spawn rates\nSummons a life aura around you that damages nearby enemies', None)), Armor(109, 'Tarragon Helmet', 15, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, '5% increased damage reduction', set_bonus=Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 115, 'Reduces enemy spawn rates\nAfter every 50 rogue critical hits you will gain 2.5 seconds of damage immunity\nThis effect has a cooldown of 25 seconds\nWhile under effects of a debuff you gain 10% increased rogue damage', None))]
    chestplates = [Armor(109, 'Tarragon Breastplate', 37, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+1 HP/s life regen and +40 max life', None)]
    leggings = Armor(109, 'Tarragon Leggings', 32, 8, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(109, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Increased heart pickup range\nEnemies have a chance to drop extra hearts on death', None)
    stage = 'Pre-Polterghast'

class PrismaticSet:
    helmets = [Armor(110, 'Prismatic Helmet', 18, 0, 0, 0, -20, 0, 0, -20, 0, 18, 12, 0, -20, 0, -20, 0, 0, 'Enemies with less than 500 health deal no damage\nThis does not occur while a boss is alive', None)]
    chestplates = [Armor(110, 'Prismatic Regalia', 33, 0, 0, 0, -20, 0, 0, -20, 0, 12, 15, 40, -20, 0, -20, 0, 0, '+20 max life\nMagic attacks occasionally fire a pair of homing rockets', None)]
    leggings = Armor(110, 'Prismatic Greaves', 21, 0, 0, 00, -20, 0, 0, -20, 0, 10, 12, 0, -20, 0, -20, 0, 0, '10% increased flight time\n2% increased jump speed', None)
    set_bonus = Armor(110, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 0, '15% reduced mana cost\nIncreased mana regeneration rate\nPress Armor Set Bonus to unleash a barrage of death lasers at the cursor for the next 5 seconds\nThis has a 30 second cooldown', None)
    stage = ''

class BloodflareSet:
    helmets = [Armor(111, 'Bloodflare Ram Mask', 49, 0, 0, 0, 10, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(111, '', 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Enemies are more likely to target you\nTrue melee strikes will heal you\nAfter striking an enemy 15 times with true melee you will enter a blood frenzy for 5 seconds\nDuring this you will gain 25% increased melee damage, critical strike chance, and contact damage is halved\nThis effect has a 30 second cooldown', None)), Armor(111, 'Bloodflare Horned Helm', 34, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, '', set_bonus=Armor(111, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Press Armor Set Bonus to unleash the lost souls of polterghast to destroy your enemies\nThis effect has a 30 second cooldown\nRanged weapons fire bloodsplosion orbs every 2.5 seconds', None)), Armor(111, 'Bloodflare Hydra Hood', 22, 0, 0, 0, 0, 0, 0, 0, 0, 20, 10, 100, 0, 0, 0, 0, 0, '17% reduced mana usage', set_bonus=Armor(111, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0 ,' Magic weapons fire ghostly bolts every 1.67 seconds\nMagic critical strikes cause flame explosions every 2 seconds', None)), Armor(111, 'Bloodflare Wyvern Helm', 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 5, 0, 0, 0, 0, '', set_bonus=Armor(111, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 3, 0, 0, 0, 'Summons polterghast mines to circle you\nAt 90% life and above you gain 10% increased summon damage\nAt 50% life and below you gain 20 defense and +1 HP/s life regen', None)), Armor(111, 'Bloodflare Imp Mask', 28, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, '', set_bonus=Armor(111, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 'Being over 80% life boosts your defense by 30 and rogue crit by 5%\nBeing below 80% life boosts your rogue damage by 10%\nRogue critical strikes have a 50% chance to heal you', None))]
    chestplates = [Armor(111, 'Bloodflare Body Armor', 35, 12, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '+40 ma life', None)]
    leggings = Armor(111, 'Bloodflare Cuisses', 29, 10, 7, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '', None)
    set_bonus = Armor(111, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Greatly increased life regen, equivalent to Crimson armor\nEnemies below 50% life drop a heart when struck\nThis effect has a 5 second cooldown', None)
    stage = ''






















armor_sets = {MiningSet, WoodSet, MahoganySet, BorealSet, PalmSet, EbonwoodSet, ShadewoodSet, AshWoodSet, RainSet, SnowSet, PinkSnowSet, AnglerSet, CactusSet, CopperSet, TinSet, PumpkinSet, 
              NinjaSet, IronSet, LeadSet, SilverSet, TungstenSet, GoldSet, PlatinumSet, FossilSet, BeeSet, ObsidianSet, GladiatorSet, MeteorSet, JungleSet, AncientCobaltSet, NecroSet, 
              ShadowSet, AncientShadowSet, CrimsonSet, MoltenSet, PearlwoodSet, SpiderSet, CobaltSet, PalladiumSet, MythrilSet, OrichalcumSet, AdamantiteSet,
              TitaniumSet, CrystalAssassinSet, FrostSet, ForbiddenSet, SquireSet, MonkSet, HuntressSet, ApprenticeSet, HallowedSet, ChlorophyteSet, TurtleSet, TikiSet, BeetleSet, ShroomiteSet,
              SpectreSet, ValhallaKnightSet, ShinobiInfiltratorSet, RedRidingSet, DarkArtistSet, SolarFlareSet, VortexSet, NebulaSet, StardustSet, WizardSet, WulfrumSet, SnowRuffianSet, DesertProwlerSet, MarniteArchitectSet, VictideSet,
              SulphurousSet, AerospecSet, StatigelSet, MolluskSet, TitanHeartSet, DaedalusSet, BrimflameSet, FathomSwarmerSet, UmbraphileSet, ReaverSet, HydrothermicSet, 
              PlagueReaperSet, PlaguebringerSet, AstralSet, LunicCorpsSet, EmpyreanSet, TarragonSet}

