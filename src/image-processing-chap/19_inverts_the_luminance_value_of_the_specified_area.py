# 画像処理編
# 19. カラー画像を読み込み，指定した領域の輝度値を反転させるプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# 処理領域を設定（left, top, right, bottom）
roi = (15, 70, 60, 130)
dst = img.copy()

# ROI領域をトリミングして，トリミングした画像を輝度値反転する
inverted = cv2.bitwise_not(img[roi[1]:roi[3], roi[0]:roi[2]])

# 元の座標に埋め込み
dst[roi[1]:roi[3], roi[0]:roi[2]] = inverted

cv2.imwrite("../../data/image-processing-chap/ip_19.jpg", dst)