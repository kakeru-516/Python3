import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import myfunction

# データ数
N = 32

# 画像の読み込み開始位置
start = int(input('position read image : '))

# 画像の読み込み終了位置
end = start + N

# サンプリング周波数[Hz]
samplingFreq = 30

# フレームサイズFs(分割するフレームのデータ数)
Fs = 16

# オーバーラップ[%]
overlap = 50

# 画像の読み込み
img = cv2.imread('./img/0.png', cv2.IMREAD_GRAYSCALE)

# 大きさを取得
height, width = img.shape

# データ用の配列宣言
img = np.zeros((N, height, width), dtype=np.uint8)
output = np.zeros((height, width), dtype=np.uint8)

# 画像読み込み用のフラグ
frame = 0

# 最大変化量のデータ
maxdiff = 0

# 画像の読み込み
for i in range(start, end):
  img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
  print('read file name : ' + str(i) + '.png')
  frame += 1

# 変化量が最大のところを探す
for h in range(height):
  for w in range(width):
      f = img[:, h, w]
      if f.max() - f.min() > maxdiff:
          maxdiff = f.max() - f.min()
      if h == height - 1 and w == width - 1:
          print('max = ', str(maxdiff))

for h in range(height):
  for w in range(width):

    # 時間軸方向のデータの抜き出し
    data = img[:, h, w]
    print(type(data))
    # 変化の割合が少なかったらそこを黒として飛ばす
    if data.max() - data.min() < maxdiff * 0.8 :
      output[h][w] = 0
      continue

    # オーバーラップ抽出された時間波形配列を取得
    time_array, N_ave = myfunction.overlap(data, samplingFreq, Fs, overlap)

    # 矩形窓を掛ける
    time_array, acf = myfunction.boxcar(time_array, Fs, N_ave)

    # FFT処理
    fft_array, fft_mean, fft_axis = myfunction.fft_ave(time_array, samplingFreq, Fs, N_ave, acf)

    id_maxOfAmp = fft_mean.argmax()

    if fft_axis[id_maxOfAmp] >= 4 and fft_axis[id_maxOfAmp] <= 6:
      output[h, w] = 255
    else:
      output[h, w] = 0
cv2.imwrite('output.png', output)

