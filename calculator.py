from Tkinter import *

class Calc:
    def __init__(self):
        self.gui()


    def gui(self):
        root = Tk()
        root.title('IT calculator')
        self.resVar = StringVar()
        self.resEntry = Entry(textvariable=self.resVar, width=20, state='disabled')
        self.resEntry.grid(row=1, column=4, columnspan=2)
        self.firstItemLabel = Label(text='number:', width=10)
        self.firstItemLabel = Label(width=10)
        self.firstItemLabel.grid(row=1, column=0)
        self.firstItemVar = StringVar()
        self.firstItemEntry = Entry(textvariable=self.firstItemVar, width=10)
        self.firstItemEntry.grid(row=1, column=1)
        self.secondItemLabel = Label( width=10)
        self.secondItemLabel.grid(row=1, column=2)
        self.secondItemVar = StringVar()
        self.secondItemEntry = Entry(textvariable=self.secondItemVar, width=10)
        self.secondItemEntry.grid(row=1, column=3)
        self.modButton = Button(width=5)
        self.modButton.grid(row=1, column=2)

        root.mainloop()
        return 0

calc = Calc()