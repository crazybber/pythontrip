#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'


'Modules Built-In'


from datetime import datetime

now = datetime.now()
print(now)
print(type(now))


dt=datetime(2015,10,5,20,1,20)

print(dt)
print(dt.timestamp())

t=1444046480.0

print(datetime.fromtimestamp(t))

print(datetime.utcfromtimestamp(t))


cday=datetime.strptime('2015-10-05 20:07:59','%Y-%m-%d %H:%M:%S')

print(cday)


now=datetime.now()
print(now.strftime('%a,%b,%d %H:%M'))

from datetime import timedelta

now = datetime.now()
print(now)

# datetime.datetime(2015,10,05,20,12,58,10054)

print(now+timedelta(hours=10))
