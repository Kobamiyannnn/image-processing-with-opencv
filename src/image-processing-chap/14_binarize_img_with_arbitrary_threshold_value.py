# 画像処理編
# 14. 画像を任意の閾値で二値化するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

th_val, bin_img = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

cv2.imwrite("../../data/image-processing-chap/ip_14.jpg", bin_img)