'''Lab5_3'''

'''
Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types 
of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on 
the vehicle type.
'''

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

class Motorcycle(Vehicle):
    def __init__(self,make,model,year,fuel,GVM,GCM):
        super().__init__(make,model,year)
        self.fuel=fuel
        self.GVM=GVM
        self.GCM=GCM

    def Mileage(self):
        return (2023-self.year)*(3000*1.60934)/(self.fuel)*(len(self.make)+len(self.model))

    def TowingCapacity(self):
        return (self.GCM-self.GVM)/2

class Car(Vehicle):
    def __init__(self,make,model,year,fuel,GVM,GCM):
        super().__init__(make,model,year)
        self.fuel=fuel
        self.GVM=GVM
        self.GCM=GCM

    def Mileage(self):
        return (2023-self.year)*16.400/(self.fuel)*(len(self.make)+len(self.model))

    def TowingCapacity(self):
        return (self.GCM-self.GVM)

class Truck(Vehicle):
    def __init__(self,make,model,year,fuel,GVM,GCM):
        super().__init__(make,model,year)
        self.fuel=fuel
        self.GVM=GVM
        self.GCM=GCM

    def Mileage(self):
        return (2023-self.year)*16.40000/(self.fuel)*(len(self.make)+len(self.model))

    def TowingCapacity(self):
        return 4*(self.GCM-self.GVM)

m1=Motorcycle("ceva","ceva",1999,186,100,200)
print(m1.make,' ',m1.model,' ',m1.year)
print("Motorcycle")
print(m1.Mileage(),' ',m1.TowingCapacity())

print()
car=Car("ceva","ceva",1999,500,2900,5885)
print("Car")
print(car.Mileage(),' ',car.TowingCapacity())

print()
truck=Truck("ceva","ceva",1999,750,4500,9885)
print("Truck")
print(truck.Mileage(),' ',truck.TowingCapacity())

