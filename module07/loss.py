#exactement la meme fonction que pour un seul parametre dans le module05

#Lost function = cost function. The loss function is basically just a measure of how 
# wrong the model is, in all of its predictions.
#Loss function = the average of the squared distances between each prediction and its 
# expected value

def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array, without any for loop.
    The two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    The half mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.array.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """

    J = 0
    for i in range(len(y)) :
        J = J + ((1/(2*len(y)) * (y_hat[i] - y[i])) * (y_hat[i] - y[i]))
    print(float(J))