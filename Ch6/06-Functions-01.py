number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))
number4 = int(input("Enter Fourth Number : "))

if number1 > number2:
    small = number2
else:
    small = number1

small = small + 1
for divisor in range(1, small):
    if (number1 % divisor == 0) and (number2 % divisor == 0):
        hcf = divisor

print ("The HCF of ", number1, " and ", number2, "is : ", hcf)

if number3 > number4:
    small = number4
else:
    small = number3

small = small + 1
for divisor in range(1, small):
    if (number3 % divisor == 0) and (number4 % divisor == 0):
        hcf = divisor

print ("The HCF of ", number3, " and ", number4, "is : ", hcf)
