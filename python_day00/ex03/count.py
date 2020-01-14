import sys
import string

def text_analyzer(str):
    nb_global = 0
    nb_maj = 0
    nb_min = 0
    nb_ponc = 0
    nb_space = 0
    for elem in str:
        if elem.isupper():
            nb_maj += 1
        elif elem.islower():
            nb_min += 1
        elif elem in string.punctuation:
            nb_ponc += 1
        elif elem == ' ':
            nb_space += 1
        nb_global += 1
    print("The text contains {0} characters:\n- {1} upper letters\n- {2} lower letters\n- {3} punctuation marks\n- {4} spaces".format(nb_global, nb_maj, nb_min, nb_ponc, nb_space))


def main():
    if (len(sys.argv) == 1):
        str = "default text"
    else:
        str = sys.argv[1]
    text_analyzer(str)
    return 0

main()
