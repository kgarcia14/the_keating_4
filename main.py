from classes import Character, Location, Item
from subprocess import call
import os


# this is our main program


# Character Instantiation
crystal = Character('Crystal', 40, "Unsuspected")
jojo = Character('JoJo', 10, "placeholder")
kurtis = Character('Kurtis', 30, "placeholder")
joshua = Character('Joshua', 5, "place holder")
annalise = Character('Annalise Keating', 0, "No mistakes!")
main_players = [crystal, jojo, kurtis, joshua]

# Location Instantiation
josh_room = Location("Sean's hide-out", "Sean's hide-out description")
liz_office = Location("Liz's Office", "Liz's Office description")
elevator = Location("Elevator", "elevator description")
roof = Location("Roof", "roof description")
kitchen = Location("Kitchen", "kitchen description")
gym = Location("Gym", "gym description")
security_desk = Location("Security Desk", "security desk description")
parking_garage = Location("Parking Garage", "parking garage description")
community_center = Location("Community Center", "community center description")
location_keys = {
    josh_room: [liz_office, kitchen, elevator],
    liz_office: [josh_room, kitchen, elevator],
    kitchen: [liz_office, josh_room, elevator],
    elevator: [liz_office, josh_room, kitchen, roof, community_center, gym],
    roof: [elevator],
    community_center: [elevator],
    gym: [elevator]
}


# Items Instantiation
# Josh's Room
monitor = Item("monitor", josh_room, "pass", False, 10)
jacket = Item("jacket", josh_room, "shirt", False, -10)
bag_of_chips = Item("bag of chips", josh_room, "pass", "pass", 5)
items_josh_room = [monitor, jacket, bag_of_chips]

# Liz's Room
tshirt = Item("t-shirt", liz_office, "shirt", False, -10)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office, "pass", "pass")
keyboard = Item("keyboard", liz_office, "pass", "pass", 15)
items_liz_office = [tshirt, book, keyboard]

# # Elevator
key_card = Item("Dropped Key Card", elevator, "pass", "pass")
trash_can = Item("Trash Can", elevator, "pass", "pass", 0, -10)
items_elevator = [key_card, trash_can]

# # Roof
tarp = Item("tarp", roof, "pass", "pass", 0, -15)
chair = Item("chair", roof, "pass", "pass", 15)
firepit = Item("firepit", roof, "pass", "pass", 0, -20)
items_roof = [tarp, chair, firepit]

# Kitchen
sink = Item("sink", kitchen, "hands", False,  -10)
bleach = Item("bleach", kitchen, "hands", False, -10)
freezer = Item("freezer", kitchen, "pass", "pass", 5)
items_kitchen = [sink, bleach, freezer]

# # Gym
shower = Item("shower", gym, "hands", False, -5)
shower_curtain = Item("shower_curtain", gym, "pass", "pass", -5)
weights = Item("weights", gym, "pass", "pass", 5)
items_gym = [shower, shower_curtain, weights]

# # Security Desk
security_desk = Item("security desk", security_desk, "pass", "pass")
items_security_desk = [security_desk]

# Parking Garage
get_away_car = Item("Brittani in the get away car",
                    parking_garage, "pass", "pass", -100)
items_parking_garage = [get_away_car]

# Community Center
arcade_game = Item("Arcade Game", community_center, "pass", "pass")
pillows = Item("Pillow", community_center, "pass", "pass")
ping_pong = Item("Ping Pong", community_center, "pass", "pass", -10)
rug = Item("Rug", community_center, -10, "pass", "pass")
blankets = Item("Blanket", community_center, "pass", "pass", -15)
items_community_center = [arcade_game,
                          pillows, ping_pong, rug, blankets]

all_items = [monitor, jacket, bag_of_chips, tshirt, book, keyboard, key_card, trash_can, tarp, chair, firepit, sink, bleach,
             freezer, shower, shower_curtain, weights, security_desk, get_away_car, arcade_game, pillows, ping_pong, rug, blankets]

# Menus

main_menu = ["Search for anything useful", "Look at my items",
             "Move to a new location", "Call the Police"]

item_use_menu = ["Use item", "Get rid of an item", "exit"]

josh_room_menu = ["Look at my items", "Move to a new location",
                  "Attempt to Escape with the body", "Call the Police"]

josh_room_menu_with_code = ["Look at my items", "Move to a new location",
                            "Attempt to Escape with the body", "Call the Police", "***Call Ryan***"]


