# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading Images For Differences
for i in range(6):
    img0 = cv2.imread('./Calibration/2020-11-18/result' +
                      str(i + 1) + '-0.jpg')
    imgB = cv2.imread('./Calibration/2020-11-18/result' +
                      str(i + 1) + '-1-b.jpg')
    imgG = cv2.imread('./Calibration/2020-11-18/result' +
                      str(i + 1) + '-1-g.jpg')
    imgR = cv2.imread('./Calibration/2020-11-18/result' +
                      str(i + 1) + '-1-r.jpg')
    rotate_img0 = cv2.rotate(img0, cv2.ROTATE_180)
    rotate_img1 = cv2.rotate(imgB, cv2.ROTATE_180)
    rotate_img2 = cv2.rotate(imgG, cv2.ROTATE_180)
    rotate_img3 = cv2.rotate(imgR, cv2.ROTATE_180)
    cv2.imwrite('./Rotate For Calibration/2020-11-18/result' +
                str(i + 1) + '-0.jpg', rotate_img0)
    cv2.imwrite('./Rotate For Calibration/2020-11-18/result' +
                str(i + 1) + '-1-b.jpg', rotate_img1)
    cv2.imwrite('./Rotate For Calibration/2020-11-18/result' +
                str(i + 1) + '-1-g.jpg', rotate_img2)
    cv2.imwrite('./Rotate For Calibration/2020-11-18/result' +
                str(i + 1) + '-1-r.jpg', rotate_img3)
