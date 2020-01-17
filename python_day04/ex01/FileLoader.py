import pandas as pd

class FileLoader:

    def load(self, path):
        db = pd.read_csv(path, header = 0, index_col = False)
        print("Loading dataset of dimensions {0} x {1}".format(len(db), len(db.columns)))
        return db

    def display(self, db, nb):
        if nb > 0:
            print(db.head(nb))
        elif nb < 0:
            print(db.tail(abs(nb)))
        else:
            print("Wrong number of lines")
