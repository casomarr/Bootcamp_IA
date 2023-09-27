#Inheritance of class : https://www.geeksforgeeks.org/inheritance-in-python/

class GotCharacter(object):
    def __init__(self, first_name, is_alive):
        self.name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Comming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False
        print(self.is_alive)

