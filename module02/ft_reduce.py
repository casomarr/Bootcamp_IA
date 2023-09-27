def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""

	try :
		if type(iterable) == list: #and type(iterable[i] == int)
			nb = iterable
	except ValueError:
		print("Error: argument is not an integer")
		sys.exit(1)
	result = 0
	temp = []
	i = 0
	while i < len(nb):
		temp.append(function_to_apply(nb[i]))
		i+=1
	i = 0
	while i < len(nb) - 1:
		result = temp[i] + temp[i + 1]
		i+=1
	print(result)
	#return result



#main
#ft_map(sys.argv[1], sys.argv[2])

nums = [1, 2, 3, 4, 5]
def fx(nb):
	result = nb + 2
	return result

ft_reduce(fx, nums)
