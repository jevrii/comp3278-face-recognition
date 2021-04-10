import sys
import smtplib
import email
from PyQt5 import QtCore, QtWidgets, QtGui
from Student_Information_GUI import Ui_Form
import datetime
import db_backend

class LessonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, course_name="", course_code="", venue="", type="", start_datetime="", end_datetime=""):
        # https://stackoverflow.com/questions/26199374/add-qwidget-to-qlistwidget
        
        QtWidgets.QWidget.__init__(self, parent=parent)

        label_course = QtWidgets.QLabel(f"{course_code}: {course_name} - {type}")
        label_course.setFixedHeight(20)
        label_venue = QtWidgets.QLabel(f"{venue}")
        label_venue.setFixedHeight(20)
        label_datetime = QtWidgets.QLabel(f"datetime 9/3/2020 15:30 - 16:20")
        label_datetime.setFixedHeight(20)

        widgetLayout = QtWidgets.QVBoxLayout()
        widgetLayout.addWidget(label_course)
        widgetLayout.addWidget(label_venue)
        widgetLayout.addWidget(label_datetime)

        self.setLayout(widgetLayout)

class InfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, student_id, timestamp):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.okay_info.clicked.connect(self.email)
        self.cancel_info.clicked.connect(self.close)

        self.fill_information(student_id, timestamp)
        self.email = None

    def email(self):
        sent_msg = email.message.EmailMessage()
        sent_msg.set_content()
        sent_msg['Subject'] = 'Lesson reminder'
        sent_msg['From'] = 'robocon@hku.hk'
        sent_msg['To'] = self.email
        smtp_server = smtplib.SMTP('mail.cs.hku.hk')
        smtp_server.send_message(sent_msg)
        smtp_server.quit()

    def fill_information(self, student_id, timestamp):
        _translate = QtCore.QCoreApplication.translate

        student_info = db_backend.GetStudentInfoAndCourse().get_info(student_id, timestamp)
        self.email = student_info['email']

        cur_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')

        if cur_time.hour < 4:
            welcome_msg = f"Good evening, {student_info['name']}!"
        elif cur_time.hour < 12:
            welcome_msg = f"Good morning, {student_info['name']}!"
        elif cur_time.hour < 18:
            welcome_msg = f"Good afternoon, {student_info['name']}!"
        else:
            welcome_msg = f"Good evening, {student_info['name']}!"

        self.label.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:18pt;\">{welcome_msg}</span></p></body></html>"))

        if len(student_info['lessons']):
            status1 = "You have lessons in 1 hour.\n"
            status2 = "Class material:\n"
            lesson_info = db_backend.GetLessonInfo().get_info(student_info['lessons'][0])
            text = str(lesson_info)
        else:
            status1 = "You do not have lessons in 1 hour.\n"
            status2 = "Your upcoming classes:\n"
            week_info = db_backend.GenerateTimetable().get_timetable(student_id, timestamp)

            for lesson in week_info:
                itemN = QtWidgets.QListWidgetItem()
                widget = LessonWidget(course_name=lesson["course_name"], course_code=lesson["course_name"],
                                      venue=lesson["venue"], type=lesson["type"],
                                      start_datetime=lesson["start_datetime"], end_datetime=lesson["start_datetime"])
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

        self.label_2.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status1}</span></p></body></html>"))
        self.label_3.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status2}</span></p></body></html>"))

        # self.message = text

if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    info_window = InfoWindow('177013', '2020-09-04 00:30')
    info_window.show()
    sys.exit(app.exec_())
