'''Lab5 4'''

'''
Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like
Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their 
roles.
 '''

class Employee:
    def __init__(self,salary,name):
        self.salary=salary
        self.name=name

class Manager(Employee):
    def __init__(self,salary,name,employeesList):
        super().__init__(salary,name)
        self.employeesList=employeesList

    def Manage(self,employee):
        if employee in self.employeesList:
            print("I already manage this employee")
        else:
            self.employeesList+=[employee]

class Engineer(Employee):
    def __init__(self,salary,name,doneProjects,remainingProjects):
        super().__init__(salary,name)
        self.doneProjects=doneProjects
        self.remainingProjects=remainingProjects

    def DoProject(self,project):
        if len(self.remainingProjects)==0:
            print("My job is done")
        elif project in self.doneProjects:
            print("Project already done")
        elif project not in self.remainingProjects:
            print("Project is not assigned")
        else:
            self.doneProjects+=[project]
            self.remainingProjects.remove(project)
class SalesMan(Employee):
    def __init__(self,name,salary,products):
        super().__init__(name,salary)
        self.products=products
    def Sell(self,product):
        if product not in self.products:
            print("I can;t sell I don't have")
        else:
            self.products.remove(product)

    def Purchase(self,product):
        self.products+=[product]

engy=Engineer(1555,"Dave",[],['a','b'])
engy.DoProject('a')
print(engy.remainingProjects,' ',engy.doneProjects)
