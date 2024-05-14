# idea
# object oriented programming
# modeling our problem as real word objects

# car
# what makes a car?
# 1.engine 
# 2.wheels
# 3.name
# 4.doors

# car
# 1.engine - v8
# 2.wheels - 4
# 3.name - ferrari
# 4.doors - 2

# 1.engine - v4
# 2.wheels - 4
# 3.name - alto
# 4.doors - 4

# car - blueprint | class

class Car:
    def __init__(self,name,engine,wheels,doors):
        # creating obj calls init(constructor)
        self.name=name
        self.engine=engine
        self.wheels=wheels
        self.doors=doors

ferrari = Car("ferrari","v8",4,2) #object
alto=Car("alto","v4",4,4) #object

print(type(ferrari))

# encapsulation - properties + action(logic) + access

# inheritance-can overide the base class 

class Animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        return"some sound"
class Dog(Animal):
    def __init__(self,name,speed):
        super().__init__(name) # base class constructor
        self.speed=speed
    def run(self):
        return "🐕 wags tail !!"
    # method overiding -> polymorphism(its like water {changes according the class it is in})
    def speak(self):
        return"woofff!!"
    
    def speed_bonus(self):
        return f"{self.name} is running at {self.speed * 2} km/hr"
        
toby= Animal("toby")

maxy= Dog("maxy",20)
print(toby.speak())
print(maxy.speak())
print(maxy.speed)
print(maxy.speed_bonus())