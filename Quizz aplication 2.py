
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from time import time
import sys





#მეორე ნაბიჯი

    clasSplashScreen(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Spash Screen Example')
            # ფიქსირებული ზომის მინიჭება
            self.setFixedSize(1100, 500)
            # ჩარჩოს გაქრობა
            self.setWindowFlag(Qt.FramelessWindowHint)
            # ბექგრაუნდის გამჭვირვალობა
            self.setAttribute(Qt.WA_TranslucentBackground)

            self.counter = 0
            self.n = 300  # total instance

            # ვიჯეტების შემქმნელი ფუნქციის გაშვება
            self.initUI()

            self.timer = QTimer()
            self.timer.timeout.connect(self.loading)
            self.timer.start(30)

        def initUI(self):
            layout = QVBoxLayout()
            self.setLayout(layout)

            self.frame = QFrame()
            layout.addWidget(self.frame)

            self.labelTitle = QLabel(self.frame)
            self.labelTitle.setObjectName('LabelTitle')

            # center labels
            self.labelTitle.resize(self.width() - 10, 150)
            self.labelTitle.move(0, 40)  # x, y
            self.labelTitle.setText('Splash Screen')
            self.labelTitle.setAlignment(Qt.AlignCenter)

            self.labelDescription = QLabel(self.frame)
            self.labelDescription.resize(self.width() - 10, 50)
            self.labelDescription.move(0, self.labelTitle.height())
            self.labelDescription.setObjectName('LabelDesc')
            self.labelDescription.setText('<strong>Working on Task #1</strong>')
            self.labelDescription.setAlignment(Qt.AlignCenter)

            self.progressBar = QProgressBar(self.frame)
            self.progressBar.resize(self.width() - 200 - 10, 50)
            self.progressBar.move(100, self.labelDescription.y() + 130)
            self.progressBar.setAlignment(Qt.AlignCenter)
            self.progressBar.setFormat('%p%')
            self.progressBar.setTextVisible(True)
            self.progressBar.setRange(0, self.n)
            self.progressBar.setValue(20)

            self.labelLoading = QLabel(self.frame)
            self.labelLoading.resize(self.width() - 10, 50)
            self.labelLoading.move(0, self.progressBar.y() + 70)
            self.labelLoading.setObjectName('LabelLoading')
            self.labelLoading.setAlignment(Qt.AlignCenter)
            self.labelLoading.setText('loading...')

        def loading(self):
            self.progressBar.setValue(self.counter)

            if self.counter == int(self.n * 0.3):
                self.labelDescription.setText('<strong>Working on Task #2</strong>')
            elif self.counter == int(self.n * 0.6):
                self.labelDescription.setText('<strong>Working on Task #3</strong>')
            elif self.counter >= self.n:
                self.timer.stop()
                self.close()

                time.sleep(1)

                self.myApp = MyApp()
                self.myApp.show()

            self.counter += 1

    class MyApp(QWidget):
        def __init__(self):
            super().__init__()
            self.window_width, self.window_height = 1200, 800
            self.setMinimumSize(self.window_width, self.window_height)

            layout = QVBoxLayout()
            self.setLayout(layout)

    if __name__ == '__main__':

        app = QApplication([])
        app.setStyleSheet('''
            #LabelTitle {
                font-size: 60px;
                color: #00FF00;
            }

            #LabelDesc {
                font-size: 30px;
                color: #000000;
            }

            #LabelLoading {
                font-size: 30px;
                color: #00FF00;
            }

            QFrame {
                background-color: #000000;
                color: rgb(220, 220, 220);
            }

            QProgressBar {
                background-color: #00FF00;
                color: rgb(200, 200, 200);
                border-style: none;
                border-radius: 10px;
                text-align: center;
                font-size: 30px;
            }

            QProgressBar::chunk {
                border-radius: 10px;
                background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #00FF00, stop:1 #000000);
            }
        ''')

        splash = SplashScreen()
        splash.show()

        try:
            app.exec_()
        except SystemExit:
            print('Closing Window...')

    #მესამე ნაბიჯი
    questions = ("How many elements are in the periodic table?: ",
                 "Which color is the first at the traffic light?: ",
                 "What time does the earth take to go around the sun?: ",
                 "How many bones are in the human body?: ",
                 "Which planet in the solar system is the hottest?: ")

    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
               ("A.green  ", "B.blue ", "C.yellow ", "D.red "),
               ("A.24hrs ", "B.2days ", "C.10hrs ", "D.23hrs "),
               ("A. 206", "B. 207", "C. 208", "D. 209"),
               ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    answers = ("C", "D", "A", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("----------------------")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")