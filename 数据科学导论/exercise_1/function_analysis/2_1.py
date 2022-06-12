import pandas as pd,numpy as np 
file = 'F:/python/Data_Science_exercise/exercise_1/function_analysis/ocean_temp.csv' 
df = pd.read_csv(file,encoding='UTF-8',header=None)
tempArr = np.array(df)
print("大小：",tempArr.size)
print("类型：",type(tempArr))