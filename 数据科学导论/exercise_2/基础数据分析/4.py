import pandas as pd, numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as st
import math
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')
u1,u2 = df['Dribbling'].mean(),df['BallControl'].mean()
std1,std2 = df['Dribbling'].std(),df['BallControl'].std()
print('Dribbling正态性检验：\n',st.kstest(df['Dribbling'],'norm',(u1,std1)))
print('Dribbling正态性检验：\n',st.kstest(df['BallControl'],'norm',(u2,std2)))
df['(x-u1)*(y-u2)'] = (df['Dribbling'] - u1) * (df['BallControl'] - u2)
df['(((x-u1)**2)*((y-u2)**2))**0.5'] = (((df['Dribbling'] - u1)**2)*((df['BallControl'] - u2)**2))**0.5
# df['((x-u1)**2)'] = (df['Dribbling'] - u1)**2
# df['((x-u2)**2)'] = (df['BallControl'] - u2)**2
r_xy = df['(x-u1)*(y-u2)']/df['(((x-u1)**2)*((y-u2)**2))**0.5']
# r_xy = sum(df['(x-u1)*(y-u2)'])/((sum(df['((x-u1)**2)'])*sum(df['((x-u2)**2)']))**0.5)
print(r_xy)
print(df['Dribbling'].corr(df['BallControl']))
df.plot.scatter(x='Dribbling',y='BallControl')
plt.show()
