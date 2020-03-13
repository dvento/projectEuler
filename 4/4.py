# coding=utf-8
'''

Daniel Vento, 2020

PROBLEM #4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.


'''


# first version of 4



def iterate():

    x, y = 999, 999
    factorState, result = 0, 0

    lastPalNum = 0
    
    print("Calculating...")

    while True:
        
        result = x * y

        if isPalindromic(result):
            if result > lastPalNum:
                lastPalNum = result

        if factorState == 1:
            y-=1
            if y < 100:
                factorState = 0
                y = 999
        else:
            x-=1
            factorState = 1

        if x < 100:
            print("Palindromic nums: ", lastPalNum)
            break


    '''
    while True:

        
        result = x * y
        print("Result: %i X: %i Y: %i" % (result, x, y))

        if isPalindromic(result):
            print("Is palindromic: %i" %(result))
            break

        if factorState == 1:
            x-=1
            factorState = 0
        elif factorState == 0:
            y-=1
            factorState = 1

        if x < 100 or y < 100:
            break
'''

def isPalindromic(res):

    resArr = [int(x) for x in str(res)]
    resLen = len(resArr)

    left = resArr[0]
    right = resArr[resLen - 1]
    halfLen = resLen / 2


    i = 0

    while halfLen > 0:

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