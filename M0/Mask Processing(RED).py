# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Setting Of Various Flags
Flag_Show_Images_Of_Mask_And_Masked = 0
Flag_Image_Display_Before_medianBlur_processing = 1


def detectRedColor(img):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set Red Range
    hsv_min = np.array([0, 64, 150])
    hsv_max = np.array([30, 255, 255])

    # Mask In The Red Area1
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # Set Red Range
    hsv_min = np.array([150, 64, 150])
    hsv_max = np.array([179, 255, 255])

    # Mask In The Red Area2
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    #The Red Area1 + The Red Area2
    mask = mask1 + mask2

    # Masking Process
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img


# Loading Images For Differences
img0 = cv2.imread(
    filename='/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/HDR Images/2020-11-28/img5-0.jpg')
img1 = cv2.imread(
    filename='/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/HDR Images/2020-11-28/img5-r.jpg')
redMask0, redMasked0 = detectRedColor(img0)
redMask1, redMasked1 = detectRedColor(img1)

# Show Images Of Mask And Masked
if Flag_Show_Images_Of_Mask_And_Masked == 1:
    cv2.imwrite('./redMask0.jpg', redMask0)
    cv2.imwrite('./redMask1.jpg', redMask1)

# Get Image Size
height, width = redMask0.shape

# Variable Declaration For medianBlur
medianFilterImage = np.empty(shape=[height, width], dtype=np.uint8)

# Difference Processing
medianFilterImage = redMask0 < redMask1
medianFilterImage = medianFilterImage * np.uint8(255)

# Image Display Before medianBlur processing
if Flag_Image_Display_Before_medianBlur_processing == 1:
    cv2.imwrite('./ImageBeforeMedianFilter.jpg', medianFilterImage)

# Store Median Blur Images
medianFilterImage = cv2.medianBlur(medianFilterImage, 15)

# Show Image
cv2.imwrite('/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Output/2020-11-28/HDR/img5-r.jpg', medianFilterImage)
