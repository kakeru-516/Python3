import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 32
img = np.array([cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(N)])

# 差分の絶対値をとる
diff = np.abs(np.diff(img.astype(np.int32), axis=0))

# 差分の総和を計算する
diffSum = np.sum(diff, axis=0)

# 差分の総和を0 ~ 255に正規化する
diffSum = diffSum * 255 / diffSum.max()
diffSum = diffSum.astype(np.uint8)

diffSum[150 <= diffSum] = 255
diffSum[150 > diffSum] = 0

cv2.imwrite('diffSum.png', diffSum)
data = cv2.imread('./diffSum.png', 0)
