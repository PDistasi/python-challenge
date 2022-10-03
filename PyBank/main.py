# Your task is to create a Python script that analyzes the records to calculate
# each of the following:
#Import .csv file
import os

import csv

#Import statistics to calculate mean (found online)
import statistics

#Read in .csv file
budgetcsv = os.path.join("Resources","budget_data.csv")

#Set output to text file
text = "output.txt"

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
#Set max profit and losses as empty strings
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
        total_profit += int(row[1])
        
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
    monthly_change = (changes[i+1] - changes[i])
    profits.append(monthly_change)

# #calculate average profits (found online)  
average_change = statistics.mean(profits)

# #print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {top_profit} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {top_loss} (${greatest_decrease})")

# #Create .txt file with same results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write("----------------------------")
f.write(f"Total Months: {month}")
f.write(f"Total: ${profit}")
f.write(f"Average Change: ${average_change}")
f.write(f"Greatest Increase in Profits: {top_profit} (${greatest_increase})")
f.write(f"Greatest Decrease in Profits: {top_loss} (${greatest_decrease})")

