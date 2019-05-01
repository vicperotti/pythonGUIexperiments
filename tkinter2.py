import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #Creating a StringVar allows easy access in and out of the Entry widget
        #using .get or .set()
        self.currentstring = tk.StringVar()
        self.currentstring.set("Type here")
        #set the textvariable property to the StringVar above
        self.entry = tk.Entry(self,textvariable=self.currentstring,width=50)
        self.entry.pack()
        close_button = tk.Button(self, text="Create List", command=lambda: self.retrieve_input())
        close_button.pack()

        #set the textvariable property to the StringVar above
        self.resultstring = tk.StringVar()
        self.resultsbox = tk.Entry(self,textvariable=self.resultstring,width=50)
        self.resultsbox.pack()

    def retrieve_input(self):
        input = self.currentstring.get()
        print(input)
        newlist = input.split(",") #create a list from a string
        results = list(map(int, newlist)) # convert newlist to integers
        print("You entered...", results)

        print(results)
        print("Our results list is %d long" % len(results))

        #FILL in the second Entry with a string showing the answer
        self.resultstring.set("The list minimum is... %f" % self.calcMinFromList(results))

    def calcMinFromList(self,mylist):
        minima = 999
        for m in mylist:
            if m < minima:
                minima = m
        return minima

    def close(self):
        global result
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return "Thank you!"

print("enter a string in the GUI")
app = MyApp()
app.geometry('350x200')
result = app.mainloop()

