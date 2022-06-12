import pandas as pd,numpy as np 
file = 'F:/python/Data_Science_exercise/exercise_1/function_analysis/ocean_temp.csv' 
df = pd.read_csv(file,encoding='UTF-8',header=None)
adjar = np.array(df)
tempArr = np.array(df)
for i in range(len(adjar)):
    adjar[i] = 20.0
newTemp = np.append(tempArr,adjar)
cTemp = []
def change(f):
    c = 5.0/9.0*(f-32.0)
    return c   
for i in range(len(newTemp)):
    temp = change(i)
    cTemp.append(temp)

print("cTemp",cTemp[20:50])