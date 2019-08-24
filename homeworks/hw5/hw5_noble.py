#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 5

Created on Fri Aug 23 15:30:21 2019
@author: bennoble
"""
# Defining Node class. Nodes take a value representation and a next feature.
class Node():
  def __init__(self, _value=None, _next=None):
    self.value = _value
    self.next = _next

# String representation of the node prints the value
  def __str__(self):
    return str(self.value)

# Defining LinkedList class
class LinkedList():
  def __init__(self, value):
# The user initializes the class with an initial value.  This value is used
# to create a new instance of a Node.
    self.value = Node(value)
# Because the linked list is just one item, that item is also set to be the tail
    self.tail = self.value
# The length of the list is set to be 1
    self.length = 1
    
# The list_length function returns self.length
  def list_length(self):
    return '%d' % (self.length)

# The addNode function takes one new value
  def addNode(self, new_value):
# The new value creates a new instance of a Node
    self.new_value = Node(new_value)
# The tail (currently the most recently created node before this one) takes on 
# a _next value of the node being created
    self.tail.next = self.new_value
    #if self.tail.value == self.value.value:
     # self.value.next = self.tail.next
# The new node becomes the tail
    self.tail = self.new_value
# Length is increased by 1
    self.length += 1

# Printing the list with a recursive function       
  def __str__(self):
# name is initially defined as self.value which is the head node
    name = self.value
# If the named node value == the tail value, then the tail value is printed
    if name.value == self.tail.value:
      return '%d' % (self.tail.value)
# Else, print the current named value, add .next to the name, and run the function
# again. This process begins with self.value and then in the next call becomes
# self.value.next (the second node) and on and on until self.value.next...next
# is the tail.
    else:
      print(name.value)
      name = name.next
      return this(name)
        
    
li = LinkedList(5)
li.addNode(12)
li.addNode(9)
li.addNode(2)

print(li)

for i in li.list_length():
  print()


a print(('.next'*2))

li.value + a
print(li.value.next.next)


print(li.value.value)
print(li.value.next)
print(li.tail.value)
print(li.tail.next)

a = li.value.next

def this(name):
  if name.value == li.tail.value:
    return '%d' % (li.tail.value)
  else:
    print(name.value)
    name = name.next
    return this(name)

this(li.value)

print(li.value.next.next.next.value)


print(li.value.next)

print(li.new_value.next)


test = [i for i in range(10)]

for i in range(15):
  try:
    print(test[i])
  except IndexError:
    pass


