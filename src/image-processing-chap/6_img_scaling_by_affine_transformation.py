# 画像処理編
# 6. アフィン変換により、画像を拡大縮小するプログラム

import cv2
import numpy as np

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

height, width = img.shape[:2]
ratio = 2.0 # 画像を2倍に拡大する

# アフィン変換を計算
# src: Coordinates of triangle vertices in the source image.
# dst: Coordinates of the corresponding triangle verices in the destination image.
src = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0]], np.float32)
affine = cv2.getAffineTransform(src = src, dst = src * ratio)

# アフィン変換を画像に適用
# dsize: size of the output image.
# flags で補間方法を指定できる
resized_img = cv2.warpAffine(src = img, M = affine, dsize = (int(ratio) * height, int(ratio) * width), flags = cv2.INTER_LANCZOS4)

cv2.imwrite("../../data/image-processing-chap/ip_6.jpg", resized_img)
