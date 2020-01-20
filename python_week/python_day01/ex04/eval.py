
class Evaluator:

    def zip_evaluate(cls, coefs, words):
        if (len(coefs) != len(words)):
            return -1
        zipped = zip(coefs, words)
        list_values = list(zipped)
        print(list_values)
        total = 0
        for elem in list_values:
            total += (elem[0] * len(elem[1]))
        return total

    def enumerate_evaluate(cls, coefs, words):
        if (len(coefs) != len(words)):
            return -1
        total = 0
        for index, elem in enumerate(coefs):
            total += (elem * len(words[index]))
        return total

    zip_evaluate = classmethod(zip_evaluate)
    enumerate_evaluate = classmethod(enumerate_evaluate)


def main():

    coefs = [1, 2, 3]
    words = ["oui", "no", "o"]

    s1 = Evaluator.zip_evaluate(coefs, words)
    print(s1)

    s2 = Evaluator.enumerate_evaluate(coefs, words)
    print(s2)

main()
