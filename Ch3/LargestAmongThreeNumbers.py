a = int(input("Please Enter the First Number\n"))
b = int(input("Please Enter the Second Number\n"))
c = int(input("Please Enter the Third Number\n"))

if (a > b) and (a > c):
    print("a is the largest among three numbers.")

elif(b > a) and (b > c):
    print("b is the largest among three numbers.")

else:
    print("c is the largest among three numbers.")