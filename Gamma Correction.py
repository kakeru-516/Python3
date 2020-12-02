# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_gamma_img(gamma, img):
    gamma_cvt = np.zeros((256, 1), dtype=np.uint8)
    for i in range(256):
        gamma_cvt[i][0] = 255*(float(i)/255)**(1.0/gamma)
    return cv2.LUT(img, gamma_cvt)


for i in range(8):

    img0 = cv2.imread('./Rotate For Calibration/result' +
                      str(i + 1) + '-0.jpg')
    img1 = cv2.imread('./Rotate For Calibration/result' +
                      str(i + 1) + '-1.jpg')
    img_gamma0 = create_gamma_img(0.33, img0)
    img_gamma1 = create_gamma_img(0.33, img1)
    cv2.imwrite('./Gamma Correction For Rotate Images/result' +
                str(i + 1) + '-0.jpg', img_gamma0)
    cv2.imwrite('./Gamma Correction For Rotate Images/result' +
                str(i + 1) + '-1.jpg', img_gamma1)
