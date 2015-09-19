#!/usr/bin/env python3
# -*- coding utf-8 -*-


__Author__ ='eamon'


print(type(123))

import types

def fn():
	pass
	
print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

a=lambda x:x*x
print(type(a) == types.LambdaType)

t= (x for x in range(10))

print(type(t) == types.GeneratorType)



v= isinstance([1,2,3],(list,tuple))


print(v)



print(dir('ABC'))
print('----------------------------')
print('----------------------------')
print(dir(list))



class mypet(object):
	def __len__(self):
		return 100
		
print('----------------------------')	
print(len(mypet()))


class Myobject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x

obj= Myobject()

r = hasattr(obj,'x')
print(r)

r=hasattr(obj,'y')
print(r)

setattr(obj,'y',19)
r=hasattr(obj,'y')
print(r)


r= getattr(obj,'x')

print(r)


# getattr(obj,'z') will thor exception

r= hasattr(obj,'power')
print(r)

fn=getattr(obj,'power')

print(fn())


class Student(object):
	name='Student'

s= Student()

print(s.name)

s.name ='Eamon'

print(s.name)

print(Student.name)

del s.name

print(s.name)