class Calculator(object):

    def multiply(self, number1, number2):
        return number1 * number2

    def division(self, number1, number2):
        return number1 / number2

    def addition(self, number1, number2):
        return number1 + number2

    def subtraction(self, number1, number2):
        if number1 > number2:
            return number1 - number2
        else:
            return number2 - number1
