letters="azwsxedcrfvtgbyhnujmikolpAQZWSXEDCRFVTGBYHNUJMIKOLP"

occurences=  {     }

text="an apple is not a tomato"

for i in range(0,len(text)):
    if text[i] not in occurences and text[i] in letters:
        occurences[text[i]]=0
for i in range(0,len(text)):
    if text[i] in occurences:
        occurences[text[i]]= occurences[text[i]]+1
max=0
letter=""
for i in occurences:
    if max<occurences[i]:
        max=occurences[i]
        letter=i

print(letter)