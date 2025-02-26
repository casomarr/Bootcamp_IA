import numpy
import matplotlib.pyplot as plt
from PIL import Image

""" When specifying positions or dimensions, we will assume that the first
coordinate is counted along the vertical axis starting from the top, and that the second
coordinate is counted along the horizontal axis starting from the left. Indexing starts
from 0. Ex: (1,3) is here:  . . . . .
							. . X . .
							. . . . .
							. . . . .
"""

class ScrapBooker:
	def crop(self, array, dim, position=(0,0)): #if we don't provide a position, it will default to (0, 0)
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
			array: numpy.ndarray
			dim: tuple of 2 integers.
			position: tuple of 2 integers.
		Return:
		-------
			new_arr: the cropped numpy.ndarray.
			None (if combinaison of parameters not compatible).
		Raise:
		------
			This function should not raise any Exception.
		"""
		# Ex: 	dim = (2, 2)
		#	 	position = (1, 3)
		# New image dimension starting from position X:
		#	. . . . . . .
		# 	. . X ─ ─ . .
		# 	. . | . . | .
		# 	. . | . . | .
		# 	. . . ─ ─ . .

		# if not isinstance(array, numpy.ndarray) or array.size == 0:
		if not isinstance(array, numpy.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		if (not isinstance(dim, tuple) or not all(isinstance(nb, int) for nb in dim) or
			len(dim) != 2 or dim[0] < 0 or dim[1] < 0): #if with parenthesis if on several lines
			print("Incorrect dim values")
			return None
		if position is None:
			position = (0, 0)
		if (not isinstance(position, tuple) or not all(isinstance(nb, int) for nb in position) or 
			len(position) != 2 or position[0] < 0 or position[1] < 0):
			print("Incorrect position values")
			return None
		if (array.shape[0] < position[0] or array.shape[1] < position[1] or
			dim[0] > array.shape[0] - position[0] or dim[1] > array.shape[1] - position[1]):
			print("Could not crop the picture : out of bounds")
			return None
		
		start_row, start_column = position # to initialize two variables from a tuple
		end_row = start_row + dim[0]
		end_column = start_column + dim[1]
		
		return array[start_row:end_row, start_column:end_column] # on crop à la mano, pas besoin d'une fonction spécifique


	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
			array: numpy.ndarray.
			n: non null positive integer lower than the number of row/column of the array
			(depending of axis value).
			axis: positive non null integer.
		Return:
		-------
			new_arr: thined numpy.ndarray.
			None (if combinaison of parameters not compatible).
		Raise:
		------
			This function should not raise any Exception.
		"""
		if not isinstance(array, numpy.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		if not isinstance(n, int) or n <= 0:
			print("n is not a positive int")
			return None
		if axis != 0 and axis != 1: #or (if axis not in (0, 1))
			print("invalid axis: only 0 (horizontal) and 1 (vertical) accepted")
			return None
		if n >= array.shape[axis]:
			print("n is out of bounds")
			return None
		
		start = n - 1
		axis_size = array.shape[axis]
		indices = list(range(start, axis_size, n))
		new_array = numpy.delete(array, indices, axis)
		return new_array
		

	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
			array: numpy.ndarray.
			n: positive non null integer.
			axis: integer of value 0 or 1.
		Return:
		-------
			new_arr: juxtaposed numpy.ndarray.
			None (combinaison of parameters not compatible).
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, numpy.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		if not isinstance(n, int) or n <= 0:
			print("n is not a positive int")
			return None
		if axis not in (0, 1):
			print("invalid axis: only 0 (horizontal) and 1 (vertical) accepted")
			return None

		new_array = numpy.concatenate([array] * n, axis)
		return new_array

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
			array: numpy.ndarray.
			dim: tuple of 2 integers.
		Return:
		-------
			new_arr: mosaic numpy.ndarray.
			None (combinaison of parameters not compatible).
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, numpy.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		if not isinstance(dim, tuple) or not all(isinstance(nb, int) for nb in dim):
			print("n is not a positive int")
			return None
		
		intermediate_array = numpy.concatenate([array] * dim[0], 0)
		new_array = numpy.concatenate([intermediate_array] * dim[1], 1)
		return new_array

#since python does not support to add functions from relative paths, to simplify,
#I just copied/paste what I learned from ex01 here:
try:
	img = plt.imread("yellow.png")
	print("img converted into numpy array")

	if img is not None:

		dim = (
			int(img.shape[0] - (img.shape[0] / 3)), 
			int(img.shape[1] - (img.shape[1] / 3))
		)
		position = (
			int(img.shape[0] / 4), 
			int(img.shape[1] / 4)
		)

		print("img shape:", img.shape)
		print("img type:", type(img))
		print("dim:", dim)
		print("position:", position)

		# croped_img = ScrapBooker.crop(img, dim, position) --> !!!! Errors because 
		# ScrapBooker.crop(img, dim, position) passes img as self, dim as array, 
		# and position as dim, leading to a type mismatch. Solution : Instantiate 
		# ScrapBooker first, then call the method on the instance.

		sb = ScrapBooker() # Create an instance of ScrapBook
		croped_img = sb.crop(img, dim, position)
		print("img croped")
		
		if croped_img is not None:
			new_img = Image.fromarray((croped_img * 255))
			new_img.show()
except Exception as e:
	print(f"Error: {e}")


try:
	sb = ScrapBooker()
	image = Image.open("muffins.png") #or image = plt.imread("muffins.png") + new_img = Image.fromarray((image * 255))
	print("img type:", type(img))
	if img is not None:
		#reduced size for visibility
		new_size = (image.width // 4, image.height // 4)
		resized_image = image.resize(new_size, Image.LANCZOS)
		print("img resized")
		resized_array = numpy.array(resized_image)
		print("img type:", type(resized_array))

		new_image = sb.thin(resized_array, 2, 0)
		print("img thined")
		if new_image is not None:
			Image.fromarray(new_image).show()
			# new_img = Image.fromarray((new_image * 255))
except Exception as e:
	print(f"Error: {e}")

try:
	sb = ScrapBooker()
	image = Image.open("muffins.png") #or image = plt.imread("muffins.png") + new_img = Image.fromarray((image * 255))
	print("img type:", type(img))
	if img is not None:
		#reduced size for visibility
		new_size = (image.width // 4, image.height // 4)
		resized_image = image.resize(new_size, Image.LANCZOS)
		print("img resized")
		resized_array = numpy.array(resized_image)
		print("img type:", type(resized_array))

		# Axis 0 = Rows Direction (Vertical Stacking) --> juxtapose in axis=0
		# means we add rows (and therefore the new image will be added underneeth)
		# Axis 1 = Columns Direction (Horizontal Stacking)
		new_image = sb.juxtapose(resized_array, 3, 1)
		print("img juxtaposed")
		if new_image is not None:
			Image.fromarray(new_image).show()
except Exception as e:
	print(f"Error: {e}")


try:
	sb = ScrapBooker()
	image = Image.open("muffins.png") #or image = plt.imread("muffins.png")
	print("img type:", type(img))
	if img is not None:
		#reduced size for visibility
		new_size = (image.width // 4, image.height // 4)
		resized_image = image.resize(new_size, Image.LANCZOS)
		print("img resized")
		resized_array = numpy.array(resized_image)
		print("img type:", type(resized_array))

		new_image = sb.mosaic(resized_array, (2,3))
		print("img mosaic")
		if new_image is not None:
			Image.fromarray(new_image).show()
except Exception as e:
	print(f"Error: {e}")
