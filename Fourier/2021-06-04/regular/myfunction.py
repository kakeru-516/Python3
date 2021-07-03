from scipy import signal
import numpy as np

# オーバーラップ処理
def overlap(data, samplingFreq, Fs, overlap):

  # データ長[sec] = (データ数) * (時間刻み幅)
  Ts = len(data) * (1 / samplingFreq)

  # フレーム周期[sec] = (フレームサイズのデータ数) * (時間刻み幅)
  Fc = Fs * (1 / samplingFreq)

  # オーバーラップ位置
  x_ol = Fs * (1 - (overlap / 100))

  # 分割数
  N_ave = int((Ts - (Fc * (overlap / 100))) / (Fc * (1 - (overlap / 100))))

  # 抽出したデータを入れるから配列の宣言
  array = []

  # forループで分割データを抽出
  for i in range(N_ave):

    # オーバーラップ位置の計算
    position = int(x_ol * i)

    # オーバーラップ位置からFs(フレームサイズ)分を1stepで抽出しarrayへ代入
    array.append(data[position:position+Fs:1])

  return array, N_ave

# 窓関数処理(矩形窓)
def boxcar(data_array, Fs, N_ave):

  # 矩形窓作成
  boxcar = signal.hanning(Fs)

  # 振幅補正係数(Amplitude Correction Factor)
  acf = 1 / (sum(boxcar) / Fs)

  # オーバーラップされた複数時間波形に全て窓関数を掛ける
  for i in range(N_ave):

    # 窓関数を掛ける
    data_array[i] = data_array[i] * boxcar

    return data_array, acf

# FFT処理
def fft_ave(data_array, samplingFreq, Fs, N_ave, acf):
  fft_array = []

  # FFTをして配列に追加、窓関数補正値を掛け、(Fs/2)の正規化を実施
  for i in range(N_ave):
    fft_array.append(acf * np.abs(np.fft.fft(data_array[i]) / (Fs / 2)))

  # 周波数軸を作成
  fft_axis = np.linspace(0, samplingFreq, Fs)

  # 型をndarrayに変換
  fft_array = np.array(fft_array)

  # 直流成分の除去
  fft_array[:, 0] = 0

  # 全てのFFT波形のパワー平均を計算してから振幅値とする
  fft_mean = np.sqrt(np.mean(fft_array ** 2, axis = 0))

  return fft_array, fft_mean, fft_axis
