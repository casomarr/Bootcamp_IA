def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for-loop.
    The three arrays must have the compatible dimensions.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector (n +1) * 1.
    Return:
    The gradient as a numpy.array, a vector of dimensions n * 1,
    containg the result of the formula for all j.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible dimensions.
    None if x, y or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    res = np.c_[np.ones(len(x)), x] @ np.insert(theta, 0, '0', axis = 0) #c'est la seule chose qui change du gradient fait pour des vecteurs (donc pour un seul paramètre) : on doit rajouiter une ligne 0 pour que les dimensions de X avec une nouvelle colonne 1 et theta collent.
    #print(np.c_[np.ones(len(x)), x], '\n')
    #print(np.c_[np.zeros(len(theta)), theta])
    #print(np.insert(theta, 0, '0', axis = 0))
    res -= y
    res = np.c_[np.ones(len(x)), x].transpose() @ res
    #print(res / len(y), '\n') #devrait s'afficher une matrice 1x4 et non 4x1!
    res = res / len(y)
    print(res.reshape(2, 2)) #(2, 2) car on veut un numpy array en 2D
    return res.reshape(2, 2)

    # res2 = []
    # for i in range(len(res)):
    #     res2.append(res[i])
    # print(res2)
    #res_transposed = np.transpose(res)
    #res_transposed = np.reshape(res, (1, -1))
    #res_transposed = np.matrix(res).T
    #res_transposed = res.shape(1, 4)
    #print(res[None].T)
    #print(res.reshape(res.shape+(1,)))
    #print(res[:,None])

    #print(res.reshape((1, 4))) #si je mets -1 au lieu de 4 : -1 in the shape vector means "fill in whatever number makes this work"
    #print(res.T)

    #print(np.array([res]).reshape((1, 4)))

    #return res_transposed
    #return res


import numpy as np

x = np.array([
[ -6, -7, -9],
[ 13, -2, 14],
[ -7, 14, -1],
[ -8, -4, 6],
[ -5, -9, 6],
[ 1, -5, 11],
[ 9, -11, 8]])
y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))

theta1 = np.array([3,0.5,-6]).reshape((-1, 1))
gradient(x, y, theta1)

#theta2 = np.array([0,0,0]).reshape((-1, 1))
#gradient(x, y, theta2)
