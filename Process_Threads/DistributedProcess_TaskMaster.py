#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'Distribute Process!'

import random,time,queue

from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager


taskSend_queue=queue.Queue()
taskReceive_queue = queue.Queue()


class QueueManager(BaseManager):
	pass


def return_taskSend_queue():
	return taskSend_queue

def return_taskreceive_queue():
	return taskReceive_queue

def testServer():
	# QueueManager.register('task_send_queue',callable=lambda:taskSend_queue)
	# QueueManager.register('task_receive_queue',callable=lambda:taskReceive_queue)
	# QueueManager.register('task_send_queue',callable=taskSend_queue)
	# QueueManager.register('task_receive_queue',callable=taskReceive_queue)
	QueueManager.register('task_send_queue',return_taskSend_queue)
	QueueManager.register('task_receive_queue',return_taskreceive_queue)


	manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
	manager.start()

	sendtask=manager.task_send_queue()
	receivetask=manager.task_receive_queue()

	for i in range(10):
		n = random.randint(0,10000)
		print('Put task %d ..' % n)
		sendtask.put(n)
		
		
	print('try to get results...')
	for i in range(10):
		r=receivetask.get(timeout=10)
		print(' result : %s ..' % r)
		
	manager.shutdown()
	print('master exit')

	
if __name__ == '__main__':
	freeze_support()
	testServer()
