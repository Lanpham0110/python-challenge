import os
import csv

#create a path
csvpath=os.path.join("..","Resources","election_data.csv")
#open the csv
#read that csv file
with open (csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    
#skip header
    csv_header=next(csvreader,None)
  
    Vote_count=0
    count_name=0
    Candidate_names=[]
    vote_list=[]
    i=0
    sumchange=0
    change_list=[]
    for row in csvreader:
        #print(row)
        Vote_count+=1
        Candidate_names.append(row[2])
        # add all values in 3rd row index 2 into cadidate name list

    for i in range(len(Candidate_names))
        count_name=name.count[i]
        count_name+=1

    #for i in range(0,(len(data)-1)):
        #change=float(data[i+1])-float(data[i])
        #sumchange=sumchange+round(change)
        #print(change)
        #change_list.append(change)
    #Greatest_value=max(change_list)
    #Lowest_value=min(change_list)
    #average_change =sumchange/len(change_list)   
    print(f'Total Votes:{Vote_count}')
    print(f'Total name: {count_name}')   
    #print(f'Average Change: {average_change}')
    #print(f'Greatest value = {Greatest_value}')
    #print(f'Lowest value = {Lowest_value}')
    
