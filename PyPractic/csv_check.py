import csv
import webbrowser

linksList = []

with open('script_check.csv', 'r', newline='') as csvfile:
    incReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in incReader:
        rowStr = (str(row))
        row = rowStr.split(';')
        incLink = row[1]
        linksList.append(incLink)


print(linksList)
for link in linksList:
    webbrowser.open(link, new=2)


