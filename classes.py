
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
    def __init__(self, name, associated_room, alert_effect_pu=0, alert_level_used=0):
        self.name = name
        self.associated_room = associated_room
        self.alert_effect_pu = alert_effect_pu
        self.alert_effect_used = alert_effect_used
