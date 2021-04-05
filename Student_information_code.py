import sys
import smtplib
import email
from PyQt5 import QtCore, QtWidgets
from Student_Information_GUI import Ui_Form

class InfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.okay_info.clicked.connect(self.email)
        self.cancel_info.clicked.connect(self.close)
        # self.textBrowser.append('<a href = http://google.com>Google</a>')
    def email(self):
        # if student has class within one hour:
        #   self.textBrowser.append()
        # else:
        #   self.textBrowser.append()
        if self.sendtoemail.isChecked():
            # sent_msg = email.message.EmailMessage()
            # sent_msg.set_content()
            # sent_msg['Subject'] = 
            # sent_msg['From'] =
            # sent_msg['To'] =
            # smtp_server = smtplib.SMTP('mail.cs.hku.hk')
            # smtp_server.send_message(sent_msg)
            # smtp_server.quit()
            pass
        self.close()

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
info_window = InfoWindow()
info_window.show()
sys.exit(app.exec_())
        
