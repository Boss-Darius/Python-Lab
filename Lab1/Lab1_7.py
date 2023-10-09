text="An apple is 123 USD"

found=0
number=""
numbers="1234567890"

for i in range(0,len(text)):
    if text[i] in (numbers) and found==0:
        found=1
        number=number+text[i]

        for j in range(i+1,len(text)-1):
            if text[j] in numbers:
                number=number+text[j]
            else:
                break
    elif found==1:
        break

print(number)