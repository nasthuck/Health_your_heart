# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout,
QHBoxLayout, QApplication, QLineEdit,
QWidget,QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import  QFont, QPixmap, QIcon
from instr import *
try:
    class Experement():
        def __init__(self, age, t1, t2, t3):
            self.age = int(age)
            if self.age > 0:    
                self.t1 = int(t1)
                self.t2 = int(t2)
                self.t3 = int(t3)
                print('consol_', self.t1, self.t2, self.t3)
                if self.t1 <= 0 or self.t2 <= 0 or self.t3 <= 0:
                    self.index = "ОШИБКА"
                    self.res_programm = ['Как вы ещё живы? Такого пульса не существует !', com_error, pct_error]
                else:
                    self.index = (4*(int(self.t1)+int(self.t2)+int(self.t3))-200)/10
                    self.srav()
            else:
                self.index = "ОШИБКА"
                self.res_programm = ['Вы ввели неверный возраст!', com_error, pct_error]
        def srav(self):
            if self.age >= 7 and self.age <= 8:
                if self.index >= 21.0:
                    self.res_programm = [slow, com_sl, pct_sl]
                elif self.index >= 17.0 and self.index <= 20.9:
                    self.res_programm = [ydovl, com_y, pct_y]
                elif self.index >= 12.0 and self.index <= 16.9:
                    self.res_programm = [srednya, com_sr, pct_sr]
                elif self.index >= 6.5 and self.index <= 11.9:
                    self.res_programm = [more_sredn, com_ms, pct_ms]
                elif self.index <= 6.4:
                    self.res_programm = [large, com_l, pct_l]
            elif self.age >= 9 and self.age <= 10:
                if self.index >= 19.5:
                    self.res_programm = [slow, com_sl, pct_sl]
                elif self.index >= 15.5 and self.index <= 19.4:
                    self.res_programm = [ydovl, com_y, pct_y]
                elif self.index >= 10.5 and self.index <= 15.4:
                    self.res_programm = [srednya, com_sr, pct_sr]
                elif self.index >= 5.0 and self.index <= 10.4:
                    self.res_programm = [more_sredn, com_ms, pct_ms]
                elif self.index <= 4.9:
                    self.res_programm = [large, com_l, pct_l]
            elif self.age >= 11 and self.age <=12:
                if self.index >= 18.0:
                    self.res_programm = [slow, com_sl, pct_sl]
                elif self.index >= 14.0 and self.index <= 17.9:
                    self.res_programm = [ydovl, com_y, pct_y]
                elif self.index >= 9.0 and self.index <= 13.9:
                    self.res_programm = [srednya, com_sr, pct_sr]
                elif self.index >= 3.5 and self.index <= 8.9:
                    self.res_programm = [more_sredn, com_ms, pct_ms]
                elif self.index <= 3.4:
                    self.res_programm = [large, com_l, pct_l]
            elif self.age >= 13 and self.age <= 14:
                if self.index >= 16.5:
                    self.res_programm = [slow, com_sl, pct_sl]
                elif self.index >= 12.5 and self.index <= 16.4:
                    self.res_programm = [ydovl, com_y, pct_y]
                elif self.index >= 7.5 and self.index <= 12.4:
                    self.res_programm = [srednya, com_sr, pct_sr]
                elif self.index >= 2 and self.index <= 7.4:
                    self.res_programm = [more_sredn, com_ms, pct_ms]
                elif self.index <= 1.9:
                    self.res_programm = [large, com_l, pct_l]
            elif self.age >= 15:
                if self.index >= 15.0:
                    self.res_programm = [slow, com_sl, pct_sl]
                elif self.index >= 11.0 and self.index <= 14.9:
                    self.res_programm = [ydovl, com_y, pct_y]
                elif self.index >= 6.0 and self.index <= 10.9:
                    self.res_programm = [srednya, com_sr, pct_sr]
                elif self.index >= 0.5 and self.index <= 5.9:
                    self.res_programm = [more_sredn, com_ms, pct_ms]
                elif self.index <= 0.4:
                    self.res_programm = [large, com_l, pct_l]
            else:
                self.index = "ОШИБКА"
                self.res_programm = ['Извините, но тут нет таких данных!(', com_error, pct_error]
    class ResultWin(QWidget):
        def __init__(self, index, result, name):
            super().__init__()
            self.index = index
            self.name = name
            self.progress = result[0]
            self.com_txt = result[1]
            self.pct = result[2]
            self.set_appear()
            self.initUI()
            self.show()
        def set_appear(self):
            self.setWindowTitle(txt_finalwin)
            self.setFixedSize(win_width, win_height)
            self.move(win_x, win_y)
            self.setWindowIcon(QIcon('heart.jpg'))
            self.setStyleSheet("background-color: rgb(29, 29, 29);")
        def initUI(self):
            #картинка
            self.pixmap = QPixmap(self.pct)
            #self.smoller_pixmap = self.pixmap.scaled(90, 60)
            self.photo_lbl = QLabel()
            self.photo_lbl.setPixmap(self.pixmap)
            #текст и стилизация его
            self.comment = QLabel('Уважаемый(ая) '+self.name+self.com_txt)
            self.comment.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 13pt \"Bahnschrift SemiBold\";")
            self.index = QLabel(txt_index + str(self.index))
            self.index.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 13pt \"Bahnschrift SemiBold\";")
            self.heart = QLabel(txt_workheart + str(self.progress))
            self.heart.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 13pt \"Bahnschrift SemiBold\";")
            #лейауты
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.index, alignment = Qt.AlignCenter)
            self.layout.addWidget(self.photo_lbl, alignment = Qt.AlignCenter)
            self.layout.addWidget(self.comment, alignment = Qt.AlignCenter)
            self.layout.addWidget(self.heart, alignment = Qt.AlignCenter)
            self.setLayout(self.layout)
except Exception as e: 
    self.f = Logg(e)