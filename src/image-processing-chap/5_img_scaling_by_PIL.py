# 画像処理編
# 5. PIL により、画像を拡大縮小するプログラム

import cv2
from PIL import Image

img = Image.open("../../data/Lenna.jpg").convert("L") # グレースケール化
# resample で補間方法を指定できる（デフォルトは Resampling.BICUBIC）
img.resize((500, 500)).save("../../data/image-processing-chap/ip_5.jpg")