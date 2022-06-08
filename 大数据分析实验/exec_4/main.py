import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import numpy as np

df = pd.read_csv('data/heart.csv')
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
scaler = MinMaxScaler()
df=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
print(df.corr())
sns.heatmap(df.corr(), annot=True, vmax=1, square=True, cmap="Greens", fmt='.2g')
plt.show()
