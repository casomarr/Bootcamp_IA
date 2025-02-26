import numpy
import matplotlib.pyplot as plt
from PIL import Image

class ImageProcessor:
	@staticmethod
	def load(path):
		try:
			image = plt.imread(path)
			print(f"Image shape: {image.shape}")
			return image
		except Exception as e:
			print(f"Error loading image: {e}")
			return None
	
	@staticmethod
	def display(array):
		if not isinstance(array, numpy.ndarray) or array.size == 0: #checks are a bit different for numpy arrays
			print("Error: not a numpy array")
			return None
		# plt.imshow(array)
		# plt.show()
		try:
			image = Image.fromarray((array * 255).astype(numpy.uint8))  # we convert the Numpy array back to an image so that it can be shown
			image.show()
		except Exception as e:
			print(f"Error displaying image: {e}")
		
	
img = ImageProcessor.load("yellow.png")
if img is not None:
	print(img)
	ImageProcessor.display(img)

img = ImageProcessor.load("unexistant_file.png")
if img is not None:
	print(img)
	ImageProcessor.display(img)