# 画像処理編
# 7. アフィン変換により、画像を平行移動するプログラム

import cv2
import numpy as np

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

height, width = img.shape[:2]

shift = 10 # 平行移動する分のピクセル値

# アフィン変換を計算
src = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0]], np.float32)
dst = src.copy()
dst[:, 0] += shift # x方向に shift だけ平行移動してみる
affine = cv2.getAffineTransform(src, dst)

# アフィン変換を画像に適用
processed = cv2.warpAffine(img, affine, (height, width))

cv2.imwrite("../../data/image-processing-chap/ip_7.jpg", processed)