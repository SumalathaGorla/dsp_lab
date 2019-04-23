r1=input("enter no.of rows for m1:")
c1=input("enter no.of coloumns for m1:")
r2=input("enter no.of rows for m2:")
c2=input("enter no.of coloumns for m2:")
if(c1==r2):
	a={}
	print("enter elements for a matrix:")
	for i in range(0,r1):
		for j in range(0,c1):
			a[i,j]=int(input())
	b={}
	print("enter elements for b matrix:")
	for i in range(0,r2):
		for j in range(0,c2):
			b[i,j]=int(input())
	c={}
	for i in range(0,r1):
		for j in range(0,c2):
			c[i,j]=0
			for k in range(0,r2):
				c[i,j]=c[i,j]+a[i,k]*b[k,j]
	print("multiplication of two matrices is:")
	for i in range(0,r1):
		for j in range(0,c2):
			print  (c[i,j])
else:
	print("matrix multiplication is not possible")
