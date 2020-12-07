"""
Basic Problem Summary:
    For 100 numbers:
    If the number is divisible by 3, print Fizz.
    If the number is divisible by 5, print Buzz
    If the number is divisible by both 3 and 5, print FizzBuzz
    Otherwise, just print the number :)

    Example Output: 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz
"""

def FizzBuzz():
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            continue
        if number % 3  == 0:
            print("Fizz")
            continue
        if number % 5 == 0:
            print("Buzz")
            continue
        print(number)

if __name__ == '__main__':
    FizzBuzz()