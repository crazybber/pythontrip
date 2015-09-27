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
		


from multiprocessing import Process,Queue
from multiprocessing import Pool
import os,time,random

def run_proc(name):
	print('run child process %s (%s)' % (name,os.getpid()))

def testCreatProc():
	if __name__ == '__main__':
		print('parent process %s' % os.getpid())
		p=Process(target=run_proc,args=('test',))
		print('Child Procee will Start.')
		p.start()
		p.join()
		print('Child Process end.')
	
	                 
	
def long_time_task(name):
	print('run task %s (%s) ...' % (name,os.getpid()))
	start=time.time()
	time.sleep(random.random()*3)
	end=time.time()
	print('Task %s run %0.2f seconds.' % (name,(end-start)))
	
	
	
def testProceessPool():
	if __name__ =='__main__':
		print('Parent process  %s.' % os.getpid())
		p=Pool(4)
		for i in range(5):
			p.apply_async(long_time_task,args=(i,))
		print('waiting for all subprocesses done...')
		p.close()
		p.join()
		print('All subProcess done.')
		
		
# testProceessPool()



import subprocess

def testuseSubProcess():
	print ('$ nslookup www.python.org')
	r=subprocess.call(['nslookup','www.python.org'])
	print('Exit code:',r)

# testuseSubProcess()


def testSubProcessCommunicate():
	print('$ nslookup')
	p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('utf-8'))
	print('Exit code:',p.returncode)
	
	
# testSubProcessCommunicate()


def write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A','B','C']:
		print('put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read %s' % os.getpid())
	while True:
		value =q.get(True)
		print('Get %s from queue.' % value)
	
	
	
def testProceeReadWrite():
	if __name__ == '__main__':
		q=Queue()
		pw=Process(target =write,args=(q,))
		pr=Process(target=read,args=(q,))
		pw.start()
		pr.start()
		pw.join()
		pr.terminate()
		
		
testProceeReadWrite()