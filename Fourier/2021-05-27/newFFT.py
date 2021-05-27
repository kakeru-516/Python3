import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 32 # サンプル数
start = 32
end = start + N
dt = 0.03 # サンプリング間隔[sec]
t = np.arange(0, N * dt, dt) # 時間軸
freq = np.linspace(0, 1.0/dt, N)

img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)
# print('y(縦) = ' + str(img.shape[0]))
# print('x(横) = ' + str(img.shape[1]))
# print('(チャネル数) = ' + str(img.shape[2]))

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((N, height, width), dtype=np.uint8)

for i in range(start, end):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    frame += 1

f = img[:, 434, 383] # y = 214, x = 351の時間軸方向の画素値を取得
plt.xlabel("Time[sec]", fontsize=12)
plt.ylabel("Pixel Value", fontsize=12)
plt.plot(t, f)
plt.show()
f = f - np.average(f) # 直流(DC)成分の除去
plt.xlabel("Time[sec]", fontsize=12)
plt.ylabel("Pixel Value", fontsize=12)
plt.plot(t, f)
plt.show()

F = np.fft.fft(f) # 高速フーリエ変換

F_abs = np.abs(F) # 複素数 -> 絶対値に変換

for i in range(len(F_abs)):
  print(str(i) + 'Amp = ' + str(F_abs[i]) + ', Freq = ' + str(freq[i]))

print('Ampが最大となる時のindex number = ' + str((F_abs).argmax()))
print('その時のAmp = ' + str(F_abs[(F_abs).argmax()]))
print('その時のFrequency = ' + str(freq[(F_abs).argmax()]) + '[Hz]')

plt.xlabel("frequency [Hz]", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.plot(freq, F_abs)
plt.show()
