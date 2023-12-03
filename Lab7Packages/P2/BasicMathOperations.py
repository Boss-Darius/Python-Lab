def Sum(a,b):
    return a+b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    if b==0: raise ArithmeticError ("Divior is 0")
    else: return a/b

def IntDivision(a,b):
    if b==0: raise ArithmeticError ("Divior is 0")
    else: return int(int(a)/int(b))