# class Student:
#     name = "Nehal Garg"

# rollOne = Student()
# print(rollOne.name)

## __init__ function: It is a constructor in all the classes , which is always get executed when the object is being initiated. 

## The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Student:

    college_name = "Graphic Era" ## class attribute are common for every students, so we make it a class attribute. class attribute are stored once in the memory and has a fixed location.
    age = 22
    #default constructor
    def __init__(self):
        pass
    
    ## parameterized constructor
    def __init__(self, fullname,age):
        self.name = fullname 
        self.age = age ## precedence of object attribute > class attribute

    def welcome(self):
        print("Welcome student")

    def get_age(self):
        return self.age

s1 = Student("Nehal",25)
print(s1.name,s1.age)


s1.welcome()
print(s1.get_age())

