# Example : 
#           bleh,akS (86) vs Aequitas,lamiV (55)
#           bleh,Aequitas (87.5) vs akS,lamiV (53.5)
#           bleh,lamiV (52.5) vs Aequitas,akS (88.5)

#Take input of number of players allowed in one team
playersInEachTeam = int(input('Enter number of players in each team : '))
if(playersInEachTeam < 1) :
    print("No match possible with less than one player")
    exit()

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
    print("Invalid details, total number of players must be at least 2 times number of players in each team")
    exit()

if((numberOfPlayers % (2*playersInEachTeam)) != 0) :
    print("Number of players must be even and multiple of two times number of players in each team in order to perform M vs M match")
    exit()
#eg {a,b,c,d,e,f} and playersInEachTeam =2, 
#3 teams can be formed but number of teams should be 4 to perform two mathes at a time


#Get all unique pairs and average scores
binaryArray = []
for i in range (1, (2**numberOfPlayers)-1) :
    binaryNumber = bin(i).replace("0b", '')
    #initalize a counter to check if binary number has 1's equal to specified team size
    counter = 0
    for j in binaryNumber :
        if j == '1' :
            counter = counter + 1
    #if number of 1's == no of players in each team, put that string in binaryArray
    if(counter == playersInEachTeam) :
        binaryArray.append(binaryNumber.zfill(numberOfPlayers)) #to keep length of all binary strings equal

possibleTeams = {}
for i in binaryArray :
    counter = 0
    score = 0
    name = ''
    for j in i :
        if j == '1' :
            name = name + playersArray[counter][0] + ','
            score = score + int(playersArray[counter][1])/playersInEachTeam
        counter = counter + 1
    possibleTeams[name] = score

#print(possibleTeams);

#get all average scores and sort
sortedAverageScores = []
for i in possibleTeams :
    sortedAverageScores.append(possibleTeams[i])

sortedAverageScores.sort()
#length of this array will always be even

#average scores are values in possibleTeamss, it can be used to extract keys(i.e teams)
#extract keys
def getKeyFromValue(val) :
    for key, value in possibleTeams.items() :
        if val == value :
            return key
#print(getKeyFromValue(25));

#print all M vs M matches
#let a = [15,20,22,25,28,30], a = sortedAverageScores
#quality matches will be 25(a[3]) vs 22(a[2]), 28(a[4]) vs 20(a[1]), 30(a[5]) vs 15(a[0])

if playersInEachTeam > 1 :
    while len(sortedAverageScores) != 0 :
        mid = int(len(sortedAverageScores)/2)
        first = sortedAverageScores[mid]
        second = sortedAverageScores[mid-1]

        print(getKeyFromValue(first), "(", first, ")" , " vs ", getKeyFromValue(second), "(", second, ")")

        sortedAverageScores.remove(first)
        sortedAverageScores.remove(second)

        del possibleTeams[getKeyFromValue(first)]
        del possibleTeams[getKeyFromValue(second)]


if playersInEachTeam == 1 :
#in this case, there will be more martches
#e.g a<10>, b<15>, c<20>, d<25> then possible matches :-
    # a vs b -> diff = 5
    # b vs  c -> diff = 5
    # c vs d -> diff = 5
    # a vs c -> diff = 10
    # b vs d -> diff = 10
    # a vs d -> diff = 15
    #TODO: get matches sorted by quality
    for i in range (0, len(sortedAverageScores)) :
        for j in range (i+1, len(sortedAverageScores)) :
            print(getKeyFromValue(sortedAverageScores[i]), "(", sortedAverageScores[i], ")", " vs ", getKeyFromValue(sortedAverageScores[j]), "(", sortedAverageScores[j], ")")
