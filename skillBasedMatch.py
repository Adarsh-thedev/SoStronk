#function to validate team size
def checkTeamSize(teamSize) :
    if(teamSize < 1) :
        raise ValueError("No match possible with less than one player")

#function to validate number of players
def validateInputs(totalPlayers, playersInOneTeam) :
    if(totalPlayers < 2*playersInOneTeam) :
        raise ValueError("Invalid details, total number of players must be at least 2 times number of players in each team!")

    if((totalPlayers % (2*playersInOneTeam)) != 0) :
        raise ValueError("Number of players must be even and multiple of two times number of players in each team in order to perform M vs M match")
    #eg {a,b,c,d,e,f} and playersInEachTeam =2, 
    #3 teams can be formed but number of teams should be 4 to perform two mathes at a time

#function to get all possible teams and their respective scores
def getAllPossibleTeams(totalPlayers, playersInOneTeam, arrayOfPlayers) :
    binaryArray = []
    for i in range (1, (2**totalPlayers)-1) :
        binaryNumber = bin(i).replace("0b", '')
        #initalize a counter to check if binary number has 1's equal to specified team size
        counter = 0
        for j in binaryNumber :
            if j == '1' :
                counter = counter + 1
        #if number of 1's == no of players in each team, put that string in binaryArray
        if(counter == playersInOneTeam) :
            binaryArray.append(binaryNumber.zfill(totalPlayers)) #to keep length of all binary strings equal

    possibleTeams = {}
    for i in binaryArray :
        counter = 0
        score = 0
        name = ''
        for j in i :
            if j == '1' :
                name = name + arrayOfPlayers[counter][0] + ','
                score = score + int(arrayOfPlayers[counter][1])/playersInOneTeam
            counter = counter + 1
        possibleTeams[name[:-1]] = score
    
    return possibleTeams

#function to print all M vs M matches where players in each team > 1
#let a = [15,20,22,25,28,30], a = sortedAverageScores
#quality matches will be 25(a[3]) vs 22(a[2]), 28(a[4]) vs 20(a[1]), 30(a[5]) vs 15(a[0])
def getMatchesForMultiplayerTeams(sortedArray, teams) :
    while len(sortedArray) != 0 :
        mid = int(len(sortedArray)/2)
        first = sortedArray[mid]
        second = sortedArray[mid-1]

        print(getKeyFromValue(first), "(", round(first,2), ")" , " vs ", getKeyFromValue(second), "(", round(second,2), ")")

        sortedArray.remove(first)
        sortedArray.remove(second)

        del teams[getKeyFromValue(first)]
        del teams[getKeyFromValue(second)]


#Take input of number of players allowed in one team
playersInEachTeam = int(input('Enter number of players in each team : '))

#validate team size
checkTeamSize(playersInEachTeam)

#empty array to store information of players
playersArray = []

#take input of player details
print('----Enter player names and scores----')
while True :
    playerInfo = input()
    #if empty line is encountered
    if playerInfo == "" :
        break
    else :
        playersArray.append(list(playerInfo.split()))
    
numberOfPlayers = len(playersArray)

#number validations
validateInputs(numberOfPlayers, playersInEachTeam)

#Get all unique pairs and average scores
possibleTeams = getAllPossibleTeams(numberOfPlayers, playersInEachTeam, playersArray)

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

#printing matches
if playersInEachTeam > 1 :
    getMatchesForMultiplayerTeams(sortedAverageScores, possibleTeams)

if playersInEachTeam == 1 :
#in this case, there will be more matches
#e.g a<10>, b<15>, c<20>, d<25> then possible matches :-
    # a vs b -> diff = 5
    # b vs c -> diff = 5
    # c vs d -> diff = 5
    # a vs c -> diff = 10
    # b vs d -> diff = 10
    # a vs d -> diff = 15
    #TODO: get matches sorted by quality
    for i in range (0, len(sortedAverageScores)) :
        for j in range (i+1, len(sortedAverageScores)) :
            print(getKeyFromValue(sortedAverageScores[i]), "(", sortedAverageScores[i], ")", " vs ", getKeyFromValue(sortedAverageScores[j]), "(", sortedAverageScores[j], ")")
