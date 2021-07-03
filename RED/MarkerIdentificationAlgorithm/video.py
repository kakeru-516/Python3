# -*- coding:utf-8 -*-
import picamera
import cv2
import os
from time import sleep

# --- Local ---
from setFileNameByTime import setFileNameByTime

# インスタンス生成
cap = picamera.PiCamera()

# 上下左右反転
cap.hflip = True
cap.vflip = True

# フレームレート : 30[fps]
cap.framerate = 30

# シャッタースピード : 1/300[s]
#cap.shutter_speed = 3333

# 保存ファイル名
video_name = setFileNameByTime()

def Capture():
  # これを入れるとフレームを取り出した時のフレームの枚数が合う？
  sleep(0.7)

  # 録画開始
  cap.start_recording(os.path.join('video', video_name) + '.h264')

  # 1[s]録画
  cap.wait_recording(1.15)

  #録画終了
  cap.stop_recording()

  return video_name

if __name__ == '__main__':
  Capture()