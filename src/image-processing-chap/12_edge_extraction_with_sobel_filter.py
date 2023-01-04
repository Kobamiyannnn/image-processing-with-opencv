# 画像処理編
# 12. sobelフィルタによるエッジ抽出プログラム

import cv2
import numpy as np

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# ddepth: output image depth.
# dx: order of the derivative x.
# dy: order of the derivative y.
# ksize: size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
processed_x = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
processed_y = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

processed = np.hstack((processed_x, processed_y))
cv2.imwrite("../../data/image-processing-chap/ip_12.jpg", processed)