import os
import csv 

PyPoll_csv = os.path.join("Electiondata.csv")

# Group votes by candidates
cd = dt.groupby('Candidate')
cd.head()
cd.indices.keys()

# Group votes by counties
ct = dt.groupby('County')
ct.head()

# List of candidates 
lc = list(cd.groups.keys())
# List of Counties
ls = list(ct.groups.keys())

# Votes by candidates
cd.get_group('Correy') 
cd.get_group('Khan') 
cd.get_group('Li') 
cd.get_group("O'Tooley") 

# Total votes cast and total number of votes won by candidates
totalVote = len(dt)
cVote = len(cd.get_group('Correy'))                                 # Total number of votes won by Correy
kVote = len(cd.get_group('Khan'))                                   # Total number of votes won by Khan
lVote = len(cd.get_group('Li'))                                     # Total number of votes won by Li
oVote = len(cd.get_group("O'Tooley"))                               # Total number of votes won by O'Tooley

# Percentage share of votes by candidates
cShare = '{0:.3f}%'.format(round(cVote / totalVote * 100))          # Correy's vote share
kShare = '{0:.3f}%'.format(round(kVote / totalVote * 100))          # Khan's vote share
lShare = '{0:.3f}%'.format(round(lVote / totalVote * 100))          # Li's vote share
oShare = '{0:.3f}%'.format(round(oVote / totalVote * 100))          # O'Tooley's vote share

# Create a dataframe of the election candidates, their vote share and percentage of the total vote won
rs = {'Candidate': list(cd.groups.keys()), 
      'Vote': [cVote, kVote, lVote, oVote],
      'PctVote': [cShare, kShare, lShare, oShare]}
df = pd.DataFrame(rs, columns = ['Candidate', 'Vote', 'PctVote'])


# Print the result to the terminal 
print('Election Results')
print('-'*25)
print(f'Total  Votes: {totalVote}')
print('-'*25)
print(f"{df.Candidate[0]}: {df.PctVote[0]} ({df.Vote[0]})")
print(f"{df.Candidate[1]}: {df.PctVote[1]} ({df.Vote[1]})")
print(f"{df.Candidate[2]}: {df.PctVote[2]} ({df.Vote[2]})")
print(f"{df.Candidate[3]}: {df.PctVote[3]} ({df.Vote[3]})")
print('-'*25)
print(f"Winner: {df[df['Vote']==df['Vote'].max()]['Candidate'][1]}")
print('-'*25)


# Export the results to a text file.
f = open("result.txt", "a")
print('Election Results', file=f)
print('-'*25, file=f)
print(f'Total  Votes: {totalVote}', file=f)
print('-'*25, file=f)
print(f"{df.Candidate[0]}: {df.PctVote[0]} ({df.Vote[0]})", file=f)
print(f"{df.Candidate[1]}: {df.PctVote[1]} ({df.Vote[1]})", file=f)
print(f"{df.Candidate[2]}: {df.PctVote[2]} ({df.Vote[2]})", file=f)
print(f"{df.Candidate[3]}: {df.PctVote[3]} ({df.Vote[3]})", file=f)
print('-'*25, file=f)
print(f"Winner: {df[df['Vote']==df['Vote'].max()]['Candidate'][1]}", file=f)
print('-'*25, file=f)
f.close()




