# 画像処理編
# 21. カラー画像を読み込み，3×3の領域で平均プーリングするプログラム

import cv2
import numpy as np
import math

def ave_pooling(img, k: int):
    """
    平均プーリング
    `img`: 入力画像
    `k`: カーネルの一辺
    """
    dst = img.copy()

    w,h,c = img.shape
    size = k

    for x in range(size, w, k):
        for y in range(size, h, k):
            dst[x-size:x+size, y-size:y+size, 0] = np.mean(img[x-size:x+size, y-size:y+size, 0])
            dst[x-size:x+size, y-size:y+size, 1] = np.mean(img[x-size:x+size, y-size:y+size, 1])
            dst[x-size:x+size, y-size:y+size, 2] = np.mean(img[x-size:x+size, y-size:y+size, 2])

    return dst

if __name__ == "__main__":
    img = cv2.imread("../../data/Lenna.jpg")
    img = ave_pooling(img, 3)
    cv2.imwrite("../../data/image-processing-chap/ip_21.jpg", img)

