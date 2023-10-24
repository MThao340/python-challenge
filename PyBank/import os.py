import os
import csv

csv_path = os.path.join("PyBank","Resources",'budget_data.csv')

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_data = list(csvreader)
    
change_list = []
months_list = []
total = []
opening_value = int(budget_data[1][1])

for row in budget_data[1:]:
    months_list.append(row[0])
    change = int(row[1]) - opening_value
    total.append(int(row[1]))
    change_list.append(change)
    opening_value = int(row[1])
    
print("Financial Analysis")
print("Total months: " + str(len(months_list)))
print("Total: " + str(sum(total)))
print("Average Change: " + str((sum(change_list) / len(change_list)))) 
print("Greatest Increase in Profits: " + months_list[change_list.index(max(change_list))] + "    (" + str(max(change_list)) + ")")
print("Greatest Decrease in Profits: " + months_list[change_list.index(min(change_list))] + "    (" + str(min(change_list)) + ")")

output = os.path.join("PyBank","Analysis", "AnalysisResults.txt")
with open(output, "w", newline='') as textfile:

    textfile.write("Total months analyzed: " + str(len(months_list)))
    textfile.write("Total Profits/Losses " + str(sum(total)))
    textfile.write("Average Change: " + str((sum(change_list) / len(change_list)))) 
    textfile.write("Greatest Increase in Profits: " + months_list[change_list.index(max(change_list))] + " (" + str(max(change_list)))
    textfile.write("Greatest Decrease in Profits: " + months_list[change_list.index(min(change_list))] + " (" + str(min(change_list)))

    textfile.close()