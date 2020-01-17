from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

class ScrapBooker:

    def __init__(self, img):
        self.img = img

    def load(self):
        im = Image.open(self.img)
        print("Loading image of dimensions {0} x {1}".format(im.size[0], im.size[1]))
        return im

    def get_array(self):
        im = self.load()
        data = np.asarray(im, dtype="int32")
        print("Returning array")
        return data

    def crop(self, dimensions, position=(0,0)):

        im = self.load()
        print("Resizing the image with height of {0} and width of {1}".format(dimensions[0], dimensions[1]))
        im1 = im.crop((position[0], position[1], dimensions[0], dimensions[1]))
        print("Displaying crop image")
        im1.show()

    def display(self, array):
        plt.imshow(array)
        print("Displaying modified image")
        plt.show()

    def thin(self, n, axis):

        array = self.get_array()
        if axis == 0:
            ax = "vertical"
            modified_array = array[::n, ::]
        elif axis == 1:
            ax = "horizontal"
            modified_array = array[::, ::n]
        print("Deleting {0} pixel row along the {1} axis ".format(n, ax))
        self.display(modified_array)

    def juxtapose(self, n, axis):
        #array = self.get_array()
        #print(array)
        #modified_array = []
        #if axis == 0:
        #    while n > 0:
        #        for elem in array:
        #            modified_array.append(elem)
    #            n -= 1
    #    elif axis == 1:
    #        for elem in array:
    #            x = n
    #            while x > 0:
    #                 modified_array.append(elem)
    #                 x -= 1
    #    self.display(modified_array)

        array = self.load()
        lst = []
        while n > 0:
            lst.append(array)
            n -= 1
        modified_array = np.concatenate(tuple(lst), axis=axis)
        self.display(modified_array)


    def mosaic(self, dimensions):
        array = self.load()
        lst = []
        n = dimensions[0]
        while n > 0:
            lst.append(array)
            n -= 1
        first_modified_array = np.concatenate(tuple(lst), axis=0)
        lst = []
        n = dimensions[1]
        while n > 0:
            lst.append(first_modified_array)
            n -= 1
        second_modified_array = np.concatenate(tuple(lst), axis=1)
        self.display(second_modified_array)
