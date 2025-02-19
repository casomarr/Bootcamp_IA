import sys

cookbook = {
	"sandwich": {
	"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
	"meal" : "lunch",
	"prep_time" : 10
	},
	"cake": {
	"ingredients": ["flour", "sugar", "eggs"],
	"meal": "dessert",
	"prep_time": 60
	},
	"salad": {
		"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "dinner",
		"prep_time": 15
	}
} #nested dictionnaries


def print_recipes_names(cookbook):
	for recipe in cookbook.keys(): #.keys() allows to print all dictionnary keys (here: the recipe's names)
		print(recipe)

def print_recipe_details(cookbook, recipe_name):
	if recipe_name in cookbook:
		recipe = cookbook[recipe_name]
		print("Recipe for ", recipe_name, ":")
		print("	Ingredients list: ", ', '.join(recipe["ingredients"]))
		print("	To be eaten for", recipe["meal"])
		print("	Takes ", recipe["prep_time"], " minutes of cooking")
		#OR print(f"Takes {recipe.prep_time} minutes of cooking")

def delete_recipe(cookbook, recipe_name):
	if recipe_name in cookbook:
		del cookbook[recipe_name]
	
def add_recipe(cookbook):
	recipe_name = input("Enter a recipe name:")
	ingredients_str = input("Enter ingredients:")
	ingredients_list = ingredients_str.split(', ')
	meal_type = input("Enter a meal type:")
	preparation_time = input("Enter a preparation_time:")
	cookbook[recipe_name] = {
		"ingredients" : ingredients_list,
		"meal": meal_type,
		"prep_time": preparation_time
	}


if len(sys.argv) != 1:
	print("Error: no arguments expected")
	sys.exit(1)

option = 0
while (option != 5):
	print("Welcome to the Python Cookbook !\n \
	List of available options:\n \
		1: Add a recipe\n \
		2: Delete a recipe\n \
		3: Print a recipe\n \
		4: Print the cookbook\n \
		5: Quit")

	option = int(input("Please select an option:\n"))

	if option == 1:
		add_recipe(cookbook)
	elif option == 2:
		recipe_name = input("Enter the name of the recipe you want to delete:\n")
		delete_recipe(cookbook, recipe_name)
	elif option == 3:
		recipe_name = input("Enter the name of the recipe you want to see:\n")
		print_recipe_details(cookbook, recipe_name)
	elif option == 4:
		print_recipes_names(cookbook)
	elif option == 5:
		print("Cookbook closed. Goodbye !")
		sys.exit(0)
	else:
		print("This option does not exist.")
	
	print("\n")

