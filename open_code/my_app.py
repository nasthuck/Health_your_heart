# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout,
QHBoxLayout, QApplication, 
QWidget,QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import  QFont, QIcon
from instr import *
from second_win import *
try:
    class MainWin(QWidget):
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
            self.hello_text = QLabel(txt_hello)
            self.hello_text.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 13pt \"Bahnschrift SemiBold\";")
            self.instruction = QLabel(txt_instruction)
            self.instruction.setStyleSheet("color: rgb(206, 206, 206);\n"
            "font: 63 13pt \"Bahnschrift SemiBold\";")
            self.button = QPushButton(txt_next)
            self.button.setFixedSize(100, 35)
            self.button.setStyleSheet("color: rgb(206, 206, 206);\n"
            "background-color: rgb(29, 29, 29);\n"
            "font: 63 16pt \"Bahnschrift SemiBold\";")
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
            self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
            self.layout.addWidget(self.button, alignment = Qt.AlignCenter)
            self.setLayout(self.layout)
        def next_click(self):
            self.hide()
            self.tw = TestWin()
        def connects(self):
            self.button.clicked.connect(self.next_click)
    app = QApplication([])
    window1 = MainWin()
    app.exec_()
except Exception as e: 
    self.f = Logg(e)