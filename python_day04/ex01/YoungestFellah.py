import pandas as pd
import numpy as np

def YoungestFellah(db):
#    for index, row in db.iterrows():
#        if row["Sex"] == "M" and  (male == 0.0 or row["Age"] < male):
#            male = row["Age"]
#        elif row["Sex"] == "F" and  (female == 0.0 or row["Age"] < female):
#            female = row["Age"]
    #female = db[db['Sex'] == 'F'].nsmallest(1, 'Age').iloc[0]['Age']
    #male = db[db['Sex'] == 'M'].nsmallest(1, 'Age').iloc[0]['Age']
    #a = a.iloc[0]['Age']
    return {'m': db[db['Sex'] == 'M'].nsmallest(1, 'Age').iloc[0]['Age'], 'f' : db[db['Sex'] == 'F'].nsmallest(1, 'Age').iloc[0]['Age']}
