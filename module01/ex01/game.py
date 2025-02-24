""" Inheritance of class : usefull for several reasons :
	1. you ensure all child classes have some common attributes that can easily be changed
	2. you avoid having to copy/paste a certain number of attributes in each child class
 """

class GotCharacter(object):
	def __init__(self, first_name, is_alive):
		self.name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	"""A class representing the Stark family."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive) #this line makes our character to be initialized in the GotCharacter parent class
		self.family_name = "Stark"
		self.house_words = "Winter is Comming"
	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

class Lannister(GotCharacter):
	"""A class representing the Lannister family."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Lannister"
		self.house_words = "Hear Me Roar!"
	def print_house_words(self):
		print(self.house_words)
	def die(self):
		self.is_alive = False

