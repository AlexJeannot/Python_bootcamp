
from PIL import Image
import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
#import cv2

class ImageProcessor:

    def __init__(self):
        pass

    def load(self, image):
        img = Image.open(image)
        print("Loading image of dimensions {0} x {1}".format(img.size[0], img.size[1]))
        img.load()
        data = np.asarray(img, dtype="int32")
        return data

    def display(self, array):
        plt.imshow(array)
        plt.show()






    #    imgplot = plt.imshow(array)


        #img = Image.fromarray(array, 'RGB')
    #    img.save('my.png')
    #    img.show()

        #new_im = Image.fromarray(array)
        #new_im.save("numpy_altered_sample2.png")

    #    im = cv2.imread(image, mode='RGB')
    #    print(type(im))


    #    face = misc.face()
    #    misc.imsave(image, face) # First we need to create the PNG file
    #    face = misc.imread('face.png')
    #    print(type(face))
