# coding=utf-8
'''

Daniel Vento, 2020

PROBLEM #4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.


'''


# first version of problem 4

def iterate():

    # initialize variables
    x, y = 999, 999
    factorState, result = 0, 0

    lastPalNum = 0
    
    print("Calculating...")

    while True:
        
        result = x * y

        if isPalindromic(result):
            # compare last found palindromic to the new one, so it keeps the higher
            if result > lastPalNum:
                lastPalNum = result

        # first, multiply 999 by 999, 998, 997... until 100
        if factorState == 1:
            y-=1
            if y < 100:
                factorState = 0
        # then, decrease x by one and multiply it by the rest of digits
        else:
            x -= 1
            y = x
            factorState = 1

        if x < 100:
            print("Palindromic nums: ", lastPalNum)
            break

def isPalindromic(res):

    # convert number into string  so we can compare its digits
    resArr = [int(x) for x in str(res)]
    resLen = len(resArr)

    left = resArr[0]
    right = resArr[resLen - 1]
    # trick to find the number of times we have to iterate through the number
    halfLen = resLen / 2

    i = 0

    # compare each digit starting from the first 
    while halfLen > 0:

        # if the first digit does not equal the last one, just skip this number (call return)
        if left != right:
            return False
        else:
            halfLen -= 1
            i += 1
            left = resArr[i]
            right = resArr[resLen - i - 1]
    
    # if is Palindromic then
    return True

iterate()