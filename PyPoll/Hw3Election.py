# Azat Dovgeldiyev
#I have not given or received any unauthorized assistance on this assignment.
import os
import csv
election_csv=os.path.join("..","Resources","election_data.csv")
cand=[]#creating list to manipulate with string obj
d={}#empty dic to store texts with correct numeric value
with open(election_csv,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    totVotes=0  
    print("Election Results")
    print("--------------------------------\n")
    for row in csvreader:
        totVotes+=1 #calculating total number of votes 
        cand.append(row[2])#adding each row in 3rd column to list  
    print("Total Votes: {}".format(totVotes)) 
    for word in cand: 
        if word in d:#if word in dict then add it to value
            d[word]=d[word]+1
        else:
            d[word]=1
    for key in list(d.keys()):
        p=round(d[key]/totVotes*100,2)#finding percent dividing each cand's vote to total,round to 2 digits     
        print("{}: {}% with total of {} votes".format(key,p,d[key]))
    print("Winner: {}".format(max(d,key=d.get)))
