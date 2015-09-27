#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__='eamon'

'threading multithreading '


import time,threading

def loop():
	print('thread %s is running ...' % threading.current_thread().name)
	n=0
	while n <5:
		n+=1
		print('thread %s >> %s ' %(threading.current_thread().name,n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)

def testThread():
	print('thread %s is running..' % threading.current_thread().name)
	t=threading.Thread(target=loop,name='LoopThread')
	t.start()
	t.join()
	print('thread % s ended.' % threading.current_thread().name)

# testThread()

balance =0
def change_it(n):
	global balance
	balance =balance +n
	balance =balance -n
	
lock = threading.Lock()
def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()
		
		
	
def testMultiThreadDanger():
	t1= threading.Thread(target=run_thread,args=(5,))
	t2= threading.Thread(target=run_thread,args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(balance)
	
	
# testMultiThreadDanger()

import threading,multiprocessing

def loop():
	x=0
	while True:
		x=x^1

def testRunfullCPU():
	print('cpu num:',multiprocessing.cpu_count())		
	for i in range(multiprocessing.cpu_count()):
		t=threading.Thread(target=loop)
		t.start()
		
		
		
