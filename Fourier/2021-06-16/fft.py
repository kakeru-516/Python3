import numpy as np
import matplotlib.pyplot as plt
import cv2
from numpy import fft
plt.rcParams['font.family'] = 'IPAexGothic'

# データ数
#N = 500
N = 256

# サンプリング間隔
#dt = 1 / 100
dt = 1 / 30

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 周波数軸の作成
freq = np.linspace(0, 1.0 / dt, N)
print(freq)

# 画像の読み込み
img = np.array([cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

# 時間軸方向の中心座標信号の抜き取り
#signal = img[:, 240 - 1, 360 - 1]
#signal = img[:, 236 - 1, 209 - 1] # 変化が少ないところ
signal = img[:, 241 - 1, 353 - 1] # マーカの中心点

# FFT処理
fft_signal = np.fft.fft(signal)

# バンドパスフィルタ
fft_signal[(freq > 5.1)] = 0
fft_signal[(freq < 4.9)] = 0

# 振幅スペクトル
fft_signal_amp = np.abs(fft_signal)
fft_signal_amp = fft_signal_amp / (N / 2)
fft_signal_amp[0] = fft_signal_amp[0] / 2

# パワースペクトル
fft_pow = np.abs(fft_signal) ** 2

# グラフ表示
plt.title('振幅スペクトル')
plt.xlabel('周波数[Hz]')
plt.ylabel('|F(ω)|')
plt.bar(freq[:int((N/2) + 1)], fft_signal_amp[:int((N/2) + 1)])
plt.show()
