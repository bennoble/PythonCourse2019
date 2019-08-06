## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

def fib(x):
# Create the starting list which includes 1 and 1
  fib_list = [1, 1]
# While the list does not meet the specified number of entries requested...
  while len(fib_list) < x:
# Add the previous two items and add it to the list
    fib_list.append(fib_list[-1] + fib_list[-2])
  return fib_list

fib(10)

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
# Split word in a list of the letters
  letters = [i for i in word]
# Start the counter at 0
  x = 0
# For each letter i, if it's an "e", increase the counter
  for i in letters:
      if i == "e":
          x += 1
# If the counter is less than 1, print True (no e's). Otherwise print 
#False (e's)
  if x < 1:
      return True
  else:
      return False

has_no_e("Hello")
has_no_e("Hola")
has_no_e("Element")
has_no_e("Wizard")

"""return true if there is e in 'word', else false"""
def has_e(word):
# Get the result from the has_no_e function and save it
  result = has_no_e(word)
# Return the opposite result of the has_no_e function  
  return not result

has_e("Hello")
has_e("Hola")
has_e("Element")
has_e("Wizard")

"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
# Break words into a list of letters
  letters1 = [i for i in word1]
  letters2 = [i for i in word2]
# Set counter
  x = 0
# If a letter in word 1 matches a letter in word 2, increase the count 
  for i in letters1:
    if i in letters2:
      x += 1
# If the count matches the number of letters in word1, the implication is that
# Every word was a match. Therefore, word1 uses only letters from word2
  if x == len(letters1):
    return True
  else:
    return False

uses_only("abccccd", "abcde")
uses_only("abcd", "abdx")

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
# Split words into lists of letters
  letters1 = [i for i in word1]
  letters2 = [i for i in word2]
# Set counter to 0
  x = 0
# For letter i in word2, if it is in word1, increase the count
  for i in letters2:
    if i in letters1:
      x += 1
# If the count matches the number of letters in word2, the implication is that
# Every letter in word2 is in word1, and therefore, the function resolves 
#to True
  if x == len(letters2):
    return True
  else:
    return False

uses_all("abcd", "accddb")
uses_all("abcd", "abcde")

"""true/false is the word in alphabetical order?"""
def is_abecedarian(word):
# Break the word into a list of letters
  letters = [i for i in word]
# Sort the list alphabetically and save as a new list
  alph_letters = sorted(letters)
# Compare the list. If they're the same, then the word is in alphabetical
# order. If not, then the word is not in alphabetical
  if alph_letters == letters:
    return True
  else: 
    return False

is_abecedarian("abc")
is_abecedarian("bac")
is_abecedarian("ainx")
