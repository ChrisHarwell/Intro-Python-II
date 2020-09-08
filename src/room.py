# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f'Location: {self.name} \nDescription: {self.description} \n Items: {self.items}'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)