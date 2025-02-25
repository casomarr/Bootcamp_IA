"""
• Column vectors are represented as list of lists of single float ([[1.], [2.], [3.]]),
	Use [i][0] to access the elements
• Row vectors are represented as a list of a list of several floats ([[1., 2., 3.]]).
	Use [0][i] to access the elements.
--> A vector is either a single line of floats or a single column of floats.
When more than a line/column is consider, it is a matrix, not a vector.
"""

class Vector:
	def __init__(self, init_info):
		if isinstance(init_info, list) and all(isinstance(i, list) and all(isinstance(j, float) for j in i) for i in init_info): # if init_info is a vector
			self.values = init_info
			if len(init_info) == 1: # row
				self.shape = (1, len(init_info[0]))
			elif len(init_info[0]) == 1: # column
				self.shape = (len(init_info), 1)
		elif isinstance(init_info, int): # if init_info is a size (int)
			self.shape = (init_info, 0)
			i = 0
			self.values = []
			while i < init_info:
				self.values.append([float(i)])
				i += 1
		elif isinstance(init_info, tuple): # if init_info is a range
			if init_info[0] > init_info[1]:
				print("Error")
				return None
			else:
				self.shape = (init_info[1] - init_info[0], 0)
				self.values = []
				for i in range (init_info[0], init_info[1]):
					self.values.append(init_info[0] + i)
		else:
			print("Error")
			return None

	def dot(self, other):
		if (self.shape[0] != 1 and self.shape[1] != 1) or (other.shape[0] != 1 and other.shape[1] != 1):
			print("Error")
			return None
		if self.shape != other.shape:
			print("Error")
			return None
		# result = 0
		# i = 0
		# if self.shape[0] != 1: # Column vector
		# 	while i < self.shape[0]:
		# 		result += self.values[i][0] * other.values[i][0]
		# 		i += 1
		# else: # Row vector
		# 	while i < self.shape[1]:
		# 		result += self.values[0][i] * other.values[0][i]
		# 		i += 1
		# return result
		return sum(x[0] * y[0] for x, y in zip(self.values, other.values))

	def T(self):
		if self.shape[0] != 1 and self.shape[1] != 1:
			print("Error")
			return None
		transposed = []
		if self.shape[0] != 1: # Column vector
			i = 0
			while i < self.shape[0]:
				transposed.append(self.values[i][0])
				i += 1
			return Vector([transposed])
		else: # Row vector
			i = 0
			while i < self.shape[1]:
				transposed.append([self.values[0][i]])
				i += 1
			return Vector(transposed)
		
	""" Difference between __add__ and __radd__:
		Without the __radd__ method, if the left operand does not support the addition 
		operation, the addition would fail with a TypeError.
		Ex: in case of mixed types or when the left operand is not an instance of the 
		class that defines the __add__ method.
		So having the radd method allows to try every way possible to do the sum.
	"""
		
	def __add__(self, other): # magic/special method : "def add(self, other)" without the "__" won't work : typeError.
		if not isinstance(other.shape, tuple) or not isinstance(other.values, list) and all(isinstance(i, float) for i in other.values): #if the other vector is not correct
			print("Error")
			return None
		if self.shape != other.shape:
			print("Error")
			return None
		return Vector([x[0] + y[0] for x, y in zip(self.values, other.values)])

	def __radd__(self, other):
		return self.__add__(other)
	
	def __sub__(self, other):
		if not isinstance(other.shape, tuple) or not isinstance(other.values, list) and all(isinstance(i, float) for i in other.values): #if the other vector is not correct
			print("Error")
			return None
		if self.shape != other.shape:
			print("Error")
			return None
		return Vector([x[0] - y[0] for x, y in zip(self.values, other.values)])

	def __rsub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, scalar):
		if not isinstance(scalar, int) and not isinstance(scalar, float):
			print("Error")
			return None
		if scalar == 0 or scalar == float(0):
			print("Error: division by 0")
			return None
		return Vector([[x[0] / scalar] for x in self.values])
	
	def __rtruediv__(self, scalar):
		if not isinstance(scalar, (int, float)): #pour check en une seule fois si int ou float
			print("Error")
			return None
		if scalar == 0 or scalar == float(0):
			print("Error: division by 0")
			return None
		for x in self.values:
			if x[0] == 0:
				print("Error: division by 0")
				return None
		return Vector([[scalar / x[0]] for x in self.values])
	
	def __mul__(self, scalar):
		if not isinstance(scalar, (int, float)): 
			print("Error")
			return None
		return Vector([[x[0] * scalar] for x in self.values])
	
	def __rmul__(self, scalar):
		return self.__mul__(self, scalar)
	
	def __str__(self):
		return(f"{self.values}")

	def __repr__(self):
		return(f"{self.values}")
	
