'''Lab3_11'''

'''Write a function that receives a variable number of positional arguments and a variable number of keyword arguments 
adn will return the number of positional arguments whose values can be found among keyword arguments values.
Ex:
my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3

'''

def keyValues(*numbers,**keyAndValues):
    numberList=[]
    occurences=0
    for number in numbers:
        numberList+=[number]

    valuesList=keyAndValues.values()

    for i in numberList:
        if i in valuesList:
            occurences=occurences+1
    return occurences

print(keyValues(1, 2, 3, 4, x=1, y=2, z=3, w=5))