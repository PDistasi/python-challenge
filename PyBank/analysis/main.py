# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
#Import .csv file
import os

import csv

#Import statistics to calculate mean (found online)
import statistics

#Read in .csv file
file = os.path.join("PyBank","Resources", "budget_data.csv")

#create lists to store data
profits = []
changes = []
date = []

#Set counters to 0
month = 0
profit = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0

#Open source file and encode
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#Skip the header line in file
    next(csvreader)
    
#Begin looping through and analyzing data
    for row in csvreader:
        
#The total number of months included in the dataset
        month += 1
        
#Populate date list for later use
        date.append(row[0])
        
#The net total amount of "Profit/Losses" over the entire period
        profit += int(row[1])
        
#If statement to calculate top profit and loss
#The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > greatest_increase:
            top_profit = (row[0])
            greatest_increase = int(row[1])
        
#The greatest decrease in profits (date and amount) over the entire period
        elif int(row[1]) < greatest_decrease:
            top_loss = (row[0])
            greatest_decrease = int(row[1])
        changes.append(int(row[1]))

#Calculate monthly changes (dollar amount)
for i in range(len(changes)-1):
    total_change = (changes[i+1] - changes[i])
    profits.append(total_change)
    
#Assign variables for display
max_profits = max(profits)
min_profits = min(profits)

max_date = date[profits.index(max_profits)+1]
min_date = date[profits.index(min_profits)+1]
    
# #calculate average profits    
average_change = round(statistics.mean(profits),2)

# #print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month}")
print(f"Total: ${profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {(max_date)} (${max_profits})")
print(f"Greatest Decrease in Profits: {(min_date)} (${min_profits})")

# #Create .txt file with same results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {month}\n")
f.write(f"Total: ${profit}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits: {max_date} (${max(profits)})\n")
f.write(f"Greatest Decrease in Profits: {min_date} (${min(profits)})\n")

