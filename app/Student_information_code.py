import sys
import yagmail
from PyQt5 import QtCore, QtWidgets
from Student_Information_GUI import Ui_Form

class InfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.okay_info.clicked.connect(self.email)
        self.cancel_info.clicked.connect(self.close)
    def email(self):
        # if student has class within one hour:
        #   self.textBrowser.append()
        # else:
        #   self.textBrowser.append()
        if self.sendtoemail.isChecked():
            # info_email = yagmail.SMTP()
            # contents = []
            # info_email.send('to email', 'Course Information', contents)
            pass
        self.close()

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
info_window = InfoWindow()
info_window.show()
sys.exit(app.exec_())
        