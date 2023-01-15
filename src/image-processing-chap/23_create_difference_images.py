# 画像処理編
# 23. 指定した2枚のカラー画像を読み込み，差分画像を作成するプログラム（類似画像を利用）

import cv2

img1 = cv2.imread("../../data/diff1.jpg")
img2 = cv2.imread("../../data/diff2.jpg")

diff = cv2.absdiff(img1, img2)

cv2.imwrite("../../data/image-processing-chap/ip_23.jpg", diff)