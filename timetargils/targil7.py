import datetime
yesterday= datetime.datetime.now().date()-datetime.timedelta(days=1)
tommorow=datetime.datetime.now().date()+datetime.timedelta(days=1)
print(f"{yesterday}, {datetime.datetime.now().date()}, {tommorow}")