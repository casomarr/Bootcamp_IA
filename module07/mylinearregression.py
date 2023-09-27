def gradient(x, y, theta):
	res = np.c_[np.ones(len(x)), x] @ theta
	res -= y
	res = np.c_[np.ones(len(x)), x].transpose() @ res
	res = res / len(y)
	return res

class MyLinearRegression():
	"""
	Description:
	My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = thetas

	def fit_(self, x, y):
		for i in range(self.max_iter):
			self.thetas -= self.alpha * gradient(x, y, self.thetas)
		#print(self.thetas. reshape(1, 5))
		return self.thetas.reshape(1, 5)

	def predict_(self, x): #reprend le self.thetas de fit
		X_apostrophe = np.c_[np.ones(len(x)), x]
		res = X_apostrophe @ self.thetas
		#print(res.transpose())
		return res

	def loss_elem_(self, y, y_hat):
		'''other losses. Ex05 module05'''

	def loss_(self, y, y_hat):
		'''Computes the half mean squared error of two non-empty numpy.array'''
		J = 0
		for i in range(len(y)):
			J = J + ((1/(2*len(y)) * (y_hat[i] - y[i])) * (y_hat[i] - y[i]))
		#print(float(J))
		return float(J)



import numpy as np

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
Y = np.array([[23.], [48.], [218.]])
MyLR = MyLinearRegression
mylr = MyLR([[1.], [1.], [1.], [1.], [1]])

# y_hat = mylr.predict_(X)
# mylr.loss_(Y, y_hat)

mylr.alpha = 1.6e-4
mylr.max_iter = 200000
mylr.fit_(X, Y)