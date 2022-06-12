import pandas as pd, numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')
def z_score(x):
    aver = x.mean()
    std = x.std()
    x = (x-aver)/std
    return x
df['Age'] = z_score(df['Age'])
df['Crossing'] = z_score(df['Crossing'])
df['Finishing'] = z_score(df['Finishing'])
box_1 = df['Age']
box_2 = df['Crossing']
box_3 = df['Finishing']
labels = 'Age','Crossing','Finishing'
plt.boxplot([box_1,box_2,box_3],labels = labels)
plt.show()
    
