# coding: utf-8
import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 24

N = 51
w_barthann = signal.barthann(N)
w_bartlett = signal.bartlett(N)
w_blackman = signal.blackman(N)
w_blackmanharris = signal.blackmanharris(N)
w_bohman = signal.bohman(N)
w_boxcar = signal.boxcar(N)
w_chebwin = signal.chebwin(N, at=100)
w_cosine = signal.cosine(N)
w_flattop = signal.flattop(N)
w_gaussian = signal.gaussian(N, std=7)
w_general_gaussian = signal.general_gaussian(N, p=1.5, sig=7)
w_hamming = signal.hamming(N)
w_hann = signal.hann(N)
w_kaiser = signal.kaiser(N, beta=14)
w_nuttall = signal.nuttall(N)
w_parzen = signal.parzen(N)
w_triang = signal.triang(N)

#plt.figure(figsize=(13,5))
#plt.subplot(1, 2, 1)
plt.plot(w_hann)
plt.xlabel('t [sec]')
plt.ylabel('w(t)')
plt.savefig("hanning0.png",bbox_inches='tight',dpi=100)

def plotFR(w):
    A = fft(w, 2048) / (len(w)/2.0)
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
    plt.plot(freq, response)
    plt.xlabel('ω [rad]')
    plt.ylabel('10$\it{log_{10}}$|W(ω)/max(W(ω))|')


#plotFR(w_hann)
#plt.axis([-0.5, 0.5, -120, 0])
##plt.suptitle('Hanning')
#plt.savefig("hanning1.png",bbox_inches='tight',dpi=100)
