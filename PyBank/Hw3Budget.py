# Azat Dovgeldiyev
#I have not given or received any unauthorized assistance on this assignment.
import os
import sys
import csv

budget_csv = os.path.join("..","Resources","budget_data.csv")
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader,None)#skip first row
    totalMonths = 0 #initial values for total months and profit/loss
    profitLos = 0
    lst = [] # set lists for numbers and dates to manipulate
    date = []
    for row in csvreader: #manipulating through row
        date.append(row[0])
        totalMonths += 1
        profitLos += int(row[1])
        lst.append(int(row[1]))
    res = [lst[i+1]-lst[i] for i in range(len(lst)-1)]#subtract previous row from current
    avgChange = round(sum(res)/len(res),2) #then calculate mean of change
    maxIncrease = max(res)#greatest change from lst,not the max prfit
    maxIndex = res.index(maxIncrease)
    maxDate = date[lst.index(max(lst))]
    maxDecrease = min(res)#same with greatest decrease
    minIndex = res.index(maxDecrease)
    minDate = date[lst.index(min(lst))]

print("Financial Analysis")
print("--------------------------------\n")
print("Total Months: {}".format(totalMonths))
print("Total: ${}".format(profitLos))
print("Average Change: ${}".format(avgChange))
print("Greatest Increase in Profits: {}, (${})".format(maxDate,maxIncrease))
print("Greatest Decrease in Profits: {}, (${})".format(minDate,maxDecrease))

output_file=os.path.join("budget_final.txt")
sys.stdout=open(output_file,"w")
print("Financial Analysis")
print("--------------------------------\n")
print("Total Months: {}".format(totalMonths))
print("Total: ${}".format(profitLos))
print("Average Change: ${}".format(avgChange))
print("Greatest Increase in Profits: {}, (${})".format(maxDate,maxIncrease))
print("Greatest Decrease in Profits: {}, (${})".format(minDate,maxDecrease))
sys.stdout.close()
