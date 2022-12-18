# 画像処理編
# 4. cv2.resize により，画像を拡大縮小するプログラム
# （最近傍補間・バイリニア補間・平均画素法など）

import cv2

img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)

# ここでは画像を縦横2倍に拡大する
# cv2.resize の interpolation を変更することで補間方法を選択できる
"""
< interpolation の種類 >
- INTER_NEAREST : 最近傍補間
- INTER_LINEAR  : バイリニア補間
- INTER_CUBIC   : バイキュービック補間
- INTER_AREA    : 平均画素法
- INTER_LANCZOS4: Lanczos法での補間
"""
nearest_neighbor = cv2.resize(img, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)