import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
print(t)
c=np.pi
a=c/6 #phase shift
print(c)
x1=np.cos(2*c*t+a)
plt.subplot(1,3,1)
plt.plot(t,x1)
plt.title("cosine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x2=np.sin(2*c*t+a)
plt.subplot(1,3,2)
plt.plot(t,x2)
plt.title("sine funtion  ")
plt.xlabel("time")
plt.ylabel("amplitude")
x3=x1+x2
plt.subplot(1,3,3)
plt.plot(t,x3)
plt.title("sine funtion addition with cosine  ")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()