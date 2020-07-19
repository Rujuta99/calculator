from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget
from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QVBoxLayout
from PyQt5.QtCore import Qt
#from PyQt5 import QApplication, QMainWindow
import sys
from functools import partial

class Calci(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(350, 350)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.createdisplay()
        self.buttons()
        #layout = QGridLayout()
        #layout.addWidget(QPushButton('But 0,0'),0,0)

    def createdisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def buttons(self):
        self.buttonsLayout = QGridLayout()
        '''self.button[7] = QPushButton('Button 0,0')
        self.button[7].setFixedSize(40,40)
        self.buttonsLayout.addWidget(self.button[7],0,0)
        self.generalLayout.addLayout(buttonsLayout)'''

        btn=self.buttonsLayout.addWidget(QPushButton('AC'),0,0)
        self.buttonsLayout.addWidget(QPushButton('Result'),0,1)
        self.buttonsLayout.addWidget(QPushButton('0'),0,2)
        self.buttonsLayout.addWidget(QPushButton('/'),0,3)
        self.buttonsLayout.addWidget(QPushButton('7'),1,0)
        self.buttonsLayout.addWidget(QPushButton('8'),1,1)
        self.buttonsLayout.addWidget(QPushButton('9'),1,2)
        self.buttonsLayout.addWidget(QPushButton('X'),1,3)
        self.buttonsLayout.addWidget(QPushButton('4'),2,0)
        self.buttonsLayout.addWidget(QPushButton('5'),2,1)
        self.buttonsLayout.addWidget(QPushButton('6'),2,2)
        self.buttonsLayout.addWidget(QPushButton('-'),2,3)
        self.buttonsLayout.addWidget(QPushButton('1'),3,0)
        self.buttonsLayout.addWidget(QPushButton('2'),3,1)
        self.buttonsLayout.addWidget(QPushButton('3'),3,2)
        self.buttonsLayout.addWidget(QPushButton('+'),3,3)
    
        self.generalLayout.addLayout(self.buttonsLayout)
        '''text=btn.text()
        btn.clicked.connect(functools.partial(self.buildExpression),text)'''


def main():
    pycalc = QApplication(sys.argv)
    view = Calci()
    view.show()
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

'''def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Calculator")
    win.show()
    sys.exit(app.exec_())

    
window()'''