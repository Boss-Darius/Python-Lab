'''Lab2_2'''

''' Write a function that receives a list of numbers and returns a list of the prime numbers found in it.'''

def primeList(listParam):
    prime=[x for x in listParam if len([d for d in range(2,x//2+1) if x%d==0])==0 and x!=1]

    return prime


print(primeList([1,2,3,4,5,6,7,8,9]))