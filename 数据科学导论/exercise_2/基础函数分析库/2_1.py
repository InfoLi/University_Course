import numpy as np 
from matplotlib import pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=14)

x = np.linspace(-np.pi*2, np.pi*2, 256, endpoint=True)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12,5))
plt.title("sinx与cosx",fontproperties=font)
plt.xlabel("x轴",fontproperties=font)
plt.ylabel("y轴",fontproperties=font)

plt.plot(x,y1,linewidth = 2.0,color = "red",label = "y1=sinx")
plt.plot(x,y2,linewidth = 2.0,color = "blue",label = "yx=cosx")
plt.show()