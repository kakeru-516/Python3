from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2

# 画像の読み込み
img = np.array([cv2.imread('./img/' + str(i) + '.png', cv2.IMREAD_GRAYSCALE) for i in range(32)])
img = img.transpose(1,2,0)

# 時間方向に差分を取る
diff = np.zeros((480, 720), dtype=np.uint64)
img = img.astype(np.uint64)
a = 8
a = a.astype(np.uint8)
diff = np.diff(img, n=1, axis=2)
print(diff.max())


# 画像の出力
#[cv2.imwrite('./output/' + str(i) + '.png', img[:, :, i]) for i in range(32)]