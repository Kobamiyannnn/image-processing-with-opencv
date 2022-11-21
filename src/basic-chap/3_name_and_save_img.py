# 基本編
# 3. カラー画像を読み込み，グレースケール化した画像を別名で保存するプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("../../data/basic_3.jpg", gray_img)