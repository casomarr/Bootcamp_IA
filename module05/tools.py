import numpy

def add_intercept(x):
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
    x: has to be a numpy.array of dimension m * n.
    Returns:
    X, a numpy.array of dimension m * (n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
    Raises:
    This function should not raise any Exception.
    """
    X = numpy.ones((lines, columns+1))
    X[:,:-1] = x #à part la dernière ligne qu'on vient de rajouter, on remplit le reste de la matrice X avec tout ce qui était dans la matrice x
    print(X)


# lst = ([[1, 2, 3, 1, 2, 3, 1, 2, 3],
#         [1, 2, 3, 1, 2, 3, 1, 2, 3],
#         [1, 2, 3, 1, 2, 3, 1, 2, 3]]) 
# #dimensions : 3 x 9 (m = 3, nb de lignes) (n = 9, nb de colonnes)
# x = numpy.asarray(lst)

lines = 5
columns = 3
x = numpy.random.rand(lines,columns) #pour créer une matrice avec numéros random
#print(x)
add_intercept(x)