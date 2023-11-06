'''Lab4 3'''

'''Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. 
The class should provide methods to access elements (get and set methods) and some methematical functions 
such as transpose, matrix multiplication and a method that allows iterating through all elements form a matrix an 
apply a transformation over them (via a lambda function).
'''

class Matrix:
    def __init__(self,rows,cols):
        self.n=rows
        self.m=cols
        self.row=[]

        for i in range(0,self.n):
            col=[]
            for i in range(0,self.m):
                col+=[i]

            self.row+=[col]


    #am facut optionalul de Quantum, mi-a raams ideea de dagger pentru transpusa
    def DaggerMatrix(self):
        daggerMatrix=[]

        for j in range(0,self.m):
            col=[]
            for i in range(0,self.n):
                col+=[self.row[i][j]]
            daggerMatrix+=[col]

        return daggerMatrix

    def MatrixMultiplication(self,matrix):

        if self.m != matrix.n: print("These matrixes can not be multiplied!")

        else:
            result=[]
            for i in range(0,self.n):
                row=[]
                for j in range(0,matrix.m):
                    row+=[0]
                    for k in range(0,matrix.n):
                        row[j]+=self.GetElement(i,k)*matrix.GetElement(k,j)
                result+=[row]

            return result

    def Transformation(self,function):
        for i in range(0,self.n):
            for j in range(0,self.m):
                self.row[i][j]=function(self.row[i][j])

    def GetElement(self,row,col):
        return self.row[row][col]

    def SetElement(self,row,col,value):
        self.row[row][col]=value

    def GetMatrix(self):
        return self.row


m1=Matrix(3,4)
m2=Matrix(4,3)
m1.SetElement(0,0,9)
print(m1.GetElement(0,0))
print(m1.GetMatrix())
print(m1.DaggerMatrix())

print(m1.MatrixMultiplication(m2))

m1.Transformation(lambda x: x+1)

print(m1.GetMatrix())