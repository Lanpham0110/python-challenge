import os
import csv

#create a path
csvpath=os.path.join("..","Resources","election_data.csv")
#open the csv
#read that csv file
with open (csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')   
#skip header using next
    csv_header=next(csvreader,None)
  
    Vote_count=0
    Totalcount_name=[]
    Candidate_names=[]
    Candidate=[]
    i=0
    percentage=[]
    dict={}
    for row in csvreader:
        #finding total vote by initialized count as 0, looping thru csvreader and start adding
        Vote_count+=1
        Candidate_names.append(row[2])
        # add all values in 3rd row index 2 into cadidate name list
    
    Candidate.append(Candidate_names[0])
    #condition inital name list
    dict[Candidate_names[0]]=[] 
    #inital dict is empty, conditioning intial as its first value
    for i in range(1,len(Candidate_names)):
        counting_name=Candidate.count(Candidate_names[i])
        #start counting in Candidate_name list and assign that count as variable called counting_name
        if counting_name ==0:
            Candidate.append(Candidate_names[i])
            #look into name list, if Candidate[i] is not in list, add that name from big list(Candidate_name[]) into Candidate list
            #identifying names of candidates 
            dict[Candidate_names[i]]=[]  
            #putting all names of candidates found in Candidate list into dictionary called dict{}
            #using dictionary to get max value and associated key: look for winner
    for j in range(0,len(Candidate)):     
            
        Totalcount_name.append(Candidate_names.count(Candidate[j]))
        #inside Candidate list, calculate total votes of each Candidate in that list
        dict[Candidate[j]]=Totalcount_name[j]
        #putting all value of votes of candidates found in Candidate list into dictionary called dict{}
        #using dictionary to get max value and associated key: look for winner
        
        percentage.append(round((Totalcount_name[j]/Vote_count)*100))

    with open ("output.txt","w") as outfile:
        print(f'Total Votes:{Vote_count}')
        outfile.write(f'Total Votes:{Vote_count}\n')
    #open file as write
    #create txt file called output.txt
    #(\n) enter new line
    #print state will show in console
    #outfile.write will oupt in Output.txt file
         
     
        for j in range(0,len(Candidate)):    
            print(f"{Candidate[j]} {Totalcount_name[j]} {percentage[j]}")
            outfile.write(f"{Candidate[j]} {percentage[j]}% ({Totalcount_name[j]})\n")
            #print(f'Winner: {winner}')
            #outfile.write(f'Winner: {winner}')
            
        winner=max(dict,key=dict.get)
       #find max vote associate with its key in dictionary
        print(winner)
        outfile.write(f'Winner: {winner}')
    
    
