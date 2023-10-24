'''Lab2_10'''

'''10. Write a function that receives a variable number of lists and returns 
a list of tuples as follows: the first tuple contains the first items in the lists, 
the second element contains the items on the position 2 in the lists, etc.
 Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

Note: If input lists do not have the same number of items, missing items will be replaced 
with None to be able to generate max ([len(x) for x in input_lists]) tuples'''

def tuples(listList):
    returnedList=[]


    maxLen=max(len(x) for x in listList)

    for i in listList:
        if len(i)<maxLen:
            for j in range(0,maxLen-len(i)):
                i+=""

    for i in range(0,maxLen):
        currentTuple = ()
        for j in listList:
            currentTuple+=tuple([j[i]])

        returnedList+=[currentTuple]

    return returnedList

print(tuples([[1,2,3], [5,6,7], ["a", "b", "c"]]))
