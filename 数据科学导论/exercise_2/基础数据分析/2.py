import pandas as pd, numpy as np 
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')
df1 = df.drop(['Photo','Flag','Club Logo'],axis = 1)
# print(df1.head())
# print(df1.tail())
# print(df.isnull().any())
# print(df.fillna(0).isnull().sum())

df.loc[df['Real Face']=='Yes','Real Face']=1
df.loc[df['Real Face']=='No','Real Face']=0
df.loc[df['Preferred Foot']=='Right','Preferred Foot']=1
df.loc[df['Preferred Foot']=='Left','Preferred Foot']=0
print(df['Real Face'])
print(df['Preferred Foot'])

