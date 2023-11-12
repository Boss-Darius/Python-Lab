'''Lab5 1'''

'''

Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle, Rectangle,
 and Triangle. Implement methods to calculate area and perimeter for each shape.

'''
import math
class Shape:
    def __init__(self,name):
        self.name=str(name)

class Circle(Shape):
    def __init__(self,name,radius):
        self.name="(Circle)"+str(name)
        self.radius=radius

    def GetArea(self):
        return math.pi*self.radius*self.radius

    def GetPerimeter(self):
        return math.pi*2*self.radius

class Rectabgle(Shape):
    def __init__(self,name,length,width):
        self.name="(Rectangle)"+ str(name)
        self.length=length
        self.width=width

    def GetArea(self):
        return self.width*self.length
    def GetPerimeter(self):
        return 2*(self.length+self.width)

class Triangle(Shape):
    def __init__(self,name,l1,l2,l3):
        if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
            print("Invalid values for a triangle's edges")
        else:
            self.name="(Triangle)"+str(name)
            self.l1=l1
            self.l2=l2
            self.l3=l3

    def GetArea(self):
        s=self.GetPerimeter()/2
        return math.sqrt(s*(s-self.l1)*(s-self.l2)*(s-self.l3))

    def GetPerimeter(self):
        return self.l3+self.l2+self.l1


circle=Circle("Shape1",4)
print(circle.name)
print(circle.GetPerimeter())
print(circle.GetArea())
print()

rectagle=Rectabgle("Shape2",4,5)
print(rectagle.name)
print(rectagle.GetPerimeter())
print(rectagle.GetArea())

print()

triangle1=Triangle("Incorect Shape",1,4,1)

triangle2=Triangle("Shape3",4,4,4)
print(triangle2.name)
print(triangle2.GetPerimeter())
print(triangle2.GetArea())
