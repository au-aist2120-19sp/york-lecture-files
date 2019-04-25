# time
import time

# epoch - unix standard time representation
#   float number of seconds since January 1, 1970

print(time.time())

start = time.time()
#time.sleep(1)
end = time.time()

elapsed = end - start
print(elapsed)

year = round(end / (60*60*24*365.24)) + 1970
print(year)


# datetime
import datetime
from datetime import datetime as dt

#print(dt.now().timestamp())
current_date = dt.now()
print(current_date)
print(current_date.year)
bd = dt(2019, 4, 20)
print(bd)

since = current_date - bd
print(since)

purty = current_date.strftime('%B %d, %Y at %I:%M %p')
print(purty)

from dateutil import parser

while True:
    timestr = input('enter a date: ')
    if not timestr:
        break
    adate = parser.parse(timestr)
    print(adate)


# subprocess - RUN STUFF!!

from subprocess import Popen as po

# po('calc.exe')
# po(['notepad.exe', '423.py'])

proc = po('calc.exe')
code = proc.wait()
print(code)

proc = po(['python.exe','423.py'])
code = proc.wait()
print(code)
