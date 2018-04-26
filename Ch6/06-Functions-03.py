
# Function to calculate the HCF
# number1 and number2 are parameters


def calculate_hcf(number1, number2):

    while(number2):
        number1, number2 = number2, number1 % number2

    print ("The HCF is : ", number1)


number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))
number4 = int(input("Enter Fourth Number : "))

# Calling the Function to Calculate the HCF
calculate_hcf(number1, number2)

# Calling the Function to calculate the HCF
calculate_hcf(number3, number4)
