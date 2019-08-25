'''

Daniel Vento, 2019

PROBLEM #3:
What is the largest prime factor of the number 600851475143 ?

'''

# first version of prime factors

theNum = 600851475143

def getCalc():

    minFactor = 2
    num = theNum

    while (minFactor < num):
    
        if num % minFactor != 0:
            minFactor += 1
        else:
            num /= minFactor            
            minFactor = 2
    print(f'{" The greatest prime factor is: "}{num}')

getCalc()
