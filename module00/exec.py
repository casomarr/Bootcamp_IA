import sys
	
nb_argv = len(sys.argv)
if nb_argv > 1:
	i = 1
	newstr = ''
	while nb_argv > 1:
		newstr = newstr + ' ' + sys.argv[i]
		i = i + 1
		nb_argv = nb_argv - 1
	newstr = newstr[::-1]
	print(newstr.swapcase())
