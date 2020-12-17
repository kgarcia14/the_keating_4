#this is our main 

class Character:
    def __init__(self, name, alert_level):
        self.name = name
        self.alert_level = alert_level
        self.items = []

    def change_alert(self, location, item_idx):
        self.alert_level += location.item[item_idx]
    
    def print_alert_status(self):
        print(self.alert_level)

    def add_items(self, item):
        self.items.append(item)

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        

class Item:
    def __init__(self, name, associated_room, alert_effect=0):
        self.name = name        
        self.associated_room = associated_room
        self.alert_effect = alert_effect


# Character Instantiation
crystal = Character('Crystal', 40)
jojo = Character('JoJo', 10)
kurtis = Character('Kurtis', 30)
joshua = Character('Joshua', 5)
annalise  = Character('Annalise Keating', 0)

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
items_josh_room = [monitor.name, jacket.name, bag_of_chips.name]

# Liz's Room
tshirt = Item("tshirt", liz_office, -10)
book = Item("book", liz_office)# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you 
keyboard = Item("keyboard", liz_office, 15)
items_liz_room = [tshirt.name, book.name, keyboard.name]

# # Elevator
key_card = Item("Dropped Key Card", elevator)
trash_can = Item("Trash Can", elevator, -10)
items_elevator = [key_card.name, trash_can.name]

# # Roof
tarp = Item("tarp", roof, -15)
chair = Item("chair", roof)
firepit = Item("firepit", roof, -20)
items_roof = [tarp.name, chair.name, firepit.name]

# Kitchen
sink = Item("sink", kitchen, -10)
bleach = Item("bleach", kitchen, -10)
freezer = Item("freezer", kitchen, 5)
items_kitchen = [sink.name, bleach.name, freezer.name]

# # Gym
shower = Item("shower", gym, -5)
shower_curtain = Item("shower_curtain", gym, -5)
weights = Item("weights", gym, +5)
items_gym = [shower.name, shower_curtain.name, weights.name]

# # Security Desk
security_desk = Item("security desk", security_desk,)
items_security_desk = [security_desk.name]


# Menus

main_menu = ["Search for anything useful", "Look at my items", "Move to a new location", "Call the Police"]



main_players = [crystal.name, jojo.name, kurtis.name, joshua.name]

def which_list(room):
    if room == josh_room:
        return items_josh_room
    if room == gym:
        return items_gym


def play_game():

    print("Welcome to How To Get Away With Murder")
# We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
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
    if choosing_player == "1000":
        active_player = annalise    
    print(f'You have selected {active_player.name} with an alert level of {active_player.alert_level}!')
    # Here we need to set the scene!
    curr_location = josh_room
    curr_items_list = which_list(curr_location)
    print("What would you like to do now?")
    for idx, choice in enumerate(main_menu):
        print(f"{idx+1}. {choice}")
    print(curr_location.description)
    active_player.print_alert_status()
    main_menu_choice = input("Please choose: ")
    if main_menu_choice == "1":
        item_loop = True
        while item_loop:
            for idx, item in enumerate(curr_items_list):
                print(f"{idx+1}. {item}")
            item_chosen = int(input("Which item would you like to pick up? "))
            active_player.add_items(curr_items_list[item_chosen-1])
            del()
            curr_items_list.pop(item_chosen-1)
            continue_choosing = input("Would you like to choose another item? y or n\n")
            if continue_choosing.lower() == "n":
                item_loop = False

       

    # if main_menu_choice == "2":
    # if main_menu_choice == "3":
    # if main_menu_choice == "4":
      


play_game()


