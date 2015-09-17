#fuction
def my_abs(x):
	if not isinstance(x,(float,int)):
		raise TypeError('Bad opend type')
	if x >=0:
		return x
	else:
		return -x
		

print(my_abs(20))

import math

def move(x,y,step,angle=0):
	nx= x+step* math.cos(angle)
	ny= y-step* math.sin(angle)
	return nx ,ny
	
x,y = move(100,100,60,math.pi/6)
print(x,y)

r= move(100,100,60,math.pi/6)
print(r)

def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError('Bad opend type')
	if not isinstance(b,(int,float)):
		raise TypeError('Bad opend type')
	if not isinstance(c,(int,float)):
		raise TypeError('Bad opend type')
	delta = pow(b,2) - 4*a*c
	if delta == 0:
		return -b/(2*a)
	elif delta < 0: 
		return
	else:
		sqrdelta = math.sqrt(delta)
		x1= (-b+sqrdelta)/(2*a)
		x2= (-b-sqrdelta)/(2*a)
		return x1,x2
		
print(quadratic(2,3,1))
print(quadratic(1,3,-4))



def power(x,n=2):
	s=1
	while n> 0:
		n-=1
		s*=x
	return s

print(power(5,2))

def add_end(L=None):
	if L is None:
		L=[]
	L.append('end')
	return L

print(add_end([1,2,4]))
print(add_end(['a','b','c']))


print(add_end())
print(add_end())
print(add_end())

def calc(*numbers):
	sum=0
	for n in numbers:
		sum = sum+n*n
	return sum
	
print(calc(1,2,3))
print(calc(1,3,4,5,6))

print(calc(*(1,3,4,5,6)))
