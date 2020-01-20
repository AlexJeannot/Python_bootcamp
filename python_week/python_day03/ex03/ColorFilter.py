from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

class ColorFilter:

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

    def display(self, array):
        plt.imshow(array)
        print("Displaying modified image")
        plt.show()

    def invert(self):
        array = self.get_array()

# Boucle version
        #inverted_array = []
        #for elem in array:
            #inverted_array_2 = []
            #for elem_2 in elem:
                #inverted_array_3 = []
                #for elem_3 in elem_2:
                    #inverted_array_3.append(255 - elem_3)
                #inverted_array_2.append(inverted_array_3)
            #inverted_array.append(inverted_array_2)
# Slicing version
        array[:, :, :] = 255 - array[:, :, :]
        print(array)
        self.display(array)

    def to_blue(self):
        array = self.get_array()
        array[:, :, 0:1] = array[:, :, 0:1] * 0.8
        array[:, :, 1:2] = array[:, :, 1:2] * 0.5
        array[:, :, 2:3] = 150
        print(array)
        self.display(array)

    def to_blue_bis(self):
        array = self.get_array()
        array[:, :, 0:2] = 0
        print(array)
        self.display(array)

    def to_red(self):
        array = self.get_array()
        array[:, :, 0:1] = 150
        array[:, :, 1:2] = array[:, :, 1:2] * 0.8
        array[:, :, 2:3] = array[:, :, 2:3] * 0.8
        print(array)
        self.display(array)

    def to_green(self):
        array = self.get_array()
        array[:, :, 0:1] = array[:, :, 1:2] * 0.8
        array[:, :, 1:2] = 130
        array[:, :, 2:3] = array[:, :, 2:3] * 0.8
        print(array)
        self.display(array)

    def to_gray(self):
        array = self.get_array()
        array[:, :, :] = (array[:, :, 0:1] * 0.299) + (array[:, :, 1:2] * 0.587) + (array[:, :, 2:3] * 0.114)
        #array[:, :, 1:2] = array[:, :, 1:2] * 0.587
        #array[:, :, 2:3] = array[:, :, 2:3] * 0.114
        print(array)
        self.display(array)

    def celluloid(self):

        #Boucle version
    #    array = self.get_array()
    #    inverted_array = []
    #    for elem in array:
    #        inverted_array_2 = []
    #        for elem_2 in elem:
    #            inverted_array_3 = []
    #            for elem_3 in elem_2:
    #                if elem_3 > 0 and elem_3 < 64:
    #                    elem_3 = 64
    #                elif elem_3 >= 64 and elem_3 < 128:
    #                    elem_3 = 128
    #                elif elem_3 >= 128 and elem_3 < 192:
    #                    elem_3 = 192
    #                elif elem_3 >= 192 and elem_3 <= 255:
    #                    elem_3 = 255
    #                inverted_array_3.append(elem_3)
    #            inverted_array_2.append(inverted_array_3)
    #        inverted_array.append(inverted_array_2)

        array = self.get_array()
        array[array <= 64] = 64
        array[(array <= 128) & (array > 64)] = 128
        array[(array <= 192) & (array > 128)] = 192
        array[(array <= 255) & (array > 192)] = 255
        self.display(array)
