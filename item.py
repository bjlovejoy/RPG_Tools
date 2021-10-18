import support_functions as sf

#TODO: combine 2+ items to make a new one (each item should have a potential ingredients list)

class Item:
    def __init__(self, names:list, description:str):
        self.name = names[0]
        self.names = names
        self.description = description

    def describe(self):
        sf.display(self.description, "narrator")

class Weapon(Item):
    def __init__(self, names:list, description:str, damage:int):
        super().__init__(names, description)
        self.damage = damage  #TODO: like wearable and armor, allow diferent types of damage

class Armor(Item):
    def __init__(self, names:list, description:str, protection:int):
        super().__init__(names, description)
        self.protection = protection
        #TODO: similar to wearables, replace protection with different types of bonuses
        #Ex. create a dictionary with all possible values

class Wearable(Item):
    def __init__(self, names:list, description:str, protection:int):
        super().__init__(names, description)
        self.protection = protection  #TODO: protection for constitution, defense, etc.
        #TODO: boost charisma, wisdom, dexterity, etc.

class Food(Item):
    def __init__(self, names:list, description:str, health_points:int):
        super().__init__(names, description)
        self.health_points = health_points  #can be negative

class Key(Item):
    def __init__(self, names:list, description:str, key_id:int):
        super().__init__(names, description)
        self.key_id = key_id
