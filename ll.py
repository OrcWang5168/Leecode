import numpy as np
import scipy.signal as sci
import matplotlib.pyplot as plt
cc = np.arange(100)
print(cc)
fs = 200
f1 = 10
f2 = 20
f3 = 30
f4 = 40
n = np.linspace(0,1,fs*2)   #真实频率只能到n[2]/2
print(n)
yn = [20*np.sin(2*np.pi*f1*i)+10*np.sin(2*np.pi*f2*i)+5*np.sin(2*np.pi*f3*i)+20*np.sin(2*np.pi*f4*i) for i in n]
print(yn)
yyf = np.fft.fft(yn)
print(yyf)
yyyf = np.fft.fftshift(abs(yyf))
N = len(n)
xf = np.linspace(-N/2,N/2-1,int(N))

a= sci.butter(N=5,Wn=(5),btype='lowpass',output='ba',fs=fs)
print(len(a))
yn_filtered = sci.filtfilt(a[0],a[1],yn)
print(type(yn_filtered))

yyff = np.fft.fft(yn_filtered)
# print(yyf)
yyyff = np.fft.fftshift(abs(yyff))
N = len(n)



plt.subplot(2,2,1)
plt.plot(n,yn)
plt.subplot(2,2,2)
plt.plot(xf,yyyf)
plt.subplot(2,2,3)
plt.plot(n,yn_filtered)
plt.subplot(2,2,4)
plt.plot(xf,yyyff)
# plt.xlim(-100,100)
# plt.show()


import numpy as np
from commpy.modulatio import QAMModem
from commpy.filters import rrcosfilter
N = 1024  # output size
mod1 = QAMModem(16)  # QAM16
sB = randint(0, 2, mod1.num_bits_symbol*N*M/4)  # Random bit stream
sQ = mod1.modulate(sB)  # Modulated baud points
sPSF = rrcosfilter(N*4, 0.8, 1, 24)[1]
qW = np.convolve(sPSF, sQ) # Waveform with PSF