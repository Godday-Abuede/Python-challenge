# Import necessary dependencies
import os
import csv

# The path for the filename  
PyBank_csv = os.path.join("budget_data.csv")


# Calculate the change in Profit/Losses and save the result in a new column in 
# dataframe named Change. 
PyBank_csv[int('Change')] = PyBank_csv['Profit/Losses"'].diff()

# Financial Analysis
month = len(PyBank_csv["Date"])                 #The total number of months included in the dataset
total = PyBank_csv['Profit/Losses'].sum()       # The net total amount of "Profit/Losses" over the entire period
average = PyBank_csv.mean()                       # The average of the changes in "Profit/Losses" over the entire period
inc = PyBank_csv.max()                        # The greatest increase in profits (date and amount) over the entire period
dec = PyBank_csv.min()                        # The greatest decrease in losses (date and amount) over the entire period

# Print the analysis to the terminal 
print('Financial Analysis')
print('-'*len('Financial Analysis'))
print(f'Total  Months: {month}')
print(f"Total: {total}")
print(f"Average Change: ${round(average[1],2)}")
print(f'Greatest Increase in Profits: {inc[0]} (${int(inc[2])})')
print(f'Greatest Decrease in Profits: {dec[0]} (${int(dec[2])})')


# Export a text file with the results.
f = open("output.txt", "a")
print('Financial Analysis', file=f)
print('-'*len('Financial Analysis'), file=f)
print(f'Total  Months: {mth}', file=f)
print(f"Total: {ttl}", file=f)
print(f"Average Change: ${round(avg[1],2)}", file=f)
print(f'Greatest Increase in Profits: {inc[0]} (${int(inc[2])})', file=f)
print(f'Greatest Decrease in Profits: {dec[0]} (${int(dec[2])})', file=f)
f.close()

    


