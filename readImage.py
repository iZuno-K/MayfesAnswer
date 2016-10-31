#-*-coding:utf-8-*-
# ↑はpython2系で日本語コメント書くときに必要

import numpy as np
import cv2

#画像の読み込み
#cv2.imread(画像のファイル名、白黒かどうか)
#今回は０なのでグレースケール画像
img = cv2.imread('test.jpg',0)
#cv2.imshow(表示するウィンドウ名, そこに表示したい画像)
cv2.imshow('image',img)
#キー入力があるまで待つ
cv2.waitKey(0)
#キー入力があったら↓
cv2.destroyAllwindows()
