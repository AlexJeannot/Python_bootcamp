import numpy as np

def mat_mat_prod(x, y):
    final_lst = []
    if len(x) == 0 or len(y) == 0:
        return None
    else:
        final_lst = []
        for nb_row in range(len(x)):
            inter_lst = []
            for nb_value in range(len(y[0])):
                sum = 0
                for index, value in enumerate(x[nb_row]):
                    sum += value * y[index][nb_value]
                inter_lst.append(sum)

            final_lst.append(inter_lst)
        return np.array(final_lst)

def main():

    W = np.array([
    [ -8, 8, -6, 14, 14, -9, -4],
    [ 2, -11, -2, -11, 14, -2, 14],
    [-13, -2, -5, 3, -8, -4, 13],
    [ 2, 13, -14, -15, -14, -15, 13],
    [ 2, -1, 12, 3, -7, -3, -6]])

    Z = np.array([
    [ -6, -1, -8, 7, -8],
        [ 7, 4, 0, -10, -10],
        [ 7, -13, 2, 2, -11],
        [ 3, 14, 7, 7, -4],
        [ -1, -3, -8, -4, -14],
        [ 9, -14, 9, 12, -7],
        [ -9, -4, -10, -3, 6]])

    print("\nMy Matrix-matrix product W & Z = \n{0}".format(mat_mat_prod(W, Z)))
    print("\nNumPy Matrix-matrix product W & Z = \n{0}".format(W.dot(Z)))

    print("\nMy Matrix-matrix product Z & W = \n{0}".format(mat_mat_prod(Z, W)))
    print("\nNumPy Matrix-matrix product Z & W = \n{0}".format(Z.dot(W)))

    #print("My Matrix vector product W & Y = {0}".format(mat_vec_prod(W, Y)))
    #print("NumPy Matrix vector product W & Y = {0}".format(W.dot(Y)))

    #print("My Dot product X = {0}".format(dot(X, X)))
    #print("NumPy Dot product X = {0}".format(np.dot(X, X)))

    #print("My Dot product Y = {0}".format(dot(Y, Y)))
    #print("NumPy Dot product Y = {0}".format(np.dot(Y, Y)))

main()
