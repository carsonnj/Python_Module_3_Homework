import os
import csv

budgetCsv = os.path.join(os.getcwd(),'resources','budget_data.csv')
# print(budgetCsv)
with open(budgetCsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    # print(header)
    dates = []
    pandl = []
    for row in csvreader:
        dates.append(row[0])
        pandl.append(row[1])
    # print(dates, pandl)
def totalMonths(dates):
    total = len(dates)
    print(total)
totalMonths(dates)
