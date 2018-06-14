import csv

with open('bio.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        # print row
        print row[0], row[1], row[2]


newFile = open('newcsv.csv', 'w')

data = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]

with newFile:
    writer = csv.writer(newFile)
    writer.writerows(data)
