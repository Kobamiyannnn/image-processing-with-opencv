# 画像処理編
# 11. ガウシアンフィルタにより、平滑化するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# sigmaX, sigmaY の両方が0だと ksizeから計算される
# sigmaX: Gaussian kernel standard deviation in X direction.
# sigmaY: Gaussian kernel standard deviation in Y direction.
blur = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=0, sigmaY=0)
cv2.imwrite("../../data/image-processing-chap/ip_11.jpg", blur)