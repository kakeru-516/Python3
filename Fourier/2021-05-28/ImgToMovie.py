import sys
import cv2

# encoder(for mp4)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# output file name, encoder, fps, size(fit to image size)
N = int(input('読み込む画像数 : '))
start = int(input('開始データ番号 : '))
end = start + N
video = cv2.VideoWriter(str(start) + '-' + str(end) + '.mp4',fourcc, 30.0, (720, 480))

if not video.isOpened():
    print("can't be opened")
    sys.exit()

for i in range(start, end):
    # hoge0000.png, hoge0001.png,..., hoge0090.png
    img = cv2.imread('./img/%d.png' % i)
    print('読み込んだファイル名 : ' + str(i) + '.png')

    # can't read image, escape
    if img is None:
        print("can't read")
        break

    # add
    video.write(img)

video.release()
print('written')