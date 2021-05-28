import cv2
import os
import sys

def extractFrames(pathIn, pathOut):
  if not os.path.exists(pathOut):
    os.mkdir(pathOut)

  cap = cv2.VideoCapture(pathIn)
  count = 0

  while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
      cv2.imwrite(os.path.join(pathOut, "{:d}.png".format(count)), frame)
      count += 1
    else:
      break

  cap.release()
  cv2.destroyAllWindows()

def main():
  args = sys.argv
  extractFrames(args[1], args[2])

if __name__=="__main__":
    main()