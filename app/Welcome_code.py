import sys
from PyQt5 import QtCore, QtWidgets
from Welcome_GUI import Ui_Form
from Student_Information_code import InfoWindow
from Teacher_Information_code import LogInfoWindow

# USB camera display using PyQt and OpenCV, from iosoft.blog
# Copyright (c) Jeremy P Bentham 2019
# Please credit iosoft.blog if you use the information or software in it

import sys, time, threading, cv2
from PyQt5.QtCore import QTimer, QPoint, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPainter, QImage, QTextCursor
import queue as Queue

from cv_backend import FaceRecognition
import time, datetime
import os, yaml

IMG_SIZE    = 640,480          # 640,480 or 1280,720 or 1920,1080
IMG_FORMAT  = QImage.Format_RGB888
DISP_SCALE  = 2                # Scaling factor for display image
DISP_MSEC   = 50                # Delay between display cycles
CAP_API     = cv2.CAP_ANY       # API: CAP_ANY or CAP_DSHOW etc...
EXPOSURE    = 0                 # Zero for automatic exposure

camera_num  = 1                 # Default camera (first in list)
image_queue = Queue.Queue()     # Queue to hold images
capturing   = True              # Flag to indicate capturing

folder = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(folder+'/config.yaml', 'r'), Loader=yaml.FullLoader)

# Grab images from the camera (separate thread)
def grab_images(cam_num, queue):
    cap = cv2.VideoCapture(cam_num-1 + CAP_API)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, IMG_SIZE[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, IMG_SIZE[1])
    if EXPOSURE:
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
        cap.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE)
    else:
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
    while capturing:
        if cap.grab():
            retval, image = cap.retrieve(0)
            if image is not None and queue.qsize() < 2:
                queue.put(image)
            else:
                time.sleep(DISP_MSEC / 1000.0)
        else:
            print("Error: can't grab camera image")
            break
        # welcome_window.show_image(image_queue, welcome_window.camera_display, DISP_SCALE)
    cap.release()


class WelcomeWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.OkayButton_Welcome.clicked.connect(self.face_login)
        self.OkayButton_Welcome_2.clicked.connect(self.text_login)
        self.OkayButton_Welcome_3.clicked.connect(self.check_log)
        self._new_window = None
        self.f = FaceRecognition(confidence=config['face_recognition_confidence'])
        self.id_detected = None
        self.last_face_time = 0.0
    def face_login(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.label_4.setText(_translate("Form", "<html><head/><body><p></p></body></html>"))
            self._new_window = InfoWindow(self.id_detected, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self._new_window.show()
        except IndexError:
            self.label_4.setText(_translate("Form", "<html><head/><body><p style=\"color:red\">Error: User not found</p></body></html>"))
    def text_login(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.label_4.setText(_translate("Form", "<html><head/><body><p></p></body></html>"))
            self._new_window = InfoWindow(self.lineEdit.text(), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self._new_window.show()
        except IndexError:
            self.label_4.setText(_translate("Form", "<html><head/><body><p style=\"color:red\">Error: User not found</p></body></html>"))

    def check_log(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.label_5.setText(_translate("Form", "<html><head/><body><p></p></body></html>"))
            self._new_window = LogInfoWindow(self.lineEdit_2.text())
            self._new_window.show()
        except IndexError:
            self.label_5.setText(_translate("Form", "<html><head/><body><p style=\"color:red\">Error: Course not found</p></body></html>"))
        
    # Start image capture & display
    def start(self):
        self.timer = QTimer(self)           # Timer to trigger display
        self.timer.timeout.connect(lambda: 
                    self.show_image(image_queue, self.camera_display, DISP_SCALE))
        self.timer.start(DISP_MSEC)
        self.capture_thread = threading.Thread(target=grab_images, 
                    args=(camera_num, image_queue))
        self.capture_thread.start()         # Thread to grab images

    # Fetch camera image from queue, and display it
    def show_image(self, imageq, display, scale):
        if not imageq.empty():
            image = imageq.get()
            if image is not None and len(image) > 0:
                try:
                    temp = self.f.get_id(image)
                    _translate = QCoreApplication.translate
                    if temp is None:
                        if time.time() - self.last_face_time > 5: # timeout
                            self.id_detected = None
                            self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">No valid face detected.</span></p></body></html>"))
                    else:
                        self.id_detected = temp
                        self.last_face_time = time.time()
                        self.label_2.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:10pt;\">Hello, {self.id_detected}</span></p></body></html>"))
                except:
                    print("Error occurred with face recognition")
                
                img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.display_image(img, display, scale)

    # Display an image, reduce size if required
    def display_image(self, img, display, scale=1):
        disp_size = img.shape[1]//scale, img.shape[0]//scale
        disp_bpl = disp_size[0] * 3
        if scale > 1:
            img = cv2.resize(img, disp_size, 
                             interpolation=cv2.INTER_CUBIC)
        qimg = QImage(img.data, disp_size[0], disp_size[1], 
                      disp_bpl, IMG_FORMAT)
        display.setImage(qimg)
    
    # Window is closing: stop video capture
    def closeEvent(self, event):
        global capturing
        capturing = False
        self.capture_thread.join()

if __name__ == '__main__':
    camera_num = 1
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    welcome_window = WelcomeWindow()
    welcome_window.show()
    welcome_window.start()
    sys.exit(app.exec_())
