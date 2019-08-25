'''

Daniel Vento, 2019

PROBLEM #3:
What is the largest prime factor of the number 600851475143 ?

'''

# first version of prime factors


def getCalc():

    # we define the minimum factor of the number we need to find prime factors of
    minFactor = 2
    num = 600851475143

    while (minFactor < num):
    
        # if the number is not a factor, increase it by 1 and try again
        if num % minFactor != 0:
            minFactor += 1
        else:
            # update the variable to be the next dividend
            num /= minFactor            
            minFactor = 2

    # the while condition told us that the last dividend is the greatest prime factor, so we print it
    '''
    How does it tells that?

    Well, if the last dividend was num = 6857 (which is, of course, the solution), the minFactor would had been reset to 2, so the if condition inside the loop 
    will increase the minFactor by 1, until it reaches the while condition, which will occur because 6857 is a prime number, so it'll be the last value of "num"
    and then, will be printed.
    '''

    print(f'{" The greatest prime factor is: "}{num}')

getCalc()
