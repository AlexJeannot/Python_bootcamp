import numpy as np

def sum_(x, f):
    total = 0.0
    if len(x) == 0:
        return None
    else:
        for elem in x:
            total += f(elem)
        return total

def main():

    my_list = np.array([0, 15, -9, 7, 12, 3, -21])
    print(sum_(my_list, lambda x: x**2))

main()
