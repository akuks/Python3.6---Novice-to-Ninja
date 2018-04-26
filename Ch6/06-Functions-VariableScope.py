def function_scope():
    number1 = 56
    string1 = "Hello, I am scoped string1 variable in side function"

    print("I am local number1 variable inside function: " + str(number1))
    print(string1)


number1 = 24
string1 = "Hello, I am global string1 variable"

print("I am global number1 variable : " + str(number1))
print(string1)

# Calling the Function
function_scope()