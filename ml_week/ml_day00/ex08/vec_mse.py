from math import sqrt
import numpy as np

def vec_mse(x, y):
    sub = np.subtract(x,y)
    total = 0.0
    for value in sub:
        total += value **2
    return total / len(sub)

def main():

    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    print("My MSE X & Y = {0}".format(vec_mse(X, Y)))
    print("My MSE X & X = {0}".format(vec_mse(X, X)))
    #print("\nNumPy Matrix-matrix product W & Z = \n{0}".format(W.dot(Z)))

    #print("\nMy Matrix-matrix product Z & W = \n{0}".format(mat_mat_prod(Z, W)))
    #print("\nNumPy Matrix-matrix product Z & W = \n{0}".format(Z.dot(W)))

    #print("My Matrix vector product W & Y = {0}".format(mat_vec_prod(W, Y)))
    #print("NumPy Matrix vector product W & Y = {0}".format(W.dot(Y)))

    #print("My Dot product X = {0}".format(dot(X, X)))
    #print("NumPy Dot product X = {0}".format(np.dot(X, X)))

    #print("My Dot product Y = {0}".format(dot(Y, Y)))
    #print("NumPy Dot product Y = {0}".format(np.dot(Y, Y)))

main()
