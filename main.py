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
tshirt = Item("tshirt", liz_office, 0, -10)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office)
keyboard = Item("keyboard", liz_office, 15)
items_liz_room = [tshirt.name, book.name, keyboard.name]

# # Elevator
key_card = Item("Dropped Key Card", elevator)
trash_can = Item("Trash Can", elevator, 5, -10)
items_elevator = [key_card.name, trash_can.name]

# # Roof
tarp = Item("tarp", roof, 5, -15)
chair = Item("chair", roof, 15)
firepit = Item("firepit", roof, 5, -20)
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

# Parking Garage
get_away_car = Item("Brittani in the get away car", parking_garage, -100)

# Community Center
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
        print()  # Add in player stats and special characteristics
        print_menu(main_players)
        choosing_player = input("Please pick a player: ")
        if choosing_player == "1":
            active_player = crystal
        # if choosing_player == "2":
        #     active_player = jojo
        # if choosing_player == "3":
        #     active_player = kurtis
        # if choosing_player == "4":
        #     active_player = joshua
        # if choosing_player == "1000":
        #     active_player = annalise
        print(
            f'You have selected {active_player.name} with an alert level of {active_player.alert_level}!')
        # Here we need to set the scene!
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

        if main_menu_choice == "2":
            print_menu(active_player.items)
            if curr_location == josh_room:

                print_menu(item_use_menu)
                choice_item_use_menu = int(input("Please choose: "))
                if choice_item_use_menu == 1:
                    print_menu(active_player.items)
                    item_to_use = int(input("Choose which item to use:"))
                    for items in curr_items_list:
                        if items == active_player.items[item_to_use -1]:
                            string_item = str(item)
                            item_used = string_item.replace(".name", "")
                            print(item_used)
                    # active_player.item_used(active_player.items[item_to_use -1])
                    # print(active_player.items)  

                elif choice_item_use_menu == 2:  # get rid of item: print items and ask to choose an item to get rid of. run method for removing item JoJo
                    print("Which item would you like get rid of?")
                    print_menu(active_player.items)

                # else:  # exit: back to main_menu print main menu This might not be necessary

                # We need a location menu! Which two locations will be connected to the current location.
        if main_menu_choice == "3":  # Move to a new location
            location_choice_list.append(location_keys[curr_location])
            print_menu(location_choice_list)
        if main_menu_choice == "4":
            pass


play_game()
