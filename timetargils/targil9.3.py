import datetime
date=input("enter date: ")
print(datetime.datetime.strptime(date,"%d %B %Y"))