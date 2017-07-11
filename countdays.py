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

firstdate=raw_input("""if you want to check how many years between two dates
please enter you fisrt date(eg.1999.08.11):""")
seconddate=raw_input('then enter your second date(eg.1996.10.08):')
yearstart=int(firstdate[:4])
monthstart=int(firstdate[5:7])
daystart=int(firstdate[-2:])
yearsend=int(seconddate[:4])
monthsend=int(seconddate[5:7])
daysend=int(seconddate[-2:])

days1=countyearsdays(yearstart)+countmonthsdays(yearstart,monthstart)+daystart
days2=countyearsdays(yearsend)+countmonthsdays(yearsend,monthsend)+daysend

raw_input('days between this two dates=')
print abs(days1-days2)


