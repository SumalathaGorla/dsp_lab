#fs=8000hz
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
fs2,data2=wav.read('rose2.wav')
print(fs2,len(data2),data2)
plt.subplot(211)
plt.plot(data2)
t=np.arange(0,len(data2)/fs2,1.0/fs2)
plt.subplot(212)
plt.plot(t,data2)
plt.show()
