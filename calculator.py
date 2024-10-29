import math
def addition(x,y):
    print(x, " + ", y, " = ", x+y)
def subtraction(x,y):
    print(x, " - ", y, " = ", x-y)
def multiplication(x,y):
    print(x, " x ", y, " = ", x*y)
def division(x,y):
    print(x, "/", y, " = ", x/y)
def square_root(x,y):
    print("Root ", x, " = ", math.sqrt(x))
    print("Root ", y, " = ", math.sqrt(y))
def square(x,y):
    print(x, "^2 = ", x*x)
    print(y, "^2 = ", y*y)
while 1:
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Square root")
    print("6 - Square")
    print("7 - Exit")
    choice=int(input("Enter your choice - "))
    if choice==7:
        print("Terminated")
        break
    x=int(input("Enter first number - "))
    y=int(input("Enter the second number - "))
    if choice==1:
        addition(x,y)
    elif choice==2:
        subtraction(x,y)
    elif choice==3:
        multiplication(x,y)
    elif choice==4:
        division(x,y)
    elif choice==5:
        square_root(x,y)
    elif choice==6:
        square(x,y)
    else:
        print("Invalid command")
    

