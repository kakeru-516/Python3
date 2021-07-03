import fft_function
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import fftpack

# 画像の大きさを調べるために一度画像を一枚読み込む
img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)
height = img.shape[0]
width = img.shape[1]

# 読み込む画像の３次元配列の宣言
img = np.zeros((32, height, width), dtype=np.uint8)

# 画像読み込み時のインデックス
frame = 0

# 画像読み込み
for i in range(32, 64):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1


samplerate = 30                    # サンプリング周波数[Hz]
Fs = 16                            # フレームサイズ
overlap = 50                       # オーバーラップ率
x = np.arange(0, 32)/samplerate    # 波形生成のための間軸の作成
t = np.arange(0, Fs)/samplerate    # グラフ描画のためのフレーム時間軸作成


#data = np.sin(2.0 * np.pi * 5 * x) #サイン波にランダム成分を重畳
data = img[:, 238, 350]           # 時間軸方向の画素値を取得


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
print(fft_axis[idOfMaxAmp])

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
#ax1.set_xticks(np.arange(0, 0.5, 0.1))
#ax1.set_yticks(np.arange(-5, 5, 1))
#ax1.set_xlim(0, 0.5)
#ax1.set_ylim(-3, 3)
#ax2.set_xticks(np.arange(0, samplerate, 5))
#ax2.set_yticks(np.arange(0, 1, 0.25))
#ax2.set_xlim(0,31)
#ax2.set_ylim(0, 1)

# データプロットの準備とともに、ラベルと線の太さ、凡例の設置を行う。
for i in range(N_ave):
    ax1.plot(t, time_array[i], label='signal', lw=1)

ax2.plot(fft_axis, fft_mean, label='signal', lw=1)

fig.tight_layout()

# グラフを表示する。
plt.show()
plt.close()