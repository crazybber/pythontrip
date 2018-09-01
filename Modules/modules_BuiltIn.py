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


from datetime import timezone

tz_utc_8 = timezone(timedelta(hours=8))

now= datetime.now()

print(now)

dt=now.replace(tzinfo=tz_utc_8)

print(dt)

print('------------------------')
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)

print(utc_dt)

bjtm=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bjtm)

tokyo_tm=bjtm.astimezone(timezone(timedelta(hours=9)))
print('------------------------')
print(tokyo_tm)



import re


def to_timestamp(dt_str,tz_str):
	tz_fmt_str='^UTC([+-]\d{1,2})\:\d{2}$'
	tm_fmt=re.match(tz_fmt_str,tz_str)
	if tm_fmt:
		tz_hours=int(tm_fmt.group(1))
		cur_datetime=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
		return cur_datetime.replace(tzinfo=timezone(timedelta(hours=tz_hours))).timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

print('Pass')
