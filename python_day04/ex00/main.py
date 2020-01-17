from FileLoader import FileLoader

obj = FileLoader()
data = obj.load("athlete_events.csv")
print("\nPOSITIVE\n")
obj.display(data, 5)
print("\nNEGATIVE\n")
obj.display(data, -5)
