def palindromeValidation(number):
    inverse=0
    numberCopy=number

    while numberCopy>0:
        inverse = inverse * 10
        inverse =inverse + numberCopy % 10
        numberCopy=int(numberCopy/10)

    if(number==inverse):
        return True
    return False

print(palindromeValidation(11))

print(palindromeValidation(21))