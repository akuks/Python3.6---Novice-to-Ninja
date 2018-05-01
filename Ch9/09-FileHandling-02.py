# Define the fileName as a variable
fileToWrite = 'outputFile.txt'

fileHandle = open(fileToWrite, 'w')

i = 0

while i < 10:
    fileHandle.write("This is line Number " + str(i) + "\n")
    i += 1

fileHandle.close()
