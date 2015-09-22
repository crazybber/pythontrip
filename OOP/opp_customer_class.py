#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'


'customer class'

class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return ('student object:(name: %s)' % self.name)
	__repr__ = __str__
	
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr =='age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		
print(Student('eamon'))

s=Student('eamon')


class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
		
	def __next__(self):
		self.a,self.b = self.b, self.a+self.b
		if self.a > 100:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			if stop is None:
				raise ValueError('you need set a end value')
			if start is None:
				start=0
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b
			return L

for n in Fib():
	print(n)
	
print(Fib()[4])
	
f=Fib()

print(f[0:5])

print(f[:10])

print(f[2:9:2])


print(s.name)

print(s.score)

print(s.age())

# s.xyz


class Chain():
	def __init__(self,path=''):
		self._path=path
	def __getattr__(self,path):
		if path=='user':
			return lambda name:Chain('%s/user/:%s' % (self._path,name))
		else:
			return Chain('%s/%s' % (self._path,path))	
	def __str__(self):
		return self._path
	__repr__ = __str__
	def __call__(self):
		print('My Name is %s.' % self.name)
		
		
# def user(self,username):
# return Chain('%s/user:%s' % (self._path,username))	
	
	
# r=Chain().status.user.timeline.list

# print(r)

r=Chain('eamon')

print(r())

t=callable(Student("eamon"))
print(t)
t=callable(Chain())
print(t)
t=callable('123')

print(t)
	
r=Chain().status.user('eamon').timeline.list

print(r)



class Chain1(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		if path == 'usr':
			return lambda usrname : Chain('%s/:%s' % (self._path, usrname))
		else:
			return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__
	

res=Chain1().status.user('eamon').timeline.list

print(res)