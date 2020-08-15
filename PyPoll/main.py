#import os and csv files
import os
import csv

#initialize variables
candidates = []
num_votes = 0
vote_counts = []

#set path
election_csv = os.path.join('Resources','election_data.csv')

#open the file, read the text
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    #Skip first row as headers
    csv_header = next(csvreader)

    #go line by line and process each vote
    for line in csvreader:

        #add to total number of votes
        num_votes = num_votes + 1

        #candidate voted for
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        max_index = count
winner = candidates[max_index]
#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#Write to csv output file
output_path = os.path.join('analysis','analysis_results.txt')

with open(output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write("Total Votes: {num_votes}\n")
    for count in range(len(candidates)):
        txtfile.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    txtfile.write("---------------------------\n")
    txtfile.write("Winner: {winner}\n")
    txtfile.write("---------------------------\n")