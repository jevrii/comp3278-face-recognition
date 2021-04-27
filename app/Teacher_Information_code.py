import sys
import smtplib
import email
from PyQt5 import QtCore, QtWidgets, QtGui
from Teacher_Information_GUI import Ui_Form
import datetime
import db_backend
import uuid
import os
import yaml


folder = os.path.dirname(os.path.abspath(__file__))
config = yaml.load(open(folder+'/config.yaml', 'r'), Loader=yaml.FullLoader)

class CheckWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, student_name="",student_id="",last_heartbeat=""):
        # https://stackoverflow.com/questions/26199374/add-qwidget-to-qlistwidget
        
        QtWidgets.QWidget.__init__(self, parent=parent)
        label_student_name = QtWidgets.QLabel(f"Student Name: {student_name}")
        label_student_name.setFixedHeight(20)
        label_student_id = QtWidgets.QLabel(f"Student ID: {student_id}")
        label_student_id.setFixedHeight(20)
        label_last_heartbeat = QtWidgets.QLabel(f"Last Login: {last_heartbeat}")
        label_last_heartbeat.setFixedHeight(20)
        widgetLayout = QtWidgets.QVBoxLayout()
        widgetLayout.addWidget(label_student_name)
        widgetLayout.addWidget(label_student_id)
        widgetLayout.addWidget(label_last_heartbeat)

        widgetLayout.addStretch()
        self.setLayout(widgetLayout)

class LogInfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, course_code):
        super(LogInfoWindow, self).__init__()
        self.msg_html = "<html><body>"
        self.setupUi(self)
        # self.okay_info.clicked.connect(self.send_email)
        self.cancel_info.clicked.connect(self.close)

        self.fill_information(course_code)
        self.session_id = str(uuid.uuid4())

    def fill_information(self, course_code):
        _translate = QtCore.QCoreApplication.translate

        student_info = db_backend.GetStudentLog().get_info(course_code)

        welcome_msg = "Check Login Time for students"
        self.msg_html += "<p>" + welcome_msg + "</p>"
        status1 = f"You are checking for - {course_code}"
        status2= ""
        status3=""
        self.msg_html += "<p>" + status1 + "</p>"

        self.label.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:18pt;\">{welcome_msg}</span></p></body></html>"))

        for stu_info in student_info:
            itemN = QtWidgets.QListWidgetItem()
            widget = CheckWidget(student_name=stu_info['name'],student_id=stu_info['student_id'],last_heartbeat=stu_info['MAX(LS.last_heartbeat)'])

            name_of_student = stu_info['name']
            id_of_student = stu_info['student_id']
            stu_last_heartbeat = stu_info['MAX(LS.last_heartbeat)']

            name1 = "Student Name"
            itemN.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(itemN)
            self.listWidget.setItemWidget(itemN, widget)   
            self.msg_html += f'<tr><td>"Name"{name_of_student}</td><td>{id_of_student}</td><td>{stu_last_heartbeat}</td></tr>'

        self.msg_html += "</body>"
        self.msg_html += "</html>"
        self.label_2.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status1}</span></p></body></html>"))
        self.label_3.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status2}</span></p></body></html>"))
        self.label_4.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status3}</span></p></body></html>"))
if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    info_window = LogInfoWindow('COMP2119_2C')
    info_window.show()
    sys.exit(app.exec_())
