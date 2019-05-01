#based on https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Get-input-using-Entry-class-Tkinter-textbox
from tkinter import *

window = Tk()

window.title("Calculate the minimum of a list app")
window.geometry('350x200')
lbl = Label(window, text="Please enter a list (comma separated)")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

def clicked():
    input = txt.get()
    print(input)
    newlist = input.split(",") #create a list from a string
    results = list(map(int, newlist)) # convert newlist to integers
    print("You entered...", results)
    themin = calcMinFromList(results)
    res = "Your minimum is..." + str(themin)
    lbl2.configure(text= res)

def calcMinFromList(mylist):
    minima = 999
    for m in mylist:
        if m < minima:
            minima = m
    return minima

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=1)

lbl2 = Label(window, text="Your answer is....")
lbl2.grid(column=0, row=1)


window.mainloop()
