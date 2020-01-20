import sys

def operations(x, y):
    res_add = x + y
    res_sub = x - y
    res_mul = x * y
    if (y != 0):
        res_div = x / float(y)
        rest_div = x % y
    else:
        res_div = rest_div = "ERROR (div by zero)"
    return "Sum:           {0}\nDifference:    {1}\nProduct:       {2}\nQuotient:      {3}\nRemainder:     {4}".format(res_add, res_sub, res_mul, res_div, rest_div)

def main():
    if len(sys.argv) != 3:
        if len(sys.argv) == 2:
            print("InputError: Not enough arguments\n")
        elif len(sys.argv) > 3:
            print("InputError: Too many arguments\n")
        print("Usage: python operations.py\nExample:\n    python operations.py 10 3")
        return 0
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    except:
        print("InputError: only numbers\n\nUsage: python operations.py\nExample:\n    python operations.py 10 3")
    print(operations(x, y))
    return 0

main()
