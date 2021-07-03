import fft_function
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import fftpack
import sys

# 画像の大きさを調べるために一度画像を一枚読み込む
img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)
height = img.shape[0]
width = img.shape[1]

# サンプル数
N = 32
start = int(sys.argv[1])
end = start + N

# 読み込む画像の３次元配列の宣言
img = np.zeros((N, height, width), dtype=np.uint8)

# 出力画像用の2次元配列の宣言
output = np.zeros((height, width), dtype=np.uint8)

# 画像読み込み時のインデックス
frame = 0

# 画像読み込み
for i in range(start, end):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1


samplerate = 30                    # サンプリング周波数[Hz]
Fs = int(N/2)                            # フレームサイズ
overlap = 90                       # オーバーラップ率
t = np.arange(0, Fs)/samplerate    # グラフ描画のためのフレーム時間軸作成
maxdiff = 0

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
    data = img[:, h, w]           # 時間軸方向の画素値を取得

    # 変化の割合が少なかったらそこを黒として飛ばす
    #if data.max() - data.min() <= maxdiff * 0.01 :
    #    output[h, w] = 0
    #    continue

    # 作成した関数を実行：オーバーラップ抽出された時間波形配列
    time_array, N_ave = fft_function.ov(data, samplerate, Fs, overlap)

    # 作成した関数を実行：ハニング窓関数をかける
    time_array, acf = fft_function.hanning(time_array, Fs, N_ave)

    # 作成した関数を実行：FFTをかける
    fft_array, fft_mean, fft_axis = fft_function.fft_ave(time_array, samplerate, Fs, N_ave, acf)

    # 直流成分の除去
    fft_mean[0] = 0

    # 周波数領域においてAmpが最大となるインデックスを取得
    idOfMaxAmp = fft_mean.argmax()

    # 周波数領域においてAmpが最大となるときの周波数
    freqOfMaxAmp = fft_axis[idOfMaxAmp]

    if freqOfMaxAmp >= 4 and freqOfMaxAmp <= 6:
      output[h, w] = 255
    else:
      output[h, w] = 0

#output = cv2.medianBlur(output, ksize=1)
#output = cv2.blur(output, (3, 3))
cv2.imwrite('output.png', output)
