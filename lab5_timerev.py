import numpy as np
n=int(input("enter number of sample:"))
x=[]
for i in range(n):
	z=int(input("enter samples:"))
	x=np.append(x,z)
print(x)
lnx=n
y=np.zeros(lnx)
for i in range(lnx):
	if lnx-i>=0 and lnx-i<=lnx:
		y[i]=x[lnx-i-1]
	print(y)
print("time revesal of x[n] is:",y)
	
