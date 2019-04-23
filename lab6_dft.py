from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
z=int(input("enter number of samples for x[n]:"))
x=[]
print("enter samples for x[n]")
for i in range(0,z):
	y=int(input())
	x=np.append(x,y)
print("x[n]=",x)
N=int(input("enter points for dft:"))
k=int(input("enter k value:"))
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,k):
	s=0
	for n in range(0,len(x)):
		v=np.exp(-j*2*np.pi*i*n/N)
		s=s+(x[n]*v)
	X.append(s)
plt.subplot(211)
plt.stem(np.abs(X))
plt.xlabel("freq(w/pi)")
plt.ylabel("magnitude")
plt.title("manitude spectrum")
plt.grid()
plt.subplot(212)
plt.stem(np.angle(X)/np.pi)
plt.xlabel("freq(w/pi)")
plt.ylabel("phase angle in radian")
plt.title("phase spectrum")
plt.grid()
plt.show()

