import calendar
from datetime import date
import datetime
today = date.today()
now = datetime.datetime.now()
yy = int(today.strftime("%Y"))   # year
mm = int(today.strftime("%m"))   # month
DD = int(today.strftime("%d"))   # date
print(calendar.month(yy, mm))
print(f'today : {DD}  {now.strftime("%A")}')
