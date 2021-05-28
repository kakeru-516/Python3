# -*- cording:utf-8 -*-
import time
import picamera
import sys
args = sys.argv

# PiCameraインスタンスの作成
camera = picamera.PiCamera()

# --- カメラの設定 ---

# 上下左右反転
camera.hflip = True
camera.vflip = True

# 撮像画像の解像度の指定
camera.resolution = (3280, 2464)

# --- カメラの設定 ---
camera.shutter_speed = 500
time.sleep(1)

# 処理前の時刻
t1 = time.time()


for i in range(1):
  camera.capture('sample' + str(i+5) + '.jpg')
  time.sleep(0.2)

# 処理後の時刻
t2 = time.time()

# 経過時間を表示
elapsed_time = t2-t1
print(f"経過時間：{elapsed_time}")