
#分布式并行计算

def f(x):
	return x*x

r= map(f,[1,2,3,4,5,6])


print(list(r))

from functools import reduce

def add(x,y):
	return x+y

r=reduce(add,[1,3,5,7,9])

print(r)

def fn(x,y):
	return x*10+y
	
r= reduce(fn,[1,3,5,7,9])
print(r)

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

r=reduce(fn,map(char2num,'13579'))
print(r)

def string2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))
	
r= string2int("24342")
print(r)


def string2int_lambda(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(lambda x,y:x*10+y,map(char2num,s))
	
r= string2int("2346904342")
print(r)

#exicese

L1=['adam', 'LISA', 'barT']

def normalize(str):	
	return str[0].upper()+	str[1:].lower()

L2=list(map(normalize,L1))
print(L2)


def prod(L):
	return reduce(lambda x,y:x*y,L)
	
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

print('123.456')


def str2float(str):
	def char2num(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
	L=str.split('.')
	x1=reduce(lambda x,y:x*10+y,map(char2num,L[0]))
	x2=reduce(lambda x,y:x*0.1+y,map(char2num,reversed(L[1])))	
	return x1+x2*0.1
s=str2float('123.456')
print(s)	



#filter 

def is_odd(n):
	return n%2==1

L=list(filter(is_odd,[1,2,3,4,56,7,8]))
print(L)


def not_empty(s):
	return s and s.strip()
	
L=list(filter(not_empty,['a',' ','B',None,'C']))

print(L)

print(list(filter(not_empty,'A B C DE')))

#求素数


def _odd_iter():
	n=3
	while True:
		yield n
		n+=2
		
 
def _not_divisible(n):
	return lambda x:x%n >0


	
def primes():
	yield 2
	it=_odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(_not_divisible(n),it)
		
for n in primes():
	if n < 100:
		print(n)
	else:
		break

		
f=_odd_iter()
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))


it=_odd_iter()
print(it)
it = filter(_not_divisible(n), it)
print(it)
print(next(it))
print(it)
print(next(it))
print(next(it))
print(next(it))

#sss

s="abcde"
print(s[::-1])

def is_palindrome(n):
	s=str(n)
	return s[::-1] == s

output = filter(is_palindrome, range(1, 1000))
print(list(output))



L=sorted([2,34,578,1,25,7,9])
print(L)

L=sorted([2,34,578,-1,-25,-7,9])
print(L)

L=sorted([2,34,578,-1,-25,-7,9],key=abs)
print(L)

L=sorted(['eamon','chen','bob','Helo','Tom'])
print(L)

L=sorted(['eamon','chen','bob','Helo','Tom'],key=str.lower)
print(L)

L=sorted(['eamon','chen','bob','Helo','Tom'],reverse=True)
print(L)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L=sorted(L,key=lambda x:x[0].lower())
print(L)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L=sorted(L,key=lambda x:x[1])
print(L)