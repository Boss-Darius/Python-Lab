'''Lab2_3'''

'''Write a function that receives as parameters two lists a and b and returns: 
(a intersected with b, a reunited with b, a - b, b - a)'''

def setOperations(listA,listB):
    operation=[]

    ab=[a for a in listA if a in listB]
    difab=[a for a in listA if a not in listB]
    difba=[b for b in listB if b not in listA]
    aUb=[]
    aUb+=difab
    aUb+=ab
    aUb+=difba

    operation+=[ab]
    operation+=[aUb]
    operation+=[difab]
    operation+=[difba]

    return operation

union,reunion,dif1,dif2=setOperations([1,2,3,4],[3,4,5,6])

print('union: ',union)
print('reunion: ',reunion)
print('a-b: ',dif1)
print('b-a: ',dif2)