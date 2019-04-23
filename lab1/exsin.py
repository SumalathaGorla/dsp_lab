import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
x1=np.exp(-t)
c=np.pi
plt.subplot(1,3,1)
plt.plot(t,x1,'g')
plt.title("decreasing signal")
x2=np.sin(2*c*t)
plt.subplot(1,3,2)
plt.plot(t,x2,'b')
plt.title("increasing signal")
x3=x1*x2
plt.subplot(1,3,3)
plt.plot(t,x3,'r')
plt.title("multiplication of two signals")
plt.show()
