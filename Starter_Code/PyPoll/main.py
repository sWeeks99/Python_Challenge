import os
import csv

csvpath = os.path.join("Resources", "election_data.csv") #removed ".." due to directory error

#title prompt
print("Election Results\n----------------------------")

voter_count = 0
names = []
name_counts = {}
charles = 'Charles Casper Stockham'
diana = 'Diana DeGette'
raymon = 'Raymon Anthony Doane'

#The total number of votes cast
with open(csvpath, encoding= 'UTF-8') as csvfile:   #same encoding used in prior activities
    csvreader = csv.reader(csvfile)
    next(csvreader) #skips header
    
    for row in csvreader:
        voter_count += 1
        names.append(row[2])    #third column

#Count the occurrences of each name
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1

#To calculate the total count of all names
total_count = sum(name_counts.values())

#To count specific candidates' names
person_count_charles = name_counts.get(charles, 0)
person_count_diana = name_counts.get(diana, 0)
person_count_raymon = name_counts.get(raymon, 0)

#Calculate the percentages
percentage_charles = (person_count_charles / total_count) * 100
percentage_diana = (person_count_diana / total_count) * 100
percentage_raymon = (person_count_raymon / total_count) * 100
#round to nearest thousandth
percentage_charles = round(percentage_charles, 3)
percentage_diana = round(percentage_diana, 3)
percentage_raymon = round(percentage_raymon, 3)


#Candidate with the most votes
winner_name = max(name_counts, key=name_counts.get)

print(f"Total Votes: {voter_count}\n----------------------------")
print(f"Charles Casper Stockham: {percentage_charles}% ({person_count_charles})")
print(f"Diana DeGette: {percentage_diana}% ({person_count_diana})")
print(f"Raymon Anthony Doane: {percentage_raymon}% ({person_count_raymon})")
print(f"-------------------------\nWinner: {winner_name}\n-------------------------")