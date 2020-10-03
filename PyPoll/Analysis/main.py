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
    count_name=[]
    Candidate_names=[]
    name=[]
    vote_list=[]
    i=0
    sumchange=0
    change_list=[]
    for row in csvreader:
        #print(row)
        Vote_count+=1
        Candidate_names.append(row[2])
        # add all values in 3rd row index 2 into cadidate name list
    
    name.append(Candidate_names[0])
    for i in range(1,len(Candidate_names)):
        counting_name=name.count(Candidate_names[i])
        if counting_name ==0:
            name.append(Candidate_names[i])
    print(name)
      #  count_name+=1

    
    for j in range(0,len(name)):     
            
        count_name.append(Candidate_names.count(name[j]))
        
        
        #sumchange=sumchange+round(change)
        #print(change)
        #change_list.append(change)
    #Greatest_value=max(winner)
   
    #average_change =sumchange/len(change_list)   
    print(f'Total Votes:{Vote_count}')
    print(f'Total name: {count_name}')   
    #print(f'Average Change: {average_change}')
    #print(f'Greatest value = {Greatest_value}')
    #print(f'Lowest value = {Lowest_value}')
    
