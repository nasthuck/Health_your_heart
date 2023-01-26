# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout,
QHBoxLayout, QApplication, QLineEdit,
QWidget ,QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import  QFont, QIcon
from instr import *
from final_win import *
try:
    class TestWin(QWidget):
        def __init__(self):
            super().__init__()
            self.set_appear()
            self.initUI()
            self.connects()
            self.show()
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.setFixedSize(win_width, win_height)
            self.move(win_x, win_y)
            self.setWindowIcon(QIcon('heart.jpg'))
            self.setStyleSheet("background-color: rgb(29, 29, 29);")
        def initUI(self):
            #виджеты
            #окна
            self.fio = QLabel(txt_name)
            self.fio.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.age_lbl = QLabel(txt_age)
            self.test1 = QLabel(txt_test1)
            self.test2 = QLabel(txt_test2)
            self.test3 = QLabel(txt_test3)
            self.text_timer = QLabel()
            #цвет окон
            self.age_lbl.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.test1.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.test2.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.test3.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.text_timer.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            #Кнопки
            self.btn_t1 = QPushButton(txt_starttest1)
            self.btn_t2 = QPushButton(txt_starttest2)
            self.btn_t2.setStyleSheet("color: rgb(29, 29, 29);\n"
            "background-color: rgb(199, 199, 199);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.btn_t3 = QPushButton(txt_starttest3)
            self.btn_ready = QPushButton(txt_sendresults)
            #цвет кнопок
            self.btn_t1.setStyleSheet("color: rgb(29, 29, 29);\n"
            "background-color: rgb(199, 199, 199);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.btn_t2.setStyleSheet("color: rgb(29, 29, 29);\n"
            "background-color: rgb(199, 199, 199);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.btn_t3.setStyleSheet("color: rgb(29, 29, 29);\n"
            "background-color: rgb(199, 199, 199);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.btn_ready.setStyleSheet("color: rgb(29, 29, 29);\n"
            "background-color: rgb(199, 199, 199);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            #Поля ввода
            self.name = QLineEdit(txt_hintname)
            self.age = QLineEdit(txt_hintage)
            self.resultat1 = QLineEdit(txt_hinttest1)
            self.resultat2 = QLineEdit(txt_hinttest2)
            self.resultat3 = QLineEdit(txt_hinttest2)
            #цвета полей ввода
            self.name.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.age.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.resultat1.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.resultat2.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            self.resultat3.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 10pt \"Bahnschrift SemiBold\";")
            #кнопка.setFixedSize(w, h) - размеры кнопки
            #лейауты
            self.l_line = QVBoxLayout()
            self.r_line = QVBoxLayout()
            self.h_line = QHBoxLayout()
            #Добавление виджетов
            self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
            self.l_line.addWidget(self.fio, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.name, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.age_lbl, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.age, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.test1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_t1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.resultat1, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.test2, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_t2, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.test3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_t3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.resultat2, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.resultat3, alignment = Qt.AlignLeft)
            self.l_line.addWidget(self.btn_ready, alignment = Qt.AlignRight)
            #закрепить лейауты
            self.h_line.addLayout(self.l_line)
            self.h_line.addLayout(self.r_line)
            self.setLayout(self.h_line)
        def next_click(self):
            self.hide()
            self.exp = Experement(self.age.text(), self.resultat1.text(),
            self.resultat2.text(), self.resultat3.text())
            print("cons", self.exp.index, self.exp.res_programm)
            self.thr = ResultWin(self.exp.index, self.exp.res_programm, self.name.text())
        def timer_test1(self):
            global time
            time = QTime(0, 0, 15)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer1Event)
            self.timer.start(1000)
        def timer1Event(self):
            global time
            time = time.addSecs(-1)
            self.text_timer.setText(time.toString("hh:mm:ss"))
            self.text_timer.setFont(QFont("Bahnschrift SemiBold", 36, QFont.Bold))
            self.text_timer.setStyleSheet("color: rgb(206, 206, 206)")
            if time.toString("hh:mm:ss") == '00:00:00':
                self.timer.stop()
        def timer_test2(self):
            global time
            time = QTime(0, 0, 45)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer2Event)
            self.timer.start(1000)
        def timer2Event(self):
            global time
            time = time.addSecs(-1)
            self.text_timer.setText(time.toString("hh:mm:ss"))
            self.text_timer.setFont(QFont("Bahnschrift SemiBold", 36, QFont.Bold))
            self.text_timer.setStyleSheet("color: rgb(206, 206, 206)")
            if time.toString("hh:mm:ss") == '00:00:00':
                self.timer.stop()
        def timer_test3(self):
            global time
            time = QTime(0, 1, 0)
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer3Event)
            self.timer.start(1000)
        def timer3Event(self):
            global time
            time = time.addSecs(-1)
            self.text_timer.setText(time.toString("hh:mm:ss"))
            self.text_timer.setFont(QFont("Bahnschrift SemiBold", 36, QFont.Bold))
            if int(time.toString("hh:mm:ss")[6:8]) >= 45:
                self.text_timer.setStyleSheet("color: rgb(176, 206, 0)")
            elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
                self.text_timer.setStyleSheet("color: rgb(176, 206, 0)")
            else:
                self.text_timer.setStyleSheet("color: rgb(206, 206, 206)")
            if time.toString("hh:mm:ss") == '00:00:00':
                self.timer.stop()
        def connects(self):
            self.btn_ready.clicked.connect(self.next_click)
            self.btn_t1.clicked.connect(self.timer_test1)
            self.btn_t2.clicked.connect(self.timer_test2)
            self.btn_t3.clicked.connect(self.timer_test3)
    #app = QApplication([])
    #window2 = TestWin()
    #app.exec_()
except Exception as e: 
    self.f = Logg(e)
