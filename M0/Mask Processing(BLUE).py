# -*- coding:utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Setting Of Various Flags
Flag_Show_Images_Of_Mask_And_Masked = 0
Flag_Image_Display_Before_medianBlur_processing = 0


def detectBlueColor(img):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Set BLUE Range
    hsv_min = np.array([90, 64, 150])
    hsv_max = np.array([150, 255, 255])

    # Mask In The BLUE Area
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # Masking Process
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img


# Loading Images For Differences
img0 = cv2.imread(
    filename='/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/HDR Images/2020-11-28/img5-0.jpg')
img1 = cv2.imread(
    filename='/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/HDR Images/2020-11-28/img5-b.jpg')
blueMask0, blueMasked0 = detectBlueColor(img0)
blueMask1, blueMasked1 = detectBlueColor(img1)

# Show Images Of Mask And Masked
if Flag_Show_Images_Of_Mask_And_Masked == 1:
    cv2.imwrite('./blueMask0.jpg', blueMask0)
    cv2.imwrite('./blueMask1.jpg', blueMask1)

# Get Image Size
height, width = blueMask0.shape

# Variable Declaration For medianBlur
medianFilterImage = np.empty(shape=[height, width], dtype=np.uint8)

# Difference Processing
medianFilterImage = blueMask0 < blueMask1
medianFilterImage = medianFilterImage * np.uint8(255)

# Image Display Before medianBlur processing
if Flag_Image_Display_Before_medianBlur_processing == 1:
    cv2.imwrite('./ImageBeforeMedianFilter.jpg', medianFilterImage)

# Store Median Blur Images
medianFilterImage = cv2.medianBlur(medianFilterImage, 15)

# Show Image
cv2.imwrite('/Users/tsukamotokakeru/Documents/Python3/OpenCV/RED/Output/2020-11-28/HDR/img5-b.jpg', medianFilterImage)
