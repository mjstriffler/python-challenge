# Modules
import os
import csv

budget_csv = os.path.join("resources", "budget_data.csv")

# lists and variables
date = []
profit =[]
money = []
count = 0
total_revenue = 0
total_profit = 0
inital_profit = 0
profit_change = 0
revenue_change = []
monthly_change =[]
revenue = []

# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first 
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

# for loop through data for total number of months
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        count += float(row[1])

# total months and revenue
total_months = len(date)
total_revenue += int(row[1])
total_revenue = sum(map(int, money))

# Calculate average profit change

i = 0
for i in range(len(money) - 1):
    profit_loss = int(money[i+1]) - int(money[i])

# append profit_loss and find monthly change

    revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)

# Find greatest monthly increase and decrease

    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = date[k+1]
    
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = date[j+1]

# Print all calculations for the financial analysis

print('Total Months: ' + str(total_months))
print('Total Revenue: ' + str(total_revenue))
print('Average Change: ' + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")


# Output analysis to text file

output_path = os.path.join('analysis', 'budget_data.txt')
with open(output_path, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow(['Total Months: ' + str(total_months)])
    csvwriter.writerow(['Total Revenue: ' + str(total_revenue)])
    csvwriter.writerow(['Average Change: ' + str(monthly_change)])
    csvwriter.writerow([f"Greatest Increase in Profits: {month_increase} (${profit_increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})"])