class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item = [self.name, self.description]

    def __str__(self):
        return f'Item:{self.name}, Desc:{self.description}'