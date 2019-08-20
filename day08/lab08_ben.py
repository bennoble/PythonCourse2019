## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
  if x == 0:
    return y
  if y == 0 :
    return x
  r = x % y 
  x = y
  y = r
  print(x, y)
  return gcd(x, y)

## Problem 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me, primes = []):
  num = []
  if me == 1:
    return primes
  for i in range(me - 1, 1, -1):
    if me%i == 0:
      num.append(me)
  if len(num) == 0:
    primes.append(me)
  me = me - 1
  return find_primes(me)      

find_primes(9, primes = [])
  
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html
import numpy as np

def my_min(li):
  try:
    return min(li)
  except ValueError:
    return 0

my_min([])

li = []
li == []

def tower(disks):
  A = [i for i in range(1, disks + 1)]
  B = []
  C = []
  master = [A, B, C]
  if max(A)%2 == 0:
    while C != [i for i in range(1, disks + 1)][::-1]:
      if B == []:
        B.append(A.pop(np.argmin(A)))
      elif A == []: 
        A.append(B.pop(np.argmin(B)))
      elif my_min(A) < my_min(B):
        B.append(A.pop(np.argmin(A)))
      else:
        A.append(B.pop(np.argmin(B)))
      print(master)
      if C == []:
        C.append(A.pop(np.argmin(A)))
      elif A == []:
        A.append(C.pop(np.argmin(C)))
      elif my_min(A) < my_min(C):
        C.append(A.pop(np.argmin(A)))
      else:
        A.append(C.pop(np.argmin(C)))
      print(master)
      if B == []:
        B.append(C.pop(np.argmin(C)))
      elif C == []:
        C.append(B.pop(np.argmin(B)))
      elif my_min(B) < my_min(C):
        C.append(B.pop(np.argmin(B)))
      else:
        B.append(C.pop(np.argmin(C)))
      print(master)
    return master
  else:
    try:
      while C != [i for i in range(1, disks + 1)][::-1]:
        if C == []:
          C.append(A.pop(np.argmin(A)))
        elif A == []:
          A.append(C.pop(np.argmin(C)))
        elif my_min(A) < my_min(C):
          C.append(A.pop(np.argmin(A)))
        else:
          A.append(C.pop(np.argmin(C)))
        print(master)
        if B == []:
          B.append(A.pop(np.argmin(A)))
        elif A == []: 
          A.append(B.pop(np.argmin(B)))
        elif my_min(A) < my_min(B):
          B.append(A.pop(np.argmin(A)))
        else:
          A.append(B.pop(np.argmin(B)))
        print(master)
        if B == []:
          B.append(C.pop(np.argmin(C)))
        elif C == []:
          C.append(B.pop(np.argmin(B)))
        elif my_min(B) < my_min(C):
          C.append(B.pop(np.argmin(B)))
        else:
          B.append(C.pop(np.argmin(C)))
        print(master)
    except ValueError: 
      return master

tower(100)
      
[i for i in range(1, 3 + 1)][::-1]
