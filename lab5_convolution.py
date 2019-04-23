import numpy as np
a=int(input("enter length of x[n]:"))
b=int(input("enter length of y[n]:"))
x=np.arange(a)
print("enter samples for x[n]")
for i in range(0,a):
	x[i]=int(input())
h=np.arange(b)
print("enter samples for y[n]")
for i in range(0,b):
	h[i]=int(input())
y=np.arange(a+b-1)
for n in range(0,a+b-1):
	sum=0
	for k in range(0,a):
		if(n-k>=0 and n-k<b):
			sum=sum+x[k]*h[n-k]
	y[n]=sum
print(y)
