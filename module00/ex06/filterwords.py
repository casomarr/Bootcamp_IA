import sys

def filterwords(S, N):
	if N < 0:
		print("The integer needs to be positive")
		sys.exit(1)

	words_list = S.split(' ')
	punctuation_ascii = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]
	#list comprehension expression : [expression for item in iterable if condition]
	words_list = [''.join(char for char in word if ord(char) not in punctuation_ascii) for word in words_list] #ord so that it checks the character's ascii value
	words_to_print_list = [word for word in words_list if len(word) > N]
	print(words_to_print_list)


if len(sys.argv) != 3:
	print("Wrong number of arguments: 2 expected.")
	sys.exit(1)

if not isinstance(sys.argv[1], str):
	print("Wrong type of arguments: string and integer expected.")
	sys.exit(1)

S = sys.argv[1]
N = int(sys.argv[2])

filterwords(S, N)