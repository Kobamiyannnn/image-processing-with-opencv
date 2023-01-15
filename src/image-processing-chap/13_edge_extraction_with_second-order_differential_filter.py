# 画像処理編
# 13. 二次微分フィルタによるエッジ抽出プログラム

import cv2
import numpy as np

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# カーネル（エッジ抽出用）
kernel = np.array([[0, -2, 0],
                   [-2, 8, -2],
                   [0, -2, 0]])

processed = cv2.filter2D(img, cv2.CV_64F, kernel=kernel)
cv2.imwrite("../../data/image-processing-chap/ip_13.jpg", processed)