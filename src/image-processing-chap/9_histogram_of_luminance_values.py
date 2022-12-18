# 画像処理編
# 9. 輝度値（ピクセル値）のヒストグラムを作成するプログラム

import cv2
import matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# channels: グレースケールであるので0
histogram = cv2.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

plt.plot(histogram)
plt.savefig("../../data/image-processing-chap/ip_9.jpg")