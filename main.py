from classes import Character, Location, Item

# this is our main program


# Character Instantiation
crystal = Character('Crystal', 40)
jojo = Character('JoJo', 10)
kurtis = Character('Kurtis', 30)
joshua = Character('Joshua', 5)
annalise = Character('Annalise Keating', 0)
main_players = [crystal.name, jojo.name, kurtis.name, joshua.name]

# Location Instantiation
josh_room = Location("Quiet Room", "pass")
liz_office = Location("Liz's Office", "pass")
elevator = Location("Elevator", "pass")
roof = Location("Roof", "pass")
kitchen = Location("Kitchen", "pass")
gym = Location("Gym", "pass")
security_desk = Location("Security Desk", "pass")
parking_garage = Location("Parking Garage", "pass")
community_center = Location("Community Center", "pass")
location_keys = {
    josh_room: liz_office,
}

# Items Instantiation
# Josh's Room
monitor = Item("monitor", josh_room)
jacket = Item("jacket", josh_room, 0, -10)
bag_of_chips = Item("bag of chips", josh_room, 5)
items_josh_room = [monitor.name, jacket.name, bag_of_chips.name]

# Liz's Room
#print("You are in Liz Carley room. Take a\n look around, but don't take\n too long, it will look suspicious if she\n catches you.")
tshirt = Item("tshirt", liz_office, 0, -10)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office)
keyboard = Item("keyboard", liz_office, 15)
items_liz_room = [tshirt.name, book.name, keyboard.name]

# # Elevator
#print("You are in the elevator. This gives you access to anywhere in the building")
key_card = Item("Dropped Key Card", elevator)
trash_can = Item("Trash Can", elevator, 5, -10)
items_elevator = [key_card.name, trash_can.name]

# # Roof
# print("You are on the roof.\n Its a stormy evening and walking around dripping\n water might draw a few eyes.\n Better hurry and gather supplies")
tarp = Item("tarp", roof, 5, -15)
chair = Item("chair", roof, 15)
firepit = Item("firepit", roof, 5, -20)
items_roof = [tarp.name, chair.name, firepit.name]

# Kitchen
#print("You are in the kitchen.\n This is the busiest room in the building.\n You should do what you need to do quickly.")
sink = Item("sink", kitchen, -10)
bleach = Item("bleach", kitchen, -10)
freezer = Item("freezer", kitchen, 5)
items_kitchen = [sink.name, bleach.name, freezer.name]

# # Gym
#print("You are in the gym.\n Its pretty hot in here. Sweating might\n not be the best idea today, I wouldnt\n take too long in here")
shower = Item("shower", gym, -5)
shower_curtain = Item("shower_curtain", gym, -5)
weights = Item("weights", gym, +5)
items_gym = [shower.name, shower_curtain.name, weights.name]

# # Security Desk
security_desk = Item("security desk", security_desk,)
items_security_desk = [security_desk.name]

# Parking Garage
#print("CONGRATULATIONS\n\n The body is in the car are you got away with MURDER\n\n now what????????")
get_away_car = Item("Brittani in the get away car", parking_garage, -100)

# Community Center
#print("You are in the community center.\n Its a lot of cameras in here!")
arcade_game = Item("Arcade Game", community_center)
pillows = Item("Pillow", community_center)
ping_pong = Item("Ping Pong", community_center, -10)
rug = Item("Rug", community_center, -10)
blankets = Item("Blanket", community_center, -15)
items_community_center = [arcade_game.name,
                          pillows.name, ping_pong.name, rug.name, blankets.name]


# Menus

main_menu = ["Search for anything useful", "Look at my items",
             "Move to a new location", "Call the Police"]

item_use_menu = ["Use item", "Get rid of an item", "exit"]

# Functions


def print_menu(menu):
    for idx, choice in enumerate(menu):
        print(f"{idx+1}. {choice}")


def which_list(room):
    if room == josh_room:
        return items_josh_room
    if room == gym:
        return items_gym


def play_game():
    play_game = True
    while play_game:
        location_choice_list = [josh_room.name, elevator.name]
        print("Welcome to How To Get Away With Murder")
        # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
        #'''
        #Please choose a player
        #Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.
        #Jojo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.
        #Kurtis starts with alert level of 30. Detail oriented. Power: After #, his alert level penalty is decreased by half points.
        #Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't need a mess
        #'''
        print()  # Add in player stats and special characteristics
        print_menu(main_players)
        choosing_player = input("Please pick a player: ")
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
        print(
            f'You have selected {active_player.name} with an alert level of {active_player.alert_level}!')
        # Here we need to set the scene!
        #first time instructions count 
        #print("Welcome to 'How To Get Away With MURDER!'\n #active_player.name has just woke up in a small room\n in the Atlanta Tech Village with a dead body\n on the floor #(keeping vague)with all evidence pointing to them.\n Looking around, it doesn't look like anyone has\n noticed yet.active_player.name has dreams of being a top notch programmer\n and know that noone will believe they\n weren't the murderer, in fact\n active_player.name isn't even sure they didn't do it.\n Help active_player.name get away with this murder\n so one day their programming dreams can be achieved.\n Navigate through the school and gather items\n that will help escape pass the guard\n with the body to\n make it to the parking lot.\n But beware -- everything you \n find will not be helpful and dont leave \n too much evidence around or you\n may be discovered. Once you feel\n your you won't attract too much attention(alert level), try\n to sneak past the security desk and out the\n door. GOOD LUCK!\n\n\nTIPS:\n You must bring picked up items back to the murder room to use\nCarrying to many items at once will raise your alert level  ")
        #description 
        #print("You are in your first room, the 'MURDER ROOM'")
        curr_location = josh_room
        curr_items_list = which_list(curr_location)
        print("What would you like to do now?")
        print_menu(main_menu)
        print(curr_location.description)
        active_player.print_alert_status()
        main_menu_choice = input("Please choose: ")
        if main_menu_choice == "1":
            item_loop = True
            while item_loop:
                print_menu(curr_items_list)
                item_chosen = int(input("Which item would you like to pick up? "))
                active_player.add_items(curr_items_list[item_chosen-1])
                curr_items_list.pop(item_chosen-1)
                continue_choosing = input(
                    "Would you like to choose another item? y or n\n")
                if continue_choosing.lower() == "n":
                    item_loop = False

        # if main_menu_choice == "2":
        #     print_menu(active_player.items)
        #     if curr_location == josh_room:
        #         print_menu(item_use_menu)
        #         choice_item_use_menu = int(input("Please choose: "))
        #         if choice_item_use_menu == 1:  # use item: print items and ask to choose an item to use. Run method for using item. Kurti
        #         #elif choice_item_use_menu == 2:  # get rid of item: print items and ask to choose an item to get rid of. run method for removing item JoJo

        #         # else:  # exit: back to main_menu print main menu This might not be necessary

        #         # We need a location menu! Which two locations will be connected to the current location.
        # if main_menu_choice == "3":  # Move to a new location
        #     location_choice_list.append(location_keys[curr_location])
        #     print_menu(location_choice_list)
        # if main_menu_choice == "4":


play_game()
