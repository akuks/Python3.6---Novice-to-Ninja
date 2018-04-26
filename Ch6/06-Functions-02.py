
# Function to calculate the HCF
# number1 and number2 are parameters


def calculate_hcf(number1, number2):
    if number1 > number2:
        small = number2
    else:
        small = number1

    small = small + 1
    for divisor in range(1, small):
        if (number1 % divisor == 0) and (number2 % divisor == 0):
            hcf = divisor

    print ("The HCF of ", number1, " and ", number2, "is : ", hcf)


number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))
number4 = int(input("Enter Fourth Number : "))

# Calling the Function to Calculate the HCF
calculate_hcf(number1, number2)

# Calling the Function to calculate the HCF
calculate_hcf(number3, number4)
