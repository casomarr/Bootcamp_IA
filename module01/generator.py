import sys
import random

def generator(string, sep=' ', option=None): #sep = espace et option =None sont les valeurs par défault
    '''Splits the text according to sep value and yield the substrings.
    Option precises if an action is performed to the substrings before it is yielded.
    You can only call one option at a time.'''

    try:
        text = str(string)
    except ValueError:
        print("Error: the text entered is not a string")
        sys.exit(1)

    split = text.split(sep)
    newstr = split #for option = None

    if option == "shuffle":
        newstr = []
        i = 0
        for i in range(len(split)):
            random_index = random.randrange(len(split))
            newstr.append(split.pop(random_index))
            i+=1

    if option == "unique":
        newstr = [*set(split)]

    if option == "ordered":
        split.sort()
        newstr = split

    print('\n'.join(newstr)) #pour que les nouvelles string s'affichent toutes séparées d'un saut à la ligne

generator(sys.argv[1], sys.argv[2], sys.argv[3])
