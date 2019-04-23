#fs=16000hz
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
fs1,data1=wav.read('rose1.wav')
print(fs1,len(data1),data1)
plt.subplot(211)
plt.plot(data1)
t=np.arange(0,len(data1)/fs1,1.0/fs1)
plt.subplot(212)
plt.plot(t,data1)
plt.show()
