#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 4

Created on Tue Aug 20 16:03:33 2019
@author: bennoble
"""
import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Generate a short list and long list to sort
num_s = [3, 2, 9, 1]
num_l = [13, 7, 15, 4, 18, 2, 14, 5, 1, 3, 19, 12, 17, 16, 10, 6, 8, 9, 11]

# Define the gnome sorter - https://en.wikipedia.org/wiki/Gnome_sort
# The idea is that if list[i] > list[i + 1], i and i+1 are swapped, the sorter
# steps backward and does the same comparison until list[i] < list[i + 1],
# then moves forward until list[i] > list[i + 1] again
def gnome(num, n = 0):
# While n (the count) is less than the length of the whole list...
  while n != len(num)-1:
# If num[n] > num[n + 1], swap and decrease the count by one. If the count would
# be reduced below 0, then set it to 0
    if num[n] > num[n + 1]:
      num[n], num[n + 1] = num[n + 1], num[n]
      if n >= 1:
        n -= 1
      else:
        n == 0
      print(n, num)  
# If the num[n] < num[n + 1], increas the count and continue
    if num[n] < num[n + 1]: 
      n+=1
      print(n, num)
  return(num)
  
gnome(num_s)
gnome(num_l)

# Define heapsort - https://en.wikipedia.org/wiki/Heapsort
# Similar to selection sort except that it iteratively takes the max and 
# generates a new sorted list
heap = [] 
def heapsort(num, heap = []):
# if the length of the original list is 0, return the reversed heap list
  if len(num) == 0:
    return heap[::-1]
# else, append the max of the original list to the heap list and run the
# heapsort again recursively
  else:
    heap.append(num.pop(np.argmax(num)))
    print(num, heap)
    return heapsort(num)
    
heapsort(num_s)
heapsort(num_l)


x = []
dur = []
# Creates 100 lists of increasing length up to 99
for i in range(1, 100):
  li = [j for j in range(1, i+1)]
# Shuffle the list
  random.shuffle(li)
# Capture the start time, run the gnome sort, and calculate the duration of the sort
  start_time = time.time()
  gnome(li)
  duration = time.time() - start_time
# Append the length of the list and duration to the relevant lists
  print(duration)
  x.append(i)
  dur.append(duration)

z = []
dur2 = []
# Creates 100 lists of increasing length up to 99
for i in range(1, 100):
  li = [j for j in range(1, i+1)]
# Shuffle the list
  random.shuffle(li)
# Capture the start time, run the heapsort sort, and calculate the duration of the sort
  start_time = time.time()
  heapsort(li)
  duration = time.time() - start_time
# Append the length of the list and duration to the relevant lists
  print(duration)
  z.append(i)
  dur2.append(duration)

# Plot the length v duration of the two sorting algorithms
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, dur, 'r')
plt.plot(z, dur2, 'b')
plt.legend(['gnome sort', 'heapsort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Duration of Sort (s)")
plt.xlabel("Length of List (n)")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
As n increases, the gnome sort tends to take an increasingly long time. This makes sense given that 
it moves backwards within the list. The gnome sort is also more variable—if the randomly generated list 
is nearly in order, it will go quickly versus if the list is very out of order. The heapsort is mostly 
invariant to the starting shuffle and list size.
"""
plt.figtext(.5, 0, txt, fontsize = 8, ha = "center")
plt.savefig('plot.pdf')

