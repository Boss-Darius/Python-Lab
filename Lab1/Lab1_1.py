print ("Lab1 1)\n")


number1 = int(input())
number2=int(input())

def CMMDC(n1,n2):
    while n1 > 0 and n2 > 0:
        rest = n1 % n2
        n1 = n2
        n2 = rest
    if n1>0:
        return n1
    return n2

cmmdc=CMMDC(number1,number2)

for i in range(0,2):
    cmmdc=CMMDC(cmmdc,int(input()))

print(cmmdc)
