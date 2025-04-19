from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QGroupBox,QRadioButton,QButtonGroup
from random import shuffle
#создай пиложение для запоминания информации
app = QApplication([])
mw = QWidget()
mw.resize(500,300)

mw.cur_question = -1

class Question():
    def __init__(self,question,right_answer,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_2


questions = [Question("Ты дурак?","да","нет","нет","нет"),
Question("Какой мем был популярен в 2020?","амогус","анонимус","52","арбуз"),
Question("pyton или c++","python","c++","c++","c#"),
Question("௸௺௸ஃ௶ஃஉஇ","ஈஉஈஅஈஊ","ஊ்இஐ்ஐ்ஐஎ","ஈஊ4ஐ்","அஓதூரபுதஅனடோ"),
]

mw.setWindowTitle("Memory Card")


text = QLabel(questions[0].question)

answers = QGroupBox("Варианты ответов")


rbtn1 = QRadioButton(questions[0].right_answer)
rbtn2 = QRadioButton(questions[0].wrong_1)
rbtn3 = QRadioButton(questions[0].wrong_2)
rbtn4 = QRadioButton(questions[0].wrong_3)

answers_ = [rbtn1,rbtn2,rbtn3,rbtn4]

shuffle(answers_)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

button_ok = QPushButton("Ответить")

ans_v_layout = QVBoxLayout()
ans_v_layout2 = QVBoxLayout()
ans_h_layout3 = QHBoxLayout()

ans_v_layout.addWidget(rbtn1)
ans_v_layout.addWidget(rbtn2)
ans_v_layout2.addWidget(rbtn3)
ans_v_layout2.addWidget(rbtn4)

ans_h_layout3.addLayout(ans_v_layout)
ans_h_layout3.addLayout(ans_v_layout2)

answers.setLayout(ans_h_layout3)

ans_box = QGroupBox("Результаты теста:")
tx_result = QLabel("прав ты или нет")
tx_correct = QLabel("ответ будет тут!")
layout_res = QVBoxLayout()
layout_res.addWidget(tx_result,alignment = (Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(tx_correct,alignment = Qt.AlignHCenter,stretch = 2)
ans_box.setLayout(layout_res)

layout_1 = QHBoxLayout()
layout_2 = QHBoxLayout()
layout_3 = QHBoxLayout()

layout_1.addWidget(text,alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layout_2.addWidget(answers)
layout_2.addWidget(ans_box)
layout_3.addStretch(1)
layout_3.addWidget(button_ok,stretch = 2)
layout_3.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_1,stretch = 2)
main_layout.addLayout(layout_2,stretch = 8)
main_layout.addStretch(1)
main_layout.addLayout(layout_3,stretch = 3)
main_layout.addStretch(1)
main_layout.addStretch(5)
state = 1
def next_question():
    if mw.cur_question < len(questions)-1:
        mw.cur_question+=1
    else:
        mw.cur_question = 0
    ask(questions[mw.cur_question])
    print(2)
def check():
    print(-1)
    if answers_[0].isChecked():
        show_correct("Правильно")
    else:
        if answers_[1].isChecked() or answers_[2].isChecked() or answers_[3].isChecked():
            show_correct("Неверно")
def show_results():
    answers.hide()
    ans_box.show()
    button_ok.setText("Следующий вопрос")
    print(1)
def show_question():
    state = 0
    ans_box.hide()
    answers.show()
    button_ok.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    button_ok.clicked.connect(check)



def ask(q_):
    shuffle(answers_)
    answers_[0].setText(q_.right_answer)
    answers_[1].setText(q_.wrong_1)
    answers_[2].setText(q_.wrong_2)
    answers_[3].setText(q_.wrong_3)
    text.setText(q_.question)
    tx_correct.setText(q_.right_answer)
    show_question()
#next_question()
def show_correct(res):
    tx_result.setText(res)
    show_results()
    print(0)
def click():
    if button_ok.text() == "Ответить":
        check()
    else:
        next_question()
mw.setLayout(main_layout)
button_ok.clicked.connect(click)
ans_box.hide()
mw.show()
app.exec_()
