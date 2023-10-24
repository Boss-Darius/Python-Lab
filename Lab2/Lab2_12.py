'''Lab2_12'''

'''Write a function that will receive a list of words  as parameter and will return a list of lists of words,
 grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

	Example:

         group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return 
                        [['ana', 'banana'], ['carte', 'parte'], ['arme']] '''

def rhyme(string1,string2):
    length1=len(string1)
    length2=len(string2)

    if string1[length1-1]==string2[length2-1] and string1[length1-2]==string2[length2-2] :
        return True
    return  False

def rhymeGroup(stringList):
    rhymeList=[]

    for i in stringList:
        newRhyme=[]
        for j in stringList:
            if rhyme(i,j)==True:
                newRhyme+=[j]

        if rhymeList.count(newRhyme)==0:
            rhymeList+=[newRhyme]

    return rhymeList

print(rhymeGroup(['ana', 'banana', 'carte', 'arme', 'parte']))