import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class ColorFilter:
	def invert(self, array):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""

		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		
		if array.ndim != 3 or array.shape[2] not in [3, 4]:
			print("Array must have 3 dimensions and 3 or 4 channels") #flamingo img does not work but arcoiris does
			return None
		
		# red = array[:, :, 0]
		# green = array[:, :, 1]
		# blue = array[:, :, 2]

		# print(f"red type : {type(red)}")
		# print(f"red value: {red}")

		height, width, channels = array.shape

# The difference in the shape of images (different number of channels) can be due to several reasons :
# 1. Image Mode: 
# 		The mode of the image (e.g., RGB, RGBA, L) determines the number of channels. 
# 		Ex: an RGB image has 3 channels, an RGBA image has 4 channels, a grayscale image (mode L) has only one channel.
# 2. Image Metadata: 
# 		The metadata of the image file might specify different modes or channels. 
# 		Ex: an image can be saved as grayscale, RGB or RGBA.
# 3. Image Library Behavior: 
# 		Different libraries or versions might handle image loading differently. 
# 		Ex: Pillow might load an image with an alpha channel, while matplotlib might not. 

		inverted_image = array.copy()

		for y in range(height): #rajouter range sinon height est juste un int et donc non iterable
			for x in range(width):
				pixel = inverted_image[y, x]
				pixel[0] = 255 - pixel[0]
				pixel[1] = 255 - pixel[1]
				pixel[2] = 255 - pixel[2]
				#on ne change rien à alpha (pixel[3])

		return np.clip(inverted_image, 0, 255)

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
			
		blue_filter = (0.0, 0.0, 1.0, 1.0) #RGB + alpha
		# .clip() enforces valid color ranges for 8-bit images (0-255)
		return np.clip(array * blue_filter, 0, 255)
		# color filter / 0: intensity / 255: safety against overflow
	
	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		
		green_filter = (0.0, 1.0, 0.0, 1.0)
		return np.clip(array * green_filter, 0, 255)
		
	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		
		red_filter = (1.0, 0.0, 0.0, 1.0)
		return np.clip(array * red_filter, 0, 255)
		
	def to_celluloid(self, array):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
			array: numpy.ndarray corresponding to the image.
		Return:
		-------
			array: numpy.ndarray corresponding to the transformed image.
			None: otherwise.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		
		#TODO
		
	def to_grayscale(self, array, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = ’mean’/’m’: performs the mean of RBG channels.
		For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or array.size == 0:
			print("Not a numpy array")
			return None
		
		#TODO


#----------------------------------------------------------------------

cf = ColorFilter()

img = Image.open("arcoiris.png")
array = np.array(img)

if array is not None:
	new_image = cf.invert(array)
	if new_image is not None:
		Image.fromarray(new_image.astype(np.uint8)).show()
	new_image = cf.to_blue(array)
	if new_image is not None:
		Image.fromarray(new_image.astype(np.uint8)).show()
	new_image = cf.to_green(array)
	if new_image is not None:
		Image.fromarray(new_image.astype(np.uint8)).show()
	new_image = cf.to_red(array)
	if new_image is not None:
		Image.fromarray(new_image.astype(np.uint8)).show()