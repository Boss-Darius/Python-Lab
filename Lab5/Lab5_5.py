'''Lab5 5'''

'''
Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird, and 
Fish. Add properties and methods to represent characteristics unique to each animal group.
'''

class Animal:
    def __init__(self,name,scientificName,lifespan,diet):
        self.name=name
        self.scientificName=scientificName
        self.lifespan=lifespan
        self.diet=diet


class Mammal(Animal):
    def __init__(self,name,scientificName,lifespan,diet,coat,sheding):
        super().__init__(name,scientificName,lifespan,diet)
        self.coat=coat
        self.sheding=sheding

    def Description(self):
        return ("Fluffy bastards that are totally dependet on their parents upon birth."
                "They all  give birth and feed their young milk, except the Platypus(the regn's"
                "''Gica contra'') who's just absolutely wierd(I still respect Perry the Platypus)")

    def Shed(self):
        if self.sheding>self.coat:
            print("Not yet")
        else:
            self.coat-=self.sheding
    def CoatGrow(self,extraCoat):
        self.coat+=extraCoat

class Bird(Animal):
    def __init__(self,name,scientificName,lifespan,diet,migrates,sound):
        super().__init__(name,scientificName,lifespan,diet)
        self.migrates=migrates
        self.sound=sound

    def Sing(self):
        return self.sound

    def Migrate(self):
        if self.migrates== True:
            return "See you around!"
        else:
            return "I shall hold the line"

    def Description(self):
        return ("Gouverment best spying device!"
                "Do you think it's just a coincidence that pigeons mess with your car?"
                "THINK AGAIN!")

class Amphybian(Animal):
    def __init__(self,name,scientificName,lifespan,diet,toxic,isHibernating):
        super().__init__(name,scientificName,lifespan,diet)
        self.toxic=toxic
        self.isHibernating=isHibernating

    def IsToxic(self):
        if self.toxic==True:
            return "I lost because of lag"
        else:
            return "GG WP!"

    def Description(self):
        return "The only animal class with an imortal member(Axolotl will never die)"

    def HibernateCycle(self):
        self.isHibernating=not(self.isHibernating)

class Reptile(Animal):
    def __init__(self,name,scientificName,lifespan,diet,bodyTemp,scalesThickness):
        super().__init__(name,scientificName,lifespan,diet)
        self.bodyTemp=bodyTemp
        self.scalesThickness=scalesThickness

    def Description(self):
        return "Cold-blooded creatures (Just like FII teachers when they grade students)"

    def Heating(self,temp):
        while(self.bodyTemp<temp):
            self.bodyTemp+=0.1
    def Cooling(self,temnp):
        while(self.bodyTemp>temnp):
            self.bodyTemp-=0.1
    def Shed(self):
        self.scalesThickness=0.1

    def TickenScales(self):
        self.scalesThickness+=0.2

class Fish(Animal):
    def __init__(self,name,scientificName,lifespan,diet,size):
        super().__init__(name,scientificName,lifespan,diet)
        self.size=size

    def Edible(self):
        if self.size<1.5:
            return "Good appetite!"
        else:
            return "I doubt you can eat that before it eats you"

    def Description(self):
        return ("The evolution says these guys got out of water and turn into humans..."
                "Take one out of water and we will see how true that statement is")

class Artropod(Animal):
    def __init__(self,name,scientificName,lifespan,diet,nrEyes,venomous,poisonous):
        super().__init__(name,scientificName,lifespan,diet)
        self.nrEyes=nrEyes
        self.venomous=venomous
        self.poisonous=poisonous

    def GetView(self):
        return self.nrEyes*18

    def IsVenomous(self):
        if self.venomous==True:
            return "If it bites you you will die"
        else:
            return "If it bites you you will not die"

    def IsPoisonous(self):
        if self.poisonous:
            return "If it touches you you will die"
        else:
            return "If it touches you you will not die"

    def Description(self):
        return ("They are so small that if you touch them you may break their whole body,"
                "Yet still they can make a grown adult heart stop just by existing in their proximity")
