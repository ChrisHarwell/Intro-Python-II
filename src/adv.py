from room import Room
from player import Player
from item import Item
from time import sleep
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

iron_sword = Item('sword', 'A simple, but sturdy iron sword')
old_broom = Item('broom', 'A broom, dustier even than this place')

# Adding items to rooms:
room['outside'].add_item(iron_sword.item)
room['foyer'].add_item(old_broom)

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
def goDirection(player, direction):
    attr = direction + '_to'

    if hasattr(player.location, attr):
        player.location = getattr(player.location, attr)
    else:
        print("You can't go in that direction!")


playing = True

while playing:
    print(f"\n {player.location.description} {player.location} \n")

    player_input = input(
        '''\n
        Where do you want to go?
        Choose [n]:North, [s]:South, [e]:East, [w]:West . . .
        Or press [q] to quit!\n
        ''').lower().split(' ')

    if player_input[0] == 'q':
        playing = False
        print('You have quit the game. See ya next time!')
    elif player_input[0] == 'n':
        goDirection(player, player_input[0])
    elif player_input[0] == 's':
        goDirection(player, player_input[0])
    elif player_input[0] == 'e':
        goDirection(player, player_input[0])
    elif player_input[0] == 'w':
        goDirection(player, player_input[0])
    elif player_input[0] == 'i':
        player.check_inv()
    if player_input[0] == 'search':
        if player.location.items == []:
            print('You did not find anything here.')
        else:
            print(player.location.items)

if len(player_input) > 1:
    if player_input[0] == 'take':
        for item in player.location.items:
            if player_input[1] == item[0]:
                player.take_item(item)
                player.location.remove_item(item)
                print(player.location.items, player.inventory)


# If the user enters "q", quit the game.
