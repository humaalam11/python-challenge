
import os
import csv

election_data = os.path.join('Resources','election_data.csv')
OTPT_PATH = os.path.join('Analysis','pypoll_analysis.txt')

# Declaring variables
TotalVotes= 0
CandidateList = []
vote ={}
winningcadidate = ""
winningcount = 0

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        #Counting Total Votes, indicating Candidat Name position
        TotalVotes = TotalVotes +1
        candidateName = row[2]

        if candidateName not in CandidateList:   
            CandidateList.append(candidateName)
            vote[candidateName] = 0 
        vote[candidateName] = vote[candidateName]+1

# Printing Ouput Statement 1:
Text_Otpt1 = (     
f"Election Results\n\n"
f"------------------------\n\n"
f"Total Votes: {TotalVotes}\n\n"  
f"------------------------\n\n")

print(Text_Otpt1)
with open(OTPT_PATH, "w") as txt_file:
    txt_file.write(Text_Otpt1)
    

# Calculating Winner:
    for winner in vote:

        votes = vote.get(winner)
        votepercentage = round(votes/TotalVotes * 100, 3)
        Text_Otpt2= (f"{winner}: {votepercentage}% ({votes})\n\n")
    
#Printing statement 2:
        print(Text_Otpt2)
        txt_file.write(Text_Otpt2)
        

# If statements comparing candidate vote total to calculate winner:
        if (votes > winningcount):
            winningcount = votes
            winningcadidate = winner
    WinnerOutput= f"{winningcadidate}"

# Printing Output Statement 3:
    Text_Otpt3 = (
    f"------------------------\n\n"
    f"Winner: {WinnerOutput}\n\n"
    f"------------------------\n\n")


    print(Text_Otpt3)
    txt_file.write(Text_Otpt3)


