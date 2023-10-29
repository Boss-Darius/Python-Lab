'''Lab3 3'''

'''Compare two dictionaries without using the operator "==" returning True or False.
(Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
'''

def typeChecking(firstElement,secondElement):
    return type(firstElement) is type(secondElement)

#checking if 2 elements are equal(numbers,boolean values,characters)
def equalityForElements(firstElement,secondElement):
    a = {}
    a[firstElement] = 1
    try:
        a[secondElement]
        return True
    except KeyError:
        return False

def equalityForSets(setA,setB):
    return equalityForElements(len(setA.difference(setB)),0)

def equalityForLists(listA,listB):
    '''checking if the list/tuples have the same length
       so len(listA)=len(listB)
    '''
    if not(equalityForElements(len(listA),len(listB))):
        print('length difference')
        return False

    '''typechecking if all the elements in the lists/tuples have
       the same type (because it doesn't make sense to compare a string to a set)
    '''
    for i in range(0,len(listA)):

        if not(typeChecking(listA[i],listB[i])):
            print('type difference')
            return False
    numbers=[int,float,complex,bool]
    for i in range(0,len(listA)):
        if isinstance(listA[i],set) and not(equalityForSets(listA[i],listB[i])):
            print('sets are not equal')
            return False
        elif isinstance(listA[i],list) and not(equalityForLists(listA[i],listB[i])):
            print('lists are not equal')
            return False
        elif isinstance(listA[i],tuple) and not(equalityForLists(listA[i],listB[i])):
            print('lists are not equal')
            return False
        elif isinstance(listA[i],dict) and not(equalDictionary(listA[i],listB[i])):
            print("dictionaries are not equal")
            return False
        elif (not(isinstance(listA[i],set) or isinstance(listA[i],list) or isinstance(listA[i],tuple) or isinstance(listA[i],dict))
              and not(equalityForElements(listA[i],listB[i]))):
            print('comparing elements')
            return False


    return True


def equalDictionary(dicA,dicB):
    #checking if the dictionaries have the same length (if not they can't be equal)
    if not equalityForElements(len(dicA),len(dicB)):
        print("Dictionaries with different lengths can't be equal")
        return False

    #checking if the keys are identical
    for key in dicA:
        if key not in dicB:
            print("Dictionaries have different keys")
            return False
    #checking the type of every key in the dictionaries
    for key in dicA:
        if not(typeChecking(dicA[key],dicB[key])):
            print("Dictionaries have different types for the same key")
            return False

    for key in dicA:
        if isinstance(dicA[key],set) and not(equalityForSets(dicA[key],dicB[key])):
            print("sets are not equal")
            return False
        elif isinstance(dicA[key],list) and not(equalityForLists(dicA[key],dicB[key])):
            print("lists are not equal")
            return False
        elif isinstance(dicA[key],tuple) and not(equalityForLists(dicA[key],dicB[key])):
            print("tuples are not equal")
            return False
        elif isinstance(dicA[key],dict) and not(equalDictionary(dicA[key],dicB[key])):
            print("subdictionaries  are not equal")
            return False
        elif (not (isinstance(dicA[key], set) or isinstance(dicA[key], list) or isinstance(dicA[key],tuple) or isinstance(dicA[key], dict))
                  and not (equalityForElements(dicA[key], dicB[key]))):
            print('comparing elements')
            return False

    return True

print(equalDictionary({'a':1,'b':{'a':"dicionary"}},{'a':1,'b':(1)}))
