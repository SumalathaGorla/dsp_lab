from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
k=int(input("enter number of samples for x[n]:"))
x=[]
print("enter samples for x[n]:")
for i in range(0,k):
	y=int(input())
	x=np.append(x,y)
print("x[n]=",x)
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	s=0
	for n in range(0,len(x)):
		s=s+(x[n]*np.exp(-n*w[i]*j))
	X.append(s)
print("X[n]=",np.abs(X))
plt.subplot(411)
plt.plot(w,np.abs(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.grid()
plt.subplot(412)
plt.plot(w,angle(X)/np.pi)
plt.xlabel("freq(w/pi)")
plt.ylabel("phase angle in radian")
plt.title("phase spectrum")
plt.grid()
plt.subplot(413)
plt.plot(w,real(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("real part")
plt.title("real values of X")
plt.grid()
plt.subplot(414)
plt.plot(w,imag(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("imaginary part")
plt.title("imaginary values of X")
plt.grid()
plt.show()
