import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from pylab import *
x=float(input("enter the passband gain="))
y=float(input("enter the stopband gain="))
wp=float(input("enter wp in rad/sec="))
ws=float(input("enter ws in rad/sec="))
if(ws>wp):
	p=np.log(((1/x**2)-1)/((1/y**2)-1))
	q=np.log(wp/ws)
	N=0.5*(p/q)
	print("order of the filter is:",N)
	a=((1/x**2)-1)
	b=(0.5/N)
	c=(a**b)
	wc=wp/c
	print("cut off frequency of the filter is:",wc)
	w=np.arange(0,100,10)
	H=1/((1+((w/wc)**(2*N)))**0.5)
	plt.plot(w,H)
	plt.show()
else:
	print("fliter designing is not possible")
