def sigmoid_(x):
	"""
	Compute the sigmoid of a vector.
	Args:
	x: has to be a numpy.ndarray of shape (m, 1).
	Returns:
	The sigmoid value as a numpy.ndarray of shape (m, 1).
	None if x is an empty numpy.ndarray.
	Raises:
	This function should not raise any Exception.
	"""
	# X_apostrophe = np.c_[np.ones(len(x)), x]
	# res = X_apostrophe @ theta
	# print(res.transpose())

	res = 0
	for i in x:
		res + res + (1 / (1 + x[i]))

	if res >= 0.5 :
		print(f"there is a {res} chance that the tumor is malignant")
	if res < 0.5 :
		print(f"there is a {res} chance that the tumor is benign")



import numpy as np
x = np.array([[-4]])
sigmoid_(x)
