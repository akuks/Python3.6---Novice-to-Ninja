def multiply(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1/number2


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    if number1 > number2:
        return number1 - number2
    else:
        return number2 - number1


value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")

print ("Multiplication of two Number is : ", multiply(value1, value2))

print ("Division of two number is : ", division(value1, value2))

print ("Addition of two number is : ", addition(value1, value2))

print ("Subtraction of two number is : ", subtraction(value1, value2))

