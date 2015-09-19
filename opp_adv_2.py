#!/usr/bin/env python3
# -*- coding utf-8 -*-

__Author__ ='eamon'

#多重继承

class Animal(object):
	pass

class Mammal(Animal)：
	pass

class Bird(Animal):
	pass
	
class Dog(Mammal):
	pass
	
	
class Bat(Mammal):
	pass
	
	
class Parrot(Bird):
	pass
	
class Ostrich(Bird):
	pass
	
class RunnableMixIn(object):
	pass
	
class FlyableMixIn(object):
	pass
	
	
	
class Dog(Mammal,RunnableMixIn):
	pass
	
class Bat(Mammal,FlyableMixIn):
	pass
	
class MyTCPServer(TCPServer,forkingMixIn):
	pass
	
class MyUDPServer(UDPServer,ThreadingMixIn):
	pass
	
class MyTCPServer(TCPServer,CoroutineMixIn):
	pass