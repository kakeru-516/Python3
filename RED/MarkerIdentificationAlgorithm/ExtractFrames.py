# -*- coding:utf-8 -*-
import cv2
import os

def extractFrames(videoName):
  cap = cv2.VideoCapture(os.path.join('video', videoName))
  count = 0
  while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
      cv2.imwrite(os.path.join('img', "{:d}.png".format(count)), frame)
      count += 1
    else:
      break
  cap.release()
  cv2.destroyAllWindows()

if __name__=="__main__":
    extractFrames()