# 基本編
# 2. カラー画像を読み込み，グレースケール表示するプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
