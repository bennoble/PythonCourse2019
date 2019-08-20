## Class 08 - Recursion & Sorting

# Search Algorithms

## returns element if it is in the list
def linear_search(mylist, element):
  steps = 0
  for item in mylist:
    steps += 1
    if item == element:
      print(steps)
      return item
  print(steps)
  return None

mylist = range(26)

linear_search(mylist, 1)
linear_search(mylist, 5)
linear_search(mylist, 30)

## returns element if it is in sorted list
def binary_search(sorted_list, element):
  print("Input list is {0}".format(sorted_list))
  print("Input size is {0}".format(len(sorted_list)))
  middle = len(sorted_list)//2
  median = sorted_list[middle]
  if len(sorted_list) <= 1:
    if element == median:
      return median
    else:
      return None
  if element < median:
    left = sorted_list[0:middle]
    return binary_search(left, element)
  else: 
    right = sorted_list[middle:]
    return binary_search(right, element)

mylist = range(1000)
binary_search(mylist, 70)



## Find n'th number in fibonacci sequence
def fib(n):
  if n<=1:
    return n
  return fib(n-1) + fib(n-2)

# fib(8) = fib(7) + fib(6) = 21
# fib(7) = fib(6) + fib(5) = 13
# fib(6) = fib(5) + fib(4) = 8
# fib(5) = fib(4) + fib(3) = 5
# fib(4) = fib(3) + fib(2) = 3
# fib(3) = fib(2) + fib(1) = 2
# fib(2) = fib(1) + fib(0) = 1
# fib(1) = 1
# fib(0) = 0 

for i in range(35):
  print("{0} : {1}".format(i, fib(i)))



# Exercise:

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

factorial(4)
##if base case:
##  return something
##else:
##  return a recursive call




# Sorting

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

# Bogo Sort
# 1) Randomize number order
# 2) If sorted: stop; else: repeat

import random

def bogo_sort(li):
  random.shuffle(li)
  sorted_list = sorted(li)
  print(li)
  if sorted_list == li:
    return li
  return bogo_sort(li)

bogo_sort(my_numbers)

# Selection Sort
# 1) Find minimum of the unsorted list
# 2) Remove minimum and place it in first element on new list
# 3) Repeat until unsorted list is empty



def selection_sort(numbers):
  min_list = []
  min_list.append(numbers.pop(numbers.index(min(numbers))))
  if len(numbers) == 0:
    return min_list
  return selection_sort(numbers)

selection_sort(my_numbers)
numbers.pop(my_numbers.index(min(my_numbers)))

# Insertion Sort
# 1) Start with the element in the second position
# 2) Insert it to the correct position to the left
# - Check left-most element until value is greater
# 3) Continue to next position

def insertion_sort(numbers):
  try:
    for i in range(len(numbers)):
      while numbers[i] > numbers[i + 1]:
        numbers.insert(i, numbers.pop(i + 1))
        #print(numbers)
        return insertion_sort(numbers)
  except IndexError:
    return numbers
    
insertion_sort(my_numbers)

# Bubble Sort
# 1) Compare first two contiguous elements, swap if necessary
# 2) Compare next two contiguous elements, swap if necessary
# 3) Continue until end of list
# 4) If swaps occurred in 1 - 3, repeat for first n - 1 elements

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

def bubble_sort(numbers):
  for i in range(len(numbers)):
      while numbers[i] > numbers[i+1]:
        numbers.insert(i + 1, numbers.pop(i))
        print(numbers)
        

bubble_sort(my_numbers)

# Plotting

#pip install matplotlib


import matplotlib.pyplot as plt

x = range(1, 101) ## # of elements in list
y = range(1, 101) ## time
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y)
plt.legend(['hi', 'bye'], loc = "upper left", prop = {"size":10})
plt.ylabel("Y")
plt.xlabel("X")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
Maybe a description here
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot.pdf')

import time

start_time = time.time()
print("hi")
time.time() - start_time