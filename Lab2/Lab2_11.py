'''Lab2_11'''

'''Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]'''

def orderKey(stringTuple):
    return stringTuple[1][2]

def orderingList(tupleList):
    return sorted(tupleList, key=lambda element: orderKey(element))

print(orderingList([('abc', 'bcd'), ('abc', 'zza')]))