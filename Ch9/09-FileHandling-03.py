# Define fileName as a Variable

fileToAppend = 'outputFile.txt'

fileHandling = open(fileToAppend, 'a+')

i = 0

while i < 10:
    fileHandling.write("Append Line Number " + str(i) + " To The File.\n")
    i += 1

fileHandling.close()
