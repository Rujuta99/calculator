import PyQt5.QtWidgets as qtw 
from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QVBoxLayout

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.setFixedSize(350, 350)
        '''btn1 = qtw.QPushButton('test')
        self.layout().addWidget(btn1)'''
        self.keypad() #calls keypad func
        self.temp_nums = []
        self.fin_nums = []
        self.show()
    
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        self.field = qtw.QLineEdit()
        btn_clear = qtw.QPushButton('AC',clicked = self.func_clear)
        btn_result = qtw.QPushButton('Result', clicked = self.func_result)
        btn_0 = qtw.QPushButton('0', clicked = lambda: self.num_pres('0'))
        btn_div = qtw.QPushButton('/', clicked = lambda: self.func_pres('/'))
        btn_7 = qtw.QPushButton('7', clicked = lambda: self.num_pres('7'))
        btn_8 = qtw.QPushButton('8', clicked = lambda: self.num_pres('8'))
        btn_9 = qtw.QPushButton('9', clicked = lambda: self.num_pres('9'))
        btn_mult = qtw.QPushButton('X', clicked = lambda: self.func_pres('x'))
        btn_4 = qtw.QPushButton('4', clicked = lambda: self.num_pres('4'))
        btn_5 = qtw.QPushButton('5', clicked = lambda: self.num_pres('5'))
        btn_6 = qtw.QPushButton('6', clicked = lambda: self.num_pres('6'))
        btn_minus = qtw.QPushButton('-', clicked = lambda: self.func_pres('-'))
        btn_1 = qtw.QPushButton('1', clicked = lambda: self.num_pres('1'))
        btn_2 = qtw.QPushButton('2', clicked = lambda: self.num_pres('2'))
        btn_3 = qtw.QPushButton('3', clicked = lambda: self.num_pres('3'))
        btn_add = qtw.QPushButton('+', clicked = lambda: self.func_pres('+'))
        container.layout().addWidget(self.field,0,0,1,4)
        container.layout().addWidget(btn_clear,1,0)       
        container.layout().addWidget(btn_result,1,1)
        container.layout().addWidget(btn_0,1,2)
        container.layout().addWidget(btn_div,1,3)
        container.layout().addWidget(btn_7,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_9,2,2)
        container.layout().addWidget(btn_mult,2,3)
        container.layout().addWidget(btn_4,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_6,3,2)
        container.layout().addWidget(btn_minus,3,3)
        container.layout().addWidget(btn_1,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_3,4,2)
        container.layout().addWidget(btn_add,4,3)
        self.layout().addWidget(container)

    def num_pres(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.field.setText (temp_string)
    
    def func_pres(self,operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums)+ ''.join(self.temp_nums)
        result_string = eval(fin_string)
        #fin_string += "="
        self.field.clear()
        fin_string = str(result_string)
        self.field.setText(fin_string)
    
    def func_clear(self):
        self.field.clear()
        self.temp_nums = []
        self.fin_nums = []
    
        
        


app = qtw.QApplication([])

mw=MainWindow()
#app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()