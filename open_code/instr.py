
win_x, win_y = 300, 200
win_width, win_height = 1300, 750
#1
txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = """Даннное приложение поможет вам с помощью теста Руфье провести первичную диагностику вашего здоровья.
Пробу Руфье можно выполнить самостоятельно, в домашних условиях. 
Проба проводится после 5-10 минут отдыха. 
Измеряют пульс в покое положении сидя. Далее исследуемый должен сделать 30 
приседаний за 45 секунд, после чего он садится, и в течение первых 15 секунд вновь фиксируются показания его пульса. 
ВАЖНО! Если у испытуемого во время прохождения прробы возникли проблему , то срочно нужно обратиться к врачу! 
Внимательно вводите данные, поля ввода должны содержать лишь цифры!"""
txt_title = 'Тест Руфье'
#2
txt_name = 'Введите ФИО'
txt_age = 'Полных лет'
txt_hintname = "Ф.И.О."
txt_hintage = "0"
txt_test1 = """Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.
Результаты запишите в соответсвующее поле."""
txt_test2 = """Выполните 30 приседаний за 45 секунд. Нажмите кнопку "Начать делать приседания", чтобы запустить таймер.
Результаты запишите в соответсвующее поле."""
txt_test3 = """Лягте на спину и замерьте пульс сначала на первые 15 секунд минуты, затем за последние 15 секунд.
Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.
Зелёным обозначены секунды, в течение которых необходимо
проводить измерение, черным - минуты без измерения пульсаций. Результаты запишите в соответствующие окна."""
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
#3
txt_finalwin = 'Результаты'
txt_index = 'Индекс руфье: '
txt_workheart = 'Работоспособность сердца:         '
#resultati
slow = 'низкая'
ydovl = 'удовлетворительная'
srednya = 'средняя'
more_sredn = ' выше среднего'
large = 'высокая '
#comments
com_sl = "\nВашему состоянию здоровья остаётся желать лишь лучшего! \nВам следует немедленно обратиться к врачу!"
com_y = '\nВаше сердце не в лучшем состоянии. \nПолучите рекомендации и план тренировок у вашего лечущего врача.'
com_sr = '\nВам стоит заняться спортом!\nПомните, здоровье у нас одно, и беречь его следует постоянно.'
com_ms = '\nВаше состояние серца в неплохом состоянии! \nНо не стоит расслабляться, продолжайте вести здоровый образ жизни\nдля поддержки своего состояния.'
com_l = '\nВыражение: "Спорт-это движение, а движение - это жизнь!" \nточно про вас! Так держать! Продолжайте занятия спортом!'
com_error = '\nНеверные данные'
#photo
pct_sl = 'bad.jpg'
pct_y = 'notbad.jpg'
pct_sr = 'center.jpg'
pct_ms = 'well.jpg'
pct_l = 'good.jpg'
pct_error = 'error.jpg'
#log massage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QPushButton, QVBoxLayout,
QHBoxLayout, QApplication, 
QWidget,QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import  QFont, QPixmap, QIcon
class Logg(QWidget):
    def __init__(self, error):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.error = error
        self.show()
    def set_appear(self):
        self.setWindowTitle("ВНИМАНИЕ: ОШИБКА РАБОТЫ ПРОГРАММЫ!")
        self.setFixedSize(450, 300)
        self.setWindowIcon(QIcon('error1.png'))
        self.move(win_x, win_y)
    def initUI(self):
        #картинка
        self.pixmap = QPixmap("error1.png")
        self.photo_lbl1 = QLabel()
        self.photo_lbl1.setPixmap(self.pixmap)
        #лог
        self.log = QLabel(log_txt)
        self.log.setStyleSheet("font: 63 13pt \"Bahnschrift SemiBold\";")
        #Кнопки
        self.exit_btn = QPushButton("Oк")
        self.exit_btn.setStyleSheet("font: 63 13pt \"Bahnschrift SemiBold\";")
        #лейатуы
        self.up_line = QHBoxLayout()
        self.down_line = QHBoxLayout()
        self.v_line = QVBoxLayout()
        self.up_line.addWidget(self.photo_lbl1, alignment = Qt.AlignLeft)
        self.up_line.addWidget(self.log, alignment = Qt.AlignRight)
        self.down_line.addWidget(self.exit_btn, alignment = Qt.AlignCenter)
        self.v_line.addLayout(self.up_line)
        self.v_line.addLayout(self.down_line)
        self.setLayout(self.v_line)
    def connects(self):
        self.exit_btn.clicked.connect(self.close)