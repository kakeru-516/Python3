# -*- coding: utf-8 -*-
import math
import cv2
import numpy as np
import glob
import os

# --- Local ---
import setFileNameByTime
# import centralRecognition
import constantSetting

# --- マーカの中心座標を求める ---
def centerCoordinates(mask):
  # 輪郭検出
  mask = cv2.medianBlur(mask, 5)
  ret,thresh = cv2.threshold(mask,127,255,0)
  contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  #リストの中の１つ目の長方形を取得
  #リストには検出された長方形がcontours[i]に格納されているが１つしかないはずなのでその１つ目(インデックス番号的には0)を取得する

  if len(contours) == 0:
    print('検出されませんでした')
    return 0, 0
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
  return Xo, Yo
# !-- マーカの中心座標を求める --!

# --- 差分座標[pixel]を求める ---
def diff(x, y):
  x = abs(x - constantSetting.Cx)
  y = abs(y - constantSetting.Cy)
  return x, y
# !-- 差分座標を求める --!

# --- ラジアン[rad]を求める ---
def rad(x, y):
  diff_x, diff_y = diff(x, y)
  return math.asin(diff_x / constantSetting.f(diff_x)), math.asin(diff_y / constantSetting.f(diff_y))
# !-- ラジアン[rad]を求める --!

# --- 距離推定 ---
def getRTheta(fileName = "", height = 0):

  # 以下の画像がGRAYかどうか調べる必要あり
  #  img = centralRecognition.centralRecognition()
  img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

  # マーカの中心座標(Mx, My)を求める
  Mx, My = centerCoordinates(img)
  if Mx == 0 and My == 0:
    print('終了します')
    print('jpgファイルを削除します')
    file_list = glob.glob("*jpg")
    for file in file_list:
      os.remove(file)
    return 0, 0
  print('Mx = ' + str(Mx) + ', My = ' + str(My))

  # マーカの中心座標を用いて角度[rad]を求める
  rad_x, rad_y = rad(Mx, My)

  # 推定距離[cm]を求める
  distance_x = constantSetting.h * math.tan(rad_x)
  distance_y = constantSetting.h * math.tan(rad_y)
  distance = math.sqrt(distance_x**2 + distance_y**2)

  # 推定角度[deg]を求める
  angle = math.degrees(math.atan2(distance, constantSetting.h))
  print('推定角度 = ' + str(angle) + '[deg]')

  # 進行方向と, 中心との角度[deg]を求める
  if Mx <= constantSetting.Cx and My > constantSetting.Cy:
    # 第3象限
    theta = math.degrees(rad_x)
  elif Mx <= constantSetting.Cx and My <= constantSetting.Cy:
    # 第2象限
    theta = 180 - math.degrees(rad_x)
  elif Mx > constantSetting.Cx and My <= constantSetting.Cy:
    # 第1象限
    theta = 180 + math.degrees(rad_x)
  elif Mx > constantSetting.Cx and My > constantSetting.Cy:
    # 第4象限
    theta = 360 - math.degrees(rad_x)

  return distance, theta
# !-- 距離推定 --!

if __name__ == "__main__":
  distance, theta = getRTheta()
  print('推定距離 : ' + str(distance) + '[cm]')