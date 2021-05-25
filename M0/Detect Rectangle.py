import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from PIL import Image
import sys
import sympy as sp

args = sys.argv
# Setting Of Various Flags
Flag_Draw_the_detected_rectangle_on_the_image_and_output = 1
Flag_Image_display_with_matplotlib = 0

img = cv2.imread(args[1])
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#リストの中の１つ目の長方形を取得
#リストには検出された長方形がcontours[i]のiに格納されているが１つしかないはずなのでその１つ目(インデックス番号的には0)を取得する
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

#カメラの座標
Cx = np.int32(1640)
Cy = np.int32(1232)
#print('カメラの中心座標(' + str(Cx) + ', ' + str(Cy) + ')')

#ピクセル数の差分を絶対値でとる
deltaX = abs(Xo - Cx)
deltaY = abs(Yo - Cy)
#print('座標の差分(' + str(deltaX) + ', ' + str(deltaY) + ')')


heightY = deltaY * 2.7 / 2464
heightX = deltaX * 3.6 / 3280

# part1
#print(str(round((heightY * (100 - 9) / 0.79), 5)) + '[cm]')

sp.init_printing()
sp.var('x, a, b, c, d')
Sol3=sp.solve (-0.0000007*x**3+0.00009*x**2+0.0116*x-heightY, x)
print('角度θ = ' + str(round(Sol3[1], 5)) + '[deg]')

a = str(round(Sol3[1], 5))
b = float(a)
print('z = ' + str(round((150-9) * math.tan(b * math.pi / 180), 4)) + '[cm]')


#sp.init_printing()
#sp.var('x, a, b, c, d')
#Sol3=sp.solve (-0.0000007*x**3+0.00009*x**2+0.0116*x-heightX, x)
#print('角度φ = ' + str(round(Sol3[1], 5)) + '[deg]')
#a = str(round(Sol3[1], 5))
#b = float(a)
#print('y = ' + str(round(100 * math.tan(b * math.pi / 180), 4)) + '[cm]')


#検出された長方形を四角で囲み, 画像を保存
if Flag_Draw_the_detected_rectangle_on_the_image_and_output == 1:
  #検出された長方形を四角で囲む
  img = cv2.drawContours(img, contours, -1, (0,255,0), 5)
  cv2.imwrite('Contour-' + str(args[1]), img)

#matplotlibで画像表示
if Flag_Image_display_with_matplotlib == 1:
  #画像の読み込み
  im = Image.open('./sample.jpg')
  #画像をarrayに変換
  im_list = np.asarray(im)
  #貼り付け
  plt.imshow(im_list)
  #表示
  plt.show()