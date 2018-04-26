# HCF Through Recursion


def calculate_hcf(number1, number2):
    if number1 > number2:
        smaller = number2
        greater = number1
    else:
        smaller = number1
        greater = number2

    if smaller == 0:
        return greater
    elif smaller == 1:
        return 1
    else:
        return calculate_hcf(smaller, greater % smaller)


# User Input


number1 = int(input("Enter First Number : "))
number2 = int(input("Enter Second Number : "))
number3 = int(input("Enter Third Number : "))
number4 = int(input("Enter Fourth Number : "))

print ("The HCF of Numbers ", number1, "and ", number2, " is : ", calculate_hcf(number1, number2))
print ("The HCF of Numbers ", number3, "and ", number4, " is : ", calculate_hcf(number3, number4))