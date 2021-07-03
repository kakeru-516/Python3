import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import myfunction

# データ数
N = 128

# 画像の読み込み開始位置
start = int(input('position read image : '))

# 画像の読み込み終了位置
end = start + N

# サンプリング周波数[Hz]
samplingFreq = 30

# フレームサイズFs(分割するフレームのデータ数)
Fs = 32

# オーバーラップ[%]
overlap = 50

# 画像の読み込み
img = cv2.imread('./img/0.png', cv2.IMREAD_GRAYSCALE)

# 大きさを取得
height, width = img.shape

# データ用の配列宣言
img = np.zeros((N, height, width), dtype=np.uint8)

# 画像読み込み用のフラグ
frame = 0

# 画像の読み込み
for i in range(start, end):
  img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
  print('read file name : ' + str(i) + '.png')
  frame += 1

# 時間軸方向のデータの抜き出し
data = img[:, 239, 355]

# オーバーラップ抽出された時間波形配列を取得
time_array, N_ave = myfunction.overlap(data, samplingFreq, Fs, overlap)

# 矩形窓を掛ける
time_array, acf = myfunction.boxcar(time_array, Fs, N_ave)

# FFT処理
fft_array, fft_mean, fft_axis = myfunction.fft_ave(time_array, samplingFreq, Fs, N_ave, acf)

# 時間軸の作成
t = np.arange(0, Fs) / samplingFreq

#ここからグラフ描画
# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'

# 目盛を内側にする。
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# グラフの上下左右に目盛線を付ける。
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
ax2 = fig.add_subplot(212)
ax2.yaxis.set_ticks_position('both')
ax2.xaxis.set_ticks_position('both')

# 軸のラベルを設定する。
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Signal [V]')
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Signal [V]')

#データの範囲と刻み目盛を明示する。
#ax1.set_xticks(np.arange(0, 2, 0.04))
#ax1.set_yticks(np.arange(-5, 5, 1))
#ax1.set_xlim(0, 0.16)
#ax1.set_ylim(-3, 3)
#ax2.set_xticks(np.arange(0, samplingFreq, 50))
#ax2.set_yticks(np.arange(0, 3, 0.5))
#ax2.set_xlim(0,200)
#ax2.set_ylim(0, 1)

# データプロットの準備とともに、ラベルと線の太さ、凡例の設置を行う。
for i in range(N_ave):
    ax1.plot(t, time_array[i], label='signal', lw=1)

ax2.plot(fft_axis, fft_mean, label='signal', lw=1)

fig.tight_layout()

# グラフを表示する。
plt.show()
plt.close()

