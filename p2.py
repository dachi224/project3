from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from time import time
import sys

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Splash Screen")
        #ფიქსირებული ფანჯრის ზომა
        self.setFixedSize(1100, 500)
        # ჩარჩოს გაქრობა
        self.setWindowFlag(Qt.FramelessWindowHint)
        #გამჭვირვალე ფონი
        #self.setAttribute(Qt.WA_TranslucentBackground)


        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.labelTitle = QLabel("Hello")
        layout.addWidget(self.labelTitle)




app = QApplication([])
window = SplashScreen()

window.show()
app.exec_()
