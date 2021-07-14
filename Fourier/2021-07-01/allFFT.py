import numpy as np
import cv2
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 24

# データ数
#N = 128
N = 64

# サンプリング間隔
#dt = 1 / 100
dt = 1 / 30

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 周波数軸の作成
freq = np.linspace(0, 1.0 / dt, N)

# 画像の読み込み
img = np.array([cv2.imread('./img/'+ str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

# 出力用変数
output = np.zeros((img.shape[1], img.shape[2]), dtype=np.uint8)


# 窓関数
# ブロードキャスト機能を使用するためにtransposeする
img = img.transpose(1, 2, 0)
img = img * np.hanning(N)
img = img.transpose(2, 0, 1)
acf = 1/(sum(np.hanning(N))/N)

# FFT処理
fft_signal = np.fft.fft(img, axis=0)
fft_signal_amp = acf * np.abs(fft_signal[:, 240, 360])
fft_signal_amp = fft_signal_amp / (N / 2)
fft_signal_amp[0] = fft_signal_amp[0] / 2

#plt.bar(freq[:int(N/2) + 1], np.abs(fft_signal_amp[:int(N/2) + 1]))
#plt.xlabel('Frequency [Hz]')
#plt.ylabel('|F(ω)|')
#plt.savefig("hanning0.png",bbox_inches='tight',dpi=100)

# バンドパスフィルタ
#fft_signal[(freq > 5.3), :, :] = 0
#fft_signal[(freq < 4.8), :, :] = 0
fft_signal_amp[(freq > 5.3)] = 0
fft_signal_amp[(freq < 4.8)] = 0

plt.bar(freq[:int(N/2) + 1], np.abs(fft_signal_amp[:int(N/2) + 1]))
plt.xlabel('Frequency [Hz]')
plt.ylabel('|F(ω)|')
plt.savefig("hanning1.png",bbox_inches='tight',dpi=100)

# 正規化処理
fft_signal_amp = acf * np.abs(fft_signal)
fft_signal_amp = fft_signal_amp / (N / 2)
fft_signal_amp[0, :, :] /= 2

# 振幅を画素値にする
output = np.max(fft_signal_amp, axis=0).astype(np.uint8)

# 判別分析法
ret, output = cv2.threshold(output, 0, 255, cv2.THRESH_OTSU)

# 出力
output = cv2.medianBlur(output, ksize=5)
cv2.imwrite('./output.png', output)
