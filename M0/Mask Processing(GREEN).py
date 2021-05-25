# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys

# Setting Of Various Flags
Flag_Show_Images_Of_Mask_And_Masked = 1
Flag_Image_Display_Before_medianBlur_processing = 0
args = sys.argv

def detectGreenColor(img):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set Green Range
    #hsv_min = np.array([30, 64, 150])
    hsv_min = np.array([40, 64, 150])
    hsv_max = np.array([90, 255, 255])

    # Mask In The Green Area
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # Masking Process
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

for i in range(len(args) - 1):
  # Loading Images For Differences
  #img0 = cv2.imread(
  #    filename='./HDR Images/2021-01-13-PM/Center/OS-5050A/' + str(args[i + 1]) + '-0.jpg')
  #img1 = cv2.imread(
  #    filename='./HDR Images/2021-01-13-PM/Center/OS-5050A/' + str(args[i + 1]) + '-1.jpg')
  img0 = cv2.imread(
      filename='./Images/Movie/2021-02-04/3[m]/' + str(args[i + 1]) + '-0.jpg')
  img1 = cv2.imread(
      filename='./Images/Movie/2021-02-04/3[m]/' + str(args[i + 1]) + '-1.jpg')
  greenMask0, greenMasked0 = detectGreenColor(img0)
  greenMask1, greenMasked1 = detectGreenColor(img1)

  # Show Images Of Mask And Masked
  if Flag_Show_Images_Of_Mask_And_Masked == 1:
      cv2.imwrite('./Mask/2021-01-13-PM/Center/OS-5050A/mask-' + str(args[i + 1]) + '-0.jpg', greenMask0)
      cv2.imwrite('./Mask/2021-01-13-PM/Center/OS-5050A/mask-' + str(args[i + 1]) + '-1.jpg', greenMask1)

  # Get Image Size
  height, width = greenMask0.shape

  # Variable Declaration For medianBlur
  medianFilterImage = np.empty(shape=[height, width], dtype=np.uint8)

  # Difference Processing
  medianFilterImage = greenMask0 < greenMask1
  medianFilterImage = medianFilterImage * np.uint8(255)

  # Image Display Before medianBlur processing
  if Flag_Image_Display_Before_medianBlur_processing == 1:
      cv2.imwrite('./BeforeMedianBlur/Fisheye camera/2020-12-15/Center/BESTSUN/HOTSPOT/img1-10.jpg', medianFilterImage)

  # Store Median Blur Images
  medianFilterImage = cv2.medianBlur(medianFilterImage, 15)

  # Show Image
  #cv2.imwrite(
  #    './Output/Fisheye camera/2021-01-13-PM/Center/OS-5050A/' + str(args[i + 1]) + '.jpg', medianFilterImage)
  cv2.imwrite('./3.jpg', medianFilterImage)
