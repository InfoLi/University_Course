import pandas as pd,numpy as np 
file = 'F:/python/Data_Science_exercise/exercise_1/function_analysis/ocean_temp.csv' 
df = pd.read_csv(file,encoding='UTF-8',header=None)
adjar = np.array(df)
tempArr = np.array(df)
for i in range(len(adjar)):
    adjar[i] = 20.0
newTemp = np.append(tempArr,adjar)
print(newTemp)
