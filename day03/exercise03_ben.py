## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.

def count_vowels(word):
  x = 0
  vowels = [ "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  if type(word) == str:
    for i in word:
      for j in vowels:
        if i == j:            
          x+=1
    return x
  else:
    raise TypeError


