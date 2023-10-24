'''Lab2_5'''

'''Write a function that receives as parameter a matrix and will 
return the matrix obtained by replacing all 
the elements under the main diagonal with 0 (zero).'''

def zero(matrix):
    newMatrix=matrix

    dimension=len(matrix)

    for i in range(1,dimension):
        for j in range(0,i):
            newMatrix[i][j]=0

    return newMatrix

matrix= [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
print("matrix before:")
for i in range(0,len(matrix)):
    print(matrix[i])

matrix=zero(matrix)
print("matrix after:")
for i in range(0,len(matrix)):
    print(matrix[i])

