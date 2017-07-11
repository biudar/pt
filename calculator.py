from Tkinter import *

class Calc():
    def modIt(self):
        firstIterm = self.firstItermEntry.get()
        secondIterm = self.secondItermEntry.get()
        result= firstIterm-secondIterm


    root = Tk()
    root .title("self-running calculator")

    firstItermlabel=Label(width=10)
    firstItermlabel.grid(row=1,column=0)
    firstItermVar = StringVar()
    firstItermEntry =Entry(textvariable=firstItermVar,width=10)
    firstItermEntry.grid(row=1,column=0)
    secondItermlabel = Label(width=10)
    secondItermlabel.grid(row=1, column=3)
    secondItermVar = StringVar()
    secondItermEntry = Entry(textvariable=secondItermVar, width=10)
    secondItermEntry.grid(row=1, column=3)
    resVar = StringVar()
    resEntry = Entry(textvariable=resVar, width=30, state='disabled')
    resEntry.grid(row=1, column=4, columnspan=2)
    calculateItermlabel=Label(width=3)
    
    calculateItermVar = StringVar()
    calculateItermVar.set('minus')


    root.mainloop()


calc = Calc()