from book import Book
from recipe import Recipe
from datetime import datetime

recipes = {
	"starter": {
		"spinach_salad": Recipe("Spinach Salad", 1, 15, ["avocado", "arugula", "tomatoes", "spinach"], "", "starter"),
		"cesar_salad": Recipe("Cesar Salad", 2, 15, ["avocado", "eggs", "tomatoes", "salad", "chicken"], "", "starter")
	},
	"lunch": {
		"sandwich": Recipe("Sandwich", 1, 10, ["ham", "bread", "cheese", "tomatoes"], "", "lunch")
	},
	"dessert": {
		"cake": Recipe("Cake", 3, 60, ["flour", "sugar", "eggs"], "", "dessert")
	}
}


try:

	print("Test 1 : this test should create and print the recipe 'muffins'")
	muffins = Recipe("Muffins", 2, 30, ["chocolate", "buter", "eggs", "flour"], "", "dessert")
	to_print = str(muffins)
	print(to_print)
	
	book = Book("cookbook", datetime.now(), datetime.now(), recipes)
	print("Book object created correctly")

	print("Starter recipes:")
	book.get_recipes_by_types("starter")

	print("Cesar Salad recipe:")
	book.get_recipe_by_name("Cesar Salad")

	print("Dessert recipes:")
	book.get_recipes_by_types("dessert")
	muffins_recipe = book.add_recipe(muffins)
	print("Muffin recipe added correctly")
	print("Dessert recipes:")
	book.get_recipes_by_types("dessert")

	print("Muffins recipe:")
	book.get_recipe_by_name("Muffins")
except Exception as e:
	print(f"Test failed: {e}")


try:
	book .get_recipes_by_types("dinner")
except Exception as e:
	print(f"Test failed as expected : {e}")

try:
	book.add_recipe("raclette")
except Exception as e:
	print(f"Test failed as expected : {e}")

try:
	book .get_recipe_by_name("paella")
except Exception as e:
	print(f"Test failed as expected : {e}")

try:
	muffins_recipe = book.add_recipe(muffins)
except Exception as e:
	print(f"Test failed as expected : {e}")