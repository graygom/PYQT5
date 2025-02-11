#
# TITLE: PyQt5 project 2
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
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from random import choice


# Main App objects and settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Second Application')
main_window.resize(250, 300)


# create all App objects/widgets
text_box = QLineEdit()
grid = QGridLayout()
clear = QPushButton('C')        # text
delete = QPushButton('<')       # text


# functionality
buttons = {'7':[0,0],'8':[0,1],'9':[0,2],'/':[0,3],
           '4':[1,0],'5':[1,1],'6':[1,2],'*':[1,3],
           '1':[2,0],'2':[2,1],'3':[2,2],'-':[2,3],
           '0':[3,0],'.':[3,1],'=':[3,2],'+':[3,3]}

def button_click():
    button = app.sender()       # who sent the message
    text = button.text()        # get message

    if text == '=':             # check if '=' is got
        symbol = text_box.text()
        try:
            res = eval(symbol)
            text_box.setText(str(res))
        except Exception as e:
            text_box.setText('Error')

    elif text == 'C':
        text_box.clear()

    elif text == '<':
        current_text = text_box.text()
        text_box.setText(current_text[:-1])

    else:
        current_text = text_box.text()
        text_box.setText(current_text + text)



# event handling
for text in buttons:
    row, col = buttons[text]
    #
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)


# design layout
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)
master_layout.addLayout(button_row)

main_window.setLayout(master_layout)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)


# show main window and run app
main_window.show()
app.exec_()
