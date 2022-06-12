import pandas as pd, numpy as np 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')
max = df['Age'].max()
min = df['Age'].min()
# print(df['Age'])
df['Age'] = (df['Age'] - min)/(max - min)
# print(df['Age'])
plt.hist(df['Age'],histtype='bar', rwidth=0.8)
# plt.legend()
plt.xlabel('Age')
plt.ylabel('number')
plt.show()