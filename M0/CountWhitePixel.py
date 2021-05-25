# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

args = sys.argv
img = cv2.imread(
  filename='./Output/Fisheye camera/2021-01-07/Center/OSG5XME3C1E/' + str(args[1]) + '.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(np.count_nonzero(gray == 255))
