import pandas as pd
file = 'F:/python/Data_Science_exercise/exercise_1/function_analysis/ocean_temp.csv'
df = pd.read_csv(file,encoding='UTF-8',header=None)
print(df.head(5))