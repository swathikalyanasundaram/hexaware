# static method vs class method | both decorators
# super charge to the normal method
# static method
# normal function

# classmethod

# perimeter 2 * pi * r

pi = 3.14
def perimeter(radius):
    return 2 * pi * radius

class Circle:
    pi = 3.14

    def __init__(self,radius):
        self.radius=radius
 
    @staticmethod
    def perimeter(radius):
        return 2 * Circle.pi * radius
    
    @classmethod
    def from_diameter(cls,diameter):
        radius = diameter/2
        return cls(radius)
        
    
    def calc_area(self):
        return Circle.pi * self.radius ** 2

# normal function but inside the class | no access to self    
print(Circle.perimeter(2))

#instance method
circle1=Circle(4)
print(circle1.calc_area())

#class method - to construct the object
circ_from_dia = Circle.from_diameter(10)
print(circ_from_dia.calc_area()) # 78.5
