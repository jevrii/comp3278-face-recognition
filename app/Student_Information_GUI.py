# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Information_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 500)
        self.cancel_info = QtWidgets.QPushButton(Form)
        self.cancel_info.setGeometry(QtCore.QRect(500, 460, 75, 23))
        self.cancel_info.setObjectName("cancel_info")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 780, 420))
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.sendtoemail = QtWidgets.QCheckBox(Form)
        self.sendtoemail.setGeometry(QtCore.QRect(10, 435, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendtoemail.setFont(font)
        self.sendtoemail.setObjectName("sendtoemail")
        self.okay_info = QtWidgets.QPushButton(Form)
        self.okay_info.setGeometry(QtCore.QRect(225, 460, 75, 23))
        self.okay_info.setObjectName("okay_info")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Information"))
        self.cancel_info.setText(_translate("Form", "Cancel"))
        self.sendtoemail.setText(_translate("Form", "Send to Email"))
        self.okay_info.setText(_translate("Form", "Okay"))