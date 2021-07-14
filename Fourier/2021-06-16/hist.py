#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'IPAexGothic'
plt.rcParams['figure.figsize']= (7, 4)
plt.rcParams["font.size"] = 24


# 入力画像を読み込み
img = cv2.imread('img-3.png', cv2.IMREAD_GRAYSCALE)
img[img > 210] = 0
hist = cv2.calcHist([img],[0],None,[256],[0,256])
x = np.arange(0, 256, 1)

# グラフの作成
plt.xlabel('画素の輝度値')
plt.ylabel('画素数')
plt.annotate("閾値t = (26, 0)", xy = (26, 0), size = 24, xytext = (30, 100),
            color = "black", arrowprops = dict(arrowstyle = '-|>', color='red'))
plt.xlim(-5, 200)
plt.ylim(0, 300)
plt.bar(x, hist[:,0])
plt.savefig("hanning1.png",bbox_inches='tight',dpi=100)