# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
#Import .csv file
import os

import csv

#Import statistics to calculate mean (found online)
import statistics

#Read in .csv file
budgetcsv = os.path.join("PyBank","Resources","budget_data.csv")

#Set output to text file
text = os.path.join("analysis","financial.analysis.txt")

#create lists to store data
profits = []
changes = []

#Set counters to 0
month = 0
profit = 0
total_change = 0
total_profit = 0
greatest_increase = 0
greatest_decrease = 0
#Set max profit and losses as empty
top_profit = ''
top_loss = ''



#Open source file and encode
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the header line in file
    next(csvreader)
    
    #Begin looping through and analyzing data
    for row in csvreader:
        
        #The total number of months included in the dataset
        month += 1
        
        #The net total amount of "Profit/Losses" over the entire period
        
        profit += int(row[1])
        
        #If statement to calculate top profit and loss
        #The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase:
            top_profit = (row[0])
            greatest_increase = int(row[1])
        
#         #The greatest decrease in profits (date and amount) over the entire period
        elif int(row[1]) < greatest_decrease:
            top_loss = (row[0])
            greatest_decrease = int(row[1])
        changes.append(int(row[1]))

# #calculate monthly changes
for i in range(len(changes)-1):
    total_change = (changes[i+1] - changes[i])
    profits.append(total_change)

# #calculate average profits    
average_change = statistics.mean(profits)

# #print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month}")
print(f"Total: ${profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {top_profit} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {top_loss} (${greatest_decrease})")

# #Create .txt file with same results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {month}\n")
f.write(f"Total: ${profit}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits: {top_profit} (${greatest_increase})\n")
f.write(f"Greatest Decrease in Profits: {top_loss} (${greatest_decrease})\n")

