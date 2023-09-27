def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""

	# try :
	# 	str = str(iterable)
	# except ValueError:
	# 	print("Error: argument is not a string")
	# 	sys.exit(1)

	str = iterable #a effacer si je mets les try et except

	result = []
	i = 0
	while i < len(str):
		result.append(function_to_apply(str[i]))
		i+=1
	print(result)
	#return result

#main
#ft_map(sys.argv[1], sys.argv[2])

string = "hola karolina"
def fx(letter):
	letter = 'a'
	return letter

ft_filter(fx, string)


