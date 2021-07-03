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
Fs = 24

# オーバーラップ[%]
overlap = 50

# 大きさを取得
height, width = 480, 720

# データ用の配列宣言
output = np.zeros((height, width), dtype=np.uint8)

# 画像の読み込み
img = np.array([cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(start, end)])

# 差分の絶対値をとる
diff = np.abs(np.diff(img.astype(np.int32), axis=0))

# 差分の総和を計算する
diffSum = np.sum(diff, axis=0)

# 差分の総和を0 ~ 255に正規化する
diffSum = diffSum * 255 / diffSum.max()
diffSum = diffSum.astype(np.uint8)

diffSum[150 <= diffSum] = 255
diffSum[150 > diffSum] = 0
#cv2.imwrite('diffSum.png', diffSum)

img = img.transpose(1,2,0)
output = np.array([myfunction.fft(img[h, w, :], samplingFreq, Fs, overlap)
          for h in range(height) for w in range(width)])
output = output.reshape([height, width])

cv2.imwrite('output.png', output)