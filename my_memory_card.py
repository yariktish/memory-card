#создай приложение для запоминания информации
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QWidget, QGroupBox, QButtonGroup 
)

from random import shuffle, randint


app = QApplication([])
memory_card = QWidget()


class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3
    ):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    RadGrBox.hide()
    RadGrBox2.show()
    button.setText('Следующий вопрос')


def show_question():
    RadGrBox2.hide()
    RadGrBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    uns1.setChecked(False)
    uns2.setChecked(False)
    uns3.setChecked(False)
    uns4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    TpAnsw.setText(q.right_answer)
    que.setText(q.question)
    show_question()


def check_answer():
    if answers[0].isChecked():
        TrFa.setText('Правильно')
        memory_card.score += 1
        show_result()
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        TrFa.setText('Неправильно')
        show_result()
    statistika()


def next_question():
    memory_card.total += 1
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)


def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def statistika():
    print('Статистика:')
    print('-Всего вопросов:', memory_card.total)
    print('-Правильных ответов', memory_card.score)
    print('Рейтинг:', memory_card.score/memory_card.total*100)


memory_card.setWindowTitle('Memory Card')

que = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')

memory_card.total = 0
memory_card.score = 0

uns1 = QRadioButton('Энцы')
uns2 = QRadioButton('Смурфы')
uns3 = QRadioButton('Чулымцы')
uns4 = QRadioButton('Алеуты')

answers = [uns1, uns2, uns3, uns4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(uns1)
RadioGroup.addButton(uns2)
RadioGroup.addButton(uns3)
RadioGroup.addButton(uns4)

layout_main = QVBoxLayout()

RadGrBox = QGroupBox('Варианты ответов')

layoutH1 = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

layoutV1.addWidget(uns1)
layoutV1.addWidget(uns2)
layoutV2.addWidget(uns3)
layoutV2.addWidget(uns4)

layoutH1.addLayout(layoutV1)
layoutH1.addLayout(layoutV2)

RadGrBox.setLayout(layoutH1)
#RadGrBox.hide()

RadGrBox2 = QGroupBox('Результат текста')
RadGrBox2.hide()

TrFa = QLabel('Правильно/неправильно')
TpAnsw = QLabel('Следующий вопрос')

layoutVer1 = QVBoxLayout()

layoutVer1.addWidget(TrFa, alignment=(Qt.AlignLeft | Qt.AlignTop))
layoutVer1.addWidget(TpAnsw, alignment = Qt.AlignHCenter)

RadGrBox2.setLayout(layoutVer1)

Gor1 = QHBoxLayout()
Gor2 = QHBoxLayout()
Gor3 = QHBoxLayout()

Gor1.addWidget(que)
Gor2.addWidget(RadGrBox)
Gor2.addWidget(RadGrBox2)
Gor3.addWidget(button)

layout_main.addLayout(Gor1)
layout_main.addLayout(Gor2)
layout_main.addLayout(Gor3)

memory_card.setLayout(layout_main)

question_list = []
question_list.append(Question('Какой из этих разделов верховой езды не является спортом?', 'Скачки', 'Выездка', 'Конкур', 'Кросс'))
question_list.append(Question('Кто является предком классической гитары?', 'Лютня', 'Балалайка', 'Гусли', 'Скрипка'))
question_list.append(Question('Сколько тигров в Бутане', '2', '19', '48', '9'))
question_list.append(Question('Максимальная достигнутая скорость на горных лыжах?', '256', '190', '96', '310'))
question_list.append(Question('2 + 2 * 2 - 14 + -2', '10', '-10', '-9', '4'))

next_question()

button.clicked.connect(click_OK)

memory_card.show()
app.exec_()