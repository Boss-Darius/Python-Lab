
'''Lab4 2'''

'''
Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek 
(the last two methods should return None if no element is present in the queue).
'''

class Queue:
    def __init__(self):
        self.numberList=list()
    def Push(self,number):
        self.numberList+=[number]

    def Pop (self):
        if len(self.numberList)==0:
            return None
        else:

            result=self.numberList[0]
            del self.numberList[0]
            return result

    def Seek (self):
        if len(self.numberList)==0:
            return None
        else:
            return self.numberList[0]

    def GetQueue(self):
        return self.numberList

q1=Queue()

q1.Push(1)
q1.Push(2)
q1.Push(3)

print(q1.GetQueue())
q1.Pop()
print(q1.GetQueue())