import pandas as pd, numpy as np 
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')
# print(df.head())
# print(df.tail())
df1 = df[(df[u'Age']<=25)] #age<=25
# print(df1.head())
# print(df1.tail())
jumping_list = df.sort_values(["Jumping"])
# print(jumping_list.head())
# print(jumping_list.tail())
print(df.Volleys.describe())
print(df.Dribbling.describe())