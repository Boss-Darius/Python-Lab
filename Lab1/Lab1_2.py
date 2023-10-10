print("Lab1 2)\n")

sir=input()

vowels="aeiouAEIOU"
nrVowels=0

for i in range(0,len(sir)):
    if sir[i] in vowels:
        nrVowels=nrVowels+1

print(nrVowels)