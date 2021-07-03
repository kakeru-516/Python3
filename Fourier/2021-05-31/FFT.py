import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys

N = 32 # サンプル数
start = int(sys.argv[1])
end = start + N
dt = 1 / 30 # サンプリング間隔[sec]
t = np.arange(0, N * dt, dt) # 時間軸
freq = np.linspace(0, 1.0/dt, N)

img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((N, height, width), dtype=np.uint8)
output = np.zeros((N, height, width), dtype=np.uint8)

for i in range(start, end):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1


# 時間軸方向の画素値を取得
f = img[:, 431, 364]

# 高速フーリエ変換
F = np.fft.fft(f)

# 正規化 + 交流成分2倍
F = F/(N/2)
F[0] = F[0]/2

# 配列Fをコピー
F2 = F.copy()

# フィルタ処理(4 <= frequency <= 6 かつ直流成分は残してある)
F2[freq > 6] = 0
F2[(freq < 4) & (freq != 0)] = 0

# 正規化 + 交流成分2倍を元に戻す
F2[0] = 2 * F2[0]
F2 = (N/2) * F2

# 高速逆フーリエ変換
f2 = np.fft.ifft(F2)
f2 = np.real(f2)

# 正規化 + 交流成分2倍
F2 = F2/(N/2)
F2[0] = F2[0]/2

# 入力信号(時間領域)の表示
plt.subplot(221)
plt.xticks(np.arange(start = 0, stop = 1.2, step = 0.25))
plt.plot(t, f)

# 入力信号(周波数領域)の表示
plt.subplot(222)
plt.plot(freq, np.abs(F))

# 出力信号(時間領域)の表示
plt.subplot(223)
plt.plot(t, f2)

# 出力信号(周波数領域)の表示
plt.subplot(224)
plt.xticks(np.arange(start=0, stop=30+1, step=5))
plt.plot(freq, np.abs(F2))
plt.show()