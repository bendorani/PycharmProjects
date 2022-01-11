import datetime
now=datetime.date.today()
i=1
while i<=5:
    print(now)
    now=datetime.date.today()+datetime.timedelta(days=i)
    i+=1