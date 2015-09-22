#advanced feature

L=[]
n=1
while n<=99:
	L.append(n)
	n+=2
print(L)

L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[1])
print(L[2]) 
print(L[3])

print(L[0:3])

r = []
k = 3
for i in range(k):
	r.append(L[i])
print(r)

print(L[-1])
print(L[-2])
print(L[-2:-1])


print('key value------')
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
for key in d.values():
	print(key)	
print('key value------')
	
for ch in 'ABCD':
	print(ch)

from collections import Iterable

print(isinstance('abc',Iterable))

for i, value in enumerate(['A','B','C']):
	print(i,value)


	
	
# list generate
print('---------------------------generate')

L=[]
L= list(range(1,11))
print(L)

L= list(range(10))
print(L)

L=[x*x for x in range(1,11)]
print(L)

import os
L=[d for d in os.listdir('.')]
print(L)


d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'=',v)

L=[k+'='+v for k,v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
 
L= [s.lower() for s in L]
print(L)


L = ['Hello', 'World', 18, 'Apple', None]
 
L=[s.lower() for s in L if isinstance(s,str)]
print(L)

g=(x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))


for n in g:
	print(n)

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b,a+b
		n+=1
	return 'done'

print(fib(6))


def fib_gen(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n+=1
	return 'done'

print(fib_gen(6))

def odd():
	print('step1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield 5

o=odd()
print(next(o))
print(next(o))
print(next(o))

# for n in fib(10):
	# print(n)
print("-------------------")
for n in fib_gen(10):
	print(n)

print("-------------------")

g=fib_gen(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return vaule:',e.value)
		break

	
# -*- coding: utf-8 -*-
print('triangles')

# def tlist(n):
	# if n==1:
		# return [1]
	# else:
		# t=tlist[n-1]
		# L=[]
		# for k in range(n):
			# if k==0 or k==n-1:
				# L.append(1)
			# else:
				# L.append(t[k]+t[k-1])
		# return L	
		
		
		


# def triangles(n):
	# for n in range(n):
		# print(tlist(n))	
	
# triangles(2)


def triangles(n):
	L=[1]
	count=0
	while True:
		if count == n:
			return None
		yield(L)
		L.append(0)
		L=[L[i-1]+L[i] for i in range(len(L))]	
		count+=1
		
for i in triangles(10):
	print(i)

g=triangles(9)	
print(g)

L=[1,2,3,4,5,6]
print(L)
print(L[2:])
print(L[1:3])
print(sum(L[1:3]))


#迭代器和迭代对象

it = iter([1,2,2,4,45])

while True:
	try:
		x= next(it)
		print(x)
	except StopIteration:
		break
		
