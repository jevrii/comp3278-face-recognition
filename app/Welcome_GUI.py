# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QPoint, pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPainter, QImage, QTextCursor

# Image widget
class ImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        self.setMinimumSize(image.size())
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QPoint(0, 0), self.image)
        qp.end()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.OkayButton_Welcome = QtWidgets.QPushButton(Form)
        self.OkayButton_Welcome.setGeometry(QtCore.QRect(600, 370, 181, 50))
        self.OkayButton_Welcome.setObjectName("OkayButton_Welcome")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 611, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.OkayButton_Welcome_2 = QtWidgets.QPushButton(Form)
        self.OkayButton_Welcome_2.setGeometry(QtCore.QRect(600, 430, 181, 50))
        self.OkayButton_Welcome_2.setObjectName("OkayButton_Welcome_2")
        self.camera_display = ImageWidget(Form)
        self.camera_display.setGeometry(QtCore.QRect(20, 140, 411, 281))
        self.camera_display.setObjectName("camera_display")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(590, 180, 191, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 260, 141, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(610, 270, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome"))
        self.OkayButton_Welcome.setText(_translate("Form", "Continue (facial recognition)"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Welcome!</span></p><p><span style=\" font-size:16pt;\">Please scan your face, or enter your student ID</span></p></body></html>"))
        self.OkayButton_Welcome_2.setText(_translate("Form", "Continue (manual input)"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">No valid face detected.</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Manual SID input:</span></p></body></html>"))
