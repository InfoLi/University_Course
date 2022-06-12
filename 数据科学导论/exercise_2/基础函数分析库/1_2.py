import random
from scipy.interpolate import interp1d
import numpy as np

x=np.arange(0,20)
y1 = np.sin(x)
y2 = np.cos(x)


f_1 = interp1d(x,y1)
f_2 = interp1d(x,y2)

x_new = [0.1,5,9]
y1_new = f_1(x_new)
y2_new = f_2(x_new)

print(y1_new)
print(y2_new)