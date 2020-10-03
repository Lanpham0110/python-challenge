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
    Totalcount_name=[]
    Candidate_names=[]
    name=[]
    vote_list=[]
    i=0
    percentage=[]
    
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
            #look into name list, if i name is not in list, add that name from big list into name list
            #identifying names of candidates 

    for j in range(0,len(name)):     
            
        Totalcount_name.append(Candidate_names.count(name[j]))
        #inside name list, calculate total votes of each name in that list
        
        percentage.append(round((Totalcount_name[j]/Vote_count)*100))

    with open ("output.txt","w") as outfile:
        print(f'Total Votes:{Vote_count}')
        outfile.write(f'Total Votes:{Vote_count}\n')
     #Greatest_value=max(winner) 
         
     
        for j in range(0,len(name)):    
            print(f"{name[j]} {Totalcount_name[j]} {percentage[j]}")
            outfile.write(f"{name[j]} {percentage[j]}% ({Totalcount_name[j]})\n")

    
    
