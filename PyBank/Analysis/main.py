import os
import csv

#create a path
csvpath=os.path.join("..","Resources","budget_data.csv")
#open the csv
#read that csv file
with open (csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
#skip header
    csv_header=next(csvreader,None)
#do a for loop to run thru each row: index [0] for month, index [1] for amount of profit/losses
#create empty list so when going thru row, adding each count into list
    countMonth=0
    Net_total=0
    average=[]
    for i in csvreader:
        countMonth+=1
        print(f'Total Month:{countMonth}')
        Net_total=Net_total +int(i[1])
        print(f'Total: {Net_total}')
       
        for j in csvreader:
        
        
            average_change =(int(j[1])-int(i[1])) /((int(j[0])-int(i[0]))
     
            print(f'Average Change: {average_change}')

    
    
    
       

