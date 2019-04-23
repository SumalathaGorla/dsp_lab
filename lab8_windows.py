import numpy as np
import matplotlib.pyplot as plt
def sinc(m):
	h1=[]
	for n in range(-m,m):
		x=np.sin(np.pi/4*n)/(np.pi*n)
		h1=np.append(h1,x)
	h1[m]=1/4
	return h1
def rect_win(m):
	h2=[]
	for n in range(0,m-1):
		x=1
		h2=np.append(h2,x)
	return h2
def tri_win(m):
	h3=[]
	for n in range(0,m-1):
		x1=np.abs(n-(m-1)/2)
		x=1-((2*x1)/(m-1))
		h3=np.append(h3,x)
	return h3
def hann_win(m):
	h4=[]
	for n in range(0,m-1):
		x=0.5-0.5*np.cos(2*np.pi*n/(m-1))
		h4=np.append(h4,x)
	return h4
def hamm_win(m):
	h5=[]
	for n in range(0,m-1):
		x=0.54-0.46*np.cos(2*np.pi*n/(m-1))
		h5=np.append(h5,x)
	return h5
		

