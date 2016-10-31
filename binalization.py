#-*-coding: utf-8-*-

import cv2
import numpy as np

if __name__=="__main__":
    # グレースケールで読み込み
    img = cv2.imread("test.jpg",0)

    # 閾値を100に
    thresh = 100
    #閾値を超えた部分は255に、その他は0に
    ret, img_dst = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)

    #表示
    cv2.imshow("Show BINARIZATION Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
