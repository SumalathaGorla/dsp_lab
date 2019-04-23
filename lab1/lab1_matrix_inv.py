e=int(input("enter no.of rows for a matrix:"))
c=int(input("enter no.of coloumns for a matrix:"))
a={}
r={}
print("enter elements for [2,2] matrix:")
for i in range(0,e):
	for j in range(0,c):
		a[i,j]=int(input())
print("a matrix is:")
for i in range(0,e):
	for j in range(0,c):
		print (a[i,j])
d=a[0,0]*a[1,1]-a[0,1]*a[1,0]
x=float(1)/float(d)
r[0,0]=a[1,1]*x
r[0,1]=-a[0,1]*x
r[1,0]=-a[1,0]*x
r[1,1]=a[0,0]*x
print("inverse of above matrix is:")
for i in range(0,e):
	for j in range(0,c):
		print (r[i,j])



