# -*- coding:utf-8 -*-
import cv2
import numpy as np
import os

# --- Local ---
import calculation
import setFileNameByTime
import video
import ExtractFrames

def centralRecognition():

  # 動画の撮影(戻り値は動画のPath)
  videoName = video.Capture()

  # 動画をフレーム分割
  ExtractFrames.extractFrames(videoName + '.h264')

  # データ数
  N = 32

  # サンプリング間隔
  dt = 1 / 30

  # 周波数軸の作成
  freq = np.linspace(0, 1.0 / dt, N)

  # 画像の読み込み
  img = np.array([cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

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
  fft_signal[(freq > 5.2), :, :] = 0
  fft_signal[(freq < 4.7), :, :] = 0

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
  cv2.imwrite(os.path.join('./output/', videoName + '.png'), output)

  return videoName

if __name__=="__main__":
  centralRecognition()