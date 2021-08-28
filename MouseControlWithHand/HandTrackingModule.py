import cv2
import mediapipe as mp

class DhiaHandTracking():
    def __init__(self, mode=False, maxHands=2, minDetectingConfidence=0.7,
                                               minTrackingConfidence=0.7):
        self.mode = mode
        self.handsNo = maxHands
        self.detectingCon = minDetectingConfidence
        self.trackingCon = minTrackingConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.handsNo,
                                        self.detectingCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils

    def process_hands(self, frame, draw=False):
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB, )
        self.result = self.hands.process(frameRGB)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)
        return frame
        #a function that returns the id(place number) and the x, y positions of the landmark
    def get_positions(self, frame, handN=0, draw=False):
        #a list that have the id, x, y information of a landmark to return it
        lmList = []
        #if a hand is on the screen 
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handN]
            #the x, y posotions loop
            for id,lm in enumerate(myHand.landmark):
                #height, width, contour of the screen
                h, w, c = frame.shape
                #turning the x, y values to a pixel position on the screen
                cx, cy = int(lm.x*w), int(lm.y*h)
                #adding the id, pixel positions to the list 
                lmList.append([id, cx, cy])
                if draw:
                    #drawing a circle around the landmarks
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        #returning the id, x, y informations list
        return lmList                                       
#the end of the Hand Tracking Class