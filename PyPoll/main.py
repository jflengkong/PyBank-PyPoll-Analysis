import csv
import os

csvpath = os.path.join('Resources','election_data.csv')

#Define variables
votes_IDS = []
election_candidates = []
candidate= [] 
number_of_votes =[]
candidate_percentage =[] 
total_votes = 0 

#Open CSV file and call it election_data_file 
with open(csvpath) as election_data_file: 
    csvreader = csv.reader(election_data_file,delimiter=',')
    print(csvreader)

    #Skip first row and save under csv_header variable 
    csv_header = next(csvreader)
        
    #Start loop to search through file 
    for row in csvreader: 
        #Add all vote IDs into the votes list and count how many votes there are  
        votes_IDS.append(row[0])
        total_votes = len(votes_IDS)      

        #Run through each row of candidate 
        candidate = row[2]
        
        #Search if candidate is in the list of election candidate, if yes 
        if candidate in election_candidates:
            candidate_index = election_candidates.index(candidate)
            number_of_votes[candidate_index] += 1
            
        else:
            election_candidates.append(candidate)
            number_of_votes.append(1)

#Loop through the election candidates and fine their total votes and percentage votes  
for count in range(len(election_candidates)):
    vote_percentage = number_of_votes[count] / total_votes * 100
    #aAdd to candidate percentage list 
    candidate_percentage.append(vote_percentage)
    
#Format percentage final into 2 decimal points 
percentage_final = ['%.3f' % elem for elem in candidate_percentage]
print(percentage_final)

#Find the winner by finding the candidate with the maximum number of votes compared to their indices in the lists 
max_votes = max(number_of_votes)
max_candidate_index = number_of_votes.index(max_votes)
winner = election_candidates[max_candidate_index]

#Print all the outputs 
print("Election Results")
print("-----------------------------------------")
print(f"Total votes: {total_votes}")
for i in range(len(election_candidates)):
    print(f"{election_candidates[i]}: {percentage_final[i]}% ({number_of_votes[i]})")
print("-----------------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------------")

#Export file into a .txt file in Analysis folder 

output_path = os.path.join('Analysis','output_pypoll.txt')\
    
with open(output_path,'a') as txtfile: 
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------------------------\n")
    txtfile.write(f"Total votes: {total_votes}\n")
    for i in range(len(election_candidates)):
        txtfile.write(f"{election_candidates[i]}: {percentage_final[i]}% ({number_of_votes[i]})\n")
    txtfile.write("-----------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-----------------------------------------\n")