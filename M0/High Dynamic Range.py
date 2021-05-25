# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

args = sys.argv
for i in range(len(args) - 1):
  # 画像を読み込む
  img_fn = [
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-10000.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-5000.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-1000.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-500.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-100.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-50.jpg",
      "./Images/Fisheye camera/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + "-10.jpg"
  ]
  img_list = [cv2.imread(fn) for fn in img_fn]
  merge_mertens = cv2.createMergeMertens()
  res_mertens = merge_mertens.process(img_list)
  res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
  cv2.imwrite("./HDR Images/2021-01-13-PM/Center/OS-5050A/" + str(args[i + 1]) + ".jpg", res_mertens_8bit)


