#-*- coding: utf-8 -*-
#背景は黒に、他は普通に表示したい
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#キー入力の前後で動作を変える用
flag=0


while True:
    #キーボード入力受付用
    key = cv2.waitKey(10)
    ret,frame = cap.read()

    if key == ord('a'):
        # aを押したときの画像をグレースケールで保持
        background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flag=1
    if flag:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 保持した画像との差分を計算
        frame[(gray_frame - background) < 50] = 0

    cv2.imshow('frame',frame)

    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
