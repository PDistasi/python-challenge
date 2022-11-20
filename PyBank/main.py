# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
#Import .csv file
import os

import csv

#Import statistics to calculate mean (found online)
import statistics

#Read in .csv file
budgetcsv = os.path.join("PyBank","Resources","budget_data.csv")

#create lists to store data
months = []
profits = []
changes = []

#Set counters to 0
month = 0
profit = 0
total_change = 0
total_profit = 0
greatest_increase = 0
greatest_decrease = 0

#Open source file and encode
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#skip the header line in file
    next(csvreader)
    
#Begin looping through and collecting data
    for row in csvreader:
        
#The total number of months included in the dataset
        month += 1
        
#Fill months list
        months.append(row[0])
        
#The net total amount of "Profit/Losses" over the entire period
        total_profit += int(row[1])
        
#If statement to calculate top profit and loss
#The greatest increase in profits over the entire period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
        
#The greatest decrease in profits over the entire period
        elif int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
        changes.append(int(row[1]))

# #calculate monthly changes
for i in range(len(changes)-1):
    monthly_change = (changes[i+1] - changes[i])
    profits.append(monthly_change)
    
#Identify highest and lowest changes
best_profit = max(profits)
worst_loss = min(profits)

#Assign variables for output
highest_profit = profits.index(best_profit)
highest_loss = profits.index(worst_loss)

best_day = months[highest_profit +1]
worst_day = months[highest_loss +1]

# #calculate average profits 
average_change = round(statistics.mean(profits),2)

# #print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {best_day} (${best_profit})")
print(f"Greatest Decrease in Profits: {worst_day} (${worst_loss})")

# #Create .txt file with same results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {month}\n")
f.write(f"Total: ${total_profit}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits: {best_day} (${best_profit})\n")
f.write(f"Greatest Decrease in Profits: {worst_day} (${worst_loss})")

