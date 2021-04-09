import sys
import smtplib
import email
from PyQt5 import QtCore, QtWidgets
from Student_Information_GUI import Ui_Form
import datetime
import db_backend

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
        student_info = db_backend.GetStudentInfoAndCourse().get_info(student_id, timestamp)
        self.email = student_info['email']

        text = ""

        cur_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M')

        if cur_time.hour < 4:
            welcome_msg = f"Good evening, {student_info['name']}!"
        elif cur_time.hour < 12:
            welcome_msg = f"Good morning, {student_info['name']}!"
        elif cur_time.hour < 18:
            welcome_msg = f"Good afternoon, {student_info['name']}!"
        else:
            welcome_msg = f"Good evening, {student_info['name']}!"

        text += welcome_msg + "\n"

        if len(student_info['lessons']):
            text += "You have lessons in 1 hour:\n"
            lesson_info = db_backend.GetLessonInfo().get_info(student_info['lessons'][0])
            text += str(lesson_info)
        else:
            text += "You do not have lessons in 1 hour:\n"
            text += "Your timetable for this week:\n"
            week_info = db_backend.GenerateTimetable().get_timetable(student_id)
            text += str(week_info)

        self.message = text

        self.textBrowser.setText(text)

if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    info_window = InfoWindow('177013', '2020-09-04 15:30')
    info_window.show()
    sys.exit(app.exec_())
