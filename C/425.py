# time
#   UNIX epoch - floating point number of SECONDS since January 1, 1970

import time
now = time.time()
print(now)

start = time.time()
# DO STUFF
#time.sleep(0.5)
end = time.time()
elapsed = end - start
print(elapsed)

current_year = int(now / (60*60*24*365.24) + 1970)
print(current_year)


# datetime
import datetime
from datetime import datetime as dt

# curr = datetime.datetime.now()
curr = dt.now()
print(curr)
print(curr.year)

bd = dt(2019,4,20)
print(bd)

ts = curr - bd
print(ts)
print(ts.days)

print(bd.strftime('%Y/%m/%d'))

# PARSE a string date
# pip install python-dateutil

from dateutil import parser
while True:
    input_str = input('Enter date: ')
    if not input_str:
        break
    date_entered = parser.parse(input_str)
    print(date_entered)


# subprocess

import subprocess
from subprocess import Popen

#Popen('calc.exe')
#proc = Popen(['notepad.exe','423.py'])
proc = Popen(['python.exe','423.py'])
exit_code = proc.wait()
print(exit_code)
