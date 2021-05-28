import RPi.GPIO as GPIO
import picamera
from time import sleep
from convertToMp4 import cvtToMp4
from ExtractFrames import extractFrames
import cv2
import os
import sys
args = sys.argv

# インスタンス生成
cap = picamera.PiCamera()

# 画像サイズの指定
#cap.resolution = (1920, 1080)

# 上下左右反転
cap.hflip = True
cap.vflip = True

# フレームレート : 30[fps]
cap.framerate = 30

# シャッタースピード : 1/300[s]
#cap.shutter_speed = 3333

# ISO感度の設定
#cap.iso = int

# 保存ファイル名
video_name = input('Save file name : ')

# これを入れるとフレームを取り出した時のフレームの枚数が合う？
cap.start_preview()
sleep(0.7)

# 録画開始
cap.start_recording(video_name + ".h264")

# 1[s]録画
cap.wait_recording(5)

#録画終了
cap.stop_recording()

# mp4形式へ変換
#cvtToMp4(video_name)

# mp4動画からフレームの取り出し
#extractFrames(video_name + '.mp4', 'outputdir')