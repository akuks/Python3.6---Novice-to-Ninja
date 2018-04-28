import os

# Prompt User to Enter the FileName
fileName = str(input("Please Enter the file Name: "))

fileName = fileName.strip()

while not fileName:
    print("Name of the File Cannot be left blank.")
    print("Please Enter the valid Name of the File.")
    fileName = str(input("Please Enter the file Name: "))
    fileName = fileName.strip()

# Check if the file Entered by the User exists
if not os.path.exists(fileName):
    print(fileName, " does not exists")
    print("Exiting the Program")
    exit(1)

print("File Name Entered by the User is : ", fileName)

fh = open(fileName, 'r')

for line in fh:
    print(line)
