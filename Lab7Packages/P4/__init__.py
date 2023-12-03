import random

def RandomPasswordGeneration(length,specialCharacterPositions,NumberPositions,MixCasePositions):
    numbers=[0,1,2,3,4,5,6,7,8,9]
    specialCharacters=['!','@','#','$','%','^','&','*','~']
    currentCase=random.randint(0,1)
    password=""

    for i in range(0,length):
        character=random.randint(0,length)
        if i in specialCharacterPositions:
            password+=specialCharacters[character%len(specialCharacters)]
        elif i in NumberPositions:
            password += str(numbers[character % len(numbers)])
        elif i in MixCasePositions:
            if currentCase==0:
                password += chr(character).upper()
            else:
                password+= chr(character).lower()
        else:
            password+= chr(character)

    return password
