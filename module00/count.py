import sys

def text_analyzer(string):
    if len(string) == 0:
        print("Enter a string")
        sys.exit(1)
    try:
        string = str(string)
    except ValueError:
        print("Error: argument is not a string")
        sys.exit(1)
    i = 0
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
        if 65 >= ord(string[i]) <= 90:
            upper +=1
        if 97 >= ord(string[i]) <= 122:
            lower +=1
        if 33 >= ord(string[i]) <= 47: #il y en a plus que ça mais flemme
            punctuation +=1
        if 8 >= ord(string[i]) <= 13: #peut être qu'il y en a plus mais flemme
            spaces +=1
        i+=1
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")



#main
if len(sys.argv) == 2:
    text_analyzer(sys.argv[1])

#Exo pas fini. Concept intéressant : https://www.geeksforgeeks.org/python-docstrings/ .
#C'est n commentaire expliquant ce que fait la fonction. Mais c'est un commentaire qui 
# peut etre accéder par un print, car il est compris par python pq il suit des règles spécifiques.