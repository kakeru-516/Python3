# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys

# 画像を読み込んでRGBからGRAYに変換
img0 = cv2.imread(filename='./Images/Fisheye camera/2021-03-16/5-0.jpg')
img1 = cv2.imread(filename='./Images/Fisheye camera/2021-03-16/5-1.jpg')
img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# 差分処理
mask = cv2.absdiff(img0, img1)

# 2値化処理
th = 100
mask[mask < th] = 0
mask[mask >= th] = 255

# 出力
cv2.imwrite('./absdiff1.jpg', mask)


