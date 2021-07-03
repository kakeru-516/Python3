from scipy import signal
import numpy as np

# 窓関数処理(矩形窓)
def boxcar(data_array, N):

  # 矩形窓作成
  boxcar = signal.hanning(N)

  # 振幅補正係数(Amplitude Correction Factor)
  acf = 1 / (sum(boxcar) / N)

  # 窓関数を掛ける
  data_array = data_array * boxcar

  return data_array, acf

# FFT処理
def fft_ave(data_array, samplingFreq, N, acf):
  fft_array = []

  # FFT処理
  fft_array = acf * np.abs(np.fft.fft(data_array) / (N / 2))

  # 周波数軸を作成
  fft_axis = np.linspace(0, samplingFreq, N)

  # 型をndarrayに変換
  fft_array = np.array(fft_array)

  # 直流成分の除去
  fft_array[0] = 0

  return fft_array, fft_axis

def fft(data, samplingFreq, N):
  time_array, acf = boxcar(data, N)
  fft_array, fft_axis = fft_ave(time_array, samplingFreq, N, acf)
  id_maxOfAmp = fft_array.argmax()
  if fft_axis[id_maxOfAmp] >= 4.5 and fft_axis[id_maxOfAmp] <= 5.5:
    return 255
  else:
    return 0
