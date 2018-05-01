import csv

# Define the filename as Variable
input_csv = 'input_csv.csv'

with open(input_csv, 'r', newline='') as csvFile:
    csvFileReader = csv.reader(csvFile, delimiter=';')

    person_list = list(csvFileReader)

for item in person_list:
    print(item)


