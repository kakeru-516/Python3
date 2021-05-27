#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

#画像の読み込み
im = Image.open(sys.argv[1])

#画像をarrayに変換
im_list = np.asarray(im)
#貼り付け
plt.imshow(im_list)
#表示
plt.show()