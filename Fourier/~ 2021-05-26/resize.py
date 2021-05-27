import cv2
from IPython.display import Image, display


def imshow(img):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    ret, encoded = cv2.imencode(".jpg", img)
    display(Image(encoded))


# 画像を読み込む。
img = cv2.imread("./hori/0.png")
# 指定した倍率でリサイズする。
# dst = cv2.resize(img, dsize=None, fx=0.3, fy=0.3)
dst = cv2.resize(img, dsize=(3280, 2464))
cv2.imwrite('sample.png', dst)

print(f"{img.shape} -> {dst.shape}")
# imshow(dst)
cv2.imshow('Window Name',dst)
cv2.waitKey(0) #キー入力待ちにして待機(0は無期限待機)
cv2.destroyAllWindows() #表示した画像表示ウィンドウを破棄