# 画像処理編
# 21. カラー画像を読み込み，3×3の領域で平均プーリングするプログラム

import cv2
import numpy as np

def ave_pooling(img, k: int):
    """
    平均プーリング
    `img`: 入力画像
    `k`: カーネルサイズ
    """
    dst = img.copy()

    w,h,c = img.shape
    # 中心画素から両端画素までの長さ
    size = k // 2

    for x in range(size, w, k):
        for y in range(size, h, k):
            dst[x-size:x+size, y-size:y+size, 0] = np.mean(img[x-size:x+size, y-size:y+size, 0])
            dst[x-size:x+size, y-size:y+size, 1] = np.mean(img[x-size:x+size, y-size:y+size, 1])
            dst[x-size:x+size, y-size:y+size, 2] = np.mean(img[x-size:x+size, y-size:y+size, 2])

    return dst

if __name__ == "__main__":
    img = cv2.imread("../../data/Lenna.jpg")
    img = ave_pooling(img, 9)
    cv2.imwrite("../../data/image-processing-chap/ip_21.jpg", img)

