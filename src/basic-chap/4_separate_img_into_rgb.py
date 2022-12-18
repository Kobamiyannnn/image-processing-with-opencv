# 基本編
# 4. カラー画像を読み込み，3チャネル（RGB）に分離し，入力画像と共に各チャネルの画像を表示するプログラム

import cv2
import numpy as np

img = cv2.imread("../../data/Lenna.jpg")

# 3チャネルに分離する
# 0: Blue, 1: Green, 2: Red
img_r = img.copy()
img_g = img.copy()
img_b = img.copy()
img_r[:, :, (0, 1)] = 0
img_g[:, :, (0, 2)] = 0
img_b[:, :, (1, 2)] = 0

cv2.imshow("img", np.vstack((np.hstack((img, img_r)), np.hstack((img_g, img_b)))))
cv2.waitKey(0)
cv2.destroyAllWindows()