import numpy as np
import matplotlib.pyplot as plt
import cv2
from numpy import fft

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

# 出力用変数
output = np.zeros((img.shape[1], img.shape[2]), dtype=np.uint8)

for h in  range(img.shape[1]):
  for w in range(img.shape[2]):
    # 時間軸方向の中心座標信号の抜き取り
    signal = img[:, h, w]

    # 窓関数
    signal = signal * np.hanning(N)
    acf = 1/(sum(np.hanning(N))/N)

    # FFT処理
    fft_signal = np.fft.fft(signal)

    # バンドパスフィルタ
    fft_signal[(freq > 5.1)] = 0
    fft_signal[(freq < 4.9)] = 0

    # 正規化処理
    #fft_signal_amp = acf * np.abs(fft_signal)
    fft_signal_amp = np.abs(fft_signal)
    fft_signal_amp = fft_signal_amp / (N / 2)
    fft_signal_amp[0] = fft_signal_amp[0] / 2

    # 振幅を画素値にする
    output[h][w] = (fft_signal_amp.max()).astype(np.uint8)

#ret, output = cv2.threshold(output, 0, 255, cv2.THRESH_OTSU)
#output = cv2.medianBlur(output, ksize=5)
cv2.imwrite('output.png', output)
