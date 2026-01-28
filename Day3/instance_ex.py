import os

class person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello",self.name)

p = person("Meet")
p.greet()


