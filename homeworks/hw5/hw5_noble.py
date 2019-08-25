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
    
# I will be printing the list with a recursive function called 'loop'
  def loop(self, name = None):
# If the named node value == the tail value, then the tail value is printed
    if name.value == self.tail.value:
      return '%s' % (self.tail.value)
# Else, print the current named value, add .next to the name, and run the function
# again. This process begins with self.value and then in the next call becomes
# self.value.next (the second node) and on and on until self.value.next...next
# is the tail.
    else:
      print(name.value)
      name = name.next
      return self.loop(name)

# Printing the LinkedList class calls the loop function and runs it with the
# head name as the starting argument. It returns the full list.
  def __str__(self):
    return self.loop(self.value)
    
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
    print(self)

  def addNodeAfter(self, new_value, after_node):        
# Create a new node with the new value
    self.new_value = Node(new_value)
# Defibe a temporary recursive function which searches the list for the node
# with the value of the 'after_node'
    def recur(name, after_node):
# If the value of the current named node matches the value the user entered for
# the 'after_node', return the node object
      if name.value == after_node:
        return name
# Otherwise, appened .next until the matching node object is found
      else:
        name = name.next
        return recur(name, after_node)
# Run the recur function starting with the head node and return the result
    match = recur(self.value, after_node)
# Suppose the new node is called B and is going between A and C:
# This line looks at what A is pointing to (C) and points B to C.
    self.new_value.next = match.next
# This line looks at A and points it to B. 
    match.next = self.new_value
    self.length += 1
# Print the updated list
    print('Linked list updated: \n', self)
    
  def reverse(self):
# Define a temporary function called tail_finder which takes a name and the 
# current tail
    def tail_finder(name, current_tail):
# If a node points to the tail... 
      if name.next.value == current_tail.value:
# Point the current tail to that node (aka, point backwards)
        current_tail.next = name
# Define new_tail as that node (this will be the node before the actual tail)
        self.new_tail = name
        return self.new_tail
      else:
# Otherwise, append. next to the name and call tail_finder again until you 
# find the node pointing to the tail
        name = name.next
        return tail_finder(name, current_tail)
# Run tail finder once
    tail_finder(self.value, self.tail)
# Check to see if the head (which I call self.value) is also the new_tail. If not
# run tail_finder until the head is ultimately the new_tail
    while self.new_tail != self.value:
      tail_finder(self.value, self.new_tail)
# The next two lines are basically bookkeeping to ensure that after the list
# is reversed, all the other functions in the class work as they're supposed to
##     
# self.tail still points the original tail, so reassign the original tail to be 
# self.value, which is what I call the head elsewhere
    self.value = self.tail
# self.new_tail (which is only used for the tail_finder funtion) is the original head, 
# so I must assign this to be the actual tail object, which I call self. tail.
    self.tail = self.new_tail
# Now we can forget about self.new_tail, and the original head is the tail and
# the original tail is the head and everything is pointing "backwards"
    print(self)

    
li = LinkedList(5)
li.addNode(12)
li.addNode(9)
li.addNode(2)
li.loop(li.value)

print(li)

li.reverse()

print(li)

li.addNodeAfter(63, 9)
li.addNode(0)

li.list_length()

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


