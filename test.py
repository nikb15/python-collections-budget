import csv

with open('data/spending_data.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        if '-' not in row[3]:
                    continue
        print(row[0],row[1], row[2])
        amount=float((row[3][2:]).replace(',',''))
        print(row[0],row[1], row[2], amount)
            
       