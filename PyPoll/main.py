import os
import csv

# opening cvs for pathway

voting_csv = os.path.join('.', 'Resources', 'election_data.csv')

# opening an empty list for candidates votes

voting_count = {}

# opening an empty list for candidates vote percentages

voting_per = {}

# total variable hold

voting_total = 0

# opening csv folders

with open(voting_csv, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

    # skip the header

    for row in voterreader:

        # total vote count
        voting_total +=1

        # vote quantity per candidate
        if row[2] in voting_count:
            voting_count[row[2]] +=1

        # if a candidate is not in dicti, add him/her and give value of '1'
        else:
            voting_count[row[2]] = 1

# to designate a winner
winning_count = 0

# opening a loop in the dictionary for vote count for winner
for candidate in voting_count:

    # voting percentage count for each candidate
    voting_per[candidate] = (voting_count[candidate] / voting_total) * 100

    # designating a winner
    if voting_count[candidate] > winning_count:
        winning_count = voting_count[candidate]
        winner = candidate

# printnig with txt file
results_txt = os.path.join('election_results.txt')

# to reach the csv file we made previously
with open (results_txt, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------------------------
Total Votes: {voting_total}
-------------------------------------------\n''')

    print(f'''\nElection Results
    ---------------------------------------
Total Votes: {voting_total}
-------------------------------------------''')


    for candidate, votes in voting_count.items():
        txtfile.write(f'{candidate}: {voting_per[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {voting_per[candidate]:.3f}% ({votes})''')

    txtfile.write(f'''----------------------------------------
Winner: {winner}
--------------------------------------------''')

    print(f'''----------------------------------------
Winner: {winner}
--------------------------------------------''')


        
        
        
        
        
        
        
        









