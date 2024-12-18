from tkinter import *

def colorchange():
    label_1.config(bg='blue')
    label_2.config(bg='red')
    label_3.config(bg='green')


root = Tk()
root.title("Label with Borders")

# Flat border

label_1=Label(root,text=1)
label_1.grid(row=0,column=0)
label_2=Label(root,text=2)
label_2.grid(row=1,column=0)
label_3=Label(root,text=3)
label_3.grid(row=2,column=0)

button=Button(root,text='press me',command=colorchange)
button.grid(row=0,column=1)
    

root.mainloop()
