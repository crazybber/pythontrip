#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'


'Regular Expression!'


import re

test= 'user input'

if re.match(r'regular pattern',test):
	print('OK')
else:
	print('Failed')
	
	
r='a b     c'.split(' ')

print(r)


r=re.split(r'\s+','a b   c')

print(r)

r=re.split(r'[\s;,]+','a, ,;;b;,   c')

print(r)

r=re.match(r'^(\d{3})-(\d{3,8})$','010-123456')

print(r.group(0))

#MATCH TIME 
t='17:56:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)

r=m.groups()

print(r)

# MATCH DATA
t='^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'

r=re.match(t,'12-03')

print(r)


# layz mode

r=re.match(r'^(\d+)(0*)$','1023000').groups()
print(r)


r=re.match(r'^(\d+?)(0*)$','1023000').groups()
print(r)

re_tel=re.compile('^(\d{3})-(\d{3,8})$')

r=re_tel.match('021-123456').groups()
print(r)

emailregex='^\w(\w?[\.\-\_]?){1,5}@gmail.com$'

re_telgmal=re.compile(emailregex)

mail='a.d_e10@gmail.com'

r=re_telgmal.match(mail)

print(r)

print(r.groups())

if r:
	print("OK")
else:
	print('not OK')
	
	
emailregexwithname='^(<\w+\s\w+>)\s+\w+(?:[.-_]\w+)?@gmail.com$'

re_telgmal=re.compile(emailregexwithname)

mail='<tony wen> a.d_e10@gmail.com'

r=re_telgmal.match(mail)

print(r)


if r:
	print("OK")
else:
	print('not OK')