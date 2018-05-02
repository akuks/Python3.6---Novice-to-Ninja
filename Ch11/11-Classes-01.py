from Calculator import *

number1 = input("Enter the First Number: ")
number2 = input("Enter the Second Number: ")

# Create an Object
calc = Calculator()

# calc.multiply is way to called multiply function
print("Multiplication of two numbers is : ", calc.multiply(number1, number2))

print("Division of two numbers is : ", calc.division(number1, number2))

print("Addition of two numbers is :", calc.addition(number1, number2))

print("Subtraction of two numbers is :", calc.subtraction(number1, number2))
