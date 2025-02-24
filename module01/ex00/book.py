from datetime import datetime

class Book :
	def __init__(self, name, last_update, creation_date, recipes_list):
		if not isinstance(name, str) or not name:
			raise ValueError("Name should be a non-empty string")
		if not isinstance(last_update, datetime):
			raise ValueError("Last Update should be a datetime")
		if not isinstance(creation_date, datetime):
			raise ValueError("Creation Date should be a datetime")
		if not isinstance(recipes_list, dict) or not all(key in recipes_list for key in["starter", "lunch", "dessert"]):
			raise ValueError("Recipes List should be a dictionnary with keys starter, lunch and dessert")
		
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for recipe_type in self.recipes_list.values(): #.values() to be added only for for loops, not if statements
			for recipe in recipe_type.values(): #if I don't add .values() I am not iterating over objects
				if recipe.name == name:
					print(recipe)
					return recipe
		print(f"Recipe {name} not found")
		return None

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		if recipe_type in self.recipes_list:
			for recipe in self.recipes_list[recipe_type].values():
				print(recipe)
			return self.recipes_list[recipe_type]
		print(f"Recipe type {recipe_type} not found")
		return None

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if recipe in self.recipes_list[recipe.recipe_type].values():
			print(f"Recipe {recipe.name} is already in book")
		elif recipe.recipe_type not in self.recipes_list:
			print("Recipe type is incorrect : recipe cannot be added to book")
		else:
			self.recipes_list[recipe.recipe_type][recipe.name] = recipe #.append() pour rajouter quelque chose à une key dans un dico
			self.last_update = datetime.now()