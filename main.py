from classes import Character, Location, Item
from arcade import tic_tac_toe, number_guess
from ascii_art import arcade_screen, game_start_graphic, caught_graphic, get_away_graphic, win_graphic , guess_number_graphic
from subprocess import call
import os
from tqdm import tqdm
import time
os.system('cls' if os.name == 'nt' else 'clear')
from pygame import mixer
mixer.init()

# Music
def sound(file):
    sound = mixer.Sound(f"audio/{file}")
    return mixer.Sound.play(sound)



# this is our main program


# Character Instantiation
crystal = Character('Crystal', 40, "she", "her", "Crystal starts with alert level of 40. Resourceful. Power: She can move to any room without the elevator.")
jojo = Character('JoJo', 10, "she", "her", "JoJo starts with alert level of 10. Sneaky. Power: She can carry 1 extra item.")
kurtis = Character('Kurtis', 30, "he", "his", "Kurtis starts with alert level of 30. Detail oriented. Power: After 80, his alert level penalty is decreased by half points.")
joshua = Character('Joshua', 5, "he", "his","Joshua starts with alert level of 5. Obsessive compulsive. Power: Doesn't leave a mess")
annalise = Character('Annalise Keating', 0, "she", "her", "No mistakes!")
main_players = [crystal, jojo, kurtis, joshua]

# Location Instantiation
josh_room = Location("Sean's hide-out", "\nYou are in your first room, the 'MURDER ROOM'.")
liz_office = Location("Liz's Office", "\nTake a look around, but don't take too long, it will look suspicious if she catches you.")
elevator = Location("Elevator", "\nThis gives you access to anywhere in the building.")
roof = Location("Roof", "\nIt's a stormy evening and walking around dripping water might draw a few eyes. Better hurry and gather supplies.")
kitchen = Location("Kitchen", "\nThis is the busiest room in the building. You should do what you need to do quickly.")
gym = Location("Gym", "\nIt's pretty hot in here. Sweating might not be the best idea today, I wouldn't take too long in here.")
security_desk = Location("Security Desk", "security desk description")
parking_garage = Location("Parking Garage", "parking garage description")
community_center = Location("Community Center", "\nYou are in the community center. Its a lot of cameras in here!")
location_keys = {
    josh_room: [liz_office, kitchen, elevator],
    liz_office: [josh_room, kitchen, elevator],
    kitchen: [liz_office, josh_room, elevator],
    elevator: [liz_office, josh_room, kitchen, roof, community_center, gym],
    roof: [elevator],
    community_center: [elevator],
    gym: [elevator]
}
# crystal_location = {
#  josh_room: [liz_office, kitchen, elevator, roof, community_center, gym],
#     liz_office: [josh_room, kitchen, elevator, roof, community_center, gym,
#     kitchen: [liz_office, josh_room, elevator, roof, community_center, gym],
#     elevator: [liz_office, josh_room, kitchen, roof, community_center, gym],
#     roof: [liz_office, josh_room, kitchen, community_center, gym, elevator],
#     community_center: [liz_office, josh_room, kitchen, roof, community_center, gym],
#     gym: [liz_office, kitchen, elevator, roof, community_center, josh_room]
# }


# Items Instantiation
# Josh's Room
monitor = Item("monitor", josh_room, "pass", False, 40)
jacket = Item("jacket", josh_room, "shirt", False, -25)
bag_of_chips = Item("bag of chips", josh_room, "pass", "pass", 35)
items_josh_room = [monitor, jacket, bag_of_chips]

# Liz's Room
tshirt = Item("t-shirt", liz_office, "shirt", False, -20)
# input code in book and if you can solve unlocks ryan phone number and he distracts security guard for you
book = Item("book", liz_office, "pass", "pass")
keyboard = Item("keyboard", liz_office, "pass", "pass", 20)
items_liz_office = [tshirt, book, keyboard]

# # Elevator
key_card = Item("Dropped Key Card", elevator, "pass", "pass")
trash_can = Item("Trash Can", elevator, "pass", "pass", 0, -10)
items_elevator = [key_card, trash_can]

# # Roof
tarp = Item("tarp", roof, "pass", "pass", 0, -25)
chair = Item("chair", roof, "pass", False, 20)
firepit = Item("firepit", roof, "pass", False, 20)
items_roof = [tarp, chair, firepit]

