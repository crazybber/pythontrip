#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

# 一个能实现ls -l输出的程序。

# 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


import os

def main():
	text=input('输入选项：')

	if text== 'dir -l':
		print('当前文件夹下所有文件如下：')
		DirCurrent()
	else:
		print('当前目录以及子目录内含有:',text,' 的文件如下:')
		SearchAllContains(text)
		

def DirCurrent():
	listCurrentDirFiles = os.listdir()
	alldirs=[x for x in listCurrentDirFiles if os.path.isdir(x)]
	print(alldirs)
	allfiles=[x for x in listCurrentDirFiles if os.path.isfile(x)]
	print(allfiles)
	
	



def SearchAllContains(text,searchdir='.'):
	files=[]
	SearchcurrentDir(files,text,searchdir)			
	print(files)
	
def SearchcurrentDir(file_list,text,searchdir='.'):
	for x in os.listdir(searchdir):
		if os.path.isfile(x):
			if x.find(text)> -1:
				file_list.append(os.path.join(searchdir,x))
		elif os.path.isdir(x):
			SearchcurrentDir(file_list,text,os.path.join(searchdir,x))


	
main()