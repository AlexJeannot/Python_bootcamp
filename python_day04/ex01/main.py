from FileLoader import FileLoader
from YoungestFellah import YoungestFellah

obj = FileLoader()
data = obj.load("athlete_events.csv")
print(YoungestFellah(data))
