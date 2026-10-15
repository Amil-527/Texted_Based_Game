# Nadia Waters
# Started on: 9/20/2026
# Completed on: 10/15/2026
# This is a remake of a college finale project I made during Jan to Mar, 2026.
# The previous project had errors that made it unfinished, so I decided to remake it from scratch.

#Dictionary that links a room to other rooms
rooms = {
    'Entrance' : {'name': 'Entrance', 'North': 'Main Room'},
    'Main Room' : {'name': 'Main Room', 'item': 'Armor', 'North': 'Stairs', 'East': 'Dining Room',
                   'South': 'Entrance', 'West': 'Study' },
    'Stairs' : {'name': 'Stairs', 'item': 'Sword', 'North': 'Top of the Tower', 'South': 'Main Room'},
    'Top of the Tower': {'name': 'Top of the Tower'}, #Villian location
    'Dining Room' : {'name': 'Dining Room', 'item': 'Shield', 'North': 'Basement', 'West': 'Main Room'},
    'Basement': {'name': 'Basement', 'item': 'Grimoire', 'South': 'Dining Room'},
    'Study' : {'name': 'Study', 'item': 'Amulet', 'East': 'Main Room', 'South': 'Garden'},
    'Garden' : {'name': 'Garden', 'item': 'Gold Apple', 'North': 'Study'}
}

#Lists of directions and items for Rooms lists
directions = ['North', 'East', 'South', 'West']
getItem = ['item']

#Player's start position
currentRoom = rooms['Entrance']
inventory = []

#Game Instruction
def game_start():
    print('Welcome to Text Based Game!')
    print('Collect 6 items in order to beat the villain of the game!')
    print(f'To move, type "NORTH", "EAST", "SOUTH", or "WEST" to go through each room.')
    print(f'Type "Get" to get a specific item and put inside your inventory.')

#Displays the player's current status during the game.
def player_status():
    print('__________________________________________')
    print('You are currently in: {}'.format(currentRoom['name']))
    print('Inventory:', inventory)
    print('__________________________________________')

#Checks if a room has an item
def room_item():
    if 'item' in currentRoom and 'item' not in inventory:
        print(f'There is a {currentRoom['item']} in the room!')
    elif 'item' not in currentRoom:
        print('This room is empty!')


# Main game code
print(game_start())
while True:
    player_status()
    room_item()

    #Movement between rooms
    command = input('Enter your command: ').title()
    #Changes between rooms based on the input
    if command in directions:
        if command in currentRoom:
            currentRoom = rooms[currentRoom[command]]
        else:
            print('You cannot go that way!')

    #Code for picking up items and placing in Inventory
    elif command == 'Get':
        try:
            if 'item' not in inventory:

                inventory.append(currentRoom['item'])
                print(f'{currentRoom['item']} has been added to your inventory!')
                del currentRoom['item']
            elif 'item' in inventory:
                print(f'{currentRoom['item']} is already in your inventory!') #not working!
        except:
            print('item pickup does not work!')
    else:
        print('Invalid command!')

    #Condition if player has all items and is in Tower
    if currentRoom['name'] == 'Top of the Tower':
        if len(inventory) == 6:
            print('CONGRATULATIONS! You have defeated the villain!')
            input(f'Type "Quit" to leave the game: ').title()
            break
        else:
            print('You have been defeated by the villain!')
            break

    #Quit game command
    if command == 'Quit':
        print('Thank you for playing!')
        break