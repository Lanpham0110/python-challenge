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
    #print(csv_header)
    #print(csvreader[1])
#do a for loop to run thru each row: index [0] for month, index [1] for amount of profit/losses
#create empty list so when going thru row, adding each count into list
    countMonth=0
    Net_total=0
    i=0
    data=[]
    sumchange=0
    change_list=[]
    for row in csvreader:
        #print(row)
        countMonth+=1
        #Profit_losses= float(row[1])
        Net_total+=float(row[1])
        data.append(row[1])
    for i in range(0,(len(data)-1)):
        change=float(data[i+1])-float(data[i])
        sumchange=sumchange+round(change)
        print(change)
        change_list.append(change)
    Greatest_value=max(change_list)
    Lowest_value=min(change_list)
    average_change =sumchange/len(change_list)   
    
    with open ("output.txt","w") as outfile:
        print(f'Total Month:{countMonth}')
        outfile.write(f'Total Month:{countMonth}\n')
        print(f'Total: {Net_total}')  
        outfile.write(f'Total: {Net_total}\n')
        print(f'Average Change: {average_change}')
        outfile.write(f'Average Change: {average_change}\n')
        print(f'Greatest value = {Greatest_value}')
        outfile.write(f'Greatest value = {Greatest_value}\n')
        print(f'Lowest value = {Lowest_value}')
        outfile.write(f'Lowest value = {Lowest_value}')
       
    
    
    
       

