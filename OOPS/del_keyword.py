# del keyword is used to delete object properties or object itself.

class Student:
    def __init__(self,name):
        self.name=name 

s1 = Student("shradha")

print(s1.name)
del s1.name 
print(s1.name) #shows error