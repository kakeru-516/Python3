import numpy as np
import matplotlib.pyplot as plt
import cv2
from numpy import fft
plt.rcParams['font.family'] = 'IPAexGothic'
plt.rcParams['figure.figsize']= (10, 5)

# データ数
N = 75

# サンプリング間隔
dt = 1 / 100

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 周波数軸の作成
freq = np.linspace(0, 1.0 / dt, N)

# 信号の作成
signal = np.sin(2 * np.pi * 1 * t)

# 窓関数を掛け合わせる
signal_window = signal * np.hanning(N)
acf = 1/(sum(np.hanning(N))/N)

# FFT処理
fft_signal = np.fft.fft(signal)
fft_signal_window = np.fft.fft(signal_window)

# 振幅スペクトル
fft_signal_amp = np.abs(fft_signal)
fft_signal_amp_window = acf * np.abs(fft_signal_window)
fft_signal_amp = fft_signal_amp / (N / 2)
fft_signal_amp_window = fft_signal_amp_window / (N / 2)
fft_signal_amp[0] = fft_signal_amp[0] / 2
fft_signal_amp_window[0] = fft_signal_amp_window[0] / 2

# グラフ表示
# 窓関数を掛ける前
#plt.suptitle('信号周期の整数倍をデータの区間として選択できた場合', fontsize=20)
plt.suptitle('窓関数を掛けていない', fontsize=20)
plt.subplot(121)
plt.xlabel('時間[sec]', fontsize=20)
plt.ylabel('振幅', fontsize=20)
plt.ylim(-1.2, 1.2)
plt.plot(t, signal, label='y = sin(2π * 1 * t)')
plt.legend(loc="upper right")
plt.subplot(122)
plt.xlabel('周波数[Hz]', fontsize=20)
plt.ylabel('振幅', fontsize=20)
plt.xlim(0, 50)
plt.ylim(0, 1)
plt.bar(freq, fft_signal_amp)

# 窓関数を掛けた後
plt.suptitle('窓関数を掛けている', fontsize=20)
plt.subplot(121)
plt.xlabel('時間[sec]', fontsize=20)
plt.ylabel('振幅', fontsize=20)
plt.ylim(-1.2, 1.2)
plt.plot(t, signal_window, label='y = sin(2π * 1 * t)')
plt.legend(loc="upper right")
plt.subplot(122)
plt.xlabel('周波数[Hz]', fontsize=20)
plt.ylabel('振幅', fontsize=20)
plt.xlim(0, 50)
plt.ylim(0, 1)
plt.bar(freq, fft_signal_amp_window)

plt.show()
