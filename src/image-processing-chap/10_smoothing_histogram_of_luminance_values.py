# 画像処理編
# 10. 輝度値（ピクセル値）のヒストグラムを平滑化（平準化）した画像を作成するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

smoothed_img = cv2.blur(src=img, ksize=(3, 3))
cv2.imwrite("../../data/image-processing-chap/ip_10.jpg", smoothed_img)