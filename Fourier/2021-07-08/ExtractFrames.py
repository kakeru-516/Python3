# -*- coding:utf-8 -*-
import cv2
import os
import sys


def extractFrames(videoName):
  cap = cv2.VideoCapture(os.path.join('./video/', videoName + '.h264'))
  count = 0
  os.mkdir('./img/' + videoName)
  while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
      cv2.imwrite(os.path.join('./img/' + videoName, "{:d}.png".format(count)), frame)
      count += 1
    else:
      break
  cap.release()
  cv2.destroyAllWindows()

if __name__=="__main__":
  for i in range(28):
    extractFrames(str(i))