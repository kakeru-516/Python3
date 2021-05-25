# -*- coding: utf-8 -*-
import math
import cv2
import numpy as np
import picamera
import time

# --- ここに中心認識のプログラムを書く ---
def cap():
  # PiCameraインスタンスの作成
  camera = picamera.PiCamera()

  # --- カメラの設定 ---

  # 上下左右反転
  camera.hflip = True
  camera.vflip = True

  # 撮像画像の解像度の指定
  camera.resolution = (3280, 2464)

  # --- カメラの設定 ---
  camera.shutter_speed = 100
  time.sleep(1)

  for i in range(5):
    camera.capture('sample' + str(i) + '.jpg')

  # 1回目
  # 画像を読み込んでRGBからGRAYに変換
  img0 = cv2.imread(filename='sample0.jpg')
  img1 = cv2.imread(filename='sample1.jpg')
  img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  # 差分処理
  mask1 = cv2.absdiff(img0, img1)
  # 2値化処理
  th = 100
  mask1[mask1 < th] = 0
  mask1[mask1 >= th] = 255

  # 2回目
  # 画像を読み込んでRGBからGRAYに変換
  img0 = cv2.imread(filename='sample1.jpg')
  img1 = cv2.imread(filename='sample2.jpg')
  img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  # 差分処理
  mask2 = cv2.absdiff(img0, img1)
  # 2値化処理
  th = 100
  mask2[mask2 < th] = 0
  mask2[mask2 >= th] = 255

  # 3回目
  # 画像を読み込んでRGBからGRAYに変換
  img0 = cv2.imread(filename='sample2.jpg')
  img1 = cv2.imread(filename='sample3.jpg')
  img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  # 差分処理
  mask3 = cv2.absdiff(img0, img1)
  # 2値化処理
  th = 100
  mask3[mask3 < th] = 0
  mask3[mask3 >= th] = 255

  # 4回目
  # 画像を読み込んでRGBからGRAYに変換
  img0 = cv2.imread(filename='sample3.jpg')
  img1 = cv2.imread(filename='sample4.jpg')
  img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  # 差分処理
  mask4 = cv2.absdiff(img0, img1)
  # 2値化処理
  th = 100
  mask4[mask4 < th] = 0
  mask4[mask4 >= th] = 255

  Mask = mask1 + mask2 + mask3 + mask4
  Mask[Mask >= 255] = 255

  cv2.imwrite('./x.jpg', Mask)
# !-- ここに中心認識のプログラムを書く --!

# --- マーカの中心座標を求める ---
def centerCoordinates(mask):
  # 輪郭検出
  mask = cv2.medianBlur(mask, 5)
  ret,thresh = cv2.threshold(mask,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  print(len(contours))
  #リストの中の１つ目の長方形を取得
  #リストには検出された長方形がcontours[i]に格納されているが１つしかないはずなのでその１つ目(インデックス番号的には0)を取得する
  a = contours[0]

  #x座標とy座標をそれぞれ抽出する.ただし, aはndarray
  x = a[:, :, 0]
  y = a[:, :, 1]

  #検出された長方形の中心座標を計算する
  X1 = (np.amax(x)).astype(np.float32)
  X2 = (np.amin(x)).astype(np.float32)
  Y1 = (np.amax(y)).astype(np.float32)
  Y2 = (np.amin(y)).astype(np.float32)
  Xo = ((X1 + X2) / np.float32(2)).astype(np.int32)
  Yo = ((Y1 + Y2) / np.float32(2)).astype(np.int32)
  #print('検出されたマーカの中心座標(' + str(Xo) + ', ' + str(Yo) + ')')
  return Xo, Yo
# !-- マーカの中心座標を求める --!

# --- カメラの内部パラメータの定義 ---
fx = 675.508479333196
fy = 674.936608139554
Cx = 1633.39414024524
Cy = 1218.19031757266
# !-- カメラの内部パラメータの定義 --!

# --- 天井までの高さ ---
# h1[cm] : 床から天井まで
h1 = 264
# h2[cm] : 床からカメラまで
h2 = 2.2
# h [cm] : カメラから天井まで
h = h1 - h2
# !-- 天井までの高さ --!


# --- 差分座標[pixel]を求める ---
def diff(x, y):
  x = abs(x - Cx)
  y = abs(y - Cy)
  return x, y
# !-- 差分座標を求める --!

# --- ラジアン[rad]を求める ---
def rad(x, y):
  diff_x, diff_y = diff(x, y)
  return math.asin(diff_x / fx), math.asin(diff_y / fy)
# !-- ラジアン[rad]を求める --!

# --- 距離推定 ---
def getRTheta(fileName = "", height = 0):
  cap()

  # 画像を読み込む
  img = cv2.imread('x.jpg', cv2.IMREAD_GRAYSCALE)

  # マーカの中心座標(Mx, My)を求める
  Mx, My = centerCoordinates(img)

  # マーカの中心座標を用いて角度[rad]を求める
  rad_x, rad_y = rad(Mx, My)

  # 距離を求める
  distance = h * math.tan(rad_y) / math.cos(rad_x)
  print(math.degrees(rad_y))
  # 進行方向と, 中心との角度[deg]を求める
  if Mx <= Cx and My > Cy:
    print('第3象限')
    theta = math.degrees(rad_x)
  elif Mx <= Cx and My <= Cy:
    print('第2象限')
    theta = 180 - math.degrees(rad_x)
  elif Mx > Cx and My <= Cy:
    print('第1象限')
    theta = 180 + math.degrees(rad_x)
  elif Mx > Cx and My > Cy:
    print('第4象限')
    theta = 360 - math.degrees(rad_x)

  return distance, theta
# !-- 距離推定 --!

if __name__ == "__main__":
  print(getRTheta())