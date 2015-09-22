#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

'unit test'


class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except:
			raise AttributeError(r"'Dict' object has no attributr: %s" % key)
	def __setattr__(self,key,value):
		self[key]=value

		
import unittest
# from unit_test improt Dict

class TestDic(unittest.TestCase):
	def test_init(self):
		d= Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
	
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
		
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
	
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty
			
	def setUp(self):
		print('setup.....')
		
	def tearDown(self):
		print('tear down....')
	
		
if __name__ == '__main__':
	unittest.main()
	