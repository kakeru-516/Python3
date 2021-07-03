from scipy.fftpack.basic import fft
import fft_function
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import fftpack

img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((32, height, width), dtype=np.uint8)
output = np.zeros((24, height, width), dtype=np.uint8)

for i in range(32, 64):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1

samplerate = 30
#t = np.arange(0, 32)/samplerate   #波形生成のための時間軸の作成
##t = np.arange(0, Fs)/samplerate     #グラフ描画のためのフレーム時間軸作成
Fs = 24       #フレームサイズ
overlap = 90    #オーバーラップ率

for h in range(height):
  for w in range(width):
    # 時間軸方向の画素値を取得
    data = img[:, h, w]

    #作成した関数を実行：オーバーラップ抽出された時間波形配列
    time_array, N_ave = fft_function.ov(data, samplerate, Fs, overlap)

    #作成した関数を実行：ハニング窓関数をかける
    time_array, acf = fft_function.hanning(time_array, Fs, N_ave)

    #作成した関数を実行：FFTをかける
    fft_array, fft_mean, fft_axis = fft_function.fft_ave(time_array, samplerate, Fs, N_ave, acf)



    fft_mean[fft_axis > 6] = 0
    fft_mean[(fft_axis < 4) & (fft_axis != 0)] = 0

    a = fftpack.ifft(fft_mean)
    a = a.real
    if h == 0 and w == 0:
      print(a.ndim)

    output[:, h, w] = a

frame = 0
for i in range(32, 56):
  cv2.imwrite('./output/' + str(i) + '.png', output[frame])
  print('i = ' + str(i))
  print('frame = ' + str(frame))
  frame += 1