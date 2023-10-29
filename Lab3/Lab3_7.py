'''Lab3_7'''

'''Write a function that receives a variable number of sets and returns a dictionary with the following operations from
 all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are
  two sets, and op is the applied operator: |, &, -. Ex:
  {1,2}, {2, 3} =>
{
    "{1, 2} | {2, 3}":  {1, 2, 3},
    "{1, 2} & {2, 3}":  { 2 },
    "{1, 2} - {2, 3}":  { 1 },
    ...
}

  '''

def setOperationsDictionary(setList):
    setDictionary=dict()

    for i in setList:
        for j in setList:
            if i==j:
                continue
            key=str(i)+" | "+str(j)
            setDictionary[key]=i|j
            key=str(i)+" & "+str(j)
            setDictionary[key]=i&j
            key=str(i)+" - "+str(j)
            setDictionary[key]=i-j
            key=str(i)+" ^ "+str(j)
            setDictionary[key]=i^j

    return setDictionary

print(setOperationsDictionary([{1,2},{2,3},{'a','b','abgcfy'},{'calkiby','kuavdcgty'}]))