# 画像処理編
# 18. 二値画像の輪郭線を抽出するプログラム

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (5, 5), 0)
th_val, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 輪郭線抽出
contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 小さい輪郭は誤検出として削除
contours = list(filter(lambda x: cv2.contourArea(x) > 100, contours))
# 輪郭の描画
cv2.drawContours(img, contours, -1, color=(0, 0, 0), thickness=2)

cv2.imwrite("../../data/image-processing-chap/ip_18.jpg", img)