# 基本編
# 4. カラー画像を読み込み，3チャネル（RGB）に分離し，入力画像と共に各チャネルの画像を表示するプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")

# 3チャネルに分離する
# 0: Blue, 1: Green, 2: Red
img_r = img_g = img_b = img.copy()
img_r[:, :, 0] = img_r[:, :, 1] = 0
img_g[:, :, 0] = img_g[:, :, 2] = 0
img_b[:, :, 1] = img_b[:, :, 2] = 0