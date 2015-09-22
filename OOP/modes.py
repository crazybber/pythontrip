#!/usr/bin/env python3
# -*- coding utf-8 -*-

'a test module'

__authot__ = 'Eamon chen'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('hello world')
	elif len(args)==2:
		print('hello %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':
	test()
	
print(sys.argv[0])


def _private_1(name):
	return ('hello ,%s' % name)

def _private_2(name):
	return ('Hi ,%s' % name)
	
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
		
		


from PIL import Image

def thumbnailPic():
	im=Image.open('image/test.png')
	print(im.format,im.size,im.mode)
	im.thumbnail((200,200))
	im.save('image/thumb.jpg','JPEG')
	
thumbnailPic()