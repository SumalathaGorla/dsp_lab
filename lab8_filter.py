from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from dtftfun import dtft
from windows import sinc
from windows import rect_win
from windows import tri_win
from windows import hann_win
from windows import hamm_win
k=int(input("enter n value:"))
m=int(input("enter m value:"))
h1=sinc(k)
h2=rect_win(m)
h3=tri_win(m)
h4=hann_win(m)
h5=hamm_win(m)
h6=dtft(h1)
plt.subplot(611)
plt.stem(h1)
plt.title("sinc function")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(612)
plt.stem(h2)
plt.title("rectangular window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(613)
plt.stem(h3)
plt.title("triangular window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(614)
plt.stem(h4)
plt.title("h4")
plt.title("hanning window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(615)
plt.stem(h5)
plt.title("hamming window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(616)
plt.stem(np.abs(h6))
plt.title("output")
plt.show()



