from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def multi(nb):
    return nb * 2

def multi_reduce(nb, nb2):
    return nb * nb2 * 10

def even(nb):
    if nb % 2 == 0:
        return True
    else:
        return False

def main():
    list_iter = [1, 2, 3, 4, 5]
    res = ft_map(multi, list_iter)
    print(res)

    res_true = map(multi, list_iter)
    print(res_true)

    list_iter2 = (1, 2, 3, 4, 5)
    res_true2 = map(multi, list_iter2)
    print(res_true2)

    print("\nTEST FILTER\n")

    list_iter = [1, 2, 3, 4, 5]
    res = ft_filter(even, list_iter)
    print(res)

    res_true = filter(even, list_iter)
    print(res_true)

    print("\nTEST FILTER\n")

    list_iter = [1, 2, 3, 4, 5, 6]
    res = ft_reduce(multi_reduce, list_iter)
    print(res)

    res_true = reduce(multi_reduce, list_iter)
    print(res_true)

main()
