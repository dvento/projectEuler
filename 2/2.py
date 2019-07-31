'''

Daniel Vento, 2019

PROBLEM #2:
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''


def getFibonacciNums():
    
        n_2 = 1
        n_1 = 1
        sum = 1
        while n_1 + n_2 < 4000000:
                tmp = n_1
                n_1 = n_1 + n_2
                n_2 = tmp
                if tmp % 2:
                        sum = sum + tmp
        print(f'{" sum: "}{sum}')


getFibonacciNums()