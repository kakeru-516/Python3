import cv2
import numpy as np
import sys

N = int(input('サンプル数 : ')) # サンプル数
start = int(input('開始データ番号 : '))
end = start + N
print('終了データ番号 : ' + str(end))

img = cv2.imread('./img/0.png', cv2.IMREAD_COLOR)
# print('y(縦) = ' + str(img.shape[0]))
# print('x(横) = ' + str(img.shape[1]))
# print('(チャネル数) = ' + str(img.shape[2]))

height = img.shape[0]
width = img.shape[1]
frame = 0

img = np.zeros((N, height, width), dtype=np.uint8)

# 画像の読み込み
for i in range(start, end):
    img[frame] = cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE)
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
threshold = int(mask.max() * 0.2)
ret, mask = cv2.threshold(mask, threshold, 255, cv2.THRESH_BINARY)

mask = cv2.medianBlur(mask, ksize=13)
cv2.imwrite(str(start) + '-' + str(end) + '.png', mask)
