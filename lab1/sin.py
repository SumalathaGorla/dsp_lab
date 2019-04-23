import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
print(t)
c=np.pi
print(c)
x1=np.sin(2*c*t+30)
plt.plot(t,x1)
plt.title("sine funtion with 30 phase shift")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
