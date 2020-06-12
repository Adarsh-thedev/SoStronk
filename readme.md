# Skill Based Matchmaking  

## Problem Statement  
You are given N players who want to play a M vs M match. Each Player has an attribute Score which is a
positive integer.  
The program needs to find possible unique matches of M vs M players depending on their Score. The
matches should be sorted based on the quality of each match. The quality of the match is defined as the closeness of the scores between the teams.  

InputNumber of players on each side: M  
Example2  
Input-  
<name of player 1> <score>  
<name of player 2> <score>  
A blank line denotes end of input.  
Example  
bleh 85  
Aequitas 90  
akS 87  
lamiV 20  
Outputsorted list of (best to worst)  
<comma separated list of players in team A>(average score) vs <comma separated list of players in team
B>(average score)  
Example  
bleh,akS (86) vs Aequitas,lamiV (55)  
bleh,Aequitas (87.5) vs akS,lamiV (53.5)  
bleh,lamiV (52.5) vs Aequitas,akS (88.5)  

## Solution Approach  

```
1. Take inputs and validate if inputs are appropriate to perform match  
2. Store each input in an array, and put all input arrays inside another array  
3. Initialize an array to store binary strings that contain 1's equal to team size  
4. Initialize a hashmap and store all possible teams as keys and socres as values  
5. Store all scores in an array and sort  
6. If number of players in each team > 1  
    - start from middle two indexes of sorted array and print names and average scores with the help  of keys in the hashmap with values as sorted_array[index] 
    - remove these two items from array and agin find mid two indexes and perform same operation  
7. If number of players in each team == 1  
    - New logic is required, still working
```