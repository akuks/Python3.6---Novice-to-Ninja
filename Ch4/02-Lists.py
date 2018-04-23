# List with Zero Elements
our_list = []

# Add Three Numbers to List
our_list.append(1)
our_list.append(24)
our_list.append(7)

# Add Three Strings to the List
our_list.append("First String")
our_list.append("Second String")
our_list.append("Third String")

# Calculate the Number of Items in the List
length_of_our_list = len(our_list)

print("Length of our_list is " + str(length_of_our_list))

# Remove the Last element from the list

our_list.pop(-1)

our_list.pop(0)

print("Length of modified our_list is " + str(length_of_our_list))

