# xmlparser.py
# First row of the csv file must be header!

# example CSV file: baseball_salaries_2003.csv
# team,player,salary,position
# New York Yankees ,"Acevedo Juan",900000,Pitcher

import csv

csvFile = 'baseball_salaries_2003.csv'
xmlFile = 'baseball_salaries_2003.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<csv_data>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")

    rowNum +=1

xmlData.write('</csv_data>' + "\n")
xmlData.close()
