# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Information_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.cancel_info = QtWidgets.QPushButton(Form)
        self.cancel_info.setGeometry(QtCore.QRect(500, 460, 75, 23))
        self.cancel_info.setObjectName("cancel_info")
        self.okay_info = QtWidgets.QPushButton(Form)
        self.okay_info.setGeometry(QtCore.QRect(225, 460, 131, 23))
        self.okay_info.setObjectName("okay_info")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 711, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 711, 51))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 180, 751, 251))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 711, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 711, 51))
        self.label_4.setObjectName("label_4")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Information"))
        self.cancel_info.setText(_translate("Form", "Exit"))
        self.okay_info.setText(_translate("Form", "Send to my email"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Good morning!</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">You do not have lessons in 1 hour.</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Upcoming classses:</span></p></body></html>"))
