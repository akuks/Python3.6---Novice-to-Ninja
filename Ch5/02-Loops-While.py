# Initialize a Counter
counter = 0

# Create Empty List
numbers = []

while counter < 10:
    # Print the value of Counter
    print ("The Value of Counter is " + str(counter))

    # Append counter Value to List
    numbers.append(counter)

    # Print the value of List
    print ("Numbers List : " + str(numbers))

    # Increase the value of Counter by 1, otherwise it will go to an indefinite loop
    counter = counter + 1;

# Iterating the numbers list and print numbers
for number in numbers:
    print("The number in the list is : " + str(number))
