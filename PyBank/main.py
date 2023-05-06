import csv
import os
CSV_PATH = os.path.join('Resources','budget_data.csv')
OTPT_PATH = os.path.join('Analysis','budget_analysis.txt')

# Declaring variables
count = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
TotalSum = 0

with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile) # Reading the file
    # Read the header row
    csv_header = next(csvreader) # Storing and Skipping Heading
    rowfirst = next(csvreader) # Defining adjacent profit values, in order to use when calculating profit change
    
    count += 1
    TotalSum += int(rowfirst[1])
    previous_profit_losses = int(rowfirst[1])
    
    for row in csvreader:
        # Total Tracking: count for total months and TotalSum for adding profit
        count += 1
        TotalSum += int(row[1])
        
        # Change Tracking:
        net_change = int(row[1]) - previous_profit_losses
        previous_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        
        # Greatest Increase Calculations, Most positive change:
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Greatest Decrease Calculations, Most negative change:
        if net_change < greatest_decrease[1]: 
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average Change Calculation, Net Change/ Length of Net Change List:
AverageChange = round((net_change) / len(net_change_list),2)

# Printing Output Statements 
Text_Otpt = (
f"Financial Analysis\n\n"
f"----------------------------\n\n"
f"Total Months: {count}\n\n"
f"Total: ${TotalSum}\n\n"
f"Average Change: ${AverageChange}\n\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n\n")

# Print the output (to terminal)
print(Text_Otpt)

# Export the results to text file
with open(OTPT_PATH, "w") as txt_file:
    txt_file.write(Text_Otpt)
