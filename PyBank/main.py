# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:20:57 2019

@author: Godday
"""
"""
import os
import csv

INPUT_DIR = os.path.join(os.getcwd(),"PyBank")
for filename in os.listdir(INPUT_DIR):
    with open(os.path.join(INPUT_DIR, "budget_data.csv")) as infile:
        reader = csv.reader(infile)
        for row in reader:
          print (row)
"""
# Import the required library/ module
import pandas as pd

# Make sure the data is saved in the same directory/ folder as the script file.
dt = pd.read_csv("budget_data.csv") 
 
def financial_analysis(data):
    date = data.iloc[:,0]
    prLo = data.iloc[:,1]
    chng = data['Change'] = prLo.diff()
    prIn = data.max()
    prDD = data.min()

    # Print the analysis to the terminal 
    print('Financial Analysis')
    print('-'*len('Financial Analysis'))
    print(f'Total  Months: {len(date)}')
    print(f"Total: {prLo.sum()}")
    print(f"Average Change: ${round(chng.mean(), 2)}")
    print(f'Greatest Increase in Profits: {prIn[0]} (${int(prIn[2])})')
    print(f'Greatest Decrease in Profits: {prDD[0]} (${int(prDD[2])})')
    
    # Export a text file with the results.
    f = open("output.txt", "a")
    print('Financial Analysis', file=f)
    print('-'*len('Financial Analysis'), file=f)
    print(f'Total  Months: {len(date)}', file=f)
    print(f"Total: {prLo.sum()}", file=f)
    print(f"Average Change: ${round(chng.mean(), 2)}", file=f)
    print(f'Greatest Increase in Profits: {prIn[0]} (${int(prIn[2])})', file=f)
    print(f'Greatest Decrease in Profits: {prDD[0]} (${int(prDD[2])})', file=f)
    f.close()

financial_analysis(dt)




