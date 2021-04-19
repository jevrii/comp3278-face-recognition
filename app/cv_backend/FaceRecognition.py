import urllib
import numpy as np
import cv2
import pyttsx3
import pickle
from datetime import datetime
import sys
import os

class FaceRecognition:
    def __init__(self, confidence):
        folder = os.path.dirname(os.path.abspath(__file__))
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(f"{folder}/train.yml")

        self.labels = {"person_name": 1}
        with open(f"{folder}/labels.pickle", "rb") as f:
            self.labels = pickle.load(f)
            self.labels = {v: k for k, v in self.labels.items()}
        
        self.confidence = confidence
        self.face_cascade = cv2.CascadeClassifier(f'{folder}/haarcascade_frontalface_default.xml')

    def get_id(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            # print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = self.recognizer.predict(roi_gray)

            color = (255, 0, 0)
            stroke = 2
            font = cv2.QT_FONT_NORMAL
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

            # If the face is recognized
            if conf >= self.confidence:
                # print(id_)
                # print(labels[id_])
                font = cv2.QT_FONT_NORMAL
                name = self.labels[id_]
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

                return name

            # If the face is unrecognized
            else: 
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                # color = (255, 0, 0)
                # stroke = 2
                # font = cv2.QT_FONT_NORMAL
                # cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                return None
