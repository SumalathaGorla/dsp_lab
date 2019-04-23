import numpy as np
n=int(input("enter number number of samples:"))
x=[]
for i in range(n):
	y=int(input("enter samples:"))
	x=np.append(x,y)
print("entered samples:",x)
y=[]
s=0
for i in range(n):
	s=s+x[i]
	y=np.append(y,s)
print("accumulator result:",y)
