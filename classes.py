
class Character:
    def __init__(self, name, alert_level):
        self.name = name
        self.alert_level = alert_level
        self.items = []

    def change_alert(self, location, item_idx):
        self.alert_level += location.item[item_idx]

    def print_alert_status(self):
        print(self.alert_level)

    # item limit within list: cap number of items and allow user to get rid of an item
    def add_items(self, item):
        self.items.append(item)

    def item_used(self):
        self.alert_level

        # Create method for using items(when items are used they affect alert level => items.alert_effect_used) Kurtis

        # Create method for removing items(when the character wants to remove the items they get removed from the list)JoJo
    def remove_items(self, item):
        self.item.pop




class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Item:
    def __init__(self, name, associated_room, alert_effect_pu=0, alert_effect_used=0):
        self.name = name
        self.associated_room = associated_room
        self.alert_effect_pu = alert_effect_pu
        self.alert_effect_used = alert_effect_used
