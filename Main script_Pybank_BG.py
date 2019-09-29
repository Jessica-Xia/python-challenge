#!/usr/bin/env python
# coding: utf-8

# In[31]:


#import dependecies
import os
#module for reading CSV files
import csv
import math

budget_file = os.path.join('budget_data.csv')

total_months = []
total_profit = []
monthly_change = []
 
with open(budget_file,newline="") as csvreader:
    csvreader = csv.reader(csvreader,delimiter=",") 
    header = next(csvreader)  

    total = 0
    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        total += int(row[1])
        
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])
        
max_increase_value = max(monthly_change)
max_decrease_value = min(monthly_change)
max_increase_month = monthly_change.index(max(monthly_change)) + 1
max_decrease_month = monthly_change.index(min(monthly_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${total}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# In[32]:


# Output files
output_file = os.path.join("Financial_Analysis_Result.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${total}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# In[ ]:




