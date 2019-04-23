import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
#print(t)
x1=np.sinc(t)
plt.plot(t,x1)
plt.show()