#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'IO Program'

try:
	f=open('E:/Codes/Python/learnpython/IO/test.txt','r')
	t=f.read()
	print(t)
finally:
	f.close()


with open('./test.txt') as f:
	print(f.read())

	
	
#binary files:

# with open('E:\Codes\Python\learnpython\IO\img.jpg','rb') as img:
	# r=img.read()
	# print(r)

	
with open('E:\Codes\Python\learnpython\IO\gbk.txt','r',encoding='gbk') as f:
	r=f.read()
	print(r)
	
	
with open('.\\test.txt','w') as f:
	r=f.write("hello lines222")
	
	

# with open('./img.jpg','rb') as f2:
	# for line in f2.readlines():
		# print(line.strip())
		
		
from io import StringIO

f = StringIO()
f.write('hello')
f.write('----')
f.write('world')
print(f.getvalue())


f = StringIO('Hello\nHi!\nGoodBye!')

while True:
	s=f.readline()
	if s=='':
		break
	print(s.strip())

from io import BytesIO
f=BytesIO()
f.write('中国'.encode('utf-8'))
print(f.getvalue())


f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
r=f.read()
print(r)


import os

print(os.name)

# print(os.uname())
print(os.environ)
print(os.environ.get('path'))

print(os.environ.get('x','Eamon'))

r=os.path.abspath('.')
print(r)

r=os.path.join('.','testdir')

print(r)

# os.mkdir('./testdir')

# os.rmdir('./testdir')

r=os.path.split('E:\Codes\Python\learnpython\IO\IO_Stream.py')

print(r)

# os.rename('test.txt','test.py')
# os.remove('test.py')


r=[x for x in os.listdir('.') if os.path.isdir(x)]
print(r)