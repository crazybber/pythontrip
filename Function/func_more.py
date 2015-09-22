#return function
def calc_sum(*args):
	ax=0
	for n in args:
		ax+=n
	return ax
	
	
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax+=n
		return ax
	return sum
	
f=lazy_sum(1,3,5,7,9)

print(f)

print(f())

f1=lazy_sum(1,3,5,7,9)
print(f1)
f2=lazy_sum(1,3,5,7,9)
print(f2)

#closure

def count():
	fs=[]
	for i in range(1,4):
		def f(j=i):
			return j*j
		fs.append(f)
	return fs
	
f1,f2,f3 = count()

print(f1())
print(f2())
print(f3())


def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
	
f4,f5,f6 = count1()

print(f4())
print(f5())
print(f6())

def count2():
	def f(j):
		return lambda :j*j
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
	
f7,f8,f9 = count2()

print(f7())
print(f8())
print(f9())

# unamed function

L=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))

print(L)

f=lambda x:x*x

print(f)

print(f(5))

def buid(x,y):
	return lambda:x*x+y*y
	
f= buid(3,4)
print(f)
print(f())



def count3():
	fs=[]
	for i in range(1,4):
		def f(i):
			return lambda:i*i
		fs.append(f(i))
	return fs
	
f11,f22,f33 = count3()

print(f11())
print(f22())
print(f33())


#decoration

def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper

	
import functools

def log1(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
	


@log1('execute')
def now():
	print('2015-09-19')
		
f=now

f()
print(f.__name__)

	
now()



