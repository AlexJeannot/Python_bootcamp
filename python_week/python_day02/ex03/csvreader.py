import csv
import json

class CsvReader():

    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.fd = None
        self.filename = filename

    def getdata(self):
        data = self.fd.read()
        list_lines = data.split("\n")
        list_elem = []
        list_final = []
        for elem in list_lines:
            elem = elem.replace(" ", "")
            elem = elem.replace('"', "")
            list_elem = elem.split(",")
            list_final.append(list_elem)
        dict_json = {}
        i = 0
        for elem in list_final:
            dict_elem = {}
            if i != 0 and elem != [""]:
                for index, value in enumerate(elem):
                    dict_elem[list_final[0][index]] = value
                label_name = "Observation_" + str(i)
                dict_json[label_name] = dict_elem
            i += 1

        with open("file.json", "w") as jsonfile:
             jsonfile.write(json.dumps(dict_json, indent=4))

    def __enter__(self):
        self.fd = open(self.filename, "r")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()
