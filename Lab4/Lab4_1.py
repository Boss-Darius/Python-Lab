'''Lab4 1'''
'''
Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek 
(the last two methods should return None if no element is present in the stack).
'''

class Stack:
    def __init__(self):
        self.numberList=list()
    def Push(self,number):
        self.numberList+=[number]





    def Pop (self):
        if len(self.numberList)==0:
            return None
        else:

            result=self.numberList[-1]
            del self.numberList[-1]
            return result

    def Seek (self):
        if len(self.numberList)==0:
            return None
        else:
            return self.numberList[-1]

    def GetStack(self):
        return self.numberList


stack1=Stack()
stack2=Stack()
print(stack1.GetStack())
stack1.Push(1)
print(stack1.GetStack())
print(stack1.GetStack())
stack1.Push(2)
stack1.Push(3)
print(stack1.GetStack())
print(stack2.GetStack())

print(stack1.Seek())
print(stack2.Seek())

stack1.Pop()
print(stack1.GetStack())