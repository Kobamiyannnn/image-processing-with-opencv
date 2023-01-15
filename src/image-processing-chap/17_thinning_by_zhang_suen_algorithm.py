# 画像処理編
# 17. Zhang Suenのアルゴリズムにより、二値画像を細線化するプログラム

# https://github.com/linbojin/Skeletonization-by-Zhang-Suen-Thinning-Algorithm
# https://qiita.com/hrs1985/items/7751d4b5241d5c314a6d

# https://emotionexplorer.blog.fc2.com/blog-entry-200.html

import cv2 # opencv-contrib-python
import numpy as np


def unpadding(image):
    """
    画像の外周1ピクセルを取り除く
    """
    return image[1:-1, 1:-1]


def neighbours(x, y, image):
    """
    画素P1(x, y)の近傍8個を時計回りに返す \n
    P9 P2 P3 \n
    P8 P1 P4 \n
    P7 P6 P5
    """
    return [image[x - 1][y], image[x - 1][y + 1], # P2, P3
            image[x][y + 1], image[x + 1][y + 1], # P4, P5
            image[x + 1][y], image[x + 1][y - 1], # P6, P7
            image[x][y - 1], image[x - 1][y - 1]] # P8, P9


def transitions(neighbours):
    """
    0 -> 1の変化の回数を数える \n
    P9 P2 P3 \n
    P8 P1 P4 \n
    P7 P6 P5
    """
    n = neighbours + neighbours[0:1]
    # (P2, P3), (P3, P4), ..., (P8, P9), (P9, P2)
    return sum((n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]))


def zhang_suen_thinning(binary_image):
    """
    Zhang-Suenの細線化アルゴリズム
    """
    # 白（輝度値255）を0、黒（輝度値0）を1に変換する
    binary_image = (~binary_image.astype(bool)).astype(int)
    # 画像中の画素が必ず8個の近傍を持つために、1ピクセル分ゼロパディング
    binary_image = np.pad(binary_image, 1)

    image_thinned = binary_image.copy() # deepcopy
    changing1 = changing2 = 1 # 初期化

    # 画像に変化が生じなくなるまで繰り返し
    while changing1 or changing1:
        """
        ステップ1:

        ステップ1は、全ての画素を検証し、以下の条件を同時に満たす画素をメモする

        1. P1が1で、8個の近傍を持つ
        2. 2 <= N(P1) (非ゼロのP1の近傍の数を数える関数) <= 6 
        3. S(P1) (P2から時計回りに見たときの、0 -> 1の遷移の数を数える関数) = 1
        4. P2 * P4 * P6 = 0
        5. P4 * P6 * P8 = 0

        画像上で繰り返し処理を行い、前述の条件を同時に満たす画素をメモした後、
        それらの画素を全て0に設定する
        """
        changing1 = []
        rows, columns = image_thinned.shape
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = neighbours(x, y, image_thinned)
                if (image_thinned[x][y] == 1    # 条件1
                        and 2 <= sum(n) <= 6    # 条件2
                        and transitions(n) == 1 # 条件3
                        and P2 * P4 * P6 == 0   # 条件4
                        and P4 * P6 * P8 == 0): # 条件5
                    changing1.append((x, y))

        for x, y in changing1:
            image_thinned[x][y] = 0

        """
        ステップ2:

        ステップ2は、全ての画素を検証し、以下の条件を同時に満たす画素をメモする

        1. P1が1で、8個の近傍を持つ
        2. 2 <= N(P1) (非ゼロのP1の近傍の数を数える関数) <= 6
        3. S(P1) (P2から時計回りに見たときの、0 -> 1の遷移の数を数える関数) = 1
        4. P2 * P4 * P8 = 0
        5. P2 * P6 * P8 = 0

        画像上で繰り返し処理を行い、前述の条件を同時に満たす画素をメモした後、
        それらの画素を全て0に設定する
        """
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = n = neighbours(x, y, image_thinned)
                if (image_thinned[x][y] == 1    # 条件1
                        and 2 <= sum(n) <= 6    # 条件2
                        and transitions(n) == 1 # 条件3
                        and P2 * P4 * P8 == 0   # 条件4
                        and P2 * P6 * P8 == 0): # 条件5
                    changing2.append((x, y))

        for x, y in changing2:
            image_thinned[x][y] = 0

    image_thinned = unpadding(image_thinned)
    # 白を255、黒を0とする二値画像に戻す
    image_thinned = (~image_thinned.astype(bool)).astype(int) * 255
    
    return image_thinned


if __name__ == "__main__":
    img = cv2.cvtColor(cv2.imread("../../data/kanji.png"), cv2.COLOR_BGR2GRAY)
    
    # ノイズの影響を軽減するために，ガウシアンフィルタで平滑化
    blur = cv2.GaussianBlur(img, (5, 5), 3)

    # グレースケール画像の二値化（大津の方法）
    # THRESH_OTSUは自動で閾値を決めるだけ，他のフラグと組み合わせる必要あり
    # https://pystyle.info/opencv-image-binarization/
    th_val, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 細線化アルゴリズムの適用
    # image_thinned = zhang_suen_thinning(bin_img)
    image_thinned = cv2.threshold(cv2.ximgproc.thinning(bin_img, cv2.ximgproc.THINNING_ZHANGSUEN), 0, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite("../../data/image-processing-chap/ip_17.jpg", image_thinned)