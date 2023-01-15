# 画像処理編
# 22. カラー画像を読み込み，3×3の領域で最大値プーリングするプログラム

import cv2
import numpy as np

def max_pooling(img, k: int):
    """
    最大値プーリング
    `img`: 入力画像
    `k`: カーネルの一辺
    """
    dst = img.copy()

    w,h,c = img.shape
    size = k

    for x in range(size, w, k):
        for y in range(size, h, k):
            dst[x-size:x+size, y-size:y+size, 0] = np.max(img[x-size:x+size, y-size:y+size, 0])
            dst[x-size:x+size, y-size:y+size, 1] = np.max(img[x-size:x+size, y-size:y+size, 1])
            dst[x-size:x+size, y-size:y+size, 2] = np.max(img[x-size:x+size, y-size:y+size, 2])

    return dst

if __name__ == "__main__":
    img = cv2.imread("../../data/Lenna.jpg")
    img = max_pooling(img, 3)
    cv2.imwrite("../../data/image-processing-chap/ip_22.jpg", img)

