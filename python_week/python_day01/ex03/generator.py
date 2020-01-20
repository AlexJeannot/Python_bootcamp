import random

def generator(text, sep=" ", option=None):
    if isinstance(text, str) and (option == None or option == "shuffle" or option == "unique" or option == "ordered"):
        list_words = text.split(sep)
        if (option == "shuffle"):
            random.shuffle(list_words)
        elif (option == "unique"):
            list_tmp = set(list_words)
            list_tmp = list(list_tmp)
            list_words = list_tmp
        elif (option == "ordered"):
            list_tmp = sorted(list_words)
            list_words = list_tmp
        return list_words
    else:
        print("ERROR")
        return 0

def main():
    print("LISTE ordered = {}".format(generator("aaa ccc ddd bbb", " ", "ordered")))
    print("LISTE shuffle = {}".format(generator("aaa ccc ddd bbb", " ", "shuffle")))
    print("LISTE unique = {}".format(generator("aaa ccc ddd bbb ccc aaa kkk lll jjj bbb kkk", " ", "unique")))



main()
