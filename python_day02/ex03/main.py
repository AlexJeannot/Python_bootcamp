from csvreader import CsvReader

if __name__ == "__main__":

    print("\n---- TEST GOOD FILE ----\n")
    with CsvReader('good.csv') as file:
        data = file.getdata()
    #    header = file.getheader()

    #print("\n---- TEST BAD FILE ----\n")
#    with CsvReader('bad.csv') as file:
    #    if file == None:
    #        print("File is corrupted")
