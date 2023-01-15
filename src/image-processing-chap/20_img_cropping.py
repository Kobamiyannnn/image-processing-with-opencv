# 画像処理編
# 20. カラー画像を読み込み，指定した領域でトリミングするプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")
cv2.imwrite("../../data/image-processing-chap/ip_20.jpg", img[15:70, 60:130])