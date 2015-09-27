#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'Distribute Process!'

import time,sys,queue

from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
	pass
	

QueueManager.register('task_send_queue')
QueueManager.register('task_receive_queue')

server_addr ='127.0.0.1'
print('connet to server %s....' % server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()

sendtask=m.task_send_queue()
receivetask=m.task_receive_queue()


for i in range(10):
	try:
		n = sendtask.get(timeout=1)
		print('run task %d*%d' % (n,n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		receivetask.put(r)
	except Queue.Empty:
		print('task queue is empty')
		
		
print('woker exit.')

