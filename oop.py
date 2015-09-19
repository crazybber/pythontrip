#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'Object Oriented Programming'


std1={'name':'Eamon','Score':99}
std2={'name':'chen','Score':100}

def print_score(std):
    print('%s: %s' % (std['name'], std['Score']))
	
	
print_score(std1)
print_score(std2)
	
class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s: %s' %(self.__name,self.__score))
	
	def get_grade(self):
		if self.__score >=90:
			return 'A'
		elif self.__score >=60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name


eamon= Student('eamon',99)
chen = Student('chen',100)

eamon.print_score()
chen.print_score()

class TestStudent(object):
    pass

tstStud = TestStudent()
print(tstStud)

tstStud.name = 'eamon_tst'

print(tstStud.name)

eamon.get_grade()

eamon.age = 10

print(eamon.age)


bart =Student('Babie cart',98)

bart.print_score()

# print(bart.__name) // Private var
print(bart._Student__name)




#inherit and multibehavior

class Animal(object):
	def run(self):
		print('Animal is running')
	def eat(self):
		print('Animal is eating')

class Dog(Animal):
	pass
	
class Cat(Animal):
	def run(self):
		print('cat is running')
	def eat(self):
		print('cat is eating')

	

dog = Dog()

dog.run()

cat = Cat()

cat.eat()

r= isinstance(cat ,Cat)
print(r)


def run_twice(animal):
	animal.run()
	animal.run()

run_twice(dog)


class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')
		

run_twice(Tortoise())

#duck like object 
class Timer(object):
	def run(self):
		print('timer is ticking  and tocking')
		
		
		
run_twice(Timer())