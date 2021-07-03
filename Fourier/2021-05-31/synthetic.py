import cv2
import numpy as np
import sys

N = 32 # サンプル数
start = int(sys.argv[1])
end = start + N

img = cv2.imread('./output/' + str(start) + '.png', cv2.IMREAD_COLOR)

height = img.shape[0]
width = img.shape[1]
frame = 0
maxdiff = 0

img = np.zeros((N, height, width), dtype=np.uint8)
for i in range(start, end):
    img[frame] = cv2.imread('./output/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    print('読み込んだファイル名 = ' + str(i) + '.png')
    frame += 1

mask = np.zeros((height, width), dtype='uint64')

for i in range(N):
    if i == N - 1:
      break
    diff = cv2.absdiff(img[i + 1], img[i]) * 0.1
    diff = diff.astype(np.uint64)
    mask = mask + diff

mask = mask.astype(np.uint8)
#threshold = int(mask.max() * 0.8)
#ret, mask = cv2.threshold(mask, threshold, 255, cv2.THRESH_BINARY)

mask = cv2.medianBlur(mask, ksize=13)
cv2.imwrite(str(start) + '-' + str(end) + '.png', mask)