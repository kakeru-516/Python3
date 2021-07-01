import numpy as np
import cv2

# データ数
N = 500
#N = 256

# サンプリング間隔
dt = 1 / 100
#dt = 1 / 30

# 時間軸の作成
t = np.arange(0, N * dt, dt)

# 周波数軸の作成
freq = np.linspace(0, 1.0 / dt, N)

# 画像の読み込み
img = np.array([cv2.imread('./2/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

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

# バンドパスフィルタ
fft_signal[(freq > 5.1), :, :] = 0
fft_signal[(freq < 4.9), :, :] = 0

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
cv2.imwrite('2.png', output)
