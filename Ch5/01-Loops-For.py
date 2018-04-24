# Initiate for Loop to iterate numbers upto to 100
for number in range(2, 100):

        """
        As we know that prime numbers are divided by 1 and itself
           - All Numbers are divided by 1 and itself. 
        In short prime numbers are not divided by any other number.
        """
        for divisor in range (2, number):

            # Check whether the number is divided by any other numbers
            if (number % divisor == 0):
                break
        else:
            # If the number is not divided by any other number,
            # Print it as Prime Number
            print (number, " is a prime number")