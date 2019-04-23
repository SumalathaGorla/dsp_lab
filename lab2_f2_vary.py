import matplotlib.pyplot as plt;
import numpy as np;
fs=1000;
f1=10;
f2=int(input("enter second wave frequency:"));
n=int(input("enter number of samples:"));
x=np.arange(n);
a=np.sin(2*np.pi*f1/fs*x);
plt.subplot(211);
plt.plot(x,a);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
b=np.sin(2*np.pi*f2/fs*x);
plt.subplot(212);
plt.plot(x,b);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
plt.show();

