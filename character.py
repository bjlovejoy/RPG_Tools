import support_functions as sf

class Inventory:
    def __init__(self, contents):
        self.contents = contents

    def list_contents(self):
        pass

    def list_filter(self):
        pass

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def equip_item(self):
        pass

class Character:
    def __init__(self, name:str, description:str, inventory:Inventory, max_health:int, current_health:int=0):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.max_health = max_health

        self.current_health = current_health
        if current_health == 0:
            self.current_health = max_health

class Player(Character):
    def __init__(self, name:str, description:str, inventory:Inventory, max_health:int, current_health:int=0):

        super().__init__(name, description, inventory, max_health, current_health)

        self.armor_slot_head = None
        self.armor_slot_body = None
        self.armor_slot_pants = None
        self.armor_slot_feet = None
        self.weapon_slot_1 = None
        self.weapon_slot_2 = None
        self.wearable_slot_1 = None
        self.wearable_slot_2 = None
        self.wearable_slot_3 = None
        self.wearable_slot_4 = None
        #consider a weight or capacity limit

    #TODO: print player status (health, weight, potion effects, hunger, protection, equipped items, etc.)

class NPC(Character):
    def __init__(self, name:str, description:str, inventory:Inventory, max_health:int, current_health:int=0):

        super().__init__(name, description, inventory, max_health, current_health)

class Enemy(Character):
    def __init__(self, name:str, description:str, inventory:Inventory, max_health:int, current_health:int=0):

        super().__init__(name, description, inventory, max_health, current_health)

        self.attacks = list()  #list of dicts

    def add_attack(self, name, description, min_damage, max_damage, probability):
        self.attacks[name] = {"description":description, "min_damage":min_damage, "max_damage":max_damage, "probability":probability}
        #probability of successful hit is ranged from 0-100
        #a random number 1-100 will be generated, and if it is under the treashold range, it will hit
        #Ex. probability = 70, rand_num = 45, 45 < 70, so hit
        #make the amount of damage dynamic based on how close/far the rand_num is to the target

class Merchant(Character):  #TODO
    def __init__(self, name:str, description:str, inventory:Inventory, max_health:int, current_health:int=0):

        super().__init__(name, description, inventory, max_health, current_health)
