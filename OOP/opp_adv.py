#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'


#using __slots__

class Student(object):
	__slots__=('name','age','set_age','score','sscore')
	
s= Student()
s.name='Eamon'
print(s.name)


def set_age(self,age):
	self.age=age
	

from types import MethodType

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

def set_score(self,score):
	self.score=score
	
def get_score(self):
	return self.score
	
Student.set_score=MethodType(set_score,Student)

Student.get_score=MethodType(get_score,Student)
	
s.age=25	
s.set_score(100)
print(s.score)                                                                                                                              
s3= Student()
s3.name ='Eamon'

s.sscore = 100
v=s.get_score()
print(v)
print(s.name)
print(s.age)

class GrandStudent(Student):
	pass
	
s4= GrandStudent()

s4.score = 99

print(s4.score)


class Stu(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value < 0 or value >100:
			raise ValueError('score must between 0~100')
		self._score =value
		
	@property
	def birth(self):
		return self._birth
		
	@birth.setter
	def birth(self,value):
		self._birth=value
		
	@property
	def age(self):
		return 2016-self._birth
		

s=Stu()
s.score=99

r= s.score
print(r)

s.birth=1986

print(s.birth)

print(s.age)






class Screen(object):
	
	@property
	def height(self):
		return self._height
	
	@height.setter
	def height(self,value):
		self._height = value
	
	@property
	def width(self):
		return self._width
	
	@height.setter
	def width(self,value):
		self._width = value
	
	@property
	def resolution(self):
		return self._width* self._height
		
		
scrn= Screen()

scrn.width =100
scrn.height=500

print(scrn.resolution)


	