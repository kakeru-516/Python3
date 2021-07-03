import numpy as np
import cv2
import matplotlib.pyplot as plt

# 画像のサイズ
height = 480
width = 720

# 円の中心座標(360 - 1, 240 - 1)
center = (int(width / 2), int(height / 2))

# 円の半径
radious = 50

# データ数
N = 500

# サンプリング間隔
dt = 1 / 100

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 信号の生成
signal = 127 * np.sin(2 * np.pi * 5 * t) + 127

# 画像の出力
for i in range(N):

  # 画像変数の宣言
  img = np.zeros((height, width), np.uint8)

  value = int(signal[i])

  # 円の描画
  cv2.circle(img, center, radious, value, thickness=-1)

  # 障害物
  cv2.rectangle(img, (10 + i, 10), (50 + i, 50), 255, -1)
  cv2.rectangle(img, (10, 10 + i), (50, 50 + i), 255, -1)
  cv2.rectangle(img, (400 - i, 400), (440 - i, 440), 255, -1)

  # 画像出力
  cv2.imwrite('./test/' + str(i) + '.png', img)

# 動画の作成
fourcc = cv2.VideoWriter_fourcc('m','p','4', 'v')
video  = cv2.VideoWriter('video.mp4', fourcc, 100.0, (width, height))

for i in range(N):
  img = cv2.imread('./test/' + str(i) + '.png')
  video.write(img)

video.release()