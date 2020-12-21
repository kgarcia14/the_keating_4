from classes import Character, Location, Item
from subprocess import call
import os
import time



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
book = Item("book", liz_office, "pass", "pass")
keyboard = Item("keyboard", liz_office, "pass", "pass", 0, 15)
items_liz_office = [tshirt, book, keyboard]

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
sink = Item("sink", kitchen, "hands", False,  -10)
bleach = Item("bleach", kitchen, "hands", "pass", 0, -10)
freezer = Item("freezer", kitchen, "pass", False)
items_kitchen = [sink, bleach, freezer]

# # Gym
#print("You are in the gym.\n Its pretty hot in here. Sweating might\n not be the best idea today, I wouldnt\n take too long in here")
shower = Item("shower", gym, "hands", False, -5)
shower_curtain = Item("shower_curtain", gym, "pass", "pass", 0, -5)
weights = Item("weights", gym, "pass", "pass", 0, 15)
items_gym = [shower, shower_curtain, weights]

# # Security Desk
security_desk = Item("security desk", security_desk,)
items_security_desk = [security_desk.name]

# Parking Garage
#print("CONGRATULATIONS\n\n The body is in the car are you got away with MURDER\n\n now what????????")
get_away_car = Item("Brittani in the get away car", parking_garage, -100)

# Community Center
#print("You are in the community center.\n Its a lot of cameras in here!")
arcade_game = Item("Arcade Game", community_center, "pass", "pass")
pillows = Item("Pillow", community_center, "pass", False, 10)
ping_pong = Item("Ping Pong", community_center, "pass", False, 5)
rug = Item("Rug", community_center, -10, "pass", "pass", 0, -5)
blankets = Item("Blanket", community_center, "pass", "pass", 0, -15)
items_community_center = [arcade_game,
                          pillows, ping_pong, rug, blankets]


# Menus

main_menu = ["Search for anything useful", "Look at my items",
             "Move to a new location", "Call the Police"]

item_use_menu = ["Use item", "Get rid of an item", "exit"]

josh_room_menu = ["Search for anything useful", "Look at my items", "Move to a new location",
                  "Call the Police", "Attempt to Escape with the body"]

josh_room_menu_with_code = ["Search for anything useful", "Look at my items", "Move to a new location",
                            "Attempt to Escape with the body", "Call the Police", "Attempt to Escape with the body", "***Call Ryan***"]


# Functions


def print_menu(menu):
    for idx, choice in enumerate(menu):
        print(f"{idx+1}. {choice}")


def which_list(room):
    if room == josh_room:
        return items_josh_room
    if room == gym:
        return items_gym

def main_menu_choice_5(location, player):
    call('clear' if os.name == 'posix' else 'cls')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!\n*-----")
    player.walking_the_hallway()
    if player.alert_level < 90:
        escape_input = int(input("You made it to the elevator! Please press 1 to go down to the garage.\nHopefully, no one joins you in the elevator!"))
        if player.alert_level < 80 and escape_input == 1:
            player.elevator_going_down()
            escape_input = int(input("You made it to the garage level without getting caught! Now you must sneak past the security guard! Good luck! Press 1 to sneak and 2 to act casual."))
            if player.alert_level < 70 and escape_input == 1:
                player.sneak_past_security()
                player.garage_scene()
                return False
            elif player.alert_level < 60 and escape_input == 2:
                player.casual_past_security()
                player.garage_scene()
                return False
            else:
                player.losing_statement()
                return False
        else:
            player.losing_statement()
            return False
    else:
        player.losing_statement()
    return False

def play_game():
    call('clear' if os.name == 'posix' else 'cls')
    # location_choice_list = [josh_room.name, elevator.name]
    print("Welcome to How To Get Away With Murder")
    # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
    print()  # Add in player stats and special characteristics
    active_player = choosing_active_player()
    curr_location = josh_room
    code_unlocked = False
    play_game = True
    time.sleep(5)
    while play_game:
        # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
        #'''
        #Please choose a player
        #Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.
        #Jojo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.
        #Kurtis starts with alert level of 30. Detail oriented. Power: After #, his alert level penalty is decreased by half points.
        #Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't need a mess
        #'''
        # Here we need to set the scene!
        #first time instructions count 
        #print("Welcome to 'How To Get Away With MURDER!'\n #active_player.name has just woke up in a small room\n in the Atlanta Tech Village with a dead body\n on the floor #(keeping vague)with all evidence pointing to them.\n Looking around, it doesn't look like anyone has\n noticed yet.active_player.name has dreams of being a top notch programmer\n and know that noone will believe they\n weren't the murderer, in fact\n active_player.name isn't even sure they didn't do it.\n Help active_player.name get away with this murder\n so one day their programming dreams can be achieved.\n Navigate through the school and gather items\n that will help escape pass the guard\n with the body to\n make it to the parking lot.\n But beware -- everything you \n find will not be helpful and dont leave \n too much evidence around or you\n may be discovered. Once you feel\n your you won't attract too much attention(alert level), try\n to sneak past the security desk and out the\n door. GOOD LUCK!\n\n\nTIPS:\n You must bring picked up items back to the murder room to use\nCarrying to many items at once will raise your alert level  ")
        #description 
        #print("You are in your first room, the 'MURDER ROOM'")

        call('clear' if os.name == 'posix' else 'cls')
        print(curr_location)
        curr_items_list = which_list(curr_location)
        same_location = True
        while same_location:
            active_player.print_alert_status()
            print("What would you like to do now?")
            elevator_only = False
            if len(location_keys[curr_location]) == 1 and location_keys[curr_location][0] == elevator:
                elevator_only = True
                print_string_menu(elevator_only_menu)
            elif curr_location == josh_room:
                print_string_menu(josh_room_menu)
            elif code_unlocked == True:
                print_string_menu(josh_room_menu_with_code)
            else:
                print_string_menu(main_menu)
            main_menu_choice = input("Please choose: ")
            if main_menu_choice == "1":
                play_game = main_menu_choice_1(curr_items_list, active_player)
            if main_menu_choice == "2":
                play_game = main_menu_choice_2(curr_location, active_player, item_use_menu)
            if main_menu_choice == "3":  # Move to a new location
                curr_location = main_menu_choice_3(curr_location)
                same_location = False
            if main_menu_choice == "4":
                play_game = False
            if main_menu_choice == "5":
                play_game = main_menu_choice_5(curr_location, active_player)
                same_location = False




play_game()
