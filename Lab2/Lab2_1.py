'''Lab2_1'''

'''functie care returneaza primele n numere din sirul Fibonacci'''
def FibonacciNumber (number):
    n1=1
    n2=1
    sequence=[]

    if number==1:
        return [1]
    if number==2:
        return [1,1]

    if number>2:
        sequence+=[n1]
        sequence+=[n2]

        for i in range(2,number):
            sequence+=[n1+n2]
            n1=n2
            n2=sequence[-1]
    return sequence

print(FibonacciNumber(10))