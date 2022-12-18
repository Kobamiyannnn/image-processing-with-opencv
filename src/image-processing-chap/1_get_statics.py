# 画像処理編
# 1. 画像の最大値，最小値，平均値を求めるプログラム

import cv2

img = cv2.imread("../../data/Lenna.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img)
print(f"最大値: {max_val} (座標: {max_loc})")
print(f"最小値: {min_val}  (座標: {min_loc})")
print(f"平均値: {img.mean()}")