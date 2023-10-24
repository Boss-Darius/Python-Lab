'''Lab2_6'''

'''Write a function that receives as a parameter a variable number of lists and a whole number x. 
Return a list containing the items that appear exactly x times in the incoming lists. '''

def exactMatch(variableList,exactNumber):
    exactList=[]
    longList=[]
    for i in variableList:
        for j in range(0,len(i)):
            longList+=[i[j]]

    for i in variableList:

        for j in range(0,len(i)):
            if longList.count(i[j])==exactNumber and i[j] not in exactList:
                exactList+=[i[j]]
    return exactList

print(exactMatch([[1,2,3],[2,3,4],[4,5,6],[4,1,"test"]],2))