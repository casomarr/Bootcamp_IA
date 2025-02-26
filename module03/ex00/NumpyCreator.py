""" The NumPy library is a fundamental package for scientific computing in Python. 
It provides support for large, multi-dimensional arrays and matrices, along with 
a collection of mathematical functions to operate on these arrays efficiently. 
NumPy is widely used in data science, machine learning, and artificial intelligence 
(AI) due to its powerful capabilities and performance. """

import numpy

class NumpyCreator(object):
	'''Receives as an argument a different type of data structure and transforms it into
a Numpy array'''
	def from_list(self, lst):
		'''Takes a list or nested lists and returns its corresponding
Numpy array.'''
		if not isinstance(lst, list) or not lst:
			return None
		return numpy.array(lst)
	
	def from_tuple(self, tpl): 
		'''Takes a tuple or nested tuples and returns its correspond-
ing Numpy array.'''
		if not isinstance(tpl, tuple) or not tuple:
			return None
		return numpy.array(tpl)
	
	def from_iterable(self, itr):
		'''Takes an iterable and returns an array which contains
all its elements.'''
		if not itr:
			return None
		return numpy.array(itr)

	def from_shape(self, shape, value):
		'''Returns an array filled with the same value. The first argument is a tuple which 
		specifies the shape of the array, and the second argument specifies the value of the 
		elements. This value must be 0 by default.'''
		if not isinstance(shape, tuple) or not shape:
			return None
		return numpy.full(shape, value)

	def random(self, shape):
		'''Returns an array filled with random values. It takes as an
argument a tuple which specifies the shape of the array.'''
		if not isinstance(shape, tuple) or not shape:
			return None
		return numpy.random.rand(*shape)

	def identity(self, n): 
		'''Returns an array representing the identity matrix of size n.'''
		if not isinstance(n, int) or n < 0:
			return None
		# (The identity array is a square array with ones on the main diagonal.)
		return numpy.identity(n)
	
	
list = [1, 2, 3]
tuple = (1, 2, 3)
iterable = range(10)
shape = (3, 3)
value = 0
size = 3

np = NumpyCreator()
print(np.from_list(list))
print(np.from_tuple(tuple))
print(np.from_iterable(iterable))
print(np.from_shape(shape, value))
print(np.random(shape))
print(np.identity(size))