from tkinter import *


root = Tk()
root.title("Calculator")
root.resizable(0,0)
n1 = 0
operator = ""
entry = Entry(root,width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(num):
    num2=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(num2)+str(num))

def clear_button():
    entry.delete(0,END)

def button_add():
    global n1
    global operator
    operator="+"
    n1=entry.get()
    n2=str(n1)+"+"
    print("add",n2)
    entry.delete(0,END)
    entry.insert(0,n2)

def button_minus():
    global n1
    global operator
    operator="-"
    n1=entry.get()
    n2=str(n1)+"-"
    entry.delete(0,END)
    entry.insert(0,n2)

def button_mull():
    global n1
    global operator
    operator="X"
    n1=entry.get()
    n2=str(n1)+"x"
    print("mul",n2)
    entry.delete(0,END)
    entry.insert(0,n2)

def button_div():
    global n1
    global operator
    operator="/"
    n1=entry.get()
    n2=str(n1)+"/"
    entry.delete(0,END)
    entry.insert(0,n2)

def button_res():
    global n1
    s=n1
    res=entry.get()
    print(len(res))
    print(res)
    if(operator=="+"):
        x = int((res.split("+")[1])) 
        print (type(x))
        print (type(s))
        final = s+int(x)
        entry.delete(0,END)
        entry.insert(0,final)
    if(operator=="-"):
        x = int((res.split("-")[1])) 
        final = int(s)-int(x)
        entry.delete(0,END)
        entry.insert(0,final)
    if(operator=="X"):
        x = int((res.split("x")[1])) 
        final = int(s)*int(x)
        entry.delete(0,END)
        entry.insert(0,final)
    if(operator=="/"):
        x = int((res.split("/")[1])) 
        final = int(s)/int(x)
        entry.delete(0,END)
        entry.insert(0,final)


    

button_ac = Button(root, text="AC", padx=35, pady=20, command=lambda: clear_button())
button_zero = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
button_res = Button(root, text="Result", padx=27, pady=20, command= button_res)

button_minus = Button(root, text="-", padx=40, pady=20, command=  button_minus)
button_add = Button(root, text="+", padx=40, pady=20, command= button_add)
button_mul = Button(root, text="X", padx=40, pady=20, command=lambda : button_mull)
button_div = Button(root, text="/", padx=41, pady=20, command=lambda : button_div)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_add.grid(row=4,column=3)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_mul.grid(row=2,column=3)

button_ac.grid(row=1,column=0)
button_res.grid(row=1,column=1)
button_zero.grid(row=1,column=2)
button_div.grid(row=1,column=3)



root.mainloop()
'''
root = Tk()
root.title("Calculator")
root.config(width=500,height=450, bg="black")

frame = LabelFrame(root,text="This is ", padx=5,pady=5)
frame.pack(padx=10,pady=10)

b = Button(frame,text="1")

root.mainloop()'''