import numpy as np
import random

class NumPyCreator():

    def __init__(self):
        pass

    def from_list(self, my_list):
        return np.array(my_list)

    def from_tuple(self, my_tuple):
        return np.array(my_tuple)

    def from_iterable(self, my_iter):
        return np.array(my_iter)

    def from_shape(self, my_shape):
        return np.zeros_like(np.arange(my_shape[0] * my_shape[1]).reshape(my_shape))

    def random(self, my_shape):
        return(np.random.rand(my_shape[0], my_shape[1]))
        #return np.arange(my_shape[0] * my_shape[1]).reshape(my_shape)
    #    return np.full((my_shape), random.uniform(0, 1))
        #return np.full_like(np.arange(my_shape[0] * my_shape[1]).reshape(my_shape), random.uniform(0, 1))

    def identity(self, n):
        return(np.identity(n))
