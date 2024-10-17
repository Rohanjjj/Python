'''x=lambda x:x*x
print(x(5))
m=lambda x,y:x+y
print(m(3,4))

x=lambda x:x*x
print(x(5))
m=lambda x,y:x+y
print(m(3,4))

list1=[1,2,5,8]
list2=[1,4,7,2]
list4=[1,2]
list5=[11,22]
list3=list(map(lambda x,y,z,d:x+y+z+d,list1,list2,list4,list5))
print(list3)

list1=[1,2,5,8]
list2=list(filter(lambda x:x>2,list1))
print(list2)

import functools
list1=[1,2,5,8]
s=functools.reduce(lambda x,y:x+y,list1)
t=functools.reduce(int.__add__,list1)
u=functools.reduce(int.__mul__,list1)
print(s,t,u,sep="\n")

str1=lambda s:print('hello'+s)
print(str1('python'))

str2=lambda s:s.upper()[::-1]
print(str2('hello'))
max=lambda a,b:a if (a>b) else b
print(max(4,5))

def func(n):
    return lambda a:a*n
double=func(2)
print(double(10))'''
#lambda with recursion ,higher order :
'''import tkinter as tk
root=tk.Tk()
root.title("Tkinter Demonstrate")
root.geometry('300x200')
root.mainloop()'''

import tkinter 
from tkinter import *
win=Tk()
win.title("Demo")
win.geometry('300x200')
b=Button(win,text='Submit')
b.pack()
win.mainloop()
