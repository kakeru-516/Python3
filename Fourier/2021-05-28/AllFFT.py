import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sys

N = 256 # サンプル数
start = int(sys.argv[1])
end = start + N
dt = 0.03 # サンプリング間隔[sec]
t = np.arange(0, N * dt, dt) # 時間軸
freq = np.linspace(0, 1.0/dt, N)

img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)
# print('y(縦) = ' + str(img.shape[0]))
# print('x(横) = ' + str(img.shape[1]))
# print('(チャネル数) = ' + str(img.shape[2]))

height = img.shape[0]
width = img.shape[1]
frame = 0
maxdiff = 0

img = np.zeros((N, height, width), dtype=np.uint8)
output = np.zeros((height, width), dtype=np.uint8)

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
    f = img[:, h, w] # y = 214, x = 351の時間軸方向の画素値を取得

    # 変化の割合が少なかったらそこを黒として飛ばす
    if f.max() - f.min() <= maxdiff * 0.7 :
        output[h][w] = 0
        continue

    f = f - np.average(f) # 直流(DC)成分の除去
    F = np.fft.fft(f) # 高速フーリエ変換
    F_abs = np.abs(F) # 複素数 -> 絶対値に変換
    if freq[(F_abs).argmax()] >= 4 and freq[(F_abs).argmax()] <= 6:
      output[h][w] = 255
    else:
      output[h][w] = 0

output = cv2.medianBlur(output, ksize=13)
cv2.imwrite(str(start) + '-' + str(end) + '.png', output)
