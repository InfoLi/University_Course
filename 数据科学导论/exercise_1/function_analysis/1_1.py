import numpy as np, pandas as pd 
arr_value = np.arange(1,5)
arr_index = ['a','b','c','d']
s1 = pd.Series(arr_value,index = arr_index)
print(s1)