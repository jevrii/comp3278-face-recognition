import sys
from PyQt5 import QtCore, QtWidgets
from Welcome_GUI import Ui_Form
from Student_Information_code import InfoWindow

class WelcomeWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.OkayButton_Welcome.clicked.connect(self.faces)
        self.CancelButton_Welcome.clicked.connect(self.close)
        self._new_window = None
    def faces(self):
        self._new_window = InfoWindow('177013', '2020-01-13 15:30')
        self._new_window.show()

if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    welcome_window = WelcomeWindow()
    welcome_window.show()
    sys.exit(app.exec_())
