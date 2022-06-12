import pandas as pd
file = 'F:/python/Data_Science_exercise/exercise_1/function_analysis/ocean_temp.csv' 
df = pd.read_csv(file,encoding='UTF-8',header=None)
print('count:%d'%df.count())
print('mean:%f'%df.mean())
print('std:%f'%df.std())
print('min:%f'%df.min())
print('quantiles:%f'%df.quantile())
print('max:%f'%df.max())
