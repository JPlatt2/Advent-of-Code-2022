#Rock A,X
#Paper B,Y
#Scissors C,Z
points = 0
input = open('Day2/input.txt')
for line in input:
    round = line.split()
    if round[0] == 'A':
        round[0] = 'Rock'
    if round[0] == 'B':
        round[0] = 'Paper'
    if round[0] == 'C':
        round[0] = 'Scissors'
    if round[1] == 'X':
        round[1] = 'Rock'
    if round[1] == 'Y':
        round[1] = 'Paper'
    if round[1] == 'Z':
        round[1] = 'Scissors'
    if round[1] == 'Rock':
        points = points + 1
    if round[1] == 'Paper':
        points = points + 2
    if round[1] == 'Scissors':
        points = points + 3
    if round[0] == round[1]:
        points = points + 3
    if round[0] == 'Paper' and round[1] == 'Scissors':
        points = points + 6
    if round[0] == 'Rock' and round[1] == 'Paper':
        points = points + 6
    if round[0] == 'Scissors' and round[1] == 'Rock':
        points = points + 6

print('Points from part one are:',points)

points = 0

#1 for Rock, 2 for Paper, and 3 for Scissors
input2 = open('Day2/input.txt')
for line2 in input2:
    round2 = line2.split()
    if round2[0] == 'A' and round2[1] == 'X':
        points = points + 3
    if round2[0] == 'A' and round2[1] == 'Y':
        points = points + 4
    if round2[0] == 'A' and round2[1] == 'Z':
        points = points + 8
    if round2[0] == 'B' and round2[1] == 'X':
        points = points + 1
    if round2[0] == 'B' and round2[1] == 'Y':
        points = points + 5
    if round2[0] == 'B' and round2[1] == 'Z':
        points = points + 9
    if round2[0] == 'C' and round2[1] == 'X':
        points = points + 2
    if round2[0] == 'C' and round2[1] == 'Y':
        points = points + 6
    if round2[0] == 'C' and round2[1] == 'Z':
        points = points + 7


print('Points from part two are:',points)