#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__='eamon'

'multi process'

import os

def forktest():
	print('Process (%s) start.. ' % os.getpid())

	returnpid=os.fork()

	if pid==0:
		print('i am child proecess (%s) and my parent is %s' % (os.getpid(),os.getppid()))
	else:
		print('I (%s) just created a child process (%s).' % (os.getpid(), returnpid))
		


from multiprocessing import Process
import os,time,random

def run_proc(name):
	print('run child process %s (%s)' % (name,os.getpid()))

if __name__ == '__main__':
	print('parent process %s' % os.getpid())
	p=Process(target=run_proc,args=('test',))
	print('Child Procee will Start.')
	p.start()
	p.join()
	print('Child Process end.')
	
	