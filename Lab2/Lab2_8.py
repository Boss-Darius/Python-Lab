'''Lab2_8'''

''' Write a function that receives a number x, default value equal to 1, a list of strings,
 and a boolean flag set to True. For each string, generate a list containing the characters that have the 
 ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the 
 ASCII code not divisible by x.'''

''' Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . 
Note: The function must return list of lists.'''

def Lab2_8(flag,stringList,x=1):
    returnedList=[]

    for i in stringList:
        generatedList=[]
        for j in range(0,len(i)):
            if flag==True:
                if ord(i[j])%x==0:
                    print(ord(i[j]))
                    generatedList+=[i[j]]
            else:

                if ord(i[j])%x !=0:
                    print(ord(i[j]))
                    generatedList+=[i[j]]

        if generatedList != []:
            returnedList+=[generatedList]

    return returnedList

print(Lab2_8(False,["test", "hello", "lab002"],2))