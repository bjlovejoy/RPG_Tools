#from RPG_Tools import *
from game import *
from room import *
from character import *
from item import *
from commands import *
from support_functions import *


tutorials = Game("RPG_Tools Tutorial", "stforek")


tutorial_01 = Level(1, "The Adventure Begins", "stforek")


#**********BEDROOM**********BEDROOM**********BEDROOM**********BEDROOM***********
bed = Item(names=["bed"],
           description="A soft and fluffy bed of white linen. A puddle of sweat remains from where you were laying. Gross.")

kitchen_key = Key(names=["silver key", "key", "kitchen key", "blank key"],
                  description="A small, polished, silver key. The inscription is blank.",
                  key_id=50)

ring = Wearable(names=["gold ring", "ring", "old ring"],
                description="An old gold ring, not worth very much. However, it's properties may grant you protection.",
                protection = 2)

sword = Weapon(names=["sword", "blade", "chipped blade", "chipped sword"],
               description="The leather-wrapped hilt and the polished, chipped blade are familiar to you. This is the sword given to you by your father. Treat it well.",
               damage=5)

jewelry_box = Box(names=["jewelry box", "jewelry", "jewelrybox"],
                  description="A deep purple, saphire-encrusted jewelry box. The lid apears slightly ajar.",
                  contents=[ring, kitchen_key])

bed_chest = Box(names=["chest", "wood chest", "wooden chest", "bed chest", "oaken chest"],
                description="An old, oaken chest. The gold paint on the wood apears to be pealing away from its age. A large brass key hole is situated in the center. It might be unlocked though.",
                contents=[sword])

foyer_door = Door(names=["foyer door", "door", "west door"],
                    description="An oak door with a brass door knob.",
                    destination=0, locked=True, key_id=51)

kitchen_door = Door(names=["kitchen door", "door", "north door"],
                    description="An oak door with a silver door knob.",
                    destination=11, locked=True, key_id=50)

bedroom = Room(location=1,
               description="You are in a bedroom. The wooden floor is "\
               "polished clean, as is most of the room. There is a long "\
               "wooden chest at the foot of the bed and a jewelry box on a "\
               "vanity table. There are two doors, one to the north and one "\
               "to the west.",
               contents=[bed, jewelry_box, bed_chest, foyer_door, kitchen_door],
               cutscene="You begin to stir as you awaken from a deep sleep. "\
               "You feel a cold sweat on your forehead and your vision is "\
               "hazy. As you sit up, your vision begins to clear and you "\
               "find yourself in a comfy bed of linen.")

tutorial_01.add_room(bedroom)


#**********KITCHEN**********KITCHEN**********KITCHEN**********KITCHEN***********
jerky = Food(names=["jerky", "meat", "dried meat", "beef jerky"],
             description="A bag of dried, salted beef.",
             health_points=5)

dried_fruit = Food(names=["dried fruit", "fruits", "fruit"],
                   description="An assortment of dried cranberries, blueberries and blackberries.",
                   health_points=3)

dried_nuts = Food(names=["dried nuts", "nuts", "nut", "dried nut"],
                  description="an assorment of salted cashews and walnuts",
                  health_points=3)

cupboard = Box(names=["cupboard", "cuboard", ],
               description="A pantry cupboard with a single door, made of solid oak.",
               contents=[jerky, dried_fruit, dried_nuts])

ice_box = Box(names=["ice box", "icebox", "ice"],
              description="An icy stone box built right into the floor.",
              contents=[])

foyer_key = Key(names=["foyer key", "key", "old key", "brass key", "old brass key"],
                description="An old, brass key. It looks like it matches the door with the brass lock you saw in the bedroom.",
                key_id=51)

stove = Interactable(names=["stove", "wood stove", "oven"],
                     description="Appears to be an old wood stove. Probably doesn't work. But I wonder what the dial is for?",
                     trigger_commands=["turn", "use", "rotate"])

bedroom_door = Door(names=["bedroom door", "door", "south door"],
                    description="An oak door with a silver door knob. This way leads to the bedroom.",
                    destination=1)

kitchen = Room(location=11,
               description="You find yourself in a neat country kitchen. The curtains are drawn, yet the room seems rather well lit. There is a cupboard above a stove and an ice box.",
               contents=[cupboard, ice_box, stove, bedroom_door])

tutorial_01.add_room(kitchen)


#**********FOYER**********FOYER**********FOYER**********FOYER**********FOYER****
outside_door = Door(names=["outside door", "front door", "door", "south door"],
                    description="A beautiful front door that appears defiled by scratches.  Or are those claw marks?",
                    destination=-1, locked=True, key_id=55)

closet_door = Door(names=["closet door", "door", "north door", "closet"],
                   description="A peeling, chipped door with a rusted knob. The crimson paint almost looks like...Maybe we should try to leave.",
                   destination=10)

bedroom_door = Door(names=["bedroom door", "door", "east door"],
                    description="An oak door with a brass door knob. This way leads to the bedroom.",
                    destination=1)

chest_plate = Armor(names=["chest plate", "plate", "armor", "chest piece"],
                    description="A polished iron chest piece, lightly worn. Weren't you wearing this when you arrived?",
                    protection=3)

wardrobe = Box(names=["wardrobe", "box", "chest"],
               description="A tall, double door wardrobe with thin, sliver handles.",
               contents=[chest_plate])

foyer = Room(location=0,
             description="The room is furnished with fine wooden furniture, among which, you find a wardrobe and a dining room table.  Two doors face opposite each other.  One appears to be a closet door and you know the other to lead outside.",
             contents=[wardrobe, outside_door, closet_door, bedroom_door],
             cutscene="As the door creaks open, you emerge in a candle-lit foyer.")

tutorial_01.add_room(foyer)


#**********CLOSET**********CLOSET**********CLOSET**********CLOSET***************
closet = Room(location=10,
              description="",
              contents=[],
              cutscene="")

tutorial_01.add_room(closet)



#**********END LEVEL**********END LEVEL**********END LEVEL**********END LEVEL***
tutorials.add_level(tutorial_01)
tutorial_01.set_starting_room(1)

#**********START GAME**********START GAME**********START GAME*******************
tutorials.start_game()
