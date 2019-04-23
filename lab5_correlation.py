import numpy as np
import matplotlib.pyplot as plt
def convolve(x,h):
	y=[]
	b=(len(x)+len(h)-1)
	for n in range(b):
		s=0
		for k in range(len(x)):
			if n-k<len(h) and n-k>=0:
				s=s+(x[k]*h[n-k])
		y=np.append(y,s)
	return(y)
def timerev(x):
	lnx=len(x)
	y=np.zeros(lnx)
	for i in range(lnx):
		if lnx-i>=0 and lnx-i<=lnx:
			y[i]=x[lnx-i-1]
	return(y)
m=int(input("enter number of samples for x[n]:"))
x=[]
for i in range(m):
	y=int(input("enter samples for x[n]:"))
	x=np.append(x,y)
print(x)
p=int(input("enter number of samples for h[n]:"))
h=np.zeros(p)
for i in range(p):
	h[i]=int(input("enter samples for h[n]:"))
print(h)
result=convolve(x,h)
print("convolution of x[n] and h[n] is:",result)
f=timerev(result)
print("time reversal of convolution result is:",f)
rxy=convolve(x,f)
print("cross correlation:",rxy)
f1=int(input("enter signal 1 frequency:"))
f2=int(input("enter signal 2 frequency:"))
fs=int(input("enter sampling frequency:"))
x1=np.arange(0,10,0.1)
y1=np.sin(2*np.pi*(float(f1)/float(fs))*x1)
y2=np.sin(2*np.pi*(float(f2)/float(fs))*x1)
r=convolve(y1,y2)
q=timerev(r)
y3=convolve(y1,q)
N=np.random.rand(y1.shape[0])
xN=y1+N
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y4=convolve(h,xN)
v=timerev(xN)
ac=convolve(v,xN)
plt.subplot(611)
plt.plot(y1)
plt.title("signal 1")
plt.subplot(612)
plt.plot(y2)
plt.title("signal 2")
plt.subplot(613)
plt.plot(r)
plt.title("convolution of signal 1 and signal 2")
plt.subplot(614)
plt.plot(y3)
plt.title("cross correlation")
plt.subplot(615)
plt.plot(y4)
plt.title("convolution of impulse response of MA system and xN")
plt.subplot(616)
plt.plot(ac)
plt.title("auto correlation")
plt.show()

