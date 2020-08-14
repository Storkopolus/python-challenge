import os
import csv

#Collect data form the resources folder
csvpath = os.path.join ('Resources', 'budget_data.csv')

with open (csvpath, 'r') as csvfile:
     #Split on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    header = next(csvreader)

    #define variables
    month = []
    revenue = []
    revenue_change = []
    greatest_increase = int()
    greatest_increase_month = []
    greatest_decrease = int()
    greatest_decrease_month = []

    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])

    #Obtain revenue based on csv
    revenue_int = map(int, revenue)
    total_revenue = (sum(revenue_int))

    #Avg Change
    i=0
    for i in range(len(revenue) - 1):
        revenue_loss = int(revenue[i + 1]) - int(revenue[i])

    #Profit Avg Change
        revenue_change.append(revenue_loss)
        Total = sum(revenue_change)  

    #Average Monthly Change
        average_monthly_change = Total / len(revenue_change)
    
    #Calc Greatest Increase
        if revenue_change [i] > revenue_change [i + 1]:
            greatest_change = revenue_change
            greatest_increase_month = row[0]
    
    #Calc Greatest Decrease
        if revenue_change [i] < revenue_change [i + 1]:
            greatest_decrease = revenue_change
            greatest_decrease_month = row[0]

    highest = max


#Print analysis
print(f"Financial Analaysis")
print(f"----------------------------")
print(f"Total Months : {len(revenue_change) + 1}")
print(f"Total:  ${total_revenue}")
print(f"Average Change: {average_monthly_change}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, ${greatest_increase} ")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, ${greatest_decrease}")

