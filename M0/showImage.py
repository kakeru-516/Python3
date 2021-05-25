#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#画像の読み込み
im = Image.open("6.0[m]-1-1.jpg")

#画像をarrayに変換
im_list = np.asarray(im)
#貼り付け
plt.imshow(im_list)
#表示
plt.show()