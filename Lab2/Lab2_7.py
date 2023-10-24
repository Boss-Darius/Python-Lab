'''Lab2_7'''

'''Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. 
The first element of the tuple will be the number of palindrome numbers found in the list and the second element will 
be the greatest palindrome number.'''

def palindrome(number):
    number2=0
    numberCopy=number

    while numberCopy>0:
        number2=number2*10 + numberCopy%10
        numberCopy=int(numberCopy//10)

    return  number2==number

def palindromeTuple(numberList):
    palindromeList=[x for x in numberList if palindrome(x)==True]

    return (len(palindromeList),max(palindromeList))

print(palindromeTuple([12,11,21,22]))
