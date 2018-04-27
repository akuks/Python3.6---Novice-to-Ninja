# Dictionaries Example

students = {
    'Akash': {
        'Roll Number': '0001',
        'Stream': 'Electronics',
        'Phone': '872348723',
        'Address': 'Somewhere in New Delhi'
    },
    'Binoy': {
        'Roll Number': '0002',
        'Stream': 'Electronics',
        'Phone': '7647567637',
        'Address': 'Somewhere in Mumbai'
    },
    'Cheteshwar': {
        'Roll Number': '0003',
        'Stream': 'Electronics',
        'Phone': '4563546536',
        'Address': 'Somewhere in Bangalore'
    },
    'Durga': {
        'Roll Number': '0004',
        'Stream': 'Electronics',
        'Phone': '3456536473',
        'Address': 'Somewhere in Chennai'
    },
    'Vinay': {
        'Roll Number': '0005',
        'Stream': 'Electronics',
        'Phone': '63576626347',
        'Address': 'Somewhere in Pune'
    },
    'Yash': {
        'Roll Number': '0006',
        'Stream': 'Electronics',
        'Phone': '5638764765',
        'Address': 'Somewhere in Mumbai'
    }
}

print(students)
print('-' * 50)
print(students['Akash'])

# Add New Student Yashica
students['Yashica'] = {
    'Roll Number': '0007',
    'Stream': 'Electronics',
    'Phone': '5638764765',
    'Address': 'Somewhere in Mumbai'
}

print('-' * 50)
print(students)

# Delete Binoy as he left from school
del students['Binoy']

print('-' * 50)
print(students)

print('-' * 50)
# Looping

for key in students:
    print("Name : ", key)
    for key1 in students[key]:
        print(key1, " : ", students[key][key1])

    print('-' * 50)
