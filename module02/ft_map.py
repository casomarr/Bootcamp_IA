import sys

def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	try :
		if type(iterable) == list: #and type(iterable[i] == int)
			nb = iterable
	except ValueError:
		print("Error: argument is not an integer")
		sys.exit(1)
	result = []
	i = 0
	while i < len(nb):
		result.append(function_to_apply(nb[i]))
		i+=1
	print(result)
	#return result

#main
#ft_map(sys.argv[1], sys.argv[2])

x = [1, 2, 3, 4, 5]
def fx(nb):
	result = nb + 2
	return result

ft_map(fx, x)
