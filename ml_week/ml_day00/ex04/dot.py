from math import sqrt
import numpy as np

def dot(x, y):
    sum = 0.0
    total = 0.0
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        return None
    else:
        for index, elem in enumerate(x):
            sum += elem * y[index]
        return sum

def main():

    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    print("My Dot product X & Y = {0}".format(dot(X, Y)))
    print("NumPy Dot product X & Y = {0}".format(np.dot(X, Y)))

    print("My Dot product X = {0}".format(dot(X, X)))
    print("NumPy Dot product X = {0}".format(np.dot(X, X)))

    print("My Dot product Y = {0}".format(dot(Y, Y)))
    print("NumPy Dot product Y = {0}".format(np.dot(Y, Y)))

main()
