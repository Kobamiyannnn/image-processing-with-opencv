# 基本編
# 1. カラー画像を読み込み，カラー表示するプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")
cv2.imshow("Lenna.jpg",img)
cv2.waitKey()