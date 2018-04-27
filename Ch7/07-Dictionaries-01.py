# Dictionaries Example

students = {
    'Akash': '0001',
    'Binoy': '0002',
    'Cheteshwar': '0003',
    'Durga': '0004',
    'Vinay': '0005',
    'Yash': '0006'
}

print(students)

# Add Student to Dictionary
students['Yashica'] = '0007'

print("Dictionary --> When new student is added")
print(students)

# Delete Student from Dictionary
del students['Binoy']

print("Dictionary --> When a student is removed")
print(students)

# Traversing a Dictionary

print ('-' * 50)

for key in students:
    print (key, ":", students[key])

