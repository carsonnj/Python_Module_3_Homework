import os
import csv

budgetCsv = os.path.join(os.getcwd(),'resources','budget_data.csv')
#variables
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []
#Open and read csv
with open(budgetCsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #read first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    #for loop to go through each row after headers
    for row in csvreader:
        dates.append(row[0])
        #calculate change in daily P&L
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        #count months
        total_months += 1
        #total net amount of P&L over whole timeframe
        total_pl = total_pl + int(row[1])
    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
#print data Points
print("Financial Analysis")
print("---------------------")
# number of months
print(f"Total Months: {str(total_months)}")
# total profit/loss from begining to end
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))