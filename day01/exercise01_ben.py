## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

def fib(x):
    fib_list = [1, 1]
    while len(fib_list) < x:
        fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)

fib(10)

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
    letters = [i for i in word]
    x = 0
    for i in letters:
        if i == "e":
            x += 1
    if x < 1:
        print(True)
    else:
        print(False)

has_no_e("Hello")
has_no_e("Hola")
has_no_e("Element")
has_no_e("Wizard")

"""return true if there is e in 'word', else false"""
def has_e(word):
        letters = [i for i in word]
        x = 0
        for i in letters:
            if i == "e":
                x += 1
        if x < 1:
            print(False)
        else:
            print(True)

has_e("Hello")
has_e("Hola")
has_e("Element")
has_e("Wizard")

"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
    letters1 = [i for i in word1]
    letters2 = [i for i in word2]
    if set(letters1) & set(letters2):
        print(True)

uses_only("Why", "Me")
uses_only("Hell", "Hello")

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):


"""true/false is the word in alphabetical order?"""
def is_abecedarian(word):
