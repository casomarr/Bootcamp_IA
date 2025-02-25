import sys
import random

def generator(text, sep=" ", option=None):
	"""Splits the text according to sep value and yield the substrings.
	option precise if a action is performed to the substrings before it is yielded.
	"""
	if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
		print("ERROR")
		sys.exit(1)

	splitted_list = text.split(sep)

	if option == "shuffle":
		i = 0
		to_print = []
		for i in range(len(splitted_list)):
			random_index = random.randrange(len(splitted_list))
			to_print.append(splitted_list.pop(random_index))
			i+=1
	elif option == "unique":
		splitted_set = set(splitted_list) # converts the list to a set because this automatically removes all duplicate elements
		to_print = list(splitted_set) # converts the set back to a list to have the right format
	elif option == "ordered":
		to_print = sorted(splitted_list)
	else:
		to_print = splitted_list #for option=None

	for substring in to_print:
		yield substring # "yiewld" allows to return but then go back where it stoped to continue. It is more efficient for long texts that storing all the text in a variable before returning all at once


# ---------------------------------------

try:
	text = "paella, carolina, chocolate, universe, 42, carolina, paella, skateboard"

	print("option = None")
	for word in generator(text, sep=", "): #il faut "sep="
			print(word)
	print()

	print("option = shuffle")
	for word in generator(text, sep=", ", option="shuffle"): #il faut "sep=" et "option="
			print(word)
	print()

	print("option = unique")
	for word in generator(text, sep=", ", option="unique"):
			print(word)
	print()

	print("option = ordered")
	for word in generator(text, sep=", ", option="ordered"):
			print(word)
	print()

	print("separator not in string")
	for word in generator(text, sep="/"):
			print(word)
	print()

	for word in generator(text, sep=", ", option="error"): #il faut "sep=" et "option="
		print(word)
except Exception as e:
	print(f"Error: {e}")