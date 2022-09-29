# Your task is to create a Python script that analyzes the records to calculate,
# each of the following:
#Import .csv file
import os

import csv
#Read in .csv file
csv_file = os.path.join("Resources",'budget_data.csv')

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average,
# of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period