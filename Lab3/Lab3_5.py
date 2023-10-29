'''Lab3 5'''

'''The validate_dict function that receives as a parameter a set of tuples 
( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary. 
A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with 
"prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
The function will return True if the given dictionary matches all the rules, False otherwise.

Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} and 
d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False 
because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
'''

def dictionaryValidation(restrictionSet,dictionary):
    '''if the dictionary doesn't have enough keys it's not valid'''
    if len(restrictionSet)!=len(dictionary):
        print("length problem")
        return False
    dictionaryKeys=list(dictionary.keys())
    restrictionList=[]

    for i in restrictionSet:
        restrictionList+=[i]
    restrictionList=sorted(restrictionList,key=lambda i:i[0])
    '''checking if the keys are correct'''
    index=0
    for i in restrictionList:
        if i[0]!=dictionaryKeys[index]:
            print(i[0],' ',dictionaryKeys[index])
            print("keys problem")
            return False
        index=index+1


    index=0
    dictionaryValues=list(dictionary.values())
    for i in restrictionList:
        if dictionaryValues[index].startswith(i[1])==False or dictionaryValues[index].find(i[2])==-1 or dictionaryValues[index].endswith(i[3])==False:
            print("values problem 1")
            return False

        substring=dictionaryValues[index].removeprefix(i[1])
        substring=substring.removesuffix(i[3])
        if substring.find(i[2])==-1:
            print("problem with middle restriction")
            return False

        index=index+1

    return True

s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}

d= {"key1": "come inside, it's too cold out", "key2": "start middle winter"}
print(dictionaryValidation(s,d))