# Kitchen
sink = Item("sink", kitchen, "hands", False,  -15)
bleach = Item("bleach", kitchen, "hands", "pass", 0, -10)
freezer = Item("freezer", kitchen, "pass", False)
items_kitchen = [sink, bleach, freezer]

# # Gym
shower = Item("shower", gym, "hands", False, -5)
shower_curtain = Item("shower curtain", gym, "pass", "pass", 0, -5)
weights = Item("weights", gym, "pass", "pass", 0, 35)
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
pillows = Item("Pillow", community_center, "pass", False, 15)
ping_pong = Item("Ping Pong", community_center, "pass", False, 10)
rug = Item("Rug", community_center, "pass", "pass", 0, -5)
blankets = Item("Blanket", community_center, "pass", "pass", 0, -15)
items_community_center = [arcade_game,
                          pillows, ping_pong, rug, blankets]

all_items = [monitor, jacket, bag_of_chips, tshirt, book, keyboard, key_card, trash_can, tarp, chair, firepit, sink, bleach,
             freezer, shower, shower_curtain, weights, security_desk, get_away_car, arcade_game, pillows, ping_pong, rug, blankets]

# Menus

main_menu = ["Search for anything useful", "Look at my items",
             "Move to a new location", "Call the Police"]

elevator_only_menu = ["Search for anything useful", "Look at my items",
             "Go to the Elevator", "Call the Police"]

item_use_menu = ["Use item", "Get rid of an item", "exit"]

josh_room_menu = ["Search for anything useful", "Look at my items", "Move to a new location",
                  "Call the Police", "Attempt to Escape with the body"]

josh_room_menu_with_code = ["Search for anything useful", "Look at my items", "Move to a new location",
                            "Attempt to Escape with the body", "Call the Police", "Attempt to Escape with the body", "***Call Ryan***"]

arcade_menu = ["tic-tac-toe", "guess my number", "EXIT"]


# Functions

def choosing_active_player():
    print()  # Add in player stats and special characteristics
    print_menu(main_players)
    active_player = True
    while active_player == True:
        choosing_player = input("Please pick a player: ")
        if choosing_player == "1":
            active_player = crystal
        elif choosing_player == "2":
            active_player = jojo  
        elif choosing_player == "3":
            active_player = kurtis    
        elif choosing_player == "4":
            active_player = joshua      
        elif choosing_player == "1000":
            active_player = annalise
        else:
            print("Please choose provided options: ")
    os.system('cls||clear')
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
    while True:
        try:
            full_menu_remove_choice = int(
            input("Which item would you like to remove?"))
            if full_menu_remove_choice <= len(player.items):
                break
            else:
                print("That is not an option. ")
        except ValueError:
            print("That is not an option, please choose provided options: ")
    player.items.pop(full_menu_remove_choice - 1)
    print("Your item has been removed")

def play_arcade_game():
    os.system('cls||clear')
    while True:
        arcade_screen()
        print("What would you like to play?")
        print_string_menu(arcade_menu)
        try:
            game_choice = int(input("Please choose: "))
            if game_choice > 3:
                print("That is not an option! Please try again.")
                time.sleep(3)
                os.system('cls||clear')
            elif game_choice == 1:
                tic_tac_toe()
            elif game_choice == 2:
                number_guess()
            elif game_choice == 3:
                os.system('cls||clear')
                return True
        except ValueError:
            print("That is not an option. Please try again.")
            time.sleep(3)
            os.system('cls||clear')

