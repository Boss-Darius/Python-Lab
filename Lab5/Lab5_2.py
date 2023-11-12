'''Lab5_2'''

'''
Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. 
Implement methods for deposit, withdrawal, and interest calculation.
'''

class Account:
    def __init__(self):
        self.name="Account"
        self.credit=0

    def Deposit(self,amount):
        self.credit+=amount

    def Withdrawal(self,amount):
        self.credit-=amount

class SavingsAccount(Account):
    def __init__(self,maximumWithdrawals,percentage):
        self.credit=0
        self.maximumWithdrawals=maximumWithdrawals
        self.interest=0
        self.percentage=percentage

    def Deposit(self,amount):
        self.credit += amount
        self.interest+=self.credit*self.percentage/100

    def Withdrawal(self,amount):
        if self.maximumWithdrawals==0:
            print("Can not withdrawal from this account anymore")
        elif self.credit-amount<=0:
            print("Not enough credit")
        else:
            self.credit-=amount
            self.maximumWithdrawals-=1
    def GetIntereste(self):
        return self.interest

class CheckingAccount(Account):
    def __init__(self,feePercentage,amount,minAmount,percentage):
        self.credit=amount
        self.feePercentage=feePercentage
        self.minAmount=minAmount
        self.interest=0
        self.percentage=percentage


        if(amount<minAmount):
            self.credit=0

    def Deposit(self,amount):
        self.credit += amount
        self.interest += self.credit * self.percentage / 100
    def Withdrawal(self,amount):
        if(self.credit<=amount):
            self.credit=0
            self.minAmount=self.minAmount+(amount-self.credit)*(self.feePercentage/100)
        else:
            self.credit-=amount
    def GetInterest(self):
        return self.interest

print("Savings Account")
savingsAccount=SavingsAccount(5)
savingsAccount.Deposit(100)
savingsAccount.Withdrawal(200)

for i in range(0,4):
    savingsAccount.Withdrawal(5)
print(savingsAccount.credit)
savingsAccount.Withdrawal(5)
print()

print("Checking Account")

checkingAccount=CheckingAccount(5,200,20)
checkingAccount.Withdrawal(20)
print(checkingAccount.credit,' ',checkingAccount.minAmount)
checkingAccount.Withdrawal(200)
print(checkingAccount.credit,' ',checkingAccount.minAmount)


