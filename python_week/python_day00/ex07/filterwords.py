import sys
import string

def filter(str, nb):
    final_list = []
    list = str.split(' ')
    for elem in list:
        if len(elem) > nb:
            final_list.append(elem)
    return final_list

def main():
    letter = False
    for elem in sys.argv[1]:
        if elem in string.letters:
            letter = True
    if (len(sys.argv) != 3 or letter == False):
        print("ERROR")
        return 0
    else:
        try:
            nb = int(sys.argv[2])
        except:
            print("ERROR")
            return 0
        print(filter(sys.argv[1], nb))

main()
