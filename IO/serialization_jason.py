#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'Serialization'

import pickle

d=dict(name='bob',age='28',score='99')

r= pickle.dumps(d)

print(r)

with open('dump.txt','wb') as f:
	pickle.dump(d,f)

with open('dump.txt','rb') as f:
	d=pickle.load(f)
	print(d)
	
import json

r=json.dumps(d)
print(r)

json_str='{"age":20,"score":99,"name":"eamon"}'

r= json.loads(json_str)
print(r)


class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('Eamon',20,29)

# print(json.dumps(s))


def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
	
	
print(json.dumps(s,default=student2dict))


print(json.dumps(s,default= lambda obj:obj.__dict__))


def dict2Student(d):
	return Student(d['name'],d['age'],d['score'])
	
o=json.loads(json_str,object_hook=dict2Student)	
print(o)