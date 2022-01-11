# import datetime
# daytime=datetime.date.today()
# print(f"{daytime} 00:00:00")
from datetime import date
from datetime import datetime
dt = date.today()
print(datetime.combine(dt, datetime.min.time()))
