# coding=utf-8
'''

Daniel Vento, 2020

PROBLEM #6:

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum of the first one hundredd natural numbers

'''

# target number
n = 100

def squaredSum():
    # the mathematical formula to calculate the sum of n numbers is (n*(n + 1)) / 2
    res = ((n*(n + 1)) / 2)**2
    return res

def sumOfSquares():
    
    # The mathematical formula to calculate the sum of n squared is (n*(n + 1)*(2*n + 1)) / 6
    res = (n*(n + 1)*(2*n + 1)) / 6
    return res
    

def diff():
    res = squaredSum() - sumOfSquares()
    print("Result of the difference between the sum of the squares of the first "
        "one hundred natural numbers and the square of the sum of the first one hundredd natural numbers is: ", int(res))

diff()
