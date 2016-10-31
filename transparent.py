#-*- coding: utf-8 -*-
import cv2
import numpy as np
# 白い物を透過させよう

if __name__=="__main__":

    cap = cv2.VideoCapture(0)
    thresh = 170 #閾値
    flag = False
    while True:
        ret,frame = cap.read()
        key = cv2.waitKey(10)

        if key == ord(" "):
            background = frame		#画像の保存
            flag = True
        

        if flag:
            img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            frame[img_gray > thresh] = background[img_gray > thresh]

        cv2.imshow("Toumei",frame)

        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
