# hey

sumVal = 0

def calculateLinear():
    currNum = 0
    global sumVal

    while currNum < 1000:

        if currNum % 3  == 0 or currNum % 5 == 0:
            sumVal = sumVal + currNum
        
        currNum = currNum + 1

def calculateGeometric(div,maxim):
    
    return int(div*(int(maxim/div)*(int((maxim/div))+1))/2)

def getAndPrintResults():
    sumVal = calculateGeometric(5,999) + calculateGeometric(3,999) - calculateGeometric(15,999)
    print(f'{"The sum of all multiples of 3 and 5 that are less than 1000 is: "}{sumVal}')

getAndPrintResults()