#!/usr/bin/env python3
# -*- coding utf-8 -*-

'a test template class(meta class)'

__authot__ = 'Eamon chen'



from enum import Enum,unique

Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name,member  in Month.__members__.items():
	print(name,'=>',member,',',member.value)
	


@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
	
	
print(Weekday.Mon)

print(Weekday['Tue'])
print(Weekday['Tue'].value)
print(Weekday(2))


for name,member in Weekday.__members__.items():
	print(name,'=>',member)
	
	
class Hello(object):
	def hello(self,name='world'):
		print('Hello,%s.' % name)		
		
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['add']=lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
	pass
	
	
L=MyList()
L.add(1)
L.add(2)
print(L)