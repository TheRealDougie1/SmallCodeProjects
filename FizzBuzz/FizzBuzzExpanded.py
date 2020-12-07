"""
Building on the basic concept of FizzBuzz, what if:
    The number set was expanded, e.g. to 1000.
    Different numbers were used instead of 3 and 5.
"""

import sys

def FizzBuzz(numberSet = 100, fizzNumber = 3, buzzNumber = 5):
    for number in range(1,numberSet):
        if number % fizzNumber == 0 and number % buzzNumber == 0:
            print("FizzBuzz")
            continue
        if number % fizzNumber  == 0:
            print("Fizz")
            continue
        if number % buzzNumber == 0:
            print("Buzz")
            continue
        print(number)

if __name__ == '__main__':
    FizzBuzz()
    print("\t New FizzBuzz")
    FizzBuzz(100,4,13)
    print("FizzBuzz")