firstString="ng"
secondString="bingchiling"

condition=secondString.find(firstString)

occurence=[]

if condition>0:
    occurence=secondString.split(firstString)
    print(len(occurence)-1)

else:
    print(0)