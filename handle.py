import numpy as np
import commpy.modulation as QAM
import matplotlib.pyplot as plt
from commpy.filters import rrcosfilter

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
N = 64  # output size
mod1 = QAM.QAMModem(16)  # QAM16
print(mod1.num_bits_symbol)
sB = np.random.randint(0, 2, mod1.num_bits_symbol*N)  # Random bit stream
sQ = mod1.modulate(sB)  # Modulated baud points
X_input = [np.real(i) for i in sQ]
Y_input = [np.imag(i) for i in sQ]
print(np.real(sQ[1]))
plt.subplot(2,3,1)
plt.scatter(X_input,Y_input)
plt.title("调整后的16QAM星座图")
plt.subplot(2,3,2)
plt.plot(X_input)
plt.title("X支路信号时域波形")
yyff = np.fft.fft(X_input)
# print(yyf)
yyyff = np.fft.fftshift(abs(yyff))

plt.subplot(2,3,3)
plt.title("X支路信号的频谱")
plt.plot(yyyff)


sPSF = rrcosfilter(4*3, 0.8, 1, 2000)[1]
qW = np.convolve(sPSF, sQ) # Waveform with PSF
X_input = [np.real(i) for i in qW]
Y_input = [np.imag(i) for i in qW]
plt.subplot(2,3,4)
plt.scatter(X_input,Y_input)
plt.title("成型后的信号星座图")
yyff = np.fft.fft(X_input)
# print(yyf)
yyyff = np.fft.fftshift(abs(yyff))
plt.subplot(2,3,5)
plt.plot(yyyff)
plt.title("成型后的X支路频谱图")
plt.show()
print(qW)