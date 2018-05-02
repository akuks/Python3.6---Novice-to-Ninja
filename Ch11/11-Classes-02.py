from Calculator_01 import *

number1 = input("Enter the First Number: ")
number2 = input("Enter the Second Number: ")

# Create an Object
calc = Calculator(number1, number2)

# calc.multiply is way to called multiply function
print("Multiplication of two numbers is : ", calc.multiply())

print("Division of two numbers is : ", calc.division())

print("Addition of two numbers is :", calc.addition())

print("Subtraction of two numbers is :", calc.subtraction())
