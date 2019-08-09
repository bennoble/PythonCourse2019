import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
  return txt.upper()

## reverse all characters in string
def reverse(txt):
  return txt[::-1]

## reverse word order in string
def reversewords(txt):
  words = txt.split()
  return ' '.join(words[::-1])

## reverses letters in each word
def reversewordletters(txt):
  rev = []
  words = txt.split()
  for i in words:
    rev.append(reverse(i))
  return ' '.join(rev)

## change text to piglatin.. google it! 
def piglatin(txt):
  pig = []
  txt = txt.lower()
  vowels = ["a", "e", "i", "o", "u", "y"]
  words = txt.split()
  for word in words:
    for letter in word:
      if letter in vowels:
          halves = word.split(letter)
          halves = halves[::-1]
          halves.insert(0, letter)  
          halves.append("ay")
          pig.append(''.join(halves))
          break
  pig = ' '.join(pig)
  return pig

## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

piglatin("I am a cat")

			
			
			
			
			

