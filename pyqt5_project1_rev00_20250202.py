#
# TITLE: PyQt5 project 1
# AUTHOR: Hyunseung Yoo
# PURPOSE:
# REVISION:
# REFERENCE: https://www.youtube.com/watch?v=f_9NBdSAo-g
#            https://www.youtube.com/watch?v=K9teElePNkk
#            https://www.youtube.com/watch?v=WlLgysXJ0Ec
#
# Code Burger
# 1. all imports
# 2. main app objects and settings
# 3. create all widgets needed in app
# 4. design layout, add widgets to the screen
# 5. set the final layout to the main window
# 6. show and execute app
#

# Imports modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice


# Main App objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('First Application')
main_window.resize(300, 200)


# create all App objects
title_text = QLabel('Random keywords')

text1 = QLabel('?')
text2 = QLabel('?')
text3 = QLabel('?')

button1 = QPushButton('Click Me')
button2 = QPushButton('Click Me')
button3 = QPushButton('Click Me')

# design: 
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)


# event handling
my_words = ['hello', 'goodbye', 'test', 'python', 'PyQt', 'strawberry', 'raspberry pi', 'nintendo', 'sony']

def random_word1():
    word = choice(my_words)
    text1.setText(word)

def random_word2():
    word = choice(my_words)
    text2.setText(word)

def random_word3():
    word = choice(my_words)
    text3.setText(word)

button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)


# show main window and run app
main_window.show()
app.exec_()
