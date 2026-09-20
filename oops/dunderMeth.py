class NewClass:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        return "This is the string which will print when defined else will print the address of the object"

    def __len__(self):
        return len(self.items)
