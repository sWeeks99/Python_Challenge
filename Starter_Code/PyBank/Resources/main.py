import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#title prompt
print("Financial Analysis\n----------------------------")

#The total number of months included in the dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_count = 0

with open(csvpath, encoding= 'UTF-8') as csvfile:   #same encoding used in prior activities
    csvreader = csv.reader(csvfile)
    next(csvreader) #skips header
    for row in csvreader:
        month = row[0].split('-')[0] #separated from profit/losses
        if month in months: #*
            month_count += 1
print(f"Total Months: {month_count}")

#Net Total amount of "Profit/Losses" over the entire period
import csv

total = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  #skips header
    
    for row in csvreader:
        if len(row) == 2:  #len for integers
            profit_loss = int(row[1])
            total += profit_loss
print(f"Total: ${total}")

#The Average in "Profit/Losses" changes
import csv

changes = []
prev_value = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  #skips header

    for row in csvreader:
        if len(row) == 2:  #len for integers
            profit_loss = int(row[1])    
            if prev_value != 0:
                change = profit_loss - prev_value
                changes.append(change)
            prev_value = profit_loss
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0
average_change = round(average_change, 2)   #round to nearest hundredth
print(f"Average Change: ${average_change}")

#Greatest increase in profits (date and amount)
import csv

great_increase = 0
great_increase_month = ""

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  #skips header
    data = list(csvreader)

for i in range(1, len(data)): #iterate to find the greatest increase in profits
    current_profit = int(data[i][1])
    previous_profit = int(data[i-1][1])
    profit_change = current_profit - previous_profit

    if profit_change > great_increase:
        great_increase = profit_change
        great_increase_date = data[i][0]
print(f"Greatest Increase in Profits: {great_increase_date} (${great_increase})")

#Greatest decrease in profits (date and amount)
import csv

great_decrease = 0
great_decrease_month = ""

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  #skips header
    data = list(csvreader)

for i in range(1, len(data)): #iterate to find the greatest increase in profits
    current_profit = int(data[i][1])
    previous_profit = int(data[i-1][1])
    profit_change = current_profit - previous_profit

    if profit_change < great_decrease:  #same format as previous, just flip the inequality sign
        great_decrease = profit_change
        great_decrease_date = data[i][0]
print(f"Greatest Increase in Profits: {great_decrease_date} (${great_decrease})")