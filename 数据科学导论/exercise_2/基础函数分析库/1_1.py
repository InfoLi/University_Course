from scipy.optimize import fsolve
import numpy as np
def f(x):
    x1,x2 = x.tolist()
    return [5*x1-pow(x2,2)-1,pow(x1,2)-x2-6]

res = fsolve(f,[1,1])

print(res)