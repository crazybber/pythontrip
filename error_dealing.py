#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'error dealing'

def func():
	try:
		print('try...')
		r=10.0/0
		print('result:',r)
	except ZeroDivisionError as e:
		print("exception:",e)
	finally:
		print('finally..')
	print('End')
	
	
func()


def ErroDemo():
	try:
		print('try...')
		r=10.0/0
		print('result:',r)
	except ValueError as e:
		print('value error',e)
	except ZeroDivisionError as e:
		print("exception:",e)
	else:
		print('no error')
	finally:
		print('finally..')
	print('End')

ErroDemo()

#错误处理可以分层次捕获

def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	bar('0')
	
	
# main()


import logging

def foo1(s):
	return 10/int(s)
def bar1(s):
	return foo1(s)*2
def main1():
	try:
		bar1('0')
	except Exception as e:
		logging.exception(e)
	print('end')

main1()



class FoolError(ValueError):
	pass
	
def foo2(s):
	n = int(s)
	if n== 0:
		raise FoolError('invalid value: %s' %s)
	return 10/n
		
# foo2('0')

print('end')


def foo3(s):
	n = int(s)
	if n==0:
		raise ValueError('invalid value: %s' % s)
	return 10 % n

def bar3():
	try:
		foo3('0')
	except ValueError as e:
		print('ValueError')
		raise
	
# bar3()


def foo4(s):
	n= int(s)
	assert n!=0,'n is zero'
	return 10/n
	
# foo4('0')
import pdb
logging.basicConfig(level=logging.INFO)

pdb.set_trace()

s='0'
n=int(s)
# logging.info('n=%d' % n)
print(10/n)
