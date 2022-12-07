from tkinter import *
root=Tk()
root.title('calculator')

exp=''
def calc(data):
    global exp
    if(exp=='0'):
        exp=data
    else:
        exp=exp+data
        inputscreen.config(text=exp)

def solution():
    global exp
    try:
        exp=str(eval(exp))
        inputscreen.config(text=exp)
    except:
        inputscreen.config(text="invalid")
def clear():
    global exp
    exp=""
    inputscreen.config(text='')

def back():
    global exp
    exp=exp[:-1]
    inputscreen.config(text=exp)


inputscreen=Label(root, text='', font=(50))
cls=Button(root,text='CLS',width=10,justify='right',bg='red',command=lambda:clear())
de=Button(root, text='back',width=10,bg='red',command=lambda:back())

one=Button(root, text='1',font=20,width=4,command=lambda:calc('1'))
two=Button(root, text='2',font=20,width=4,command=lambda:calc('2'))
three=Button(root, text='3',font=20,width=4,command=lambda:calc('3'))
four=Button(root, text='4',font=20,width=4,command=lambda:calc('4'))
five=Button(root, text='5',font=20,width=4,command=lambda:calc('5'))
six=Button(root, text='6',font=20,width=4,command=lambda:calc('6'))
seven=Button(root, text='7',font=20,width=4,command=lambda:calc('7'))
eight=Button(root, text='8',font=20,width=4,command=lambda:calc('8'))
nine=Button(root, text='9',font=20,width=4,command=lambda:calc('9'))
zero=Button(root, text='0',width=4,font=20,command=lambda:calc('0'))
dot=Button(root, text='.',width=4,font=20,command=lambda:calc('.'))
add=Button(root, text='+',font=20,width=4,command=lambda:calc('+'))
sub=Button(root, text='-',font=20,width=4,command=lambda:calc('-'))
mul=Button(root, text='x',font=20,width=4,command=lambda:calc('*'))
div=Button(root, text='/',width=6,bg='red',command=lambda:calc('/'))
eql=Button(root, text='=',font=20,width=9,bg='blue',command=lambda:solution())


inputscreen.pack()
cls.place(x=5,y=34)
de.place(x=80,y=34)
div.place(x=160,y=34)
nine.place(x=5,y=60)
eight.place(x=55,y=60)
seven.place(x=105,y=60)
six.place(x=5,y=100)
five.place(x=55,y=100)
four.place(x=105,y=100)
three.place(x=5,y=140)
two.place(x=55,y=140)
one.place(x=105,y=140)
zero.place(x=4,y=180)
dot.place(x=55,y=180)
add.place(x=160,y=60)
sub.place(x=160,y=100)
mul.place(x=160,y=140)
eql.place(x=105,y=180)

root.geometry('250x250')
root.mainloop()



 
 
 
