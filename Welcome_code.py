import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome_GUI import Ui_Form

class WelcomeWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, parent = None):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.OkayButton_Welcome.clicked.connect(self.faces)
        self.CancelButton_Welcome.clicked.connect(self.close)
    def faces(self):
        self.p = QtCore.QProcess()
        self.p.start("python3", ['faces.py'])
        self.p.waitForFinished(1000)

app = QtWidgets.QApplication(sys.argv)
w = WelcomeWindow()
w.show()
sys.exit(app.exec_())
        
