import csv
def getCSVData(fileName):

    # create a empty list to store rows
    rows = []

    # open the csv file
    dataFile = open(fileName, "r")

    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)

    # skip the headers
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
