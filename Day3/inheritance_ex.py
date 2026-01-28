import os

class Animal:
    def sound(self):
        print("Animal sound")

    
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

    

d = Dog()
print(d.sound())





