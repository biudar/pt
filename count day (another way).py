firstdate=raw_input("""if you want to check how many dates between two dates
please enter you fisrt date(eg.1999.08.11):""")
seconddate=raw_input('then enter your second date(eg.1996.10.08):')
yearstart=int(firstdate[:4])
monthstart=int(firstdate[5:7])
daystart=int(firstdate[-2:])
yearsend=int(seconddate[:4])
monthsend=int(seconddate[5:7])
daysend=int(seconddate[-2:])
yd=yearstart-yearsend
md=monthstart-monthsend
dd=daystart-daysend

def not_enough_month_days(month):
    totalmonth=abs(12-monthstart)+monthsend
    return


def yearnumber(n):
    if n==0:
        day=0
    elif n==1:
        not_enough_month_days()



