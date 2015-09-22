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


# ORM Framework test

# class User(Model):
	# id=IntegerField('id')
	# name=StringField('username')
	# eamail=StringField('eamail')
	# password=StringField('password')
	
	
# u = User(id=1234,name='Eamon',eamail='test@orm.me',password='my-pwd')

# u.Save()



class Field(object):
	def __init__(self,name,colum_type):
		self.name=name
		self.colum_type=colum_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.name__,self.name)
	

class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')
		
class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name,'bigint')
		
		
# class ModelMetaclass(type):
	# def __new__(cls,name,bases,attrs):
		# if name == 'Model':
			# return type.__new__(cls,name,bases,attrs)
		# print('Found model:%s' % name)
		# mappings= dict()
		# for k,v in attrs.items():
			# if isinstance(v,Field):
				# print(foun)
				
s=StringField('name')

print(dir(s))