# -*- coding:utf-8 -*-
import cv2

img = cv2.imread('./output.jpg')
print(img[1640][1232])

cv2.imwrite('detect center.jpg', img)


