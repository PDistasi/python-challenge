# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
#Import data
import os
import csv

#Set variable and path for csv file
pollcsv = os.path.join("PyPoll\Resources","election_data.csv")

#Create empty lists to store the data from each column
unique_candidates = []
unique_votes = {}

# * The total number of votes cast
#Set variables as integers and start counters at 0
vote = 0
winning_vote = 0

#Open source file and encode
with open(pollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#skip the header line in file
    next(csvreader)
    
#Begin looping through and collecting data
    for row in csvreader:
        #The total number of votes cast
        vote += 1

# * A complete list of candidates who received votes
        #Set variable for 3rd row data capture
        candidate = row[2]
        
# * The total number of votes each candidate won
        if candidate not in unique_candidates:
            #Add candidates as unique values
            
            unique_candidates.append(candidate)
            #Begin tallying unique votes
            unique_votes[candidate] = 0
            
        #Add vote to the unique candidates
        unique_votes[candidate] +=1
        
# print(unique_votes) SUCCESS!
        
#* The percentage of votes each candidate won
    #Loop through vote data per candidate
    for candidate in unique_votes:
        votes = unique_votes[candidate]
        
#       #Perform calculation of unique to total votes
        percentage = (votes) / (vote) * 100
        #Set variable to capture results for printing
        results = (f"{candidate}: {percentage:.3f}% ({votes})\n")git ad
        
# # # * The winner of the election based on popular vote.
        if (votes > winning_vote):
            winning_vote = votes
            winner = candidate
    
# #Print results

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote))
print("-------------------------")
print(results)
print("-------------------------")
print(f"Winner: " + winner)
print("-------------------------")











