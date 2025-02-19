import sys

def text_analyzer(string):
	"""This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text."""
	if not isinstance(string, str): #cannot use try str(string) and except for a string. It can also be used for int, float and bool
		print("ERROR: expected a string")
		sys.exit(1)
	
	characters = len(string)
	upper = 0
	lower = 0
	punctuation = 0
	spaces = 0
	for i in string: #i = 0 by default
		if i.isupper():
			upper = upper + 1
		elif i.islower():
			lower = lower + 1
		elif i == ' ':
			spaces = spaces + 1
		else:
			punctuation = punctuation + 1
	
	print("The text contains ", characters, " character(s):")
	print("- ", upper, " upper letter(s)")
	print("- ", lower, " lower letter(s)")
	print("- ", punctuation, " punctuation mark(s)")
	print("- ", spaces, " space(s)")


if __name__ == "__main__": #indenting everything underneeth under this command allows
	# both to run this program directly from the command line or imported as a module 
	# in another Python script : 
	# Option 1: 
	# 	python3 count.py 'Hello World!'
	# Option2:
	# 	python3
	# 	>>> from count import text_analyzer
	# 	>>> text_analyzer("Hello World")
	if len(sys.argv) > 2:
		print("ERROR: too many arguments")
		sys.exit(1)

	if len(sys.argv) < 2:
		string = input("Enter a string: ")
	else:
		string = sys.argv[1]

	text_analyzer(string)