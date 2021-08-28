import cv2
import numpy as np
import HandTrackingModule as htm
import win32api



cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,400)
detector = htm.DhiaHandTracking(maxHands=1)
counter = 0
while True:
    success, frame = cap.read()
    frame = detector.process_hands(frame)
    lmList = detector.get_positions(frame)
    if len(lmList) > 0:
        x, y = lmList[8][1], lmList[8][2]
        cv2.circle(frame, (x,y), 10, (255,0,255), cv2.FILLED)    
        posxn = np.interp(x, [50,550], [0,1365])
        posx = 1365 - posxn
        posy = np.interp(y, [50,350], [0,767])
        win32api.SetCursorPos((int(posx),int(posy)))
    cv2.imshow("Mouse Controller -Dhia-", frame)
    c = cv2.waitKey(1)
    if c == 27 : break