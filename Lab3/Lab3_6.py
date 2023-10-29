'''Lab3_6'''

'''Write a function that receives as a parameter a list and returns a tuple (a, b), 
representing the number of unique elements in the list, and b representing the number of duplicate elements in the list 
(use sets to achieve this objective)'''


def uniqueAndDuplicates(numberList):
    numberSet=set(numberList)

    return tuple([len(numberSet),len(numberList)-len(numberSet)])

uniques,duplicates=uniqueAndDuplicates([1,1,2,3,4,4])

print("number of uniques=",uniques)
print("number of duplicates=",duplicates)