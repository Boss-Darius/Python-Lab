matrix=[
            ['f','i','r','s'],
            ['n','_','l','t'],
            ['o','b','a','_'],
            ['h', 't','y','p'],
        ]

length=len(matrix)

str=""

for k in range(0,int(length//2)):
    for i in range (k,length-1-k):
        str=str+matrix[k][i]

    for i in range (k,length-1-k):
        str=str+matrix[i][length-1-k]

    for i in range (k,length-1-k):
        str=str+matrix[length-1-k][length-1-i]

    for i in range (k,length-1-k):
        str=str+matrix[length-1-i][k]

print(str)