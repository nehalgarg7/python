#input() statement is used to accept values(using keyword) form user.

# string input

name = input("Name : ")

# int input

age = int(input("age: "))

# float input

price = float(input("price: "))

## conditional statement

if age>45:
    print("age is greater than 45") ## you have take 4 spaces because python is an indentation language
elif age<45:
    print("age is less than 45")
else:
    print("age is equal to 45")

## Ternary operator

food = input("food : ")
eat = "Yes" if food == "cake" else "no"
print(eat)