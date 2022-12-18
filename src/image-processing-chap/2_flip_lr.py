# 画像処理編
# 2. 画像を左右反転するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

cv2.imwrite("../../data/image-processing-chap/ip_2.jpg", cv2.flip(img, 1)) # flipCode > 0 で左右反転