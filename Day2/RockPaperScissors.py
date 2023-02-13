#Rock A,X - 1 point
#Paper B,Y - 2 points
#Scissors C,Z - 3 points
points = 0
points2 = 0

#Read each line of the file. Split the line into 2 entries of a list. Compare the first entry and second entry and calculate points based on result.
input = open('Day2/input.txt')
for line in input:
    round = line.split()
    if round[0] == 'A' and round[1] == 'X':
        points = points + 4
        points2 = points2 + 3
    if round[0] == 'A' and round[1] == 'Y':
        points = points + 8
        points2 = points2 + 4
    if round[0] == 'A' and round[1] == 'Z':
        points = points + 3
        points2 = points2 + 8
    if round[0] == 'B' and round[1] == 'X':
        points = points + 1
        points2 = points2 + 1
    if round[0] == 'B' and round[1] == 'Y':
        points = points + 5
        points2 = points2 + 5
    if round[0] == 'B' and round[1] == 'Z':
        points = points + 9
        points2 = points2 + 9
    if round[0] == 'C' and round[1] == 'X':
        points = points + 7
        points2 = points2 + 2
    if round[0] == 'C' and round[1] == 'Y':
        points = points + 2
        points2 = points2 + 6
    if round[0] == 'C' and round[1] == 'Z':
        points = points + 6
        points2 = points2 + 7

print('Points from part one are:',points)
print('Points from part two are:',points2)