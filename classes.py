from subprocess import call
import os
import time


class Character:
    def __init__(self, name, alert_level, ability):
        self.name = name
        self.alert_level = alert_level
        self.items = []
        self.ability = ability
        self.hands = ["hands", True]
        self.shirt = ["shirt", True]
        self.parts = [self.hands, self.shirt]

    def print_alert_status(self):
        print(f"\n***Your alert level is: {self.alert_level}***\n")

    # item limit within list: cap number of items and allow user to get rid of an item
    def add_items(self, item):
        if item.on_use == False:
            for part in self.parts:
                if item.character_part == part[0]:
                    part[1] = False
        else:
            self.items.append(item)
        self.alert_level += item.alert_effect_pu
        play_game = self.alert_level_change(item)
        return play_game

    def alert_level_change(self, item):
        play_game = True
        if self.alert_level > 80:
            print("Your alert level is getting high! Be careful!")
        if self.alert_level < 0:
            self.alert_level = 0
        elif self.alert_level > 100:
            play_game = False
        else:    
            return play_game


# Create method for using items(when items are used they affect alert level => items.alert_effect_used) Kurtis

    def item_used(self, item):
        self.alert_level += item.alert_effect_used
        play_game = self.alert_level_change(item)
        if item.on_use == True:
            for part in self.parts:
                if item.character_part == part[0]:
                    part[1] = False
        self.items.remove(item)
        return play_game

    def losing_statement(self):
        print(f"Oh no, {self.name}! Your alert level was too high and they are suspicious! They are coming!!!\n\nYou have been caught! Better luck next time. You should find Ryan....")

    def walking_the_hallway(self):
        os.system('cls||clear')
        print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
        time.sleep(5)
        print("*----")
        time.sleep(1)
        os.system('cls||clear')
        print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
        print("**---")
        time.sleep(1)
        os.system('cls||clear')
        print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
        print("***--")
        time.sleep(1)
        os.system('cls||clear')
        print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
        print("****-")
        time.sleep(1)
        os.system('cls||clear')
        print("You are trying to escape! Good luck.\nRememeber, if your alert level is too high, you will get caught!\nIt's time to sneak down to the lobby. You gather up the body and head down the hall. Hopefully, no one catches you!")
        print("*****")
        time.sleep(1)
        os.system('cls||clear')

    def elevator_going_down(self):
        os.system('cls||clear')
        print('''
        | * |
        |   |
        |   |
        |   |
        |   |
        ''')
        time.sleep(1)
        os.system('cls||clear')
        print('''
        |   |
        | * |
        |   |
        |   |
        |   |
        ''')
        time.sleep(1)
        os.system('cls||clear')
        print('''
        |   |
        |   |
        | * |
        |   |
        |   |
        ''')
        time.sleep(1)
        os.system('cls||clear')
        print('''
        |   |
        |   |
        |   |
        | * |
        |   |
        ''')
        time.sleep(1)
        os.system('cls||clear')
        print('''
        |   |
        |   |
        |   |
        |   |
        | * |
        ''')
        time.sleep(1)
        os.system('cls||clear')

    def sneak_past_security(self):
        os.system('cls||clear')
        print("*----")
        time.sleep(1)
        os.system('cls||clear')
        print("-*---")
        time.sleep(1)
        os.system('cls||clear')
        print("--*--")
        time.sleep(1)
        os.system('cls||clear')
        print("---*-")
        time.sleep(1)
        os.system('cls||clear')
        print("----*")
        time.sleep(1)
        os.system('cls||clear')

    def casual_past_security(self):
        os.system('cls||clear')
        print("|----")
        time.sleep(1)
        os.system('cls||clear')
        print("-|---")
        time.sleep(1)
        os.system('cls||clear')
        print("--|--")
        time.sleep(1)
        os.system('cls||clear')
        print("---|-")
        time.sleep(1)
        os.system('cls||clear')
        print("----|")
        time.sleep(1)
        os.system('cls||clear')

    def garage_scene(self):
        print("You made it to the garage! You did it! But is Brittani waiting for you?")
        time.sleep(3)
        if self.alert_level < 55:
            print("She's driving the getaway car! You made it!")#<<<<----Create a great win statement!
        else:
            print("It looks like you were too big of a risk! She isn't coming. Good luck running with a body....\n")
            self.losing_statement()

        # Create method for removing items(when the character wants to remove the items they get removed from the list)JoJo
    # def remove_items(self, item):
    #     self.item.pop

    def __str__(self):
        return f"****You have chosen {self.name}! Congrats!****\n\n{self.name} has a starting alert level of {self.alert_level}.\n\nAlso, surprise! Each character has a hidden special ability.\nWe like to call {self.name}'s:\n****{self.ability}****"


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"You are in the {self.name}!\n{self.description}\n\n"


class Item:
    def __init__(self, name, associated_room, character_part="body", on_use=True, alert_effect_pu=0, alert_effect_used=0):
        self.name = name
        self.associated_room = associated_room
        self.character_part = character_part
        self.on_use = on_use
        self.alert_effect_pu = alert_effect_pu
        self.alert_effect_used = alert_effect_used

    def __str__(self):
        if self.on_use:
            time_of_use = "when used"
            level = self.alert_effect_used
            in_inventory = "will"
        else:
            time_of_use = "when picked up"
            level = self.alert_effect_pu
            in_inventory = "will not"
        return f"\nYou have chosen the {self.name}.\nThis item effects your alert level when {time_of_use}.\nIt has a {level} point effect on your alert level {time_of_use}.\nThis item {in_inventory} be in your inventory."