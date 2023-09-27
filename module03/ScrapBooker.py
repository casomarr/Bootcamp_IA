import numpy
from PIL import Image

#(colonne, ligne)

class ScrapBooker(object):
    def crop(array, dim, position):
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
        # # Load image
        # image = Image.open('test.jpg')

        # # Convert image to array
        # image_arr = numpy.array(image)

        # Crop image
        array = array[dim[0]:dim[1], position[0]:position[1]]
        print(array)

        # Convert array to image
        image = Image.fromarray(array)

        # Display image
        image.show()

        #To create Numpy array out of this object, we passed it through the np.array() method, 
        # which extracted all the Pixel data from the image and stored it in the variable 
        # image_arr. This resulted us in having a Numpy array of shape (1280, 743, 3). 

        #Then we sliced the array from each dimension. In the statement image_arr[700:1400, 1450:2361] 
        # the 700 is denoting the starting row, and 1400 is denoting the ending row. Where, 1450 
        # represents starting column, and 2316 represents the ending column. All these values 
        # depict the pixel at the location, therefore the crop with the top left coordinates of 
        # (1450, 700) and bottom left coordinates of (2361, 1400). 
    
        #Finally, we converted the Numpy array back to an image using Image.fromarray(). In the 
        # end we displayed the image using the show() function.  

    def thin(array, n, axis):
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

        print("before thin : ", array)
        # Thin image
        array = numpy.delete(array, n, axis) #Ça marche! même si ça ne se voit pas sur l'image, ça marche qd on print la array :)
        print("after thin : ", array)


    def juxtapose(array, n, axis): #NE MARCHE PAS
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
        print("before juxtapose : ", array)
        # Juxtapose n images
        i = 1
        while i < n:
            array_copy = numpy.copy(array)
            concatenation = numpy.concatenate((array, array_copy), axis)#array.copy n'existe pas
            i+=1

        print("after juxtapose : ", concatenation)


    def mosaic():
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



# Load image
image = Image.open('test.jpg')
# Convert image to array
array = numpy.array(image)

new_height = 100
new_width = 600
dim = (new_height, new_width)
position = 30, 100
#ScrapBooker.crop(array, dim, position)

n = 0 #number of the row or column to delete. First line is number 0, second line is number 1...
axis = 0 #axis : 0 = line / 1 = column
#ScrapBooker.thin(array, n, axis)

n = 3
axis = 1
ScrapBooker.juxtapose(array, n, axis)