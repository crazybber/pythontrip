#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'Collections..'

from collections import namedtuple

Point=namedtuple('point',['x','y'])
p=Point(1,2)
print(p)

check=isinstance(p,Point)

print(check)

from collections import deque

q=deque(['a','b','c'])

q.append('x')
q.appendleft('y')

print(q)


# defaultdict

from collections import defaultdict

dd = defaultdict(lambda:'N/A')

dd['key1']='abc'

print(dd['key1'])
print(dd['key2'])


from collections import OrderedDict

d= dict([('a',1),('c',3),('b',2)])

print(d)

od=OrderedDict([('a',1),('c',3),('b',2)])


print(od)


od=OrderedDict()
od['z']=1
od['x']=2
od['y']=3

print(list(od.keys()))


class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self,capacity):
		super(LastUpdatedOrderedDict,self).__init__()
		self._capacity=capacity
		
	def __setitem__(self,key,value):
		containsKey= 1 if key in self else 0
		if len(self) - containsKey > self._capacity:
			last = self.popitem(last=False)
			print('remove',last)
		if containsKey:
			del self[key]
			print('set:',(key,value))
			
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)
		
		
tdict=LastUpdatedOrderedDict(3)

tdict[1]='a'
tdict[2]='b'
tdict[3]='c'
print(tdict)

tdict[4]='d'
tdict[5]='e'



from collections import Counter

c=Counter()

for ch in 'Programming':
	c[ch]+=1

print(c)