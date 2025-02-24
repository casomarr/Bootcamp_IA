# import sys

class Recipe :
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if not isinstance(name, str) or not name :
			raise ValueError("Name must be a non-empty string")
		if not isinstance (cooking_lvl, int) or not 1 <= cooking_lvl <= 5:
			raise ValueError("Cooking Level must be an integer between 1 and 5")
		if not isinstance(cooking_time, int) or cooking_time < 0:
			raise ValueError("Cooking Time must be a positive integer")
		if not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
			raise ValueError("Ingredients must be a list of strings")
		if not isinstance(description, str):
			raise ValueError("Description has to be a string if not left empty")
		if not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
			raise ValueError("recipe_type can only have the values 'starter', 'lunch' or 'dessert'")
		
		self.name = name
		self. cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		return f"""{self.name}:
		description : {self.description} 
		recipe_type : {self.recipe_type} 
		cooking level : {self.cooking_lvl} 
		cooking time : {self.cooking_time} 
		ingredients : {self.ingredients}""" # pas besoin d'itérer pour les listes