# Functions

def choosing_active_player():
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
    print(active_player)
    return active_player


def print_string_menu(menu):
    for idx, choice in enumerate(menu):
        print(f"{idx+1}. {choice}")


def print_menu(menu):
    for idx, choice in enumerate(menu):
        # print(type(choice))
        print(f"{idx+1}. {choice.name}")


def print_location_options(location_options):
    location_name_list = []
    for location in location_options:
        location_name_list.append(location)
    for idx, choice in enumerate(location_name_list):
        print(f"{idx+1}. {choice.name}")


def which_list(room):
    if room == josh_room:
        return items_josh_room
    if room == liz_office:
        return items_liz_office
    if room == elevator:
        return items_elevator
    if room == roof:
        return items_roof
    if room == kitchen:
        return items_kitchen
    if room == gym:
        return items_gym
    if room == security_desk:
        return items_security_desk
    if room == parking_garage:
        return items_parking_garage
    if room == community_center:
        return items_community_center


def remove_item_from_inventory(player):
    print_menu(player.items)
    full_menu_remove_choice = int(
        input("Which item would you like to remove?"))
    player.items.pop(full_menu_remove_choice - 1)
    print("Your item has been removed")


def main_menu_choice_1(list_option, player):
    item_loop = True
    while item_loop:
        print_menu(list_option)
        if len(player.items) >= 5:
            full_menu_choice = (input(
                "You are already holding the maximum number of items. Would you like to remove one? y or n:  "))
            if full_menu_choice.lower() == "y":
                remove_item_from_inventory(player)
            elif full_menu_choice == "n":
                pass
            # incorrect responce error catch
            else:
                print()
                pass
        else:
            try:
                item_chosen = int(input(
                    "Which item would you like to pick up?\nNote: To exit, press 9.\nPlease choose: "))
                if item_chosen == 9:
                    item_loop = False
                else:
                    choice_item = list_option[item_chosen-1]
                    player.add_items(choice_item)
                    print(choice_item)
                    player.print_alert_status()
                    list_option.pop(item_chosen-1)
                    continue_choosing = input(
                        "Would you like to choose another item? y or n\n")
                    if continue_choosing.lower() == "n":
                        item_loop = False
            except ValueError:
                print("Please choose an available menu choice!")


def main_menu_choice_2(location, player, list_option):
    if len(player.items) > 0:
        print_menu(player.items)
    else:
        print("You have no items in your inventory.")
    if location == josh_room:
        print_string_menu(list_option)
        choice_item_use_menu = int(input("Please choose: "))
        if choice_item_use_menu == 1:
            print_menu(player.items)
            user_choice = int(input("Choose which item to use:"))
            item_being_used = player.items[user_choice-1]
            player.item_used(item_being_used)
        elif choice_item_use_menu == 2:  # get rid of item: print items and ask to choose an item to get rid of. run method for removing item JoJo
            remove_item_from_inventory(player)


def main_menu_choice_3(location):
    location_list = []
    if len(location_keys[location]) == 1 and location_keys[location][0] == elevator:
        new_location = elevator
        print("\n\n***You must take the elevator to your next location.***")
    else:
        for location in location_keys[location]:
            location_list.append(location)
        print("Where would you like to go?")
        print_location_options(location_list)
        location_choice = int(input("Please choose: "))
        new_location = location_list[location_choice - 1]
    return new_location


def play_game():
    call('clear' if os.name == 'posix' else 'cls')
    # location_choice_list = [josh_room.name, elevator.name]
    print("Welcome to How To Get Away With Murder")
    # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
    print()  # Add in player stats and special characteristics
    active_player = choosing_active_player()
    curr_location = josh_room
    play_game = True
    while play_game:
        call('clear' if os.name == 'posix' else 'cls')
        print(curr_location)
        curr_items_list = which_list(curr_location)
        same_location = True
        while same_location:
            active_player.print_alert_status()
            print("What would you like to do now?")
            print_string_menu(main_menu)
            main_menu_choice = input("Please choose: ")
            if main_menu_choice == "1":
                main_menu_choice_1(curr_items_list, active_player)
            if main_menu_choice == "2":
                main_menu_choice_2(curr_location, active_player, item_use_menu)
            if main_menu_choice == "3":  # Move to a new location
                curr_location = main_menu_choice_3(curr_location)
                same_location = False
            if main_menu_choice == "4":
                play_game = False
            call('clear' if os.name == 'posix' else 'cls')


play_game()
