import numpy

def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.array, a vector of dimension m * 1.
    None if x and/or theta are not numpy.array.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    # f = numpy.dot(theta[0], x) + theta[1]

    f = []
    m = len(x)
    for j in range (0, m) : #pas besoin de spécifier 0 / n est exclus donc va jusqu'à n - 1
        f.append(theta[1] * x[j] + theta[0])
    print(f)

x = numpy.arange(1,6) # idem que : x = numpy.array([1, 2, 3, 4, 5, 6])
theta1 = numpy.array([[5], [0]]) #theta[0] = b / theta[1] = w
predict_(x, theta1)
theta2 = numpy.array([[0], [1]])
predict_(x, theta2)