def main_menu_choice_1(list_option, player):
    item_loop = True
    play_game = True
    while item_loop:
        print_menu(list_option)
        if len(player.items) >= 5:
            while True:
                full_menu_choice = (input(
                    "You are already holding the maximum number of items. Would you like to remove one? y or n:  "))
                if full_menu_choice.lower() == "y":
                    remove_item_from_inventory(player)
                    break
                elif full_menu_choice == "n":
                    item_loop = False
                    break
                # incorrect responce error catch
                else:
                    print("\nThat is not a valid option, try again:") 
        elif len(list_option) == 0:
            print("\nThere are no items left in this room")
            item_loop = False     
        else:
            try:
                item_chosen = int(input(
                    f"Which item would you like {player.name} to pick up or use?\nNote: To exit, press 9.\nPlease choose: "))
                if item_chosen == 9:
                    item_loop = False
                elif item_chosen > len(list_option):
                    print("\nThat is not an option, try again:")
                else:
                    choice_item = list_option[item_chosen-1]
                    if choice_item == arcade_game:
                        play_game = play_arcade_game()
                        return play_game
                    play_game = player.add_items(choice_item)
                    print(choice_item)
                    player.alert_banner()
                    #player.print_alert_status()
                    list_option.pop(item_chosen-1)
                    if len(list_option) > 0:
                        continue_choosing = input(
                            "Would you like to choose another item? y or n\n")
                        if continue_choosing.lower() == "y":
                            pass
                        elif continue_choosing.lower() == "n":
                            os.system('cls||clear')
                            item_loop = False
                        else:
                            print("That isn't an option. Please choose 'y' or 'n': ")
            except ValueError:
                print("Please choose an available menu choice!")
    return play_game

def main_menu_choice_2(location, player, list_option):
    play_game = True
    if len(player.items) > 0:
        print_menu(player.items)
        user_input = input("Press ENTER to continue")
    else:
        print("\n**You have no items in your inventory.**\n")
        return play_game
    if user_input == "041221":
            print("You have unlocked the secret line to Ryan!\nNo worries, Ryan knows how to get rid of a body.\nYou can continue practicing your programming...\n\n\n*****GAME OVER*****")
            win_graphic()
            play_game = "fart"
    elif location == josh_room:
        print_string_menu(list_option)
        while True:
            try:
                choice_item_use_menu = int(input("Please choose: "))
                if choice_item_use_menu == 1:
                    print_menu(player.items)
                    while True:
                        try:
                            user_choice = int(input("Choose which item to use:")) 
                            if user_choice <= len(player.items):
                                item_being_used = player.items[user_choice-1]
                                play_game = player.item_used(item_being_used)
                                return play_game
                            else:
                                print("That is not a valid choice! Try again.")
                        except ValueError:
                            print("That is not an option. Please try again.")
                if choice_item_use_menu == 2:
                    remove_item_from_inventory(player)
                    break
                if choice_item_use_menu == 3:
                    break
                else:
                    print("Please choose an available menu choice")
            except ValueError:
                print("Please choose an available menu choice")
    return play_game

def main_menu_choice_3(location, player):
    location_list = []
    if len(location_keys[location]) == 1 and location_keys[location][0] == elevator:
        new_location = elevator
        print("\n\n***You must take the elevator to your next location.***")
    else:
        for loc in location_keys[location]:
            location_list.append(loc)        
        print("Where would you like to go?")
        print_location_options(location_list)
        while True:
            try:
                location_choice = int(input("Please choose: "))
                if location_choice <= len(location_list):
                    new_location = location_list[location_choice - 1]
                    if location == elevator:
                        player.elevator_going_down()
                    else:
                        sound("footsteps.wav")
                        print("\n\nWalking.....")
                        for i in tqdm(range(int(13e6))): 
                            pass
                        time.sleep(3)
                    break
                else:
                    print("That is not a valid choice. Please try again.")
            except ValueError:
                print("That is not a valid choice. Please try again.")
    return new_location

def main_menu_choice_5(location, player):
    os.system('cls||clear')
    print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!\n*-----")
    player.walking_the_hallway()
    if player.alert_level < 90 and player.hands[1] == False and player.shirt[1] == False:
        while True:
            escape_input = input("You made it to the elevator! Please press 1 to go down to the garage.\nHopefully, no one joins you in the elevator!")
            if player.alert_level < 75 and escape_input == "1":
                player.elevator_going_down()
                print("You made it to the garage level without getting caught! Now you must sneak past the security guard! Good luck!")
                while True:
                    try:
                        escape_input = int(input("Press 1 to sneak and 2 to act casual."))
                        if escape_input > 2:
                            print("That isn't a choice! Choose a valid option quickly so you can escape!!!")
                        elif player.alert_level < 60 and escape_input == 1:
                            player.sneak_past_security()
                            player.garage_scene()
                            return False
                        elif player.alert_level < 50 and escape_input == 2:
                            player.casual_past_security()
                            player.garage_scene()
                            return False
                        else:
                            player.losing_statement()
                            return False
                    except ValueError:
                        print("C'mon! Pick an option! You are running out of time!")
            elif player.alert_level < 75:
                print("That isn't an option! Not when you have a body to move.\nYou need to choose the first floor quickly before someone jumps on the elevator with you!")
            else:
                player.losing_statement()
                return False
    else:
        player.losing_statement()
    return False

