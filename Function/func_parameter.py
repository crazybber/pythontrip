#关键字参数

def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
	
person('Bob',30)

person('bob',30,city='beijing')

extra={'city':'beijing','job':'engineer'}

person('jack',24,city=extra['city'],job=extra['job'])

person('jack',24,**extra)

#命名关键字参数

def person_1(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
	    pass
	print('name:',name,'age:',age,'other:',kw)

person_1('jack',24,city='beijing',addr='shanghai',zipcode=12345)

	
	
def person_2(name,age,*,city,job):
	print(name,age,city,job)
	
person_2('jack',24,city='beijing',job='engineer')


def f1(name,sex,age=18,*args,**kw):
	print('name:',name,'gender:',sex,'age:',age,'args:',args,'kw=',kw)
	
def f2(name,sex,age=18,*,other,**kw):
	print('name:',name,'gender:',sex,'age:',age,'other:',other,'kw=',kw)
	
	
pargs=('bob',23,'beijing','live')
kword={'color':'red','shape':'cube','size':'large'}


f1('eamon',20)
f1('eamon','male')
f1('eamon','male',20,'hello','world','100times')

f1('eamon','male',22,*('hello','world','100times'))

f1('eamon','male',23,*('hello','world','100times'),extra='bengbeng')
f1('eamon','male',*pargs,extra='bengbeng')
f1('eamon','male',28,*pargs,extra='bengbeng')
f1('eamon','male',28,*pargs,**kword)


f2('eamon','male',100,other='long time',**kword)

f2('eamon','male',other='long time',**kword)


#more test
def f3(a, b, c = 0, *d, **kw):
    print('a =', a, 'b =', b, 'c =', c ,'d =', d, 'kw =', kw)
args = (1, 2, 3,4,5,99)
kw = {'x': '##'}
f3(*args, **kw)

# 递归函数

def fact(n):
	if n==1:
		return 1		
	return n * fact(n-1)
	
	
print(fact(2))
print(fact(5))
print(fact(100))



def fibonacci(n):
	return fibo_iter(n,1)

def fibo_iter(num,product):
	if num==1:
		return product
	return fibo_iter(num-1,num*product)

print(fibonacci(5))
print(fibonacci(3))

# I I I 
def move_hano(n,a,b,c):
	if n==1:
		print(a,'-->',c)
	else:
		move_hano(n-1,a,c,b)
		move_hano(1,a,b,c)
		move_hano(n-1,b,a,c)

	
 
move_hano(3,'A','B','C')
	