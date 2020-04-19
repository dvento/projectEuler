# coding=utf-8
'''

Daniel Vento, 2020

PROBLEM #5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''


def findNum():
    num = 2520
    success = False
    print("Calculating...")
    while not success:
        for i in range(1,21):
            if num % i != 0:
                num +=20
                success = False
                break
            else:
                success = True

    print("The number is: %i", num)

findNum()