def play_game():
    continue_playing = True
    while continue_playing:
        os.system('cls||clear')
        game_start_graphic()# Here we can have a graphic for our game...
        # We need some info here about the game....so you know what character you want to choose, must use items in Josh's room!
        print('Loading Game')
        for i in tqdm(range(int(9e6))): 
            pass
        print('Loading Graphics')
        for i in tqdm(range(int(13e6))): 
            pass
        print('Loading Objects')
        for i in tqdm(range(int(18e6))): 
            pass
        print('Loading Murderer')
        for i in tqdm(range(int(25e6))): 
            pass
        print(f'''
*****Player Characteristics******
Crystal starts with alert level of {crystal.alert_level}. Resourceful. Power: She can move to any room without the elevator.

Jojo starts with alert level of {jojo.alert_level}. Sneaky. Power: She can carry 1 extra item.

Kurtis starts with alert level of {kurtis.alert_level}. Detail oriented. Power: After 80, his alert level penalty is decreased by half points.

Joshua starts with alert level of {joshua.alert_level}. Obsessive compulsive. Power: Doesn't leave a mess.
        ''')  # Add in player stats and special characteristics
        active_player = choosing_active_player()
        welcome_message = f"Welcome to 'How To Get Away With MURDER!'\n\n{active_player.name} just woke up in a small room in the Atlanta Tech Village with a dead body on the floor, bloody clothes and hands, with all evidence pointing to {active_player.pronoun2}.\nAfter looking around, it doesn't look like anyone has noticed yet. \n{active_player.name} has dreams of becoming a top notch programmer and knows that noone will believe {active_player.pronoun} wasn't the murderer.\nIn fact, {active_player.name} isn't even sure {active_player.pronoun} didn't do it. \n\nHelp {active_player.name} get away with this murder so one day {active_player.pronoun2} programming dreams can be achieved. \n\nNavigate through the school and gather items that will help {active_player.pronoun2} escape past the guard with the body to make it to the parking lot. \nBut beware -- everything you find will not be helpful and dont leave too much evidence around or you may be discovered. \nOnce you feel like you won't attract too much attention(alert level), try to sneak past the security desk and out of the door. \n\n\n****GOOD LUCK!****\n\n\nTIPS: \n*You must bring picked up items back to the murder room to use them. \n*Carrying too many items at once will raise your alert level.\n\n\n"
        sound("breathing.wav")
        print(welcome_message)
        curr_location = josh_room
        code_unlocked = False
        play_game = True
        hands = "dirty"
        shirt = "dirty"
        continue_on = input("Press ENTER to continue")
        while play_game:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(curr_location)
            curr_items_list = which_list(curr_location)
            same_location = True
            while same_location:
                # print(curr_location.name)
                active_player.alert_banner()
                #active_player.print_alert_status()
                print(f"What would you like {active_player.name} to do now?")
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
                    if play_game == "fart":
                        play_game = False
                        same_location = False
                elif main_menu_choice == "2":
                    play_game = main_menu_choice_2(curr_location, active_player, item_use_menu)
                    if play_game == "fart":
                        play_game = False
                        same_location = False
                elif main_menu_choice == "3":  # Move to a new location
                    curr_location = main_menu_choice_3(curr_location, active_player)
                    same_location = False
                elif main_menu_choice == "4":
                    play_game = False
                    same_location = False
                    print("The police are on their way! You lose!")
                    sound("siren.wav")
                    sound("siren2.wav")
                    caught_graphic()
                elif main_menu_choice == "5":
                    play_game = main_menu_choice_5(curr_location, active_player)
                    same_location = False
                else:
                    print("That isn't a choice. Please choose a valid option this time, silly!")
        play_again = input("Would you like to play again? 'Y' or 'N': ")
        if play_again.lower() == 'y':
            continue_playing = True
        elif play_again.lower() == 'n':
            continue_playing = False
        else:
            print("That isn't a choice! Please choose a valid option.")




play_game()
