import support_functions as sf

class Room:
    def __init__(self, location:int, description:str, contents:list, cutscene:str=""):
        self.location = location   # TODO: should room have a name?
        self.description = description
        self.contents = contents
        self.cutscene = cutscene
        self.first_enter = True

        self.check_for_duplicates()

    def add_contents(self, content):
        self.contents.append(content)

    def describe(self):
        sf.display(self.description, "narrator")

    def play_cutscene(self):
        if self.cutscene and self.first_enter:
            self.first_enter = False
            sf.display(self.cutscene, "narrator")

    def find_matches(self, name):
        """
        Recursively search through all contents in the room and compares
        param 'name' to all the names of each content.  A list of all
        matches are saved and returned.
        """
        items_found = list()
        for content in self.contents:
            if name in content.names:
                items_found.append(content)
            if type(content) is Box:
                if content.opened:
                    for item in content.contents:
                        if name in item.names:
                            items_found.append(item)

        return items_found

    def find_match(self, name):
        """
        Calls 'find_matches' to collect list of all matches.  Prompts the user
        to clarify which item they wish to interact with.
        """
        items_found = self.find_matches(name)
        if len(items_found) == 0:
            return items_found  #empty list
        elif len(items_found) == 1:
            return items_found[0]  #found one item
        else:
            quote = sf.random_selection(["Multiple matches detected, please refine:", "Which one? :", "I found a couple:", "Please select from the list below:"])
            sf.display(quote, "warning")
            for i, item in enumerate(items_found):
                sf.display(str(i+1) + ") " + item.name, "list")

            selection = sf.read_number_input(1, len(items_found), error_text="Choose an item from the list above (by number).")

            return items_found[selection-1]  #return selected item

    def check_for_duplicates(self):
        """
        Make sure all items in room are unique (check first name in names)
        otherwise, raise Assertion
        """
        all_contents = list()
        for content in self.contents:
            all_contents.append(content.name)
        if len(set(all_contents)) < len(all_contents):
            error_msg = 'Duplicate names in room: ' + str(self.location)
            raise AssertionError(error_msg)


class RoomItem:
    def __init__(self, names:list, description:str):
        self.name = names[0]
        self.names = names
        self.description = description

    def describe(self):
        sf.display(self.description, "narrator")

class Door(RoomItem):
    def __init__(self, names:list, description:str, destination:int, locked:bool=False, key_id:int=0):
        super().__init__(names, description)
        #self.cutscene = cutscene
        self.destination = destination  #-1 or any negative number means end of level
        self.locked = locked
        self.key_id = key_id

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def change_key_id(self, new_id):
        self.key_id = new_id

#TODO: doors with passwords/phrases, doors to transport, ladders

class Box(RoomItem):
    def __init__(self, names:list, description:str, contents:list, locked:bool=False, key_id:int=0, capacity:int=0):
        super().__init__(names, description)
        self.contents = contents
        self.locked = locked
        self.key_id = key_id      #0 is universally ulockable
        self.capacity = capacity  #0 is infinite (may want to make this negative in the future)

        self.opened = False  #all boxes begin closed and have to be opened,
                             #either in game or by calling the open() function

        #TODO: material of box with strength value to break/force open

    def list_contents(self):
        if len(self.contents) == 0:
            quote = sf.random_selection(["There's nothing inside.", "It's empty.", "It appears to be empty.", "The " + self.name + " is empty."])
            sf.display(quote, "narrator")
        else:
            sf.display("Inside you find the following item(s):", "narrator")
            for item in self.contents:
                sf.display(item, "list")

    def add_item(self, item):  #Item
        self.contents.append(item)

    def remove_item(self, item_name:str):
        for i in self.contents:
            if i.name == item_name:
                temp = self.contents.pop(i)
                break
        return temp

    def remove_all(self):
        temp = self.contents
        self.contents.clear()
        return temp

    def lock(self):
        self.locked = True  #Make lock/unlock cmd handle checking key_id

    def unlock(self):
        self.locked = False

    def change_key_id(self, new_id):
        self.key_id = new_id

    def open(self):
        self.opened = True

    def close(self):
        self.opened = False


#Boxes have to be opened, but Tables are always "opened"
#Do not use for now
class Table(RoomItem):
    def __init__(self, names:list, description:str, contents:list, capacity:int):
        super().__init__(names, description)
        self.contents = contents
        self.capacity = capacity

    def list_contents(self):
        pass  #if look at, print description
              #if look on or just look, list contents

    def add_item(self):
        pass

    def remove_item(self, item):
        pass

    def remove_all(self):
        pass

#TODO: encounter object?

class Interactable(RoomItem):
    def __init__(self, names:list, description:str, trigger_commands:list):
        super().__init__(names, description)
        self.trigger_commands = trigger_commands
