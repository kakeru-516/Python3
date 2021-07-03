import cv2
import numpy as np

img0 = cv2.imread('./diffSum.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('./output.png', cv2.IMREAD_GRAYSCALE)
img = np.zeros((480, 720), dtype=np.uint8)

for i in range(480):
  for j in range(720):
    if img0[i][j] == 255 and img1[i][j] == 255:
      img[i][j] = 255
    else:
      img[i][j] = 0
img = cv2.medianBlur(img, ksize=15)
cv2.imwrite('sample.png', img)