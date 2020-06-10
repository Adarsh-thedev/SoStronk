# You are given N players who want to play a M vs M match. Each Player has an attribute Score which is a
# positive integer.
# The program needs to find possible unique matches of M vs M players depending on their Score. The
# matches should be sorted based on the quality of each match. The quality of the match is defined as the
# closeness of the scores between the teams.
# Example for quality
# Let's say we have 1vs1 matches with the following scoresMatch1 100 vs 98
# Match2 60 vs 40
# Match3 62 vs 64
# The sorted order here would be:
# Match1, Match3, Match2
# For matches with multiple players on one side, the average score should be used.
# InputNumber of players on each side: M
# Example2
# Input-
# <name of player 1> <score>
# <name of player 2> <score>
# A blank line denotes end of input.
# Examplebleh 85
# Aequitas 90
# akS 87
# lamiV 20
# Outputsorted list of (best to worst)
# <comma separated list of players in team A>(average score) vs <comma separated list of players in team
# B>(average score)
# Examplebleh,akS (86) vs Aequitas,lamiV (55)
# bleh,Aequitas (87.5) vs akS,lamiV (53.5)
# bleh,lamiV (52.5) vs Aequitas,akS (88.5)

#Take input of number of players allowed in one team
playersInEachTeam = int(input('Enter number of players in each team : '))

#empty array to store information of players
playersArray = []

#take input of player details
while True :
    playerInfo = input('Enter player name and score : ')
    #if empty line is encountered
    if playerInfo == "" :
        break
    else :
        playersArray.append(list(playerInfo.split()))

#validation of number of players
numberOfPlayers = len(playersArray)
if(numberOfPlayers < 2*playersInEachTeam) :
    print("Invalid details, total number of players must be 2 times number of players in each team")
    exit()

if(numberOfPlayers % 2 !=0) :
    print("Number of players must be even to perform M vs M match")
    exit()

print(playersArray)

setOfPossibleTeams = {}

#Get all unique pairs and average scores
for i in range (0, numberOfPlayers) :
    for j in range (i+1, numberOfPlayers) :
        temp = playersArray[i][0] + ',' + playersArray[j][0]
        avgScore = (int(playersArray[i][1]) + int(playersArray[j][1]))/2
        setOfPossibleTeams[temp] = avgScore

print(setOfPossibleTeams)