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
# 振幅を元の信号のスケールに抑える
# F_abs = F_abs / (N/2) # 交流成分
# F_abs[0] = F_abs[0] / 2 # 直流成分
# F_abs[0] = 0# 直流成分

# グラフ表示(時間軸)
# plt.figure(figsize=(8, 6))
# plt.subplot(211)
# plt.plot(t, f)
# plt.xlabel('Time(s)')
# plt.ylabel('Signal')


# FFTデータからピークを自動検出
maximal_idx = signal.argrelmax(F_abs, order=1)[0]
ampMax_id = F_abs[maximal_idx].argmax()

# グラフ表示（周波数軸）
# plt.subplot(212)
plt.xlabel('Frequency[Hz]')
plt.ylabel('Amplitude')

plt.axis([0,1.0/dt/2,0,max(F_abs)*1.5])
plt.plot(freq, F_abs)
plt.plot(freq[maximal_idx[ampMax_id]], F_abs[maximal_idx[ampMax_id]],'ro')

# グラフにピークの周波数をテキストで表示
for i in range(len(maximal_idx)):
    plt.annotate('{0:.0f}(Hz)'.format(np.round(freq[maximal_idx[ampMax_id]])),
                 xy=(freq[maximal_idx[ampMax_id]], F_abs[maximal_idx[ampMax_id]]),
                 xytext=(10, 20),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2")
                )

# FFTデータからピークを自動検出
maximal_idx = signal.argrelmax(F_abs, order=1)[0]
if any(F_abs[maximal_idx]):
    ampMax_id = F_abs[maximal_idx].argmax()
    if freq[maximal_idx[ampMax_id]] >= 4 and freq[maximal_idx[ampMax_id]] <= 6:
        print('4 <= freq <= 6')
    else:
        print('ピークは4 <= freq <= 6 にない')
else:
    print('')

plt.show()

F2 = F.copy()
F2[(freq > 6)] = 0
f2 = np.fft.ifft(F2)
f2 = np.real(f2*N)
plt.plot(t, f2)
plt.show()

# グラフ表示
fig = plt.figure(figsize=(10.0, 8.0))
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# 時間信号（元）
plt.subplot(221)
plt.plot(t, f, label='f(n)')
plt.xlabel("Time", fontsize=12)
plt.ylabel("Signal", fontsize=12)
plt.grid()
leg = plt.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 周波数信号(元)
plt.subplot(222)
plt.plot(freq, np.abs(F), label='|F(k)|')
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.grid()
leg = plt.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 時間信号(処理後)
plt.subplot(223)
plt.plot(t, f2, label='f2(n)')
plt.xlabel("Time", fontsize=12)
plt.ylabel("Signal", fontsize=12)
plt.grid()
leg = plt.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)

# 周波数信号(処理後)
plt.subplot(224)
plt.plot(freq, np.abs(F2), label='|F2(k)|')
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.grid()
leg = plt.legend(loc=1, fontsize=15)
leg.get_frame().set_alpha(1)
plt.savefig('./sample.png')

