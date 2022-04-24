import os
import csv
budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")
#Create Lists
date = []
total_profit = []
profit_change = []
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    print(f"Header: {header}")
    for row in csv_reader:
        date.append(row[0])
        total_profit.append(int(row[1]))    
     
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])

average_profit_change = round(sum(profit_change)/ len(profit_change),2)
maximum = max(profit_change)
minimum = min(profit_change)
date_maximum = date[profit_change.index(maximum)+1]
date_minimum = date[profit_change.index(minimum)+1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {average_profit_change}")
print(f"Greatest Increase in Profits: {date_maximum} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {date_minimum} (${(str(minimum))})")

text_file = open("Budget_Summary.txt", "w")
n = text_file.write(
"Financial Analysis\n"
"------------------------\n"
f"Total Months: {len(date)}\n"
f"Total: ${sum(total_profit)}\n"
f"Average Change: ${average_profit_change}\n"
f"Greatest Increase in Profits: {date_maximum} (${maximum})\n"
f"Greatest Decrease in Profits: {date_minimum} (${minimum})\n")
text_file.close()