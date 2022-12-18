# 基本編
# 5. カラー画像を読み込み，RGB成分を数式
# Y = 0.2126R + 0.7152G + 0.0722B
# に従い変換し，グレースケール化した画像を別名で保存するプログラム

import cv2

def bgr2gray(blue, green, red):
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue

img = cv2.imread("../../data/Lenna.jpg")

for height in range(img.shape[0]):
    for width in range(img.shape[1]):
        img[height, width, :] = bgr2gray(img[height, width, 0], img[height, width, 1], img[height, width, 2])

cv2.imwrite("../../data/basic_5.jpg", img)