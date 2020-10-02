import os
import csv
import statistics

#create a path
csvpath=os.path.join("Resources","budget_data.csv")
#open the csv
#read that csv file
with open (csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#skip header
    csv_header=next(csvreader,None)
#do a for loop to run thru each row: index [0] for month, index [1] for amount of profit/losses
#create empty list so when going thru row, adding each count into list
    countMonth=[]
    Net_total_profit_losses=[]
    Net_total=0
    average=[]
    for row in csvreader:
        countMonth.append(row[0])
        print(f'Total Month: {len(countMonth)}')
        Net_total=Net_total +int(row[1])
        Net_total_profit_losses.append(Net_total)
        print(f'Total: {Net_total}')
        average_change = Net_total/(len(Net_total_profit_losses))
        #aversge= statistics.mean(row[1])
        print(f'Average Change: {average_change}')

    
    
    
       

