#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 5

Created on Fri Aug 23 15:30:21 2019
@author: bennoble
"""

class Node():
  def __init__(self, _value=None, _next=None):
    self.value = _value
    self.next = _next

  def __str__(self):
    return str(self.value)

class LinkedList():
  def __init__(self, value):
    self.value = Node(value)
    self.length = 1
    
  def __str__(self):
    print('%s' % (self.value))
    
  def length(self):
    return '%d' % (self.length)
  
  def addNode(self, new_value):
    self.new_value = Node(new_value)
    
    

node5 = Node(5)
node12 = Node(12)

print(node5)

li = LinkedList(5)

li.length()

print(li)

li.addNode(node5)

test = [i for i in range(10)]

for i in range(15):
  try:
    print(test[i])
  except IndexError:
    pass