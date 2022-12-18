# 画像処理編
# 3. 画像を上下反転するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

cv2.imwrite("../../data/image-processing-chap/ip_3.jpg", cv2.flip(img, 0)) # flipCode = 0 で上下反転