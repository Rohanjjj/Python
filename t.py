import customtkinter as tk
import tkinter
from tkinter import messagebox
import datetime
from tkinter import *
from PIL import Image,ImageTk

tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

root=tk.CTk()
root.geometry("1000x800")

from PIL import Image, ImageTk
image = Image.open("projectimg.png")
resized_image = image.resize((1000, 800))
img = ImageTk.PhotoImage(resized_image)
label = Label(image=img)
label.image = img
label.pack()


x=0
a=0
n=0
t=[]
o=""
j=[0]
i=0
g=0
r=0
idk15=0
def p_val():
    global j
    global i
    j[i]=1
def l():
    global g
    global t
    global j
    global i
    global r
    g=0
    r=0
    o = int(check.get())
    f=open('dwe.txt','r')
    s=f.read()
    p=s.splitlines()
    f.close()
    for i in p:
        t.append(int(i))
    for i in range(len(t)-len(j)):
        j.append(0)
    for g in range(0,len(t)):
        r=r+1
        if(o==t[g]):
            i=t.index(o)
            if j[i]==0:
                p_val()
                buttonframe.pack()
            else:
                messagebox.showinfo(message="Already voted")
                check.delete(0,"end")
            break
        elif (r==len(t)):
            messagebox.showinfo(message="could not be identified")
            check.delete(0,"end")
            break
def comm():
    now=datetime.datetime.now()
    data=open('data.txt','a')
    now=str(now)
    the_input=check.get()
    data.write(the_input+'   '+now+'\n')
    data.close()
def b():
    global x
    x=x+1
    buttonframe.pack_forget()
    comm()
    check.delete(0, "end")



def c():
    global a
    a=a+1
    buttonframe.pack_forget()
    comm()
    check.delete(0, "end")

def d():
    global n
    n=n+1
    buttonframe.pack_forget()
    comm()
    check.delete(0,'end')

def show():
  global x
  global a
  global n
  if (x>a):
      if (x>n):
          messagebox.showinfo(title="RESULT", message="BJP WON")
          exit()
  if (a>x):
      if (a>n):
          messagebox.showinfo(title="RESULT", message="Congress won:")
          exit()
  if(n>a):
      if(n>x):
          messagebox.showinfo(title="RESULT", message="AAP won")
          exit()
  if n==a and n==x:
      messagebox.showinfo(title='RESULT',message='ALL 3 parties ties ')
      exit()
  if x==a and x>n:
      messagebox.showinfo(title='result',message='BJP and Congress are tied ')
      exit()
  if x==n and a<n:
      messagebox.showinfo(title='result',message='AAP and Congress are tied')
      exit()
  if a==n and x<a:
      messagebox.showinfo(title='result',message='AAp and Congress are tied')
      exit()
def k():
    if(reveal.get().isdigit()==True):
        if(int(reveal.get())==456):
            buttonframe2.pack()
        else:
            messagebox.showinfo(message="incorrect")
            reveal.delete(0,'end')
    else:
        messagebox.showinfo(message="Incorrect")
        reveal.delete(0,'end')
def ball():
    text12.pack()
    butn_confirm.pack(padx=10,pady=10)
    buttonframe2.pack_forget()
    reveal.delete(0,'end')

def addtolist():
    if (text12.get()).isdigit()==True:
        y = ''
        numbers = []
        reader = 0
        f = open('dwe.txt', 'r')
        file = f.read()
        lines = file.splitlines()
        f.close()
        for i in lines:
            numbers.append(int(i))
        reader = int(text12.get())
        if (numbers.count(reader) == 1):
            messagebox.showinfo(message='already registered')
            text12.delete(0, 'end')
            text12.pack_forget()
            buttonframe2.pack_forget()
            butn_confirm.pack_forget()
        else:
            f = open("dwe.txt", 'a')
            y = y + '\n' + str(reader)
            f.write(y)
            messagebox.showinfo(message="Registration complete")
            text12.delete(0, 'end')
            text12.pack_forget()
            buttonframe2.pack_forget()
            butn_confirm.pack_forget()
    else:
        messagebox.showinfo(message="Enter integer values")
        text12.delete(0,'end')
        text12.pack_forget()
        butn_confirm.pack_forget()

output=tk.CTkLabel(master=root,text="EVM",font=("Jetbrains Mono ExtraBold",50))
output.pack(padx=10,pady=20)

idk=tk.CTkButton(master=root,text="Voter id:",height=10,text_color='red',font=('Monotype Corsiva',30),fg_color='cyan')
idk.pack(padx=10,pady=10)
check=tk.CTkEntry(master=root,height=2)
check.pack(padx=10,pady=10)

btn100=tk.CTkButton(master=root,text="Enter",command=l,font=('MV Boli',18))
btn100.pack()

buttonframe = tk.CTkFrame(master=root)
buttonframe.columnconfigure(0, weight=1)

btn1=tk.CTkButton(master=buttonframe,text="BJP",font=("Ariel", 18),text_color='orange',command=b)
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2=tk.CTkButton(master=buttonframe,text="CONGRESS",font=("Ariel", 18),text_color='pink',command=c)
btn2.grid(row=1,column=0,sticky=tk.W+tk.E)
btn3=tk.CTkButton(master=buttonframe,text="AAP",font=("Ariel", 18),text_color='white',command=d)
btn3.grid(row=2,column=0,sticky=tk.W+tk.E)
buttonframe.pack_forget()
buttonframe2=tk.CTkFrame(master=root)
buttonframe2.columnconfigure(0,weight=1)
btn4=tk.CTkButton(master=buttonframe2,text="show result",font=("MV Boli", 18),command=show)
btn4.grid(row=0,column=0,sticky=tk.W+tk.E)
btn5=tk.CTkButton(master=buttonframe2,text="add user",command=ball,font=("MV Boli", 18))
btn5.grid(row=1,column=0,sticky=tk.W+tk.E)
btn6=tk.CTkButton(master=buttonframe2,text="Delete Voting Logs from temp",command=ball,font=("MV Boli", 18))
btn6.grid(row=2,column=0,sticky=tk.W+tk.E)

buttonframe2.pack_forget()

text12=tk.CTkEntry(master=root,height=1,width=250,font=('ariel',18),placeholder_text="Enter the username here:")
text12.pack_forget()
butn_confirm=tk.CTkButton(master=root,text="Enter(note: only accepting integer usernames):",command=addtolist)
butn_confirm.pack_forget()

noti=tk.CTkLabel(master=root,text="ENTER CODE TO REVEAL RESULT:",font=('Bookman Old Style',20),text_color='cyan')
noti.pack(padx=10,pady=20)
reveal=tk.CTkEntry(master=root,height=1,width=230,placeholder_text="Enter the password here",show='*',font=('Ariel',20))
reveal.pack(padx=10,pady=5)
btn20=tk.CTkButton(master=root,text="OK",font=("Ariel", 18),command=k)
btn20.pack(padx=10,pady=10)
root.mainloop()
