'''Lab3 1'''

'''Write a function that receives as parameters two lists a and b and returns a list of sets containing: 
(a intersected with b, a reunited with b, a - b, b - a)'''

def setOperations(listA,listB):
    setA=set(listA)
    setB=set(listB)

    return [setA.intersection(setB),setA.union(setB),setA.difference(setB),setB.difference(setA)]

ab,aUb,a_b,b_a=setOperations([1,2,3,4,5],[3,4,5,6,7])

print('intresectie : ', ab)
print('reuniune : ', aUb)
print('a-b : ',a_b)
print('b-a : ',b_a)