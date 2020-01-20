from math import sqrt
import numpy as np

def mat_vec_prod(x, y):
    final_lst = []
    if len(x) == 0 or len(y) == 0:
        return None
    else:
        for col in x:
            sum = 0
            for index, elem in enumerate(row):
                sum += elem * y[index]
            final_lst.append(list(sum))
        return np.array(final_lst)

def main():

    X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((7,1))
    Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((7,1))

    W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

    print(W)

    #print("My Matrix vector product W & X = {0}".format(mat_vec_prod(W, X)))
    #print("NumPy Matrix vector product W & X = {0}".format(W.dot(X)))

    #print("My Matrix vector product W & Y = {0}".format(mat_vec_prod(W, Y)))
    #print("NumPy Matrix vector product W & Y = {0}".format(W.dot(Y)))

    #print("My Dot product X = {0}".format(dot(X, X)))
    #print("NumPy Dot product X = {0}".format(np.dot(X, X)))

    #print("My Dot product Y = {0}".format(dot(Y, Y)))
    #print("NumPy Dot product Y = {0}".format(np.dot(Y, Y)))

main()
