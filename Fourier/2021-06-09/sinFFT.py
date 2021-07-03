import numpy as np
import matplotlib.pyplot as plt
#import matplotlib as mpl
#print(mpl.get_configdir())
#print(matplotlib.matplotlib_fname())
plt.rcParams['font.family'] = 'IPAexGothic'

# サンプリング数
N = 64

# サンプリング周波数
samplingFreq = 64

# 時間軸の作成
t = np.arange(0, N / samplingFreq, 1 / samplingFreq)

# 周波数軸の作成
freq = np.linspace(0, samplingFreq, N)

# 信号波形の作成
f = np.sin(2 * np.pi * 1 * t)

# FFT
F = np.fft.fft(f)

# 振幅スペクトルの計算 + 正規化
F_amp = np.abs(F)

# 高速フーリエ逆変換
ifft = np.fft.ifft(F)
F_amp = F_amp / (N / 2)
F_amp[0] = F_amp[0] / 2

plt.figure(figsize=(6,4))
plt.title('周波数領域')
plt.ylabel('|F(2πf)|')
plt.xlabel('f[Hz]')
plt.bar(freq, F_amp)
plt.show()