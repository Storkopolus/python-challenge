import os
import csv

#Define file path
budget_csv = os.path.join('Resources','budget_data.csv')

#Define variables to store values we are concerned about
monthcount = 0
total_profit_loss = 0
previous_month = 0
greatest_increase = 0
greatest_decrease = 0
cumulative_increase_decrease = 0

#Import data
with open(budget_csv) as csv_file:

    #Read data, create dictionary if necessary, skip first row as headers
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    csv_dictionary = csv.DictReader(csv_file)

    #Iterate through rows, count, total and store increases/decreases
    for row in csv_reader:
        monthcount = monthcount + 1
        total_profit_loss = total_profit_loss + int(row[1])
        current_month = int(row[1]) 
        increase_decrease = current_month - previous_month

        #Probably could do this more efficienty, but I'm trying to skip the first row, it was messing up the averages.
        if previous_month != 0:
            cumulative_increase_decrease =  cumulative_increase_decrease + increase_decrease

        #Checking against the greatest increase, if true, storing values
        if increase_decrease > greatest_increase:
            greatest_increase = increase_decrease
            greatest_increase_month = row[0]
        
        #Checking against the greatesr decrease, if true, storing values
        if increase_decrease < greatest_decrease:
            greatest_decrease = increase_decrease
            greatest_decrease_month = row[0]

        #Reset previous month     
        previous_month = current_month

#Calculate average loss/profit - had to remove first month to get correct answer, similar issue to lines 30 - 32
average_profit_loss = cumulative_increase_decrease / (monthcount - 1)

#Change data types to be a little cleaner when I print
monthcount = int(monthcount)
total_profit_loss = int(total_profit_loss)
average_profit_loss = int(average_profit_loss)
greatest_increase = int(greatest_increase)
greatest_decrease = int(greatest_decrease)

#Print final answers to terminal
print ("Financial Analysis")
print ("---------------------------")
print (f"Total Months: {monthcount}")
print (f"Total Profit/Loss: ${total_profit_loss}") 
print (f"Average Change: ${average_profit_loss}")
print (f"Greatest Increase in Profit: {greatest_increase_month} ${greatest_increase}")
print (f"Greatest Decrease in Profit: {greatest_decrease_month} ${greatest_decrease}")

#Write to csv output file
output_path = os.path.join('analysis','analysis_results.txt')

with open(output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write("Total Months: " + str(monthcount) + " : ")
    txtfile.write("Total Profit/Loss: $" + str(total_profit_loss) + " : ")
    txtfile.write("Average Change: $" + str(average_profit_loss) + " : ")
    txtfile.write("Greatest Increase in Profit: " + greatest_increase_month + " $" + str(greatest_increase) + " : ")
    txtfile.write("Greatest Decrease in Profit: " + greatest_decrease_month + " $" + str(greatest_decrease))
