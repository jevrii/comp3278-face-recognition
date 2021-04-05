import sys
from PyQt5 import QtCore, QtWidgets
from Welcome_GUI import Ui_Form

class WelcomeWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.OkayButton_Welcome.clicked.connect(self.faces)
        self.CancelButton_Welcome.clicked.connect(self.close)
    def faces(self):
        QtCore.QProcess.p.start("python3", ['faces.py'])
        QtCore.QProcess.p.waitForFinished(1000)

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
welcome_window = WelcomeWindow()
welcome_window.show()
sys.exit(app.exec_())
        
