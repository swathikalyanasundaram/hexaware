# Abstract or Interface
# Force other class to implement certain methods
# Autocomplete
from abc import ABC, abstractmethod
 
 
# Abstract class / Interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
    @abstractmethod
    def move(self):
        pass
 
 
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
 
    def move(self):
        print("Runnning... 🐕")
 
    def jump(self):
        print("Jumps 🦘")
 
 
maxy = Dog()
maxy.move()
 

 # bird class

class Bird(Animal):
    def make_sound(self):
        print("tweet tweet")
 
    def move(self):
        print("flyinggg... 🕊️")
 
    def eat(self):
        print("chirp chirp ")

dove=Bird()
dove.make_sound()


