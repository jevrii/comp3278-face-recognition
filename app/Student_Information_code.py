import sys
import smtplib
import email
from PyQt5 import QtCore, QtWidgets, QtGui
from Student_Information_GUI import Ui_Form
import datetime
import db_backend
import uuid

class LessonWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, course_name="", course_code="", venue="", type="", start_datetime="", end_datetime=""):
        # https://stackoverflow.com/questions/26199374/add-qwidget-to-qlistwidget
        
        QtWidgets.QWidget.__init__(self, parent=parent)

        label_course = QtWidgets.QLabel(f"{course_code}: {course_name} - {type}")
        label_course.setFixedHeight(20)
        label_venue = QtWidgets.QLabel(f"{venue}")
        label_venue.setFixedHeight(20)
        label_datetime = QtWidgets.QLabel(f"{start_datetime.day}/{start_datetime.month}/{start_datetime.year} {start_datetime.hour}:{start_datetime.minute} - {end_datetime.hour}:{end_datetime.minute}")
        label_datetime.setFixedHeight(20)

        widgetLayout = QtWidgets.QVBoxLayout()
        widgetLayout.addWidget(label_course)
        widgetLayout.addWidget(label_venue)
        widgetLayout.addWidget(label_datetime)

        self.setLayout(widgetLayout)

class MaterialWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, name="", link=""):
        # https://stackoverflow.com/questions/26199374/add-qwidget-to-qlistwidget
        
        QtWidgets.QWidget.__init__(self, parent=parent)

        label_name = QtWidgets.QLabel(f"{name}")
        label_name.setFixedHeight(20)
        label_link = QtWidgets.QLabel(f"<a href=\"{link}\">{link}</a>")
        label_link.setTextFormat(QtCore.Qt.RichText)
        label_link.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        label_link.setOpenExternalLinks(True)
        label_link.setFixedHeight(20)

        widgetLayout = QtWidgets.QVBoxLayout()
        widgetLayout.addWidget(label_name)
        widgetLayout.addWidget(label_link)
        widgetLayout.addStretch()
        self.setLayout(widgetLayout)

HEARTBEAT_MSEC = 5000

class InfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, student_id, timestamp):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.okay_info.clicked.connect(self.email)
        self.cancel_info.clicked.connect(self.close)

        self.fill_information(student_id, timestamp)
        self.email = None
        self.session_id = str(uuid.uuid4())

        self.session_db_handler = db_backend.GenerateLoginLog()

        self.session_db_handler.login_record(student_id, self.session_id)

    def start(self):
        self.timer = QtCore.QTimer(self)           # Timer to trigger heartbeat log
        self.timer.timeout.connect(lambda: self.session_db_handler.heartbeat(self.session_id))
        self.timer.start(HEARTBEAT_MSEC)

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

        cur_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

        if cur_time.hour < 4:
            welcome_msg = f"Good evening, {student_info['name']}!"
        elif cur_time.hour < 12:
            welcome_msg = f"Good morning, {student_info['name']}!"
        elif cur_time.hour < 18:
            welcome_msg = f"Good afternoon, {student_info['name']}!"
        else:
            welcome_msg = f"Good evening, {student_info['name']}!"

        welcome_msg += " Your login time is %02d:%02d:%02d"%(cur_time.hour, cur_time.minute, cur_time.second)

        self.label.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:18pt;\">{welcome_msg}</span></p></body></html>"))

        if len(student_info['lessons']):
            start_datetime = student_info['lessons'][0]['start_datetime']
            end_datetime = student_info['lessons'][0]['end_datetime']
            status1 = f"You have lessons in 1 hour - {student_info['lessons'][0]['course_code']} {start_datetime.hour}:{start_datetime.minute} - {end_datetime.hour}:{end_datetime.minute}  -- Venue: {student_info['lessons'][0]['venue']}" 
            status2 = "Class material:"
            status3 = f"Teacher's Message: {student_info['lessons'][0]['teacher_msg']}"
            lesson_info = db_backend.GetLessonMaterial().get_info(student_info['lessons'][0]['course_code'])

            if len(student_info['lessons'][0]['zoom_link']):
                itemN = QtWidgets.QListWidgetItem()
                widget = MaterialWidget(name="Zoom link", link=student_info['lessons'][0]['zoom_link'])
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

            for material in lesson_info:
                itemN = QtWidgets.QListWidgetItem()
                widget = MaterialWidget(name=material["material_name"], link=material["material_link"])
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

        else:
            status1 = "You do not have lessons in 1 hour."
            status2 = "Your upcoming classes:"
            week_info = db_backend.GenerateTimetable().get_timetable(student_id, timestamp)

            for lesson in week_info:
                itemN = QtWidgets.QListWidgetItem()
                widget = LessonWidget(course_name=lesson["course_name"], course_code=lesson["course_code"],
                                      venue=lesson["venue"], type=lesson["type"],
                                      start_datetime=lesson["start_datetime"], end_datetime=lesson["end_datetime"])
                itemN.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(itemN)
                self.listWidget.setItemWidget(itemN, widget)

        self.label_2.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status1}</span></p></body></html>"))
        self.label_3.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status2}</span></p></body></html>"))
        self.label_4.setText(_translate("Form", f"<html><head/><body><p><span style=\" font-size:12pt;\">{status3}</span></p></body></html>"))
if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    info_window = InfoWindow('177013', '2020-09-03 15:00:00')
    info_window.show()
    info_window.start()
    sys.exit(app.exec_())
