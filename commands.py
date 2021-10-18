import support_functions as sf

def filter_cmd(cmd:list, filler_words:list=[], use_default:bool=False, exceptions:list=[]):
    """
    Removes unimportant words from cmd
    Ex. at, in, inside, over, for, the, a, an, to, my, his, her
    """
    if use_default:
        filler_words = ['at', 'in', 'inside', 'on', 'ontop', 'over', 'for', 'the', 'a', 'an', 'to', 'my', 'his', 'her']
    for word in cmd:
        if (word in filler_words) and (word not in exceptions):
            cmd.remove(word)

def failed_search(name):
    quote = sf.random_selection(["Sorry, I don't see any.", "Not sure what you're looking at?", f"I'm not seeing any \"{name}\".", f"What is \"{name}\"?"])
    sf.display(quote, "warning")

#TODO: this is where I left off #################################################################################
def look(cmd, game):
    room = game.current_level.current_room  #TODO: add a quick function to do this

    if len(cmd) == 1:
        room.describe()

    elif len(cmd) == 2:
        item = room.find_match(cmd[1])
        if item:
            item.describe()
        else:
            failed_search(cmd[1])

    elif len(cmd) > 2:
        item_name = ' '.join(cmd[1:])
        item = room.find_match(item_name)
        #also have a filtered version
        if not item:
            filter_cmd(cmd, use_default=True)
            filtered_item_name = ' '.join(cmd[1:])
            item = room.find_match(filtered_item_name)

        if type(item) is Box:
            if any(i in cmd for i in ['in', 'inside']) and item.opened:
                pass
            elif any(i in cmd for i in ['in', 'inside']):
                pass
        elif not item:
            failed_search(item_name)
        else:
            item.describe()


def opens(cmd, game):
    pass

def take(cmd, game):
    pass

def unlock(cmd, game):
    pass

def go(cmd, game):
    pass  #look if there is a door in the desired direction if nsew


def quit(cmd, game):
    #TODO: make sure to reset colors to default "normal"
    #ask user if they are sure y/n
    game.playing = False

#contains all command functions as keys and their keywords as values
game_cmds = {}
level_cmds = {}
room_cmds = {}

all_cmds = {look: ['look', 'see', 'study', 'view', 'check', 'search'],
            opens: ['open', 'enter', 'unlock'],
            take: ['take', 'grab'],
            go: ['go', 'walk', 'run', 'travel', 'head', 'move']}

def parse_cmd(user_cmd, game):
    #TODO: check interactables in room first and curse words/joke cmds last
    found_match = False

    for cmd, keywords in all_cmds.items():
        if user_cmd[0] in keywords:
            cmd(user_cmd, game)
            found_match = True

            #May want to pass game if quit/save/load cmd, level if moving rooms,
            #character if affecting inventory or player, or just room if altering room
            #(selectively passing objects to reduce repetitive calls to game.current_level.current_room.etc...)

    if not found_match:
        pass  #print from random selection of strings that we don't understand
        sf.display("Didn't Work", "warning")
