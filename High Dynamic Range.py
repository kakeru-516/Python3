# -*- coding: utf-8 -*-
import cv2
import numpy as np

# ３枚の画像ファイルを読み込む
img_fn = ["/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Images/Fisheye camera/2020-11-28/img1-0-10000.jpg",
          "/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Images/Fisheye camera/2020-11-28/img1-0-5000.jpg",
          "/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Images/Fisheye camera/2020-11-28/img1-0-1000.jpg",
          "/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Images/Fisheye camera/2020-11-28/img1-0-500.jpg",
          "/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Images/Fisheye camera/2020-11-28/img1-0-100.jpg"]
img_list = [cv2.imread(fn) for fn in img_fn]

# 4枚の画像に対して露出時間をセット
exposure_times = np.array([0.01, 0.005, 0.001, 0.0005, 0.0001], dtype=np.float32)

#mtb = cv2.createAlignMTB()
#mtb.process(img_list, img_list)

# Mertens法によるHDR合成
merge_mertens = cv2.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')

cv2.imwrite(
    "/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/HDR Images/2020-11-28/img1-0.jpg", res_mertens_8bit)
