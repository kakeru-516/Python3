import cv2
import numpy as np

N = 32 # サンプル数

img = cv2.imread('./hori/0.png', cv2.IMREAD_COLOR)
# print('y(縦) = ' + str(img.shape[0]))
# print('x(横) = ' + str(img.shape[1]))
# print('(チャネル数) = ' + str(img.shape[2]))

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((N, height, width), dtype=np.uint8)

# 画像の読み込み
for i in range(0, N):
    img[frame] = cv2.imread('./hori/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
    frame += 1


mask = np.zeros((height, width), dtype='uint64')

for i in range(1, N):
    diff = cv2.absdiff(img[i - 1], img[i]) * 0.1
    diff = diff.astype(np.uint64)
    mask = mask + diff

mask[mask.max() * 0.2 < mask] = 255
mask[mask.max() * 0.2 >= mask] = 0

mask = mask.astype(np.uint8)

#mask = cv2.medianBlur(mask, ksize=1)

cv2.imwrite('sample.png', mask)