import numpy as np
import cv2
import matplotlib.pyplot as plt
#plt.rcParams["font.size"] = 24

# データ数
N = 256
#N = 64

# サンプリング間隔
dt = 1 / 100
#dt = 1 / 30

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 周波数軸の作成
freq = np.linspace(0, 1.0 / dt, N)

# 画像の読み込み
img = np.array([cv2.imread('./imgForVideo/'+ str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

# 窓関数
# ブロードキャスト機能を使用するためにtransposeする
img = img.transpose(1, 2, 0)
img = img * np.hanning(N)
img = img.transpose(2, 0, 1)
acf = 1/(sum(np.hanning(N))/N)

# FFT処理
fft_signal = np.fft.fft(img, axis=0)

# FFT処理の複製
fft1 = fft_signal.copy()
fft2 = fft_signal.copy()

# バンドパスフィルタ
fft1[(freq > 5.3), :, :] = 0
fft1[(freq < 4.8), :, :] = 0
fft2[(freq > 10.2), :, :] = 0
fft2[(freq < 9.9), :, :] = 0


# 正規化処理
fft1_amp = acf * np.abs(fft1)
fft1_amp = fft1_amp / (N / 2)
fft1_amp[0, :, :] /= 2
fft2_amp = acf * np.abs(fft2)
fft2_amp = fft2_amp / (N / 2)
fft2_amp[0, :, :] /= 2

# 振幅を画素値にする
output1 = np.max(fft1_amp, axis=0).astype(np.uint8)
output2 = np.max(fft2_amp, axis=0).astype(np.uint8)

# 判別分析法
ret, output1 = cv2.threshold(output1, 0, 255, cv2.THRESH_OTSU)
ret, output2 = cv2.threshold(output2, 0, 255, cv2.THRESH_OTSU)

# 出力
output1 = cv2.medianBlur(output1, ksize=5)
output2 = cv2.medianBlur(output2, ksize=5)
cv2.imwrite('./output1.png', output1)
cv2.imwrite('./output2.png', output2)
