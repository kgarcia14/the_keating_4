#this is our main 

class Character:
    def __init__(self, name, alert_level):
        self.name = name
        self.alert_level = alert_level
        self.items = []

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        

class Item:
    def __init__(self, name, associated_room, alert_effect=0):
        self.name = name        
        self.associated_room = associated_room
        self.alert_effect = alert_effect
        
# Location Instantiation
josh_room = Location("Quiet Room", "pass")
liz_office = Location("Liz's Office", "pass")
elevator = Location("Elevator", "pass")
roof = Location("Roof", "pass")
kitchen = Location("Kitchen", "pass")
gym = Location("Gym", "pass")
security_desk = Location("Security Desk", "pass")

# Items Instantiation
# Josh's Room
monitor = Item("monitor", josh_room)
jacket = Item("jacket", josh_room, -10)
bag_of_chips = Item("bag of chips", josh_room, 5)

# Liz's Room
tshirt = Item("tshirt", liz_office, -10)
book = Item("book", liz_office)# riddle/game in book and if you can solve unlocks ryan phone number and he distracts security guard for you 
keyboard = Item("keyboard", liz_office, 15)

# Elevator
key_card = ("Dropped Key Card", elevator)
trash_can = ("Trash Can", elevator, -10)

# Roof
tarp = ("tarp", roof, -15)
chair = ("chair", roof)
firepit = ("firepit", roof, -20)
# Kitchen
sink = ("sink", kitchen, -10)
bleach = ("bleach", kitchen, -10)
freezer = ("freezer", kitchen, 5)
# Gym
shower = ("shower", gym, -5)
shower_curtain = ("shower_curtain", shower, -5)
weights = ("weights", gym, +5)

# Security Desk
security_desk = ("security desk", security_desk,)
# Menus

main_menu = ["Look around my space", "Check Alert Status", "Look at my items", "Move to a new location", "Call the Police"]



def play_game():

    print("Welcome to How To Get Away With Murder")
# We need some info here about the game....so you know what character you want to choose
    crystal = Character('Crystal', 40)
    jojo = Character('JoJo', 10)
    kurtis = Character('Kurtis', 30)
    joshua = Character('Joshua', 5)
    annalise  = Character('Annalise Keating', 0)
    main_players = [crystal.name, jojo.name, kurtis.name, joshua.name]
    print() #Add in player stats and special characteristics
    for idx, player in enumerate(main_players):
        print(f"{idx+1}. {player}")
    
    choosing_player = input("Please pick a player: ")
    # selection = main_players[int(choosing_player)-1]
    # print(selection)
    if choosing_player == "1":
        active_player = crystal
    if choosing_player == "2":
        active_player = jojo
    if choosing_player == "3":
        active_player = kurtis
    if choosing_player == "4":
        active_player = joshua
    if choosing_player == '1000':
        active_player = annalise    
    print(f'You have selected {active_player.name} with an alert level of {active_player.alert_level}!')
    # Here we need to set the scene!
    curr_location = josh_room
    print("What would you like to do now?")
    for idx, choice in enumerate(main_menu):
        print(f"{idx+1}. {choice}")
    
    main_menu_choice = input()

    if main_menu_choice == "1":
        print(curr_location.description)
    if main_menu_choice == "2":
    if main_menu_choice == "3":
    if main_menu_choice == "4":
      
        


play_game()
