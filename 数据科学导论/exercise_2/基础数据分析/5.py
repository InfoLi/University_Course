import pandas as pd, numpy as np 
import matplotlib.pyplot as plt
df = pd.read_csv('F:/python/Data_Science_exercise/exercise_2/fifa19/data.csv')

df.plot.scatter(x='Age',y='Finishing')
# df['Special'].plot.bar()
# df['Age'].plot.hist(alpha=0.5)
plt.show()