number=int(input())
one=0
while number>0:
    if number%2==1:
        one=one+1
    number=int(number//2)

print(one)