import sys

def create():
    list = sys.argv
    del list[0]
    str = ""
    for elem in enumerate(list):
        str += elem[1]
        if elem[0] != len(list) - 1:
            str += ' '
    return str

def reverse(str):
    return str [::-1]

def caps(str):
    str_cpy = ""
    for elem in str:
        if elem.isupper():
            str_cpy += elem.lower()
        elif elem.islower():
            str_cpy += elem.upper()
        else:
            str_cpy += elem
    return(str_cpy)

def main():
    str = create()
    str = reverse(str)
    str = caps(str)
    print(str)

main()
