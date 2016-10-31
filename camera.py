#-*-coding: UTF-8-*-
import numpy as np
import cv2

#0番目のカメラデバイスを使うという宣言
cap = cv2.VideoCapture(0)

#無限ループ
while(True):
    # カメラから画像をframeに読み込む
    # retは使いませんが出力を二つ受けなければならないので書きましょう
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    # 1000msキー入力を受け付ける。qが押されたらbreak
    if cv2.waitKey(1000) == ord('q'):
    	break

#カメラデバイス解放(必ず行う)
cap.release()
cv2.destroyAllWindows()
