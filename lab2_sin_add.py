import matplotlib.pyplot as plt;
import numpy as np;
fs=int(input("enter sample frequency:"));
f1=int(input("enter first wave frequency:"));
f2=int(input("enter second wave frequency:"));
n=int(input("enter number of samples:"));
x=np.arange(n);
a=np.sin(2*np.pi*f1/fs*x);
plt.subplot(311);
plt.plot(x,a);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
b=np.sin(2*np.pi*f2/fs*x);
plt.subplot(312);
plt.plot(x,b);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
c=a+b;
plt.subplot(313);
plt.plot(x,c);
plt.xlabel("samples(n)");
plt.ylabel("amplitude(v)");
plt.show();
python 

