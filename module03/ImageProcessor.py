from matplotlib import pyplot
from matplotlib import image
import cv2
from PIL import Image
import numpy

class ImageProcessor(object):
    def load(path):
        '''Opens the PNG file specified by the path argument and returns an
array with the RGB values of the pixels image. It must display a message specifying
the dimensions of the image.'''
        img = cv2.imread(path) #to read image
        height = img.shape[0]
        width = img.shape[1]
        print("Loading image of dimensions : ", height, 'x', width)

        # dimensions = img.shape 
        # print (dimensions) #height, width, channels
        # print(img.dtype) #dtype (unit8 pour RGB)

    def display(array): 
        '''Takes a numpy array as an argument and displays the corre-
sponding RGB image.'''
    #methode 1: non conclusive car je mets des zeros partout
        # img_numpy = numpy.zeros(array, dtype=numpy.uint8) #unit8 = RGB car de range 0 à 255
        # img = Image.fromarray(img_numpy, 'RGB')
        # print(img_numpy)
        # img.show()

    #methode 2 : non conclusive et j'aime moins que la premiere methode car moins maniable
        # pic = Image.open("test.jpg")
        # pix = numpy.array(pic.getdata()).reshape(pic.size[0], pic.size[1], 3)
        # print(pix)
        # img = Image.fromarray(pix, 'RGB')
        # #img.save('output_test.png')
        # img.show()

    #methode 3: MARCHE mais je ne peux lui donner le array en paramètres.
        # img = image.imread('test.jpg')
        # pyplot.imshow(img)
        # pyplot.show()

    #méthode 4: bof piste nulle
        # load_img = numpy.array(Image.open('test.jpg'))
        # print(load_img)
        # img = Image.fromarray(load_img)
        # print(img)
        
    #méthode 5:
        # Load image
        image = Image.open('test.jpg')
       
        # Convert image to array
        image_arr = numpy.array(image)
       
        # Crop image #au lieu de crop array ici on lui donne ses propres dimensions
        # image_arr = image_arr[700:1400, 1450:2361]
       
        # Convert array to image
        image = Image.fromarray(image_arr)
       
        # Display image
        image.show()
#/home/carolina/Documents/tronc_commun_newGit/bootcampIA/module03/test.jpg

path = '/home/carolina/Documents/tronc_commun_newGit/bootcampIA/module03/test.jpg'
ImageProcessor.load(path)

height = 743
width = 1280
channel = 3
array = (height, width, channel)
ImageProcessor.display(array)