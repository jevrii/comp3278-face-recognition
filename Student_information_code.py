import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Student_Information_GUI import Ui_Form

class InfoWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent = None):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.okay_info.clicked.connect(self.email)
        self.cancel_info.clicked.connect(self.close)
    def email(self):
        if self.sendtoemail.isChecked():
            pass
        self.close()

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
w = InfoWindow()
w.show()
sys.exit(app.exec_())
        
