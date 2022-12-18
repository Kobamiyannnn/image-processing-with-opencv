# 画像処理編
# 8. アフィン変換により、画像を回転するプログラム

import cv2

# 左上を原点とした回転
def rotate(img, angle):
    height, width = img.shape[:2]
    affine = cv2.getRotationMatrix2D(center=(0, 0), angle=angle, scale=1.0)
    return cv2.warpAffine(img, affine, (height, width)), "ip_8-rotate.jpg"

# 画像の中心を原点とした回転
def rotate_center(img, angle):
    height, width = img.shape[:2]
    affine = cv2.getRotationMatrix2D(center=(height / 2, width / 2), angle=angle, scale=1.0)
    return cv2.warpAffine(img, affine, (height, width)), "ip_8-rotate_center.jpg"

if __name__ == "__main__":
    img = cv2.cvtColor(cv2.imread("../../data/Lenna.jpg"), cv2.COLOR_BGR2GRAY)
    processed = rotate_center(img, 60)
    cv2.imwrite(f"../../data/image-processing-chap/{processed[1]}", processed[0])