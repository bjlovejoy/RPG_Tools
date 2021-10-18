import support_functions as sf
from commands import parse_cmd

#TODO: in the future, only load up one room (and the player/inventory) at a time
#      when leaving the room, save its current state and delete/garbage collect before loading the next

class Profile:
    def __init__(self, name, player):
        self.name = name

    def save(self):
        pass

    def load(self):
        pass

    def add_player(self):
        pass


class Level:
    def __init__(self, level_num:int, title:str, title_font='ascii', rooms:list=[], starting_room:int=-1):
        self.level_num = level_num
        self.title = title
        self.title_art = sf.ascii_art(self.title, font=title_font)  #TODO: add colors
        self.rooms = list()
        self.add_rooms(rooms)

        self.set_starting_room = self.set_current_room
        self.current_room_index = None
        self.current_room = None
        if starting_room >= 0 and len(rooms):
            raise AssertionError(f"The starting room cannot be defined until that room is added to the level.")
        elif starting_room > 0:
            self.set_current_room(starting_room)

    def add_room(self, room):
        self.rooms.append(room)
        #TODO: add checking to make sure room is okay (room obj, no repeat location, etc.)

    def add_rooms(self, rooms:list):
        for room in rooms:
            self.add_room(rooms)

    def get_room_index(self, room_num):
        """
        The room_num is the desired room's location property
        """
        for i, room in enumerate(self.rooms):
            if room.location == room_num:
                return i
        raise AssertionError(f"No room with number {room_num} available.")

    def get_room(self, room_num):
        """
        The room_num is the desired room's location property
        """
        for room in self.rooms:
            if room.location == room_num:
                return room
        raise AssertionError(f"No room with number {room_num} available")

    def set_current_room(self, room_num):
        self.current_room_index = self.get_room_index(room_num)
        self.current_room = self.rooms[self.current_room_index]
        #Could also do a "get_current_room" and remove the self.current_room object


class Game:
    def __init__(self, title:str, title_font:str='ascii', levels:list=[]):
        self.title = title
        self.title_art = sf.ascii_art(self.title, font=title_font)  #TODO: add colors
        self.levels = levels
        self.Profiles = list()

        self.playing = True
        self.current_level_index = None
        self.current_level = None
        self.title_foreground = "normal"
        self.title_background = "normal"

    def start_game(self):
        while True:
            sf.clear_screen()
            sf.display_title(self.title_art, self.title_foreground, self.title_background)
            #TODO: (title menu) select/create profile, load game, exit game, add option to customize text_to_proceed, etc.
            sf.write_to_log(new_session=True)
            self.level_menu()

    #currently only supports selecting level or exit (needs to handle more)
    def level_menu(self):
        sf.display(self.title + ' Menu\n', "settings")
        sf.display("Select Level", "settings")
        for level in self.levels:
            sf.display(str(level.level_num) + ') ' + level.title, "settings")
        sf.display(str(len(self.levels)+1) + ') ' + "Quit Game", "settings")

        selection = sf.read_number_input(1, len(self.levels)+1, error_text="Please select one of the listed levels (by number):")
        sf.clear_screen()

        if selection == len(self.levels)+1:
            sf.display("Thank you for playing!!!\n\n", "settings")
        else:
            self.set_current_level(selection)
            self.main()

    def customize_title(self, fore, back):
        self.title_foreground = fore
        self.title_background = back

    def add_profile(self):
        pass  #TODO: character creation (here or in profile)?

    def remove_profile(self):
        pass

    def add_level(self, level):
        self.levels.append(level)
        self.levels.sort(key=lambda lev: lev.level_num)
        #check for starting rooms and anything else that would prevent normal operation

    def get_level_index(self, level_num):
        """
        The level_num is the desired level's assigned number
        TODO: unless changed, can just return level_num -1
        """
        for i, level in enumerate(self.levels):
            if level.level_num == level_num:
                return i
        raise AssertionError(f"No level with number {level_num} available")

    def get_level(self, level_num):
        for level in self.levels:
            if level.level_num == level_num:
                return level
        raise AssertionError(f"No level with number {level_num} available")

    def set_current_level(self, level_num):
        self.current_level_index = self.get_level_index(level_num)
        self.current_level = self.levels[self.current_level_index]

    def main(self):

        self.current_level.current_room.play_cutscene()

        while self.playing:
            user_input = sf.read_input()
            parse_cmd(user_input, self)
