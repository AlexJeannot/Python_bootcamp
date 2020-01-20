from math import sqrt
import numpy as np

def std(x):
    sum = 0.0
    total = 0.0
    if len(x) == 0:
        return None
    else:
        for elem in x:
            sum += elem
        mean = sum / len(x)
        for elem in x:
            total += (elem - mean) ** 2
        return sqrt(total / len(x))

def main():

    X = np.array([0, 15, -9, 7, 12, 3, -21])
    print("My standard deviation X = {0}".format(std(X)))
    print("NumPy standard deviation X = {0}".format(np.std(X)))

    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    print("My standard deviation Y = {0}".format(std(Y)))
    print("NumPy standard deviation Y = {0}".format(np.std(Y)))

main()
