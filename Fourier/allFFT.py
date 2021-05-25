import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 32 # サンプル数
dt = 0.03 # サンプリング間隔[sec]
t = np.arange(0, N * dt, dt) # 時間軸
freq = np.linspace(0, 1.0/dt, N)

img = cv2.imread('./hori/0.png', cv2.IMREAD_COLOR)
# print('y(縦) = ' + str(img.shape[0]))
# print('x(横) = ' + str(img.shape[1]))
# print('(チャネル数) = ' + str(img.shape[2]))

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((N, height, width), dtype=np.uint8)
output = np.zeros((height, width), dtype=np.uint8)

for i in range(0, N):
    img[frame] = cv2.imread('./hori/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    frame += 1

max = 0

# 変化している最大値を探す
for h in range(height):
    for w in range(width):
        f = img[:, h, w]
        if f.max() - f.min() > max:
            max = f.max() - f.min()

        if h == height - 1 and w == width - 1:
            print('max = ', str(max))

for h in range(height):
    for w in range(width):

        f = img[:, h, w] # 0 ~ 255の範囲

        # 変化の割合が少なかったらそこを黒として飛ばす
        if f.max() - f.min() <= max * 0.2 :
            output[h][w] = 0
            continue

        F = np.fft.fft(f) # 高速フーリエ変換

        F_abs = np.abs(F) # 複素数 -> 絶対値に変換

        # 振幅を元の信号のスケールに抑える
        F_abs = F_abs / (N/2) # 交流成分
        F_abs[0] = F_abs[0] / 2 # 直流成分

        # FFTデータからピークを自動検出
        maximal_idx = signal.argrelmax(F_abs, order=1)[0]
        if any(F_abs[maximal_idx]):
            ampMax_id = F_abs[maximal_idx].argmax()
            if np.round(freq[maximal_idx[ampMax_id]]) == 5:
                output[h][w] = 255
            else:
                output[h][w] = 0
        else:
            output[h][w] = 0

output = cv2.medianBlur(output, ksize=13)
cv2.imwrite('output.png', output)

