import numpy as np

def mean(x):
    total = 0.0
    if len(x) == 0:
        return None
    else:
        for elem in x:
            total += elem
        return total / len(x)

def main():

    my_list = np.array([0, 15, -9, 7, 12, 3, -21])
    print(mean(my_list ** 2))

main()
