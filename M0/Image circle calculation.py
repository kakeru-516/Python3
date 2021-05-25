import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('img1-1.jpg')

# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ガウシアンフィルタ
gray = cv2.medianBlur(gray, 5)

#plt.imshow(gray, cmap='gray')
#plt.axis('off')
#plt.show()

# ハフ変換による円検出
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=200, param2=50)
circles = np.squeeze(circles, axis=0)  # (1, N, 3) -> (N, 3)

# 描画する。
if circles is not None:
    for x, y, radius in np.rint(circles).astype(int):
        if x == 1618 :
          print('center: ({}, {}), radius: {}'.format(x, y, radius))
          cv2.circle(img, (x, y), radius, (0, 255, 0), 5)
          #cv2.circle(img, (1610, 1231), radius, (0, 255, 0), 5)
          #cv2.circle(img, (1610, 1231), 2, (0, 0, 255), 5)
          cv2.circle(img, (x, y), 2, (0, 0, 255), 5)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
cv2.imwrite('sample.jpg', img)
plt.axis('off')
plt.show()
