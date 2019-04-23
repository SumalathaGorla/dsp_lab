import numpy as np
import matplotlib.pyplot as plt
def movavg(x):
	p=int(input("enter order:"))
	n=len(x)
	z=[]
	for i in range(n):
		s=0
		for k in range(p):
			if i-k<n and i-k>=0:
				s=s+x[i-k]
		y=float(s)/float(p)
		z=np.append(z,y)
	return(z)
x=[]
g=int(input("enter number of samples:"))
for j in range(g):
	s=int(input("enter samples:"))
	x=np.append(x,s)
print(x)
result=movavg(x)
print(result)
f1=int(input("enter signal frequency:"))
fs=int(input("enter sampling frequency:"))
x1=np.arange(0,100,0.1)
y1=np.sin(2*np.pi*(float(f1)/float(fs))*x1)
plt.subplot(411)
plt.plot(y1)
N=np.random.rand(y1.shape[0])
plt.subplot(412)
plt.plot(N)
y2=y1+N
plt.subplot(413)
plt.plot(y2)
d=movavg(y2)
plt.subplot(414)
plt.plot(d)
plt.xlabel("samples")
plt.ylabel("amplitude")
plt.show()

