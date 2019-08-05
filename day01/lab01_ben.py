## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
def binarify(num):
# Create the empty list for the binary number
    bin = []
# While loop iterates through division and remainder, adding
# remainders to bin list until the number is 0
    while num > 0:
        bin.append(num%2)
        num //= 2
# Reverse the list
    bin.reverse()
# Convert list to string
    string = "".join(str(i) for i in bin)
    return string

binarify(50)

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
# Create the empty list
    base_conversion = []
# While loop iterates through division by the base and saves the remainder,
# adding remainders to bin list until the number is 0
    while num > 0:
        base_conversion.append(num%base)
        num //= base
# Reverse the list
    base_conversion.reverse()
# Convert list to string
    string = "".join(str(i) for i in base_conversion)
    return string

int_to_base(734,5)

"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
    answer = 0
    str_to_list = [i for i in string]
    str_to_list.reverse()
    int_list = []
    for i in str_to_list:
        int_list.append(int(i))
    for i in range(len(int_list)):
        answer += int_list[i]*base**i
    return answer

# base_to_int("1111", 2)

"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
    answer = base_to_int(str1, base1) + base_to_int(str2, base2)
    print(answer)

flexibase_add("10", "40", 2, 5)

"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
    answer = base_to_int(str1, base1) * base_to_int(str2, base2)
    print(answer)

flexibase_multiply("10", "40", 2, 5)

"""given an integer, return the Roman numeral version"""
def romanify(num):


# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
