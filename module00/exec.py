import sys

if (len(sys.argv) < 2): #(len(sys.argv) < 2 est la même chose que argc < 3
	sys.exit(1) #return 1

#si la len = 2 alors argv[0] est le nom du programme (et non "python3") et argv[1] est la str
str =' '.join(sys.argv[1:]) #plutôt que de faire if > 2 alors while on join, [1:]
#signifie : tant qu'on est pas arrivé à la fin tu prends chaque argv séparément.
#la syntaxe est : sequence[start:stop:step] mais là on a besoin que de sequence[start:]
#et ça va par défault jusqu'à la fin
str = ''.join(reversed(str)) # or str = str[::-1] because reversed returns an iterator object, not a string
str = str.swapcase()

print(str)