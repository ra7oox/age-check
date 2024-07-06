#Ra7oox


from tkinter import *
from tkinter import messagebox

root=Tk()

root.geometry("400x400")
label1=Label(root,text="how old are you?")

label1.place(x=140,y=40)

input1=Entry(root)
input1.place(x=120,y=60)

def check():
    if int(input1.get())<18:
        messagebox.showerror("error",message="sorry you are minor")
    else:
        root.destroy()
        root2=Tk()
        root2.geometry("400x400")
        label2=Label(root2,text="good you are not minor")
        label2.place(x=120,y=70)
        
btn=Button(root,command=check,text="enter")
btn.place(x=160,y=90)






root.mainloop()