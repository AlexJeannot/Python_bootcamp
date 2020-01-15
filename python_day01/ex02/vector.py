
class Vector:

    def __init__(self, initializer):
        if isinstance(initializer, list):
            self.values = initializer
            self.size = len(initializer)
        elif isinstance(initializer, tuple) and len(initializer) == 2 and initializer[0] < initializer[1]:
            list_vec = []
            i = 0
            vec = initializer[0]
            while (initializer[1] > vec):
                list_vec.append(vec)
                vec += 1.0
                i += 1
            self.values = list_vec
            self.size = i
        elif isinstance(initializer, int) and initializer >= 0:
            i = 0.0
            list_vec = []
            while initializer > i:
                list_vec.append(i)
                i += 1.0
            self.values = list_vec
            self.size = int(i)
        else:
            self.values = [0.0]
            self.size = 1

    def __str__(self):
        txt = "(Vector {0})".format(self.values)
        return txt

    def __add__(self, nb):
        list_vec = []
        for elem in self.values:
            list_vec.append(elem + float(nb))
        return Vector(list_vec)

    def __mul__(self, nb):
        list_vec = []
        for elem in self.values:
            list_vec.append(elem * float(nb))
        return Vector(list_vec)

    def __sub__(self, nb):
        list_vec = []
        for elem in self.values:
            list_vec.append(elem - float(nb))
        return Vector(list_vec)

    def __truediv__(self, nb):
        list_vec = []
        for elem in self.values:
            list_vec.append(elem / float(nb))
        return Vector(list_vec)
