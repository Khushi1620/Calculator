from tkinter import *

def btn1click(event):
    s = inp1.get()
    s = s + "1"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn2click(event):
    s = inp1.get()
    s = s + "2"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn3click(event):
    s = inp1.get()
    s = s + "3"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn4click(event):
    s = inp1.get()
    s = s + "4"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn5click(event):
    s = inp1.get()
    s = s + "5"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn6click(event):
    s = inp1.get()
    s = s + "6"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn7click(event):
    s = inp1.get()
    s = s + "7"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn8click(event):
    s = inp1.get()
    s = s + "8"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn9click(event):
    s = inp1.get()
    s = s + "9"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def btn0click(event):
    s = inp1.get()
    s = s + "0"
    inp2.delete(0 , 'end')
    inp2.insert(0 , s)

def addbtnclick(event):
    s = inp1.get()
    s = s + "+"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def subbtnclick(event):
    s = inp1.get()
    s = s + "-"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def mulbtnclick(event):
    s = inp1.get()
    s = s + "*"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def divbtnclick(event):
    s = inp1.get()
    s = s + "/"
    inp1.delete(0 , 'end')
    inp1.insert(0 , s)

def eqbtnclick(event):
    s = inp1.get()
    a = eval(s)
    inp1.delete(0 , 'end')
    inp1.insert(0 , a)

def bcbtnclick(event):
    s = inp1.get()
    s1 = s[0:-1]
    inp1.delete(0 , 'end')
    inp1.insert(0 , s1)

def clrbtnclick(event):
    inp1.delete(0 , 'end')


root = Tk()

root.geometry("600x500")
root.title("Simple Calculator by Khushi Gupta")

inp1 = Entry(width=60,borderwidth=5, relief=GROOVE)
inp1.grid(row=0,column=0,columnspan=5)

btn1 = Button(text="1",width=8,height=3,font=20)
btn1.grid(row=1,column=1)

btn2 = Button(text="2",width=8,height=3,font=20)
btn2.grid(row=1,column=2)

btn3 = Button(text="3",width=8,height=3,font=20)
btn3.grid(row=1,column=3)

btn4 = Button(text="4",width=8,height=3,font=20)
btn4.grid(row=2,column=1)

btn5 = Button(text="5",width=8,height=3,font=20)
btn5.grid(row=2,column=2)

btn6 = Button(text="6",width=8,height=3,font=20)
btn6.grid(row=2,column=3)

btn7 = Button(text="7",width=8,height=3,font=20)
btn7.grid(row=3,column=1)

btn8 = Button(text="8",width=8,height=3,font=20)
btn8.grid(row=3,column=2)

btn9 = Button(text="9",width=8,height=3,font=20)
btn9.grid(row=3,column=3)

btn0 = Button(text="0",width=8,height=3,font=20)
btn0.grid(row=4,column=2)

addbtn = Button(text="+",width=8,height=3,font=20)
addbtn.grid(row=1,column=4)

subbtn = Button(text="-",width=8,height=3,font=20)
subbtn.grid(row=2,column=4)

mulbtn = Button(text="*",width=8,height=3,font=20)
mulbtn.grid(row=3,column=5)

divbtn = Button(text="/",width=8,height=3,font=20)
divbtn.grid(row=3,column=4)

eqbtn = Button(text="=",width=8,height=3,font=20)
eqbtn.grid(row=4,column=4)

clrbtn = Button(text="AC",width=8,height=3,font=20,bg="orange")
clrbtn.grid(row=1,column=5)

bcbtn = Button(text="C",width=8,height=3,font=20)
bcbtn.grid(row=2,column=5)



btn1.bind("<Button-1>" , btn1click)
btn2.bind("<Button-1>" , btn2click)
btn3.bind("<Button-1>" , btn3click)
btn4.bind("<Button-1>" , btn4click)
btn5.bind("<Button-1>" , btn5click)
btn6.bind("<Button-1>" , btn6click)
btn7.bind("<Button-1>" , btn7click)
btn8.bind("<Button-1>" , btn8click)
btn9.bind("<Button-1>" , btn9click)
btn0.bind("<Button-1>" , btn0click)

addbtn.bind("<Button-1>" , addbtnclick)
subbtn.bind("<Button-1>" , subbtnclick)
mulbtn.bind("<Button-1>" , mulbtnclick)
divbtn.bind("<Button-1>" , divbtnclick)
clrbtn.bind("<Button-1>" , clrbtnclick)
bcbtn.bind("<Button-1>" , bcbtnclick)
eqbtn.bind("<Button-1>" , eqbtnclick)


root.mainloop()