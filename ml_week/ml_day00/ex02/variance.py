import numpy as np

def variance(x):
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
        return total / len(x)

def main():

    my_list = np.array([0, 15, -9, 7, 12, 3, -21])
    print("My variance = {0}".format(variance(my_list)))
    print("NumPy variance = {0}".format(np.var(my_list)))
    print("My variance  / 2 = {0}".format(variance(my_list / 2)))
    print("NumPy variance / 2 = {0}".format(np.var(my_list / 2)))
main()
