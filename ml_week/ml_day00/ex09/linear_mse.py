from math import sqrt
import numpy as np

def linear_mse(x, y, z):

    dot_list = []
    for elem in x:
        sum = 0
        for index, value in enumerate(elem):
            sum += value * z[index]
        dot_list.append(sum)

    sub = np.subtract(dot_list, y)
    total = 0.0
    for value in sub:
        total += value **2
    return total / len(sub)

def main():

    X = np.array([
            [ -6, -7, -9],
            [ 13, -2, 14],
            [ -7, 14, -1],
            [ -8, -4, 6],
            [ -5, -9, 6],
            [ 1, -5, 11],
            [ 9, -11, 8]])

    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    Z = np.array([3, 0.5, -6])

    print("My MSE X & Y & Z = {0}".format(linear_mse(X, Y, Z)))

    W = np.array([0,0,0])
    print("My MSE X & X & W= {0}".format(linear_mse(X, Y, W)))

main()
