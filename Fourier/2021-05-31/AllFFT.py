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
maxdiff = 0

img = np.zeros((N, height, width), dtype=np.uint8)
output = np.zeros((N, height, width), dtype=np.uint8)

for i in range(start, end):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1

# 変化している最大値を探す
for h in range(height):
    for w in range(width):
        f = img[:, h, w]
        if f.max() - f.min() > maxdiff:
            maxdiff = f.max() - f.min()

        if h == height - 1 and w == width - 1:
            print('max = ', str(maxdiff))

for h in range(height):
  for w in range(width):

    # 時間軸方向の画素値を取得
    f = img[:, h, w]

    # 変化の割合が少なかったらそこを黒として飛ばす
    if f.max() - f.min() <= maxdiff * 0.8 :
        output[:, h, w] = 0
        continue

    f = f * np.blackman(N)

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # 正規化 + 交流成分2倍
    F = F/(N/2)
    F[0] = F[0]/2

    # 配列Fをコピー
    F2 = F.copy()

    # フィルタ処理①(4 <= frequency <= 6 かつ直流成分は残してある)
    #F2[freq > 6] = 0
    #F2[(freq < 4) & (freq != 0)] = 0

    # フィルタ処理②(4 <= frequency <= 6)
    F2[freq > 5.5] = 0
    F2[freq < 4.5] = 0

    # 正規化 + 交流成分2倍を元に戻す
    F2[0] = 2 * F2[0]
    F2 = (N/2) * F2

    # 高速逆フーリエ変換
    f2 = np.fft.ifft(F2)
    f2 = np.real(f2)

    # 正規化 + 交流成分2倍
    F2 = F2/(N/2)
    F2[0] = F2[0]/2

    output[:, h, w] = f2

frame = 0
for i in range(start, end):
  cv2.imwrite('./output/' + str(i) + '.png', output[frame])
  frame += 1
