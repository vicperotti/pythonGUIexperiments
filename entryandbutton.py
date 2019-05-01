import tkinter as tk

thelist = []

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.entry = tk.Entry(self)
        #self.entry.pack()

        self.myText_Box = tk.Text(self, height=2, width=10)
        self.myText_Box.pack()
        close_button = tk.Button(self, text="Add to List", command=lambda: self.retrieve_input())
        close_button.pack()
        self.string = ""

    def retrieve_input(self):
        input = self.myText_Box.get("1.0","end-1c")
        print(input)
        newlist = input.split(",") #create a list from a string
        results = list(map(int, newlist)) # convert newlist to integers
        print("You entered...", results)
        thelist = results
        print(results)
        print("Our results list is %d long" % len(results))
        print("the overall list is %d long" % len(thelist))



    def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

print("enter a string in the GUI")
app = MyApp()
result = app.mainloop()
print("you entered:", result)
