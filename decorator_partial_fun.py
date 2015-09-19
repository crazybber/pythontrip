#decorator and partial function


import functools
from collections import Iterable

def log(content = None):
	if content == None:
		def Decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('begin call')
				print('function name: %s' %  func.__name__)
				func(*args,**kw)
				print('end call')
			return wrapper
		return Decorator	
	else:
		def Decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('begin call')
				print('function name: %s log %s' %  (func.__name__, content))
				func(*args,**kw)
				print('end call')
			return wrapper
		return Decorator
	

def log1(content = None):
	def Decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call')
			if content==None:
				print('function name: %s' %  func.__name__)
			else:
				print('function name: %s log %s' %  (func.__name__, content))
			fn=func(*args,**kw)
			print('end call')
			return fn
		return wrapper
	return Decorator


def log3(func):
	if not isinstance(text,Iterable):
		def Decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('begin call')
				print('function name: %s' %  func.__name__)
				func(*args,**kw)
				print('end call')
			return wrapper
		return Decorator	
	else:
		def Decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('begin..')
				print('function name: %s log: %s' %  (func.__name__,text))
				func(*args,**kw)
				print('end...')		
			return wrapper
		return Decorator


def log4(inargs):
#无参数类型
# now = log(now)
	if isinstance(inargs,Iterable):
		@functools.wraps(inargs)
		def Decorator_1(*args,**kw):
			print('begin call')
			print('function name: %s' %  inargs.__name__)
			inargs(*args,**kw)
			print('end call')
		return Decorator_1
	#有参数类型
	else:
	# now = log('execute')(now)
		def Decorator_2(func):
			def wrapper(*args,**kw):
				print('begin..')
				print('function name: %s log: %s' %  (func.__name__,inargs))
				func(*args,**kw)
				print('end...')		
			return wrapper
		return Decorator_2
			

import functools
from collections import Iterable

def log5(inArgs):
#带参数的函数
    def Decorator_withPara(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            print('decorator_function with parameter')
            print('args:',inArgs)
            fn(*args,**kw)
        return wrapper
#无参数的函数
    @functools.wraps(inArgs)
    def Decorator_withoutPara(*args,**kw):
        print('decorator_function without parameter')
        print('args:',args)
        inArgs(*args,**kw)

    if isinstance(inArgs,Iterable):
        return Decorator_withPara
    else:
        return Decorator_withoutPara

		
@log5('22222')
def now1():
	print('2015-09-19-now1')

@log5
def now2():
	print('2015-09-19-now2')
	
now1()
print('function name:',now1.__name__)
now2()
print('function name:',now2.__name__)


#偏函数12

def int2(x,base=2):
	v=int(x,base)
	print(v)
# 23	22222222222222222222222222222222222222222222222222222222
int2('100000')
int2('10101010')


import functools
int22= functools.partial(int,base=2)

v=int22('100000')
print(v)
v=int22('1010101')
print(v)