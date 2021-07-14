import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import shutil

# 画像のサイズ
height = 480
width = 720

# 円1の中心座標
coordinates1 = (int(width / 4), int(height / 2))
# 円2の中心座標
coordinates2 = (int(width * 3 / 4), int(height / 2))

# 円の半径
radious = 50

# データ数
N = 500

# サンプリング間隔
dt = 1 / 100

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 信号の生成
freq5 = 127 * np.sin(2 * np.pi * 5 * t) + 127
freq10 = 127 * np.sin(2 * np.pi * 10 * t) + 127

# 画像の出力
for i in range(N):

  # 画像変数の宣言
  img = np.zeros((height, width), np.uint8)

  value1 = int(freq5[i])
  value2 = int(freq10[i])

  # 円の描画
  cv2.circle(img, coordinates1, radious, value1, thickness=-1)
  cv2.circle(img, coordinates2, radious, value2, thickness=-1)

  # 障害物
  #cv2.rectangle(img, (10 + i, 10), (50 + i, 50), 255, -1)
  #cv2.rectangle(img, (10, 10 + i), (50, 50 + i), 255, -1)
  #cv2.rectangle(img, (400 - i, 400), (440 - i, 440), 255, -1)

  # 保存ディレクトリの存在有無
  if not os.path.exists('./imgForVideo'):

    # 保存ディレクトリがなければディレクトリの作成を行う
    os.mkdir('./imgForVideo')

  # 画像出力
  cv2.imwrite('./imgForVideo/' + str(i) + '.png', img)

# 動画の作成
fourcc = cv2.VideoWriter_fourcc('m','p','4', 'v')
video  = cv2.VideoWriter('video.mp4', fourcc, 100.0, (width, height))

for i in range(N):
  img = cv2.imread('./imgForVideo/' + str(i) + '.png')
  video.write(img)

# 画像が保存してあるディレクトリを削除
shutil.rmtree('./imgForVideo')

video.release()