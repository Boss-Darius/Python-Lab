letters="qazwsxedcrfvtgbyhnujmikoplAQZWSXEDCRFVTGBYHNUJMIKOLP,.;/[']\"|\n\t1234567890-=`~!@#$%^&*()_+\\<>:?{}"
words=0
letter=0
text=input()
index=0
while index<len(text) and letter==0:
    if text[index] in letters:
        words=words+1
        letter=1

for i in range(0,len(text)-1):
    if text[i] in letters and text[i+1]==' ':
        words=words+1

print(words)