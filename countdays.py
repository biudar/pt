
from Tkinter import *

def two_dates():

    def is_366_or_365(n):
        if n%4==0 and n%100!=0 or n%400==0:
            return 366
        else:
            return 365

    def countmonthsdays(years,months):
        a =is_366_or_365(years)
        if a==365:
            if months==1:
                days=0
            elif months==2:
                days=31
            elif months==3:
                days=31+28
            elif months==4:
                days=31+28+30
            elif months==5:
                days=31+28+30+31
            elif months==6:
                days=31+28+30+31+30
            elif months==7:
                days=31+28+30+31+30+31
            elif months==8:
                days=31+28+30+31+30+31+30
            elif months==9:
                days=31+28+30+31+30+31+30+31
            elif months==10:
                days=31+28+30+31+30+31+30+31+30
            elif months==11:
                days=31+28+30+31+30+31+30+31+30+31
            elif months==12:
                days=31+28+30+31+30+31+30+31+30+31+30
            return days
        elif a==366:
            if months==1:
                days=0
            elif months==2:
                days=31
            elif months==3:
                days=31+29
            elif months==4:
                days=31+29+30
            elif months==5:
                days=31+29+30+31
            elif months==6:
                days=31+29+30+31+30
            elif months==7:
                days=31+29+30+31+30+31
            elif months==8:
                days=31+29+30+31+30+31+30
            elif months==9:
                days=31+29+30+31+30+31+30+31
            elif months==10:
                days=31+29+30+31+30+31+30+31+30
            elif months==11:
                days=31+29+30+31+30+31+30+31+30+31
            elif months==12:
                days=31+29+30+31+30+31+30+31+30+31+30
            return days

    def countyearsdays(years):
        yearlist=range(1,years)
        yeardays=0
        for year in yearlist:
            yeardays +=is_366_or_365(year)
        return yeardays

    def start_end_day(datestart='2017.07.11',dateend='2017.07.10'):
        datestartlist=datestart.split('.')
        firstdate=start_var.get()#raw_input("""if you want to check how many years between two dates
        #please enter you fisrt date(eg.1999.08.11):""")
        seconddate=end_var.get()#raw_input('then enter your second date(eg.1996.10.08):')
        yearstart=int(datestartlist[0])
        monthstart=int(datestartlist[1])
        daystart=int(datestartlist[2])
        dateendlist=dateend.split('.')
        yearsend=int(dateendlist[0])
        monthsend=int(dateendlist[1])
        daysend=int(dateendlist[2])

        print 'start:', yearstart, monthsend, daystart
        print 'end:', yearsend, monthsend, daysend
        return yearstart, monthstart, daystart, yearsend, monthsend, daysend

    def count_final():
        start = start_var.get()
        end = end_var.get()
        yearstart, monthstart, daystart, yearsend, monthsend, daysend = start_end_day(start, end)

        if yearstart == yearstart:
            if monthsend == monthstart:
                days = abs(daysend - daystart)
            else:
                days = countmonthsdays(yearsend, monthsend) + daysend - countmonthsdays(yearstart,monthstart) - daystart
        else:
            days = countyearsdays(yearsend) + countmonthsdays(yearsend, monthsend) + daysend - countyearsdays(
                yearstart) - countmonthsdays(
                yearstart, monthstart) - daystart
        result_var.set(abs(days))
        print days
        return abs(days)

    lable_width = 15
    entry_width = 25
    button_width = lable_width + entry_width
    root = Tk()
    root.title('Count Your Days')
    info = Label(root, text="you may entery you dates", width=button_width)
    info.grid(row=0, column=0, columnspan=2)
    start_info = Label(root, text="date start:", width=lable_width)
    start_info.grid(row=1, column=0)
    start_var = StringVar()
    start_var.set('2017.07.11')
    start_Entry = Entry(root, width=entry_width, textvariable=start_var)
    start_Entry.grid(row=1, column=1)
    end_info = Label(root, text="date end:", width=lable_width)
    end_info.grid(row=2, column=0)
    end_var = StringVar()
    end_var.set('2017.07.10')
    end_Entry = Entry(root, width=entry_width, textvariable=end_var)
    end_Entry.grid(row=2, column=1)

    submit_button = Button(text='Count Days', command=count_final, width=button_width)
    submit_button.grid(row=4, column=0, columnspan=2)
    res_info = Label(root, text="total days:", width=lable_width)
    res_info.grid(row=6, column=0)
    result_var = StringVar()
    result_Entry = Entry(root, width=entry_width, textvariable=result_var, state='disabled')
    result_Entry.grid(row=6, column=1)
    root.mainloop()

if __name__ == '__main__':
    two_dates()