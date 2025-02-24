import sys
from random import randint

def guess_game():
	number_to_guess = randint(1, 99)
	number_of_attempts = 1
	answer = input("\nWhat's your guess between 1 and 99?\n")
	while answer != "exit":
		answer = int(answer)
		if answer == number_to_guess:
			if number_to_guess == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if (number_of_attempts == 1):
				print("Congratulations! You got it on your first try")
			else:
				print("Congratulations, you've got it!")
				print(f"You won in {number_of_attempts} attempts!")
			sys.exit(0)
		elif answer < number_to_guess:
			print("Too low")
		else:
			print("Too high!")
		number_of_attempts = number_of_attempts + 1
		answer = input("\nWhat's your guess between 1 and 99?\n")
	if answer == "exit":
		print("Goodbye!")
		sys.exit(0)


if len(sys.argv) > 1:
	print("Wrong number of arguments: 1 expected")
	sys.exit(1)
else:
	print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit'to end the game.
Good luck""") #triple quotes make sure new lines, tabs and spaces are respected (so no need to add backslashes at the end of each line)
	guess_game()