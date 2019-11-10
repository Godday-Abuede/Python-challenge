import os
import csv

# The path for the filename
PyBank_csv = os.path.join("..", "budget_data.csv")

# Define a function to have it accept Date and profit/losses parameters
def financial_analysis(column):
    print("financial_analysis")
    print(column)
    Date =int(column[1])
    total_amount =int(column[2])
    average_change =int(column[3])
    greatest_increase_in_profit =int(column[4])
    greatest_decrease_in_profit =int(column[5])
    total_months =sum(Date)
    print(total_months)
    total_amount = sum("Profit/Losses")
    print(total_amount)





    

