from tkinter import *


window = Tk()
window.title("Miles to Km")
window.config(padx=10, pady=10)

inputBox = Entry()
inputBox.grid(column=1,row=0)


miles = Label(text="miles")
miles.grid(column=2,row=0)



equal = Label(text="is equal to")
equal.grid(column=0,row=1)


answer = Label(text="0")
answer.grid(column=1,row=1)


km = Label(text="Km")
km.grid(column=2,row=1)

def action():
    a = float(inputBox.get()) * 1.609
    answer["text"] = str(a)

calculate = Button(text="calculate", command=action)
calculate.grid(column=1, row=2)





window.mainloop